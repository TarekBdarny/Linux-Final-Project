import argparse
import os
from functions import no_ext , sha256sum as hash , decode_file
parser = argparse.ArgumentParser(
                    prog='decrypt',
                    description='This tool decrypt a file ,  allow permissions and check hash for the file',
                    epilog = "Example: decrypt.py -file=Photo.jpeg "
                    )
parser.add_argument('-file',
'--file' ,
help="you can insert file name to decrypt the file",
required=True)

args = parser.parse_args()
# change permission of the file make it read write execute
# so we can decode the file , without changing permissions we cant decode the file

os.chmod(args.file , 0o777)

# function that decodes the given file
decode_file(args.file)
#decode_file() is a function from the functions module
try:
 # getting the hash of the file 
 f= open(no_ext(args.file)+"_hash.txt" , "r")
 prev_hash = f.read() # storing the value inside variable
 wanted_file_hash = hash(args.file) # making hash for the file that was given to the program
   # if the hashes match
 if prev_hash == wanted_file_hash:
    print("Files Match")
 else:
    print("Files Don't Match")
except:
    # if there was an error like the hash file is not found ,
    # the file that was givien to the program not found
    print()
    print(f'1) check {no_ext(args.file)}_hash.txt exists in the folder')
    print(f'*) without {no_ext(args.file)} cant validate the file')
    print(f'2) check that {args.file} exists in the folder')