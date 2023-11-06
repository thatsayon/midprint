import platform
import os 
import subprocess

class PonAny:
    def __init__(self, path):
        self.path = path 
    

    def print_on_linux(self):
        try:
            subprocess.run(["lp", self.path], check=True)
            print(f"Printing {self.path}...")
        except subprocess.CalledProcessError as e:
            print(f"Failed to print {self.path}: {e}")

    def print_on_windows(file_to_print):
        try:
            # Get the default printer
            printer_name = win32print.GetDefaultPrinter()
            printer_handle = win32print.OpenPrinter(printer_name)

            # Set up the printer job
            printer_info = win32print.GetPrinter(printer_handle, 2)
            printer_job = win32print.StartDocPrinter(printer_handle, 1, ("My Document", None, "RAW"))
            win32print.StartPagePrinter(printer_handle)

            # Open the file to print
            file = open(file_to_print, "rb")

            # Read the file content and send it to the printer
            data = file.read()
            win32ui.ExtTextOut(printer_job, 100, 100, 0, 0, data)

            # End the printing job
            win32print.EndPagePrinter(printer_handle)
            win32print.EndDocPrinter(printer_handle)
            win32print.ClosePrinter(printer_handle)

            # Close the file
            file.close()

            print(f"Printing {file_to_print} on the default printer")

        except Exception as e:
            print(f"Failed to print {file_to_print}: {e}")
        

def nprint(path) -> None:
    pone = PonAny(path)
    if platform.system() == 'Linux':
        pone.print_on_linux()
    elif platform.system() == 'Windows':
        pone.print_on_windows()
    elif platform.system() == 'Darwin':
        pone.print_on_linux()

