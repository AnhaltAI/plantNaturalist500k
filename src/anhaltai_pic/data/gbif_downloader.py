import json
import os
import subprocess
import threading

import numpy as np
import pandas as pd
import progressbar
from PIL import Image, ImageFile

Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

class GBIFDownloader:
    METADATA_FILENAME = "metadata.json"

    def __init__(self,
                 occurrence_file_path: str,
                 download_path: str,
                 num_items: int,
                 num_threads: int = 8,
                 ):
        self.occurrence_file_path = occurrence_file_path
        self.download_path = download_path
        self.num_items = num_items
        self.num_threads = num_threads

        self.lock = threading.Lock()
        self.progress_bar = None

    def _download_occurrence(self, row: pd.Series):
        # skip occurrences with unspecified species
        if np.isnan(row["speciesKey"]):
            return
        occurrence_path = os.path.join(self.download_path,
                                       str(int(row["kingdomKey"])),
                                       str(int(row["phylumKey"])),
                                       str(int(row["classKey"])),
                                       str(int(row["orderKey"])),
                                       str(int(row["familyKey"])),
                                       str(int(row["genusKey"])),
                                       str(int(row["speciesKey"])),
                                       str(int(row["gbifID"])))
        os.makedirs(occurrence_path, exist_ok=True)

        # download metadata
        metadata_path = os.path.join(occurrence_path, self.METADATA_FILENAME)
        if not os.path.exists(metadata_path):
            occurrence_url = f"https://api.gbif.org/v1/occurrence/{int(row['gbifID'])}"
            with open(os.devnull, 'w') as devnull:
                subprocess.call(["wget", occurrence_url, "-O", metadata_path], stdout=devnull, stderr=devnull)
        with open(metadata_path, 'r', encoding="utf-8") as metadata_file:
            try:
                metadata = json.load(metadata_file)
            except Exception as e:
                print(f"could not load metadata: {metadata_file}, because of exception: {e}")
                os.remove(metadata_path)
                return

        # download images
        for idx, media in enumerate(metadata["media"]):
            # skip media entries without available url
            if "identifier" not in media:
                continue
            media_path = os.path.join(occurrence_path, f"media_{idx:04d}.jpg")
            if not os.path.exists(media_path):
                media_tmp_path = os.path.join(occurrence_path, f"media_{idx:04d}.tmp")
                with open(os.devnull, 'w') as devnull:
                    subprocess.call(["wget", media["identifier"], "-O", media_tmp_path], stdout=devnull, stderr=devnull)
                try:
                    image = Image.open(media_tmp_path)
                    image = image.convert("RGB")
                    image.save(media_path)
                    os.remove(media_tmp_path)
                except Exception as e:
                    print(f"could not load image: {media_tmp_path}, because of exception: {e}")
                    continue

    def download(self, chunk_size: int = 1000):
        os.makedirs(self.download_path, exist_ok=True)

        df_iterator = pd.read_csv(self.occurrence_file_path, encoding="utf-8", sep="\t", quotechar="", quoting=3,
                                  chunksize=chunk_size)

        widgets = [' [',
                   progressbar.Timer(format='elapsed time: %(elapsed)s'),
                   '] ',
                   progressbar.Bar('*'), ' (',
                   progressbar.ETA(), ') ',
                   ]

        bar = progressbar.ProgressBar(max_value=self.num_items, widgets=widgets).start()

        # Create and start the download threads
        def _download_chunk():
            while True:
                with self.lock:
                    try:
                        df = next(df_iterator)
                    except StopIteration:
                        # No more occurrence keys, exit the thread
                        return

                for row in df.iterrows():
                    self._download_occurrence(row[1])
                    with self.lock:
                        bar.increment()

        threads = []
        for _ in range(self.num_threads):
            thread = threading.Thread(target=_download_chunk)
            thread.start()
            threads.append(thread)

        # Wait for all download threads to finish
        for thread in threads:
            thread.join()
