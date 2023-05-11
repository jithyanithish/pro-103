import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/harish chandar/Downloads"

class Fileeventhandler(FileSystemEventHandler):
    def on_created(self,event):
        print("created a new file")
    def on_deleted(self,event):
        print("file has been deleted")
    def on_moved(self,event):
        print("file has been moved")

eventhandler=Fileeventhandler()
observer=Observer()
observer.schedule(eventhandler,from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
