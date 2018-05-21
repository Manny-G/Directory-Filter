#! python3
# filter.py [dir_name] [file_name] [regex_on] [case_sensitivity]
# Recursively looks in dir_name for a pattern 'file_name,' whose meaning is
# determined by the regex_on parameter. If regex is off (off by default) it will
# default to searching each file name from left to right and will match if the
# input file_name is found at the beginning (this case exists for when you're
# searching for file_name values that would be interpreted as something else in
# regex, such as '._'). If regex is on then it will look for a pattern in the
# file's name (case sensitive by default).

import glob, os, re, shutil, sys, time

dir_name = sys.argv[1]
file_name = sys.argv[2]

found_dump = 'found_dump'

if os.path.isdir(found_dump):
	shutil.rmtree(found_dump)

time.sleep(5)

os.makedirs(found_dump)
absolute_path_found_dump = os.path.abspath(found_dump)

error_log = open('error_log.txt', 'w')

try:
	if sys.argv[3] == '1' or sys.argv[3] == 'true' or sys.argv[3] == 'True':
		regex_on = True
	
	elif sys.argv[3] == '0' or sys.argv[3] == 'false' or sys.argv[3] == 'False':
		regex_on = False
		
except:
	regex_on = False
	print('no valid sys.argv[3] (regex_on) input, setting to default value', regex_on)

try:
	if sys.argv[4] == '1' or sys.argv[4] == 'true' or sys.argv[4] == 'True':
		case_sensitive = True
	
	elif sys.argv[4] == '0' or sys.argv[4] == 'false' or sys.argv[4] == 'False':
		case_sensitive = False

except:
	case_sensitive = True
	print('no valid sys.argv[4] (case_sensitive) input, setting to default value', case_sensitive)

if not(dir_name == '.' or dir_name == './' or dir_name == '.\\'):
	starting_dir = os.getcwd()
	os.chdir(dir_name)

curr_dir = os.getcwd()

print('\nCurrently in', curr_dir, '\n')

# recurse through all files in the directory
for dirs, subdirs, files in os.walk(curr_dir):
	for file in files:
		if dirs != absolute_path_found_dump:
		
			if regex_on == True:
				pattern = re.compile(str(file_name)) if case_sensitive == True else re.compile(str(file_name), re.IGNORECASE)
				result = pattern.search(file)
				if result != None:
					print('file with name', file, 'had pattern', str(file_name), 'in position', result.span(),
					      '(case insensitive)')
					source_dir = os.path.join(dirs, file)
					dest_dir = os.path.join(absolute_path_found_dump, file)
					
					try:
						print('moving', source_dir, 'into', dest_dir, '\n')
						shutil.move(source_dir, dest_dir)
					except:
						error_log.write('in directory %s\n' % str(dirs))
						error_log.write('on file %s\n' % str(file))
			
			else:
				if file.startswith(str(file_name)):
					print('file with name', file, 'had pattern', str(file_name))
					source_dir = os.path.join(dirs, file)
					dest_dir = os.path.join(absolute_path_found_dump, file)
					
					try:
						print('moving', source_dir, 'into', dest_dir, '\n')
						shutil.move(source_dir, dest_dir)
						
					except:
						error_log.write('in directory %s\n' % str(dirs))
						error_log.write('on file %s\n' % str(file))

if not(dir_name == '.' or dir_name == './' or dir_name == '.\\'):
	os.chdir(starting_dir)

error_log.flush()
error_log.close()

if os.path.getsize('error_log.txt') == 0:
	os.remove('error_log.txt')