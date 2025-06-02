from anhaltai_pic.data.gbif_downloader import GBIFDownloader

if __name__ == '__main__':
    downloader = GBIFDownloader("/storage/datasets/gbif/inaturalist-300k/occurrence.txt",
                                "/storage/datasets/gbif/inaturalist-300k/data",
                                301_000,
                                num_threads=16)
    downloader.download(chunk_size=1000)
