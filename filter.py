import glob, os
os.chdir("./test_dir/")
#os.chdir("/mnt/c/Users/manny/Documents/Git/Directory_filter/test_dir/")

curr_dir = os.getcwd()

print("\nCurrently in", curr_dir, "\n")

print("List of all recursive files:")
for filename in glob.iglob('./**/*.txt', recursive = True):
	print(filename)

