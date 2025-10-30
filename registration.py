import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()
    gender = gender_var.get()
    country = country_var.get()

    if not name or not email or not password or gender == "" or country == "Select Country":
        messagebox.showerror("Error", "All fields are required!")
    else:
        messagebox.showinfo("Success", f"Registration Successful!\n\nName: {name}\nEmail: {email}\nGender: {gender}\nCountry: {country}")

# Create main window
root = tk.Tk()
root.title("Registration Form")
root.geometry("400x450")
root.config(bg="#f2f2f2")

# Title
tk.Label(root, text="User Registration", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#333").pack(pady=15)

# Name
tk.Label(root, text="Full Name:", font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=40)
entry_name = tk.Entry(root, width=30, font=("Arial", 12))
entry_name.pack(pady=5)

# Email
tk.Label(root, text="Email:", font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=40)
entry_email = tk.Entry(root, width=30, font=("Arial", 12))
entry_email.pack(pady=5)

# Password
tk.Label(root, text="Password:", font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=40)
entry_password = tk.Entry(root, width=30, font=("Arial", 12), show="*")
entry_password.pack(pady=5)

# Gender
tk.Label(root, text="Gender:", font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=40)
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg="#f2f2f2").pack(anchor="w", padx=60)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg="#f2f2f2").pack(anchor="w", padx=60)

# Country dropdown
tk.Label(root, text="Country:", font=("Arial", 12), bg="#f2f2f2").pack(anchor="w", padx=40)
country_var = tk.StringVar(value="Select Country")
countries = ["Select Country", "India", "USA", "UK", "Canada", "Australia"]
country_menu = tk.OptionMenu(root, country_var, *countries)
country_menu.config(width=25)
country_menu.pack(pady=5)

# Submit Button
tk.Button(root, text="Submit", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", width=15, command=submit_form).pack(pady=20)

# Run the GUI
root.mainloop()
