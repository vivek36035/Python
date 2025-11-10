import tkinter as tk
from tkinter import messagebox

class ExpertSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Expert System - Computer Diagnosis")
        self.root.geometry("500x400")
        
        # Knowledge base: rules
        self.questions = [
            "Does the computer turn on?",
            "Is it showing any error message?",
            "Is the computer running very slowly?",
            "Is the internet not working?",
        ]

        self.answers = {}
        self.current_question = 0

        self.label = tk.Label(root, text=self.questions[self.current_question], font=("Arial", 14), wraplength=400)
        self.label.pack(pady=50)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.yes_button = tk.Button(self.button_frame, text="Yes", command=lambda: self.next_question("yes"), width=10, height=2)
        self.yes_button.grid(row=0, column=0, padx=10)

        self.no_button = tk.Button(self.button_frame, text="No", command=lambda: self.next_question("no"), width=10, height=2)
        self.no_button.grid(row=0, column=1, padx=10)

    def next_question(self, answer):
        self.answers[self.questions[self.current_question]] = answer
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.label.config(text=self.questions[self.current_question])
        else:
            self.diagnose()

    def diagnose(self):
        q = self.answers

        # Simple rule base
        if q[self.questions[0]] == "no":
            diagnosis = "Check power cable or battery. The computer might not be receiving power."
        elif q[self.questions[1]] == "yes":
            diagnosis = "Note the error message and search online or reinstall the system."
        elif q[self.questions[2]] == "yes":
            diagnosis = "Your system might have too many background apps. Try cleaning up or adding more RAM."
        elif q[self.questions[3]] == "yes":
            diagnosis = "Check your Wi-Fi connection or restart your router."
        else:
            diagnosis = "No issues detected. Your computer seems fine."

        messagebox.showinfo("Diagnosis Result", diagnosis)
        self.root.quit()  # Graceful exit


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystemGUI(root)
    root.mainloop()
