# importing other models in python - system, global and OS (navigate within computer)
import sys, glob, os

# Get the directory name
# HOME for Mac
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# HOME will be JBL70 - wildcard is the *
pattern = os.path.join(hdir,'*')
print(pattern)

# OBTAIN LIST OF FILENAMES
# TODO: Use the glob.glob() function to obtain the list of filenames
# glob.glob goes into my file directory and names my files
filenames = glob.glob(pattern)
print(filenames)

# FULL LOOP
# TODO: use os.path.getsize to find each file's size
# to obtain each file, need full loop rather than list of files
# the below shows: for a file in my filenames list, print me the size of each file
for file in filenames:
    print(os.path.getsize(file))

# FULL LOOP AND IF STATEMENT
# TODO: Add a test to only display files that are not zero length
# # checks each item and prints the file name and size if the file size is greater than 0
for file in filenames:
    size = os.path.getsize(file)
    if size >0:
        print(file, size)

# FULL LOOP AND IF STATEMENT
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
# for means full loop is starting
# everything after the first statement needs to be indented
for file in filenames:
    size = os.path.getsize(file)
    if size >0:
        print(os.path.basename(file))

