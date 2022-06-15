import os
import shutil

downloads = 'C:/Temp/'
downloadfiles = os.listdir(downloads)
pdf_destination = 'C:/Destination/PDF-Files/'
count = 0
for file in downloadfiles:
    count = count + 1
    print(count)
    if file.endswith('.pdf'):
        shutil.move(os.path.join(downloads, file), os.path.join(pdf_destination, file))
    else:
        continue
