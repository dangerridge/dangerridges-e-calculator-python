import decimal
import tkinter as tk
from tkinter import ttk
import pyperclip

def calculate_e(n):
    # Limit n to 50,000
    if n > 50000:
        n = 50000
    # Increase precision to avoid overflow/underflow errors
    context = decimal.getcontext()
    context.prec = n + 10
    # Calculate e using Taylor series
    e = decimal.Decimal(1)
    factorial = decimal.Decimal(1)
    for i in range(1, n+1):
        factorial *= i
        e += decimal.Decimal(1) / factorial
    # Convert result to string and truncate to n+2 decimal places
    return str(e)[:n+2]

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculate e")
        self.style = ttk.Style(self.master)
        self.style.theme_use('clam')
        self.create_widgets()

    def create_widgets(self):
        # Prompt the user to enter the number of digits to calculate
        self.label = tk.Label(self.master, text="Enter the number of digits of e to calculate (max 50,000):", font=('Arial', 12))
        self.label.pack(pady=10)

        # Entry widget for user input
        self.entry = tk.Entry(self.master, font=('Arial', 12))
        self.entry.pack(pady=10)

        # Button to initiate calculation
        self.button = tk.Button(self.master, text="Calculate", font=('Arial', 12), command=self.calculate)
        self.button.pack(pady=10)

        # Text widget to display result
        self.result = tk.Text(self.master, font=('Arial', 12), height=10, width=50)
        self.result.pack(pady=10)

        # Button to copy result to clipboard
        self.copy_button = tk.Button(self.master, text="Copy", font=('Arial', 12), command=self.copy)
        self.copy_button.pack(pady=10)

    def calculate(self):
        # Get user input and calculate e
        n = int(self.entry.get())
        e = calculate_e(n)
        # Clear previous output and display new result
        self.result.delete('1.0', tk.END)
        self.result.insert('1.0', f"e with {n} digits of accuracy:\n{e}")

    def copy(self):
        # Copy result to clipboard
        result = self.result.get('1.0', tk.END)
        pyperclip.copy(result)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
