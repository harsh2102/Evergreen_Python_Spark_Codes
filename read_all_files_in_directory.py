from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('folder_name/') if isfile(join('folder_name/', f))]
print(onlyfiles)
