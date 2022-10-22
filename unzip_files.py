from zipfile import ZipFile

with ZipFile('filename.zip', 'r') as zip_object:
    zip_object.extractall()

#list of files that are extracted from Zipped file
print(zip_object.namelist())