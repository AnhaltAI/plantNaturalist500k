from anhaltai_pic.data.gbif_downloader import GBIFDownloader

if __name__ == '__main__':
    downloader = GBIFDownloader("/storage/datasets/occurrence.txt",
                                "/storage/datasets/iNaturalistRGO",
                                25_000_000,
                                num_threads=64)
    downloader.download(chunk_size=1000)
