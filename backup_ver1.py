# -*- coding:utf-8 -*-
import os
import time
#안녕
# 1. the files and directories to backed up are
# specified in a list.
# Example on Windows:
source = ['"C:\\My Documents"', 'C:\\Code']
# Example on max os x and linux:
# source = ['/Users/swa/notes']
# Notice we had to use double quotes inside the string
# for names with spaces in it

# 2. The backup must be stored in a
# main backup directory
# Example on Windows:
target_dir = 'C:\\Backup'
# Example on Mac OS X and Linux:
# target_dir='/User/swa/backup'


# 3. the files are backed up into a zip file
# 4. The name of the zip archive is the current date and time
target = target_dir + os.sep + \
    time.strftime('%Y%m%d%H%M%S') + '.zip'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory

# 5. We use the zip command to put the files in a zip archive
zip_command = "zip -r {0} {1}".format(target,' '.join(source))

# Run the backup
print "zip command is:"
print zip_command
print "Running"
if os.system(zip_command) == 0:
    print 'Successful backup to',target
else:
    print 'Backup FAILED'
