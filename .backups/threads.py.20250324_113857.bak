# threads.py

from PyQt5.QtCore import QThread, pyqtSignal
import subprocess
import time

class ScrcpyThread(QThread):
    error_occurred = pyqtSignal(str)
    
    def __init__(self, command):
        super().__init__()
        self.command = command
        
    def run(self):
        try:
            subprocess.run(self.command, check=True)
        except Exception as e:
            self.error_occurred.emit(str(e))