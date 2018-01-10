#! python3
# filter.py [ext] - Search a directory recursive for files with repeat names and
#					separate them into different folders. Enter desired file
#					extension as an argument in the command line.

import glob, os, shutil, sys

arg_in = sys.argv[1]
orig_dir = "originals_" + arg_in
rep_dir = "repeats_" + arg_in
generic_file = "./**/*." + arg_in

os.makedirs(orig_dir)
os.makedirs(rep_dir)
os.chdir("./test_dir/")

# initialize empty dictionary and current working directory
filenames_dict = {}
curr_dir = os.getcwd()

print("\nCurrently in", curr_dir, "\n")
print("List of all recursive files:")

# recurse through all files in the directory
for filename in glob.iglob(generic_file, recursive = True):
	
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
			dest_dir = "./" + orig_dir + "/" + filename
			shutil.move( source_dir, dest_dir )
			
		else:
			source_dir = "./test_dir/" + filepath + "/" + filename
			dest_dir = "./" + rep_dir + "/" + filename
			shutil.move( source_dir, dest_dir )