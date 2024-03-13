import os
import shutil
import getpass
import tkinter as tk
from tkinter import messagebox

# Function to clean the temp files and show completion message
def clean_temp_files():
    # Your file cleaning logic here
    
    # Show completion message with info icon
    messagebox.showinfo("انتهاء - by:Essam", "تم تنظيف الملفات المؤقتة بنجاح!")

root = tk.Tk()
root.withdraw()

# Show starting message with info icon
messagebox.showinfo("بدء - by:Essam", "سيبدأ تنظيف الملفات المؤقتة الآن.")

# Start cleaning process
root.after(100, clean_temp_files)

# Start the Tkinter loop
root.mainloop()





