import platform
import os 
import subprocess

class PonAny:
    def __init__(self, path):
        self.path = path 
    

    def printonlinux(self):
        try:
            subprocess.run(["lp", self.path], check=True)
            print(f"Printing {self.path}...")
        except subprocess.CalledProcessError as e:
            print(f"Failed to print {self.path}: {e}")
    
def nprint(path) -> None:
    pone = PonAny(path)
    if platform.system() == 'Linux':
        pone.printonlinux()
    elif platform.system() == 'Windows':
        os.startfile(path, "print")
    elif platform.system() == 'Darwin':
        pass 