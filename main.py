import os
import shutil

downloads = "/storage/emulated/0/Download"
images = ("jpg", "jpeg", "png", "svg")
docs = ('.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.xlsx', '.pptx')
images_saved  = "/storage/emulated/0/Pictures/downloads"
docs_saved  = "/storage/emulated/0/Documents"


for root, dirs, files in os.walk(downloads):
    for file in files:
        if file.endswith(images):
            path = os.path.join(root, file)
            shutil.move(path, images_saved)
            print(path)
            
        elif file.endswith(docs):
            path = os.path.join(root, file)
            shutil.move(path, docs_saved)
            print(path)
        
        