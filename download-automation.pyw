import os
import shutil
from pathlib import WindowsPath

downloads = os.path.join('C:\\', 'Users', os.getlogin(), 'Downloads\\')
doc_destination = os.path.join('C:\\', 'Users', os.getlogin(), 'Documents', 'Download-Automation', 'Documents\\')
ppt_destination = os.path.join('C:\\', 'Users', os.getlogin(), 'Documents', 'Download-Automation', 'PowerPoint\\')
zip_destination = os.path.join('C:\\', 'Users', os.getlogin(), 'Documents', 'Download-Automation', 'Archives\\')
img_destination = os.path.join('C:\\', 'Users', os.getlogin(), 'Documents', 'Download-Automation', 'Images\\')
ins_destination = os.path.join('C:\\', 'Users', os.getlogin(), 'Documents', 'Download-Automation', 'Installer\\')
sys_destination = os.path.join('C:\\', 'Users', os.getlogin(), 'Documents', 'Download-Automation', 'System-Files\\')
downloadfiles = os.listdir(downloads)

for file in downloadfiles:
    if file.endswith('.pdf'):
        shutil.move(os.path.join(downloads, file), os.path.join(doc_destination, file))
    else:
        continue


    if file.endswith('.pptx') or file.endswith('.potx'):
        shutil.move(os.path.join(downloads, file), os.path.join(ppt_destination, file))
    else:
        continue


    if file.endswith('.dll') or file.endswith('.conf'):
        shutil.move(os.path.join(downloads, file), os.path.join(sys_destination, file))
    else:
        continue


    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.svg'):
        shutil.move(os.path.join(downloads, file), os.path.join(img_destination, file))
    else:
        continue


    if file.endswith('.zip'):
        shutil.move(os.path.join(downloads, file), os.path.join(zip_destination, file))
    else:
        continue