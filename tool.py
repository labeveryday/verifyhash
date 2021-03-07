import csv
import glob
import os
import getpass
from filehash import FileHash
from tabulate import tabulate
from pathlib import Path
from time import sleep


def get_file():
    home = Path.home() / 'Downloads/' / '*'
    list_of_files = glob.glob(str(home))
    latest_download = max(list_of_files, key=os.path.getctime)
    return latest_download

def get_hash(latest_download, hash_type='sha256'):
    # sha256hash = FileHash('sha256')
    sha256hash = FileHash(hash_type)
    downloaded_file = sha256hash.hash_file(latest_download)
    return downloaded_file

def print_hash_results(latest_download, downloaded_file, web_address, verify_hash):
    print("-----------FILEHASH RESULTS-----------")
    print(tabulate([[latest_download, downloaded_file], [web_address, verify_hash]],
                            headers=["FileName", "FileHash"], tablefmt="pretty"))
    if downloaded_file  == verify_hash:
        print('\n✅ Success HASH MATCH!!! ✅')
    else:
        print('\n❌ FAILED!!!! HASH DOES NOT MATCH ❌')
        print('\n')
        print(f'Downloaded hash: {downloaded_file}\n Correct Hash: {verify_hash}')
    input('\n Press any key to exit')

if __name__ == "__main__":
    # Enter the verified hash
    verify_hash = input('Enter hash: ')
    web_address = input('Enter web address:')
    hash_type = input('Enter hashtype: ')
    latest_download = get_file()
    downloaded_file = get_hash(latest_download)
    print_hash_results(latest_download, downloaded_file, web_address, verify_hash)

# Note need to clean up the file and create an output to csv to track csv