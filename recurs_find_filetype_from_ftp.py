# use to recursively find all .[ext] in a FTP location, including subdirs
# dumps all .[ext] into same dir as the .py location
# with ipython, use:  $ %run get_all_shp_ftp.py

#!/usr/bin/env python



from ftplib import FTP
from time import sleep
import os

my_dirs = []  # global
my_files = [] # global
curdir = ''   # global

def get_dirs(ln):
  global my_dirs
  global my_files
  cols = ln.split(' ')
  objname = cols[len(cols)-1] # file or directory name
  if ln.startswith('d'):
    my_dirs.append(objname)
  else:
    if objname.endswith('.dbf'):  # change '.dbf' to the needed file extension
      my_files.append(os.path.join(curdir, objname)) # full path

def check_dir(adir):
  global my_dirs
  global my_files # let it accrue, then fetch them all later
  global curdir
  my_dirs = []
  gotdirs = [] # local
  curdir = ftp.pwd()
  print("going to change to directory " + adir + " from " + curdir)
  ftp.cwd(adir)
  curdir = ftp.pwd()
  print("now in directory: " + curdir)
  ftp.retrlines('LIST', get_dirs)
  gotdirs = my_dirs
  print("found in " + adir + " directories:")
  print(gotdirs)
  print("Total files found so far: " + str(len(my_files)) + ".")
  sleep(1)
  for subdir in gotdirs:
    my_dirs = []
    check_dir(subdir) # recurse  
    
  ftp.cwd('..') # back up a directory when done here
  
try:
  ftp = FTP('subdomain.domain.com')
  print('test1') # ensure ftp server correct, if so, will print
  ftp.login('user','password')
  print('test2') # ensure ftp server correct, if so, will print
  check_dir('/startingDir')
  print('test3') # directory to start in
  # ftp.cwd('/.') # change to root directory for downloading (uncomment if dumping to ftp location)
  # print('test4') 
  for f in my_files:
    print('getting ' + f)
    file_name = f.replace('/', '_') # use path as filename prefix, with underscores
    ftp.retrbinary('RETR ' + f, open(file_name, 'wb').write)
    sleep(1)
except:
  print('oh dear.')
  ftp.quit()

ftp.quit()
print('all done!')