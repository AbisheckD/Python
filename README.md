# Tkinter GUI Examples using Python 🎨🖥️

This repository contains **10 beginner-friendly Python GUI programs** using **Tkinter**. Each example demonstrates a different Tkinter widget or concept to help you get started with graphical programming.

📂 Repository: [AbisheckD/Python](https://github.com/AbisheckD/Python)

---

## 📌 1. Basic Tkinter Window

Creates a simple Tkinter window.

```python
import tkinter as tk

# Create the main window
top = tk.Tk()
top.title("Basic Tkinter Window")

# Run the application
top.mainloop()
```

💡 **Expected Output**:  
A blank GUI window with the title "Basic Tkinter Window".

---

## 📌 2. Creating a Tkinter Application Class

Uses an object-oriented approach to create a window.

```python
import tkinter as tk

class App(tk.Tk):
   def __init__(self):
      super().__init__()
      self.title("Tkinter Class Example")

# Create and run the application
app = App()
app.mainloop()
```

💡 **Expected Output**:  
A GUI window titled "Tkinter Class Example".

---

## 📌 3. Adding a Label and Button

Creates a label and a Quit button.

```python
import tkinter as tk

root = tk.Tk()
root.title("Label and Button Example")

label = tk.Label(root, text="Hello, World!")
label.pack()

button = tk.Button(root, text="Quit", command=root.destroy)
button.pack()

root.mainloop()
```

💡 **Expected Output**:  
A window with the text "Hello, World!" and a "Quit" button.

---

## 📌 4. Taking User Input with Entry Field

Takes user input and prints a greeting in the console.

```python
import tkinter as tk

root = tk.Tk()
root.title("User Input Example")

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

def greet():
    name = entry.get()
    print("Hello, " + name + "!")

button = tk.Button(root, text="Greet", command=greet)
button.pack()

root.mainloop()
```

💡 **Expected Output**:  
A window with a text entry field and "Greet" button. Console prints "Hello, <name>!" on clicking the button.

---

## 📌 5. Simple Button Example

A button without functionality.

```python
import tkinter as tk

root = tk.Tk()
root.title("Button Example")

button = tk.Button(root, text="Click me!")
button.pack()

root.mainloop()
```

💡 **Expected Output**:  
A GUI window with a button labeled "Click me!".

---

## 📌 6. Button with Functionality

Prints "Hello, World!" when clicked.

```python
import tkinter as tk

root = tk.Tk()
root.title("Button Click Example")

def say_hello():
    print("Hello, World!")

button = tk.Button(root, text="Click me!", command=say_hello)
button.pack()

root.mainloop()
```

💡 **Expected Output**:  
A button that prints "Hello, World!" in the console when clicked.

---

## 📌 7. Entry Field with Button

User enters text and it is printed in the console.

```python
import tkinter as tk

root = tk.Tk()
root.title("Entry Field Example")

entry = tk.Entry(root)
entry.pack()

def print_text():
    text = entry.get()
    print(text)

button = tk.Button(root, text="Print text", command=print_text)
button.pack()

root.mainloop()
```

💡 **Expected Output**:  
A text entry and "Print text" button. Console displays the entered text when clicked.

---

## 📌 8. Checkbox Example

Demonstrates a checkbox and prints its state.

```python
import tkinter as tk

root = tk.Tk()
root.title("Checkbox Example")

var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Select me!", variable=var)
checkbutton.pack()

def print_value():
    value = var.get()
    print(value)

button = tk.Button(root, text="Print value", command=print_value)
button.pack()

root.mainloop()
```

💡 **Expected Output**:  
Checkbox and button. Console prints `1` when selected, `0` when not selected.

---

## 📌 9. Radio Button Example

Radio buttons to select an option.

```python
import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")

var = tk.IntVar()
radiobutton1 = tk.Radiobutton(root, text="Option 1", variable=var, value=1)
radiobutton2 = tk.Radiobutton(root, text="Option 2", variable=var, value=2)

radiobutton1.pack()
radiobutton2.pack()

def print_value():
    value = var.get()
    print(value)

button = tk.Button(root, text="Print value", command=print_value)
button.pack()

root.mainloop()
```

💡 **Expected Output**:  
Two radio buttons and a button. Console prints `1` or `2` depending on the selected option.

---

## 📌 10. Getting User Input with askinteger

Uses a popup dialog to get an integer input.

```python
from tkinter.simpledialog import askinteger
from tkinter import *

top = Tk()
top.title("Integer Input Example")
top.geometry("200x100")

def show():
   num = askinteger("Input", "Enter an Integer:")
   print(num)

B = Button(top, text="Click", command=show)
B.pack()

top.mainloop()
```

💡 **Expected Output**:  
A window with a button. Clicking it shows a popup for number input, and prints the number in the console.

---

## 📥 Clone This Repository

```sh
git clone https://github.com/AbisheckD/Python.git
cd Python
```

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

Happy GUI coding! ✨
