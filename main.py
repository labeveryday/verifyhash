#!/usr/bin/env python
import csv
import glob
import os
import getpass
from filehash import FileHash
from tabulate import tabulate
from pathlib import Path


def get_file():
    """
    Function locates the latest downloaded file from the
    current user's download directory.
        return: string of the latest downloaded file
        rtype: str
    """
    home = Path.home() / 'Downloads/' / '*'
    list_of_files = glob.glob(str(home))
    latest_download = max(list_of_files, key=os.path.getctime)
    return latest_download

def get_hash(latest_download, hash_type='sha256'):
    # sha256hash = FileHash('sha256')
    sha256hash = FileHash(hash_type)
    downloaded_file = sha256hash.hash_file(latest_download)
    return downloaded_file

def print_hash_results(latest_download, downloaded_file, verify_hash, hash_type):
    print("\n", " " * 33, "-" * 20, "FILEHASH RESULTS", "-" * 20, "\n")
    if downloaded_file  == verify_hash.strip():
        print(" " * 39, "*" * 10, "✅ Success HASH MATCH!!! ✅", "*" * 10)
    else:
        print(" " * 33, "*" * 10, "❌ FAILED!!!! HASH DOES NOT MATCH ❌", "*" * 10)
        print('\n')
    print(tabulate([["Downloaded File: " + latest_download, verify_hash],
                    ["Verified Hash: " + " " * len(latest_download),
                    downloaded_file]], headers=["FileName", f"{hash_type} FileHash"],
                    tablefmt="pretty"))
    input('\n Press enter to exit')


if __name__ == "__main__":
    # Enter the verified hash
    verify_hash = input('Enter verified hash: ')
    hash_type = input('Enter hashtype: ')
    latest_download = get_file()
    downloaded_file = get_hash(latest_download)
    print_hash_results(latest_download, downloaded_file,
                       verify_hash, hash_type)
