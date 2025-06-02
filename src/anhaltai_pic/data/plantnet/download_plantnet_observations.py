from anhaltai_pic.data.gbif_downloader import GBIFDownloader

if __name__ == '__main__':
    downloader = GBIFDownloader("/storage/datasets/plantnet-observations/occurrence.txt",
                                "/storage/datasets/PlantNetO",
                                1_800_000,
                                num_threads=64)
    downloader.download(chunk_size=1000)
