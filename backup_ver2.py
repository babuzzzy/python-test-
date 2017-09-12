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

if not os.path.exists(target_dir):
    os.mkdir(target_dir)


# 3. the files are backed up into a zip file
# 4. The current day is the name of the subdirectory
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')
# The name of the zip file
target = today + os.sep + now +'.zip'

# Create the subdirectory if it isn't alreay there
if not os.path.exists(today):
    os.mkdir(today) # make directory
    print 'Successfully created directory', today

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


