from filehash import FileHash
import glob
import os
import getpass

user = getpass.getuser()

list_of_files = glob.glob(f'C:\\Users\\{user}\\Downloads\\*') # * means all if need specific format then *.csv
latest_download = max(list_of_files, key=os.path.getctime)
print(latest_download)

# Enter the correct hash
verify_hash = input('Enter hash: ')

sha256hash = FileHash('sha256')

downloaded_file = sha256hash.hash_file(latest_download)

if downloaded_file  != verify_hash:
    print('STOP!!!! HASH DOES NOT MATCH')
    print('\n')
    print(f'Downloaded hash: {downloaded_file}\n Correct Hash: {verify_hash}')
else:
    print('Success HASH MATCH!!!')

input('\n Press any key to exit')
