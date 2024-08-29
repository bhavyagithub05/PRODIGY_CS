import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]',password))
    lowercase_criteria = bool(re.search(r'[a-z]',password))
    number_criteria = bool(re.search(r'[0-9]',password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]',password))

    
    criteria_met = sum([length_criteria,uppercase_criteria,lowercase_criteria,number_criteria,special_criteria])

    if criteria_met == 5:
        return "Strong"
    elif criteria_met >=3:
        return "Moderate"
    else:
        return "Weak"
    
def evaluate_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error","Please enter a password to check.")
        return

    strength = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}")

root = tk.Tk()
root.title("Password Complexity Checker")

frame = tk.Frame(root)
frame.pack(padx=10,pady=10)

label = tk.Label(frame, text="Enter Password:")
label.grid(row=0,column=0,pady=5)

entry = tk.Entry(frame,show="*")
entry.grid(row=0,column=1,pady=5)

check_button = tk.Button(frame,text="Check Strength",command=evaluate_password)
check_button.grid(row=1,column=0,columnspan=2,pady=5)

result_label = tk.Label(frame, text = "Password Strength:")
result_label.grid(row = 2,column=0,columnspan=2,pady=5)

root.mainloop()