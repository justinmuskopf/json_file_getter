import os
import sys
import subprocess
from json_file_getter import JsonFileGetter

save_location = os.path.dirname(os.path.realpath(__file__)) + os.sep + 'img'

file_path = JsonFileGetter.save_file_from_url('http://xkcd.com/info.0.json', 'img', save_location)

# Shamelessy stolen from https://stackoverflow.com/questions/35304492/python-open-multiple-images-in-default-image-viewer
imageViewerFromCommandLine = {'linux':'xdg-open',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
p = subprocess.run([imageViewerFromCommandLine, file_path])
