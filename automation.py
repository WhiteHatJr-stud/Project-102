import os
import shutil

folderPath = input("Enter the path of the directory: ")
listOfFiles = os.listdir(folderPath)



for file in listOfFiles:
    name, ext = os.path.splitext(file)

    if(ext == ""):
        continue

    source = folderPath + "/" + file
    dest = folderPath + "/" + ext + "/" + file
    print(name)
    print(ext[1:])
    print(source)
    print(dest)
    print("----------------------------------------------------------------------")
    if(os.path.exists(folderPath + "/" + ext)):
        
        shutil.move(source, dest)
    else:
        os.mkdir(folderPath + "/" + ext)
        shutil.move(source, dest)

        

   