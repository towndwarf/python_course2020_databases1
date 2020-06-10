from tkinter import messagebox

messagebox.showinfo("מידע","Informative message")
messagebox.showerror("Error", "הודעת שגיה")
messagebox.showwarning("Warning","Warning message אני השתגעתי")

answer = messagebox.askokcancel("Question","Do you want to open this file?")
answer = messagebox.askretrycancel("Question", "Do you want to try that again?")
answer = messagebox.askyesno("Question","Do you like Python?")
answer = messagebox.askyesnocancel("Question", "Continue playing?")