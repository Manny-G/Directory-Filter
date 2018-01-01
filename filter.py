#! python3
# filter.py - Search a directory recursive for files with repeat names and
#			  separate them into different folders

import glob, os, shutil

os.makedirs("originals")
os.makedirs("repeats")
os.chdir("./test_dir/")

# initialize empty dictionary and current working directory
filenames_dict = {}
curr_dir = os.getcwd()

print("\nCurrently in", curr_dir, "\n")
print("List of all recursive files:")

# recurse through all files in the directory
for filename in glob.iglob('./**/*.txt', recursive = True):
	
	# extract filenames and filepaths out into our dictionary
	base_name = os.path.basename(filename)
	relative_path = os.path.dirname(filename)
	
	# check if this file has already been seen, then store the relative path
	filenames_dict.setdefault( base_name, [] )
	filenames_dict[base_name].append( relative_path )
	
	print(filename)

os.chdir("../")



for filename in filenames_dict:
	# keep track of how many times we've seen this file
	counter = 0
	print( "\nFile '{}' was found in: ".format(filename) )
	
	for filepath in filenames_dict[filename]:
		counter += 1
		print( "Encounter number {} at path {}".format(counter, filepath) )
		
		if counter == 1:
			source_dir = "./test_dir/" + filepath + "/" + filename
			dest_dir = "./originals/" + filename
			shutil.move( source_dir, dest_dir )
			
		else:
			source_dir = "./test_dir/" + filepath + "/" + filename
			dest_dir = "./repeats/" + filename
			shutil.move( source_dir, dest_dir )