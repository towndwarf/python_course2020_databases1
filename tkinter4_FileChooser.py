import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
import os

application_window = tk.Tk()

# Build a list of tuples for each file type the file dialog should display
my_filetypes = [('all files', '.*'), ('text files', '.txt')]

# Ask the user to select a folder.
answer4 = filedialog.askdirectory(parent=application_window,
                                  initialdir=os.getcwd(),
                                  title="Please select a folder:")

# Ask the user to select a single file name.
answer3 = filedialog.askopenfilename(parent=application_window,
                                     initialdir=os.getcwd(),
                                     title="Please select a file:",
                                     filetypes=my_filetypes)

# Ask the user to select a one or more file names.
answer2 = filedialog.askopenfilenames(parent=application_window,
                                      initialdir=os.getcwd(),
                                      title="Please select one or more files:",
                                      filetypes=my_filetypes)

# Ask the user to select a single file name for saving.
answer1 = filedialog.asksaveasfilename(parent=application_window,
                                       initialdir=os.getcwd(),
                                       title="Please select a file name for saving:",
                                       filetypes=my_filetypes)

# COLOR CHOOSER
rgb_color, web_color = colorchooser.askcolor(parent=application_window,
                                             initialcolor=(255, 0, 0))
