#! python3
# filter.py [dir_name] [file_ext] - Search a directory recursively for files with
#									repeat names and separate them into different
#									folders. Enter desired directory to filter
#									and file extension as arguments in the
#									command line.

import glob, os, shutil, sys, time

dir_name = sys.argv[1]
file_ext = sys.argv[2]

orig_dir = 'originals_' + file_ext
rep_dir = 'repeats_' + file_ext
generic_file = './**/*.' + file_ext

if os.path.isdir(orig_dir):
	shutil.rmtree(orig_dir)
	
if os.path.isdir(rep_dir):
	shutil.rmtree(rep_dir)
	
time.sleep(5)

os.makedirs(orig_dir)
os.makedirs(rep_dir)

if not(dir_name == '.' or dir_name == './' or dir_name == '.\\'):
	starting_dir = os.getcwd()
	os.chdir(dir_name)

# initialize empty dictionary and current working directory
filenames_dict = {}
curr_dir = os.getcwd()

print('\nCurrently in', curr_dir, '\n')
print('List of all recursive files:')

# recurse through all files in the directory
for filename in glob.iglob(generic_file, recursive = True):
	
	# extract filenames and filepaths out into our dictionary
	base_name = os.path.basename(filename)
	relative_path = os.path.dirname(filename)
	
	# check if this file has already been seen, then store the relative path
	filenames_dict.setdefault(base_name, [])
	filenames_dict[base_name].append(relative_path)
	
	print(filename)

if not(dir_name == '.' or dir_name == './' or dir_name == '.\\'):
	os.chdir(starting_dir)

for filename in filenames_dict:
	# keep track of how many times we've seen this file
	counter = 0
	print('\nFile ', str(filename),' was found in: ')
	
	for filepath in filenames_dict[filename]:
		counter += 1
		print('Encounter number ', str(counter), ' at path ', str(filepath))
		
		source_dir = './' + dir_name + filepath + '/' + filename
		dest_dir = './' + orig_dir + '/' + filename if counter == 1 else './' + rep_dir + '/' + filename
		shutil.copy(source_dir, dest_dir)
		

