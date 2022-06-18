import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

username = os.getlogin()
downloads = os.path.join('C:\\', 'Users', username, 'Downloads\\')
doc_destination = os.path.join('C:\\', 'Users', username, 'Downloads', 'Documents\\')
img_destination = os.path.join('C:\\', 'Users', username, 'Downloads', 'Images\\')
ins_destination = os.path.join('C:\\', 'Users', username, 'Downloads', 'Installer\\')
ppt_destination = os.path.join('C:\\', 'Users', username, 'Downloads', 'PowerPoint\\')
sys_destination = os.path.join('C:\\', 'Users', username, 'Downloads', 'System-Files\\')
web_destination = os.path.join('C:\\', 'Users', username, 'Downloads', 'Website-Files\\')
zip_destination = os.path.join('C:\\', 'Users', username, 'Downloads', 'Archives\\')

if not os.path.exists(doc_destination):
    os.mkdir(doc_destination)
else:
    pass

if not os.path.exists(img_destination):
    os.mkdir(img_destination)
else:
    pass

if not os.path.exists(ins_destination):
    os.mkdir(ins_destination)
else:
    pass

if not os.path.exists(ppt_destination):
    os.mkdir(ppt_destination)
else:
    pass

if not os.path.exists(sys_destination):
    os.mkdir(sys_destination)
else:
    pass

if not os.path.exists(web_destination):
    os.mkdir(web_destination)
else:
    pass

if not os.path.exists(zip_destination):
    os.mkdir(zip_destination)
else:
    pass


class Watcher():
    DIRECTORY_TO_WATCH = downloads

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created' or event.event_type == 'modified':
            # Take any action here when a file is first created.
            print('event here')
            print(event)
            file_mover()


def file_mover():
    while True:
        download_dir = os.listdir(downloads)
        try:
            for file in download_dir:
                # documents
                if file.lower().endswith('.pdf'):
                    shutil.move(os.path.join(downloads, file), os.path.join(doc_destination, file))

                elif file.lower().endswith('.doc'):
                    shutil.move(os.path.join(downloads, file), os.path.join(doc_destination, file))

                elif file.lower().endswith('.docx'):
                    shutil.move(os.path.join(downloads, file), os.path.join(doc_destination, file))


                # installer
                elif file.lower().endswith('.exe'):
                    shutil.move(os.path.join(downloads, file), os.path.join(ins_destination, file))

                elif file.lower().endswith('.msi'):
                    shutil.move(os.path.join(downloads, file), os.path.join(ins_destination, file))


                # powerpoint
                elif file.lower().endswith('.pptx'):
                    shutil.move(os.path.join(downloads, file), os.path.join(ppt_destination, file))

                elif file.lower().endswith('.potx'):
                    shutil.move(os.path.join(downloads, file), os.path.join(ppt_destination, file))


                # system-files
                elif file.lower().endswith('.dll'):
                    shutil.move(os.path.join(downloads, file), os.path.join(sys_destination, file))

                elif file.lower().endswith('.conf'):
                    shutil.move(os.path.join(downloads, file), os.path.join(sys_destination, file))

                elif file.lower().endswith('.pfx'):
                    shutil.move(os.path.join(downloads, file), os.path.join(sys_destination, file))


                # images
                elif file.lower().endswith('.png'):
                    shutil.move(os.path.join(downloads, file), os.path.join(img_destination, file))

                elif file.lower().endswith('.jpg'):
                    shutil.move(os.path.join(downloads, file), os.path.join(img_destination, file))

                elif file.lower().endswith('.jpeg'):
                    shutil.move(os.path.join(downloads, file), os.path.join(img_destination, file))

                elif file.lower().endswith('.svg'):
                    shutil.move(os.path.join(downloads, file), os.path.join(img_destination, file))


                # archives
                elif file.lower().endswith('.zip'):
                    shutil.move(os.path.join(downloads, file), os.path.join(zip_destination, file))


                # website-files
                elif file.lower().endswith('.html'):
                    shutil.move(os.path.join(downloads, file), os.path.join(web_destination, file))

                elif file.lower().endswith('.css'):
                    shutil.move(os.path.join(downloads, file), os.path.join(web_destination, file))

                elif file.lower().endswith('.scss'):
                    shutil.move(os.path.join(downloads, file), os.path.join(web_destination, file))

                elif file.lower().endswith('.sass'):
                    shutil.move(os.path.join(downloads, file), os.path.join(web_destination, file))

                elif file.lower().endswith('.js'):
                    shutil.move(os.path.join(downloads, file), os.path.join(web_destination, file))

                elif file.lower().endswith('.ts'):
                    shutil.move(os.path.join(downloads, file), os.path.join(web_destination, file))


                # else
                else:
                    continue
        except:
            continue


if __name__ == '__main__':
    w = Watcher()
    w.run()
