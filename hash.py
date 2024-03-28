import argparse
from functions import no_ext , sha256sum as hash
parser = argparse.ArgumentParser(
                    prog='hash',
                    description='This tool checks the hash of two files if they are the same',
                    epilog = "Example: hash -file=Photo.png "
                    )
parser.add_argument('-file',
'--file' ,
help="you can insert file name to check thae hash",
required=True)

args = parser.parse_args()
try:
 # get the hash of the file if the file exists
 f = open(no_ext(args.file)+"_hash.txt" , "r") # open the hash file
 prev_hash = f.read() # saving the value of the hash inside variable
 # wanted_file_hash is the hash of the file that was givien inside the program
 wanted_file_hash = hash(args.file)
# hash() is a function from the functions module
 if prev_hash == wanted_file_hash: # if the two hashes match
    print("Files Match")
 else: # if the hashes does'nt match
    print("Files Don't Match")
except:
    # if there was an error like the hash file is not found ,
    # the file that was givien to the program not found
    print()
    print(f'1) check {no_ext(args.file)}_hash.txt exists in the folder')
    print(f'*) without {no_ext(args.file)} cant validate the file')
    print(f'2) check that {args.file} exists in the folder')

