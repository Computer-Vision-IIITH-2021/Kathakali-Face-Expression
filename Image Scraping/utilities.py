# Import libraries
import pickle
import os
from pytrie import StringTrie as Trie

TRIE_URLS_DATA_STRUCT_PATH = './trie_urls.pkl'

class ImageUrls:
    def __init__(self) -> None:
        '''
            Class to store all the URLs found so far
        '''

        # Check if the trie data structure already exists
        if os.path.isfile(TRIE_URLS_DATA_STRUCT_PATH):
            with open(TRIE_URLS_DATA_STRUCT_PATH, "rb") as file_trie:
                temp = pickle.load(file_trie)
                self.trie_urls = temp.trie_urls
                self.len = temp.len
        else:
            self.trie_urls = Trie()
            self.len = 0
    
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
        with open(TRIE_URLS_DATA_STRUCT_PATH, "wb") as file_output:
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

if __name__ == "__main__":
    i = ImageUrls()
    # i.add('https://google.com/')
    # i.add('https://yandex.com/')
    print(i.fetch_all_urls())
    del i # this is necessary. Else there will be run time error.