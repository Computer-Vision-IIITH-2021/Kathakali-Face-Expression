from bing_image_downloader import downloader
import pickle
list_urls = downloader.download("kathakali", limit=10000, output_dir='../dataset/', adult_filter_off=True, timeout=60, verbose=True)

with open("./urls_bing_external.pkl", "wb") as file_output:
    pickle.dump(list_urls, file_output)