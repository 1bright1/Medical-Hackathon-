import tkinter as tk
from tkinter import messagebox, simpledialog  # Import simpledialog here

# Sample data for the quiz section
questions = {
    "Anatomy": [("What is the largest organ in the human body?", "Skin")],
    "Pharmacology": [("What drug is used to treat bacterial infections?", "Antibiotics")],
    "Pathology": [("What is the study of disease?", "Pathology")]
}


# Function to show the quiz questions
def show_question(subject):
    question, answer = questions[subject][0]
    response = simpledialog.askstring("Quiz", question)
    if response is not None and response.lower() == answer.lower():
        messagebox.showinfo("Result", "Correct!")
    elif response is not None:
        messagebox.showinfo("Result", "Incorrect. The correct answer was " + answer + ".")


# Main application window
class StudyToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MedTool")
        self.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Welcome to MedTool!", font=('Helvetica', 16)).pack(pady=20)

        tk.Button(self, text="Anatomy", command=lambda: show_question("Anatomy")).pack(fill='x')
        tk.Button(self, text="Pharmacology", command=lambda: show_question("Pharmacology")).pack(fill='x')
        tk.Button(self, text="Pathology", command=lambda: show_question("Pathology")).pack(fill='x')


if __name__ == "__main__":
    app = StudyToolApp()
    app.mainloop()

