import tkinter as tk
from tkinter import messagebox

class ExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Expert System - Computer Diagnosis")
        self.root.geometry("600x450")

        # Knowledge base (questions + options)
        self.questions = [
            {
                "question": "What issue are you facing?",
                "options": ["Computer won't start", "Slow performance", "Internet problem", "Strange noise", "Other"],
                "key": "main_issue"
            },
            {
                "question": "When did the problem start?",
                "options": ["Today", "Few days ago", "A week ago", "More than a month ago"],
                "key": "duration"
            },
            {
                "question": "Have you installed any new software recently?",
                "options": ["Yes", "No"],
                "key": "new_software"
            },
            {
                "question": "What operating system are you using?",
                "options": ["Windows", "Mac", "Linux", "Other"],
                "key": "os"
            }
        ]

        self.answers = {}
        self.current_question = 0

        self.label = tk.Label(root, text=self.questions[0]["question"], font=("Arial", 14), wraplength=500)
        self.label.pack(pady=30)

        self.var = tk.StringVar()
        self.buttons = []

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.create_option_buttons()

        self.next_button = tk.Button(root, text="Next", command=self.next_question, width=12, height=2, bg="#4CAF50", fg="white")
        self.next_button.pack(pady=20)

    def create_option_buttons(self):
        # Remove old buttons if any
        for btn in self.buttons:
            btn.destroy()
        self.buttons = []

        options = self.questions[self.current_question]["options"]
        self.var.set(None)
        for opt in options:
            btn = tk.Radiobutton(self.button_frame, text=opt, variable=self.var, value=opt, font=("Arial", 12))
            btn.pack(anchor="w")
            self.buttons.append(btn)

    def next_question(self):
        answer = self.var.get()
        if not answer:
            messagebox.showwarning("Warning", "Please select an option before proceeding.")
            return

        key = self.questions[self.current_question]["key"]
        self.answers[key] = answer

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.label.config(text=self.questions[self.current_question]["question"])
            self.create_option_buttons()
        else:
            self.diagnose()

    def diagnose(self):
        issue = self.answers.get("main_issue")
        new_software = self.answers.get("new_software")
        os_type = self.answers.get("os")

        # Simple inference rules
        if issue == "Computer won't start":
            diagnosis = "Check if the power cable or battery is properly connected. Try a different socket."
        elif issue == "Slow performance":
            if new_software == "Yes":
                diagnosis = "Recently installed software might be causing lag. Try uninstalling it or scanning for malware."
            else:
                diagnosis = "Clean temporary files, disable startup apps, or consider upgrading RAM."
        elif issue == "Internet problem":
            diagnosis = "Check if Wi-Fi is connected and router is working. Restart both router and computer."
        elif issue == "Strange noise":
            diagnosis = "It might be a fan or hard disk issue. Avoid using the computer until a technician checks it."
        else:
            diagnosis = "Try running a system diagnostic tool or contacting technical support."

        # OS-based advice
        if os_type == "Windows":
            diagnosis += "\n\n💡 Tip: Use 'Task Manager' to monitor background processes."
        elif os_type == "Mac":
            diagnosis += "\n\n💡 Tip: Try resetting the NVRAM or PRAM if issues persist."
        elif os_type == "Linux":
            diagnosis += "\n\n💡 Tip: Use 'top' or 'htop' to check resource usage."

        messagebox.showinfo("Diagnosis Result", diagnosis)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpertSystem(root)
    root.mainloop()
