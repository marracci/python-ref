
# python utility for listing files within a directory				#
#   which have a specific set of characters in the filename			#
#   and then copying that list of files to a specific directory 	#
#																	#


import glob  # py util, used for listing filenames with wildcards
import shutil  # py util, used for copying to specific directory

for name in glob.glob('/users/myUsername/desktop/tmp/*SHAPE*.*'):     # using '*' before and after
    print name														   # lists out the files it finds
    shutil.copy(name,'/users/myUsername/destinationDir/')	           # copies over those files to the dir

print('all done!')													   # indicates finished
