import shutil
import os.path

#creating the zip file
archived=shutil.make_archive('result','zip','folder')

if os.path.exists('result.zip'):
    print(archived)
else:
    print('ZIP file not created')
