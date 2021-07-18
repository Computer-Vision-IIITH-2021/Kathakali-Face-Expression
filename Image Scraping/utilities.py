# Import libraries
import pickle
import os
from pytrie import StringTrie as Trie
import sys
sys.setrecursionlimit(100000)

TRIE_URLS_DATA_STRUCT_PATH = './trie_urls.pkl' # stores all the URLs
TRIE_URLS_DOWNLOAD_PATH = './trie_downloaded_urls.pkl' # stores all the URLs that have been downloaded

class ImageUrls:
    def __init__(self, category: str = 'url') -> None: # category can be either {url, download}
        '''
            Class to store all the URLs found so far
        '''
        if category == 'url':
            # Check if the trie data structure already exists
            if os.path.isfile(TRIE_URLS_DATA_STRUCT_PATH):
                with open(TRIE_URLS_DATA_STRUCT_PATH, "rb") as file_trie:
                    temp = pickle.load(file_trie)
                    self.trie_urls = temp.trie_urls
                    self.len = temp.len
            else:
                self.trie_urls = Trie()
                self.len = 0
        elif category == 'download':
            if os.path.isfile(TRIE_URLS_DOWNLOAD_PATH):
                with open(TRIE_URLS_DOWNLOAD_PATH, "rb") as file_trie:
                    temp = pickle.load(file_trie)
                    self.trie_urls = temp.trie_urls
                    self.len = temp.len
            else:
                self.trie_urls = Trie()
                self.len = 0
        else: raise Exception("Error: Invalid category")
        self.category = category
    
    def add(self, url: str) -> None:
        '''
            Adds a URL to the data structure
        '''
        self.trie_urls[url] = 0
        self.len += 1
    
    def delete(self, url: str) -> None:
        '''
            Deletes a URL from the data structure
        '''
        del self.trie_urls[url]
        self.len -= 1
    
    def contains(self, url: str) -> bool:
        '''
            Checks for the existence of the URL in the data structure
        '''
        return url in self.trie_urls
    
    def __del__(self) -> None: # Please explicitly call the del object_reference for this to work
        # saving the trie data structure
        if self.category == "url":
            with open(TRIE_URLS_DATA_STRUCT_PATH, "wb") as file_output:
                pickle.dump(self, file_output)
        elif self.category == "download":
            with open(TRIE_URLS_DOWNLOAD_PATH, "wb") as file_output:
                pickle.dump(self, file_output)
    
    def fetch_all_urls(self) -> list:
        '''
            Fetches all the URLs stored in the data structure in the form of a list
        '''
        return self.trie_urls.keys()
    
    def add_all_urls(self, urls: list) -> None:
        '''
            Adds multiple URLs in the datastructure
        '''
        for url in urls:
            self.add(url)

# # Fetch all the URLs stored in the data structure
# if __name__ == "__main__":
#     i = ImageUrls()
#     # i.add('https://google.com/')
#     # i.add('https://yandex.com/')
#     print(i.fetch_all_urls())
#     del i # this is necessary. Else there will be run time error.

# # Fetch the number of URLs stored in the data structure
# if __name__ == "__main__":
#     i = ImageUrls()
#     print(i.len, i.category)
#     del i

# Shift all the URLs in the data structure to a text file
if __name__ == "__main__":
    FILE_NAME = "./trie_urls.txt"
    i = ImageUrls()
    with open(FILE_NAME, "w") as file_output:
        for url in i.fetch_all_urls():
            file_output.write(url + '\n')
        file_output.write('\n')
    del i

# # Shift all the URLs in the text file to the data structure
# if __name__ == "__main__":
#     FILE_NAME = "./trie_urls.txt"
#     i = ImageUrls()
#     with open(FILE_NAME, "r") as file_input:
#         while True:
#             url = file_input.readline().replace("\n", "")
#             if url == "": break
#             i.add(url)
#     del i

# # Shift all the downloaded URLs in the data structure to a text file
# if __name__ == "__main__":
#     FILE_NAME = "./trie_downloaded_urls.txt"
#     i = ImageUrls(category='download')
#     with open(FILE_NAME, "w") as file_output:
#         for url in i.fetch_all_urls():
#             file_output.write(url + '\n')
#         file_output.write('\n')
#     del i

# # Shift all the downloaded URLs in the text file to the data structure
# if __name__ == "__main__":
#     FILE_NAME = "./trie_downloaded_urls.txt"
#     i = ImageUrls(category='download')
#     with open(FILE_NAME, "r") as file_input:
#         while True:
#             url = file_input.readline().replace("\n", "")
#             if url == "": break
#             i.add(url)
#     del i