import sys, zipfile
#import os, fnmatch

archive_dir = 'C:\temp\temp_zip_archive'
#output_file = '_Filtered_output.txt'
#output = open(output_file,'w')

# there is a commandline
if len(sys.argv) > 1:
    arglist = []
    # sys.argv[0] is the program filename, slice it off
    for element in sys.argv[1:]:
        arglist.append(element)
else:
    print "usage %s element1 element2 [element3 ...]" % sys.argv[0]
    sys.exit(1)
# if the arguments were 1 2 3 4 5
# arglist should be ['1', '2', '3', '4', '5']
#print(arglist)

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.psv'):
		print "Processing file " + file + "..."
		input = open(file)
		for i, line in enumerate(input):
			if i > 1:
				if line.startswith(tuple(arglist)):
					output.write(line)
		input.close()	
		
output.close()
print "Done."
os.system(output_file)

