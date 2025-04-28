# SIP_Calculator

## 📝 Overview
This repository contains a simple and interactive **SIP (Systematic Investment Plan) Calculator** built using **Python** and **Tkinter**.  
It allows users to estimate the **maturity value** and **total investment** based on adjustable inputs like **monthly investment**, **investment tenure**, and **expected annual return rate**.

## ✨ Features
- **Real-time** SIP calculation as you move the sliders
- **User-friendly GUI** made with Tkinter
- **Dynamic updates** without needing to press buttons
- Displays **monthly investment**, **investment tenure**, **total invested amount**, and **maturity value**

## 🛠 Hardware Requirements
- A basic **PC or Laptop** capable of running Python applications

## 💻 Software Requirements
- **Python 3.x** installed on your machine  
  👉 [Download Python](https://www.python.org/downloads/)
- **Tkinter** library (comes pre-installed with Python)

## 🚀 Getting Started
1. Make sure **Python 3.x** is installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/AbisheckD/Python
   ```
3. Navigate to the project directory:
   ```bash
   cd Python
   ```
4. Run the script:
   ```bash
   python sip_calculator.py
   ```

## 📂 Repository Structure
- `sip_calculator.py` — Main Python script containing the SIP Calculator with GUI.

## 📸 GUI Preview
- Three sliders to adjust:
  - **Monthly Investment** (₹100 to ₹20,000)
  - **Investment Tenure** (1 to 50 years)
  - **Expected Annual Return Rate** (1% to 50%)
- Results displayed dynamically showing:
  - Monthly Investment
  - Tenure (in years and months)
  - Annual Return Rate
  - Total Invested
  - Maturity Value

## Code

```python
import tkinter as tk

def update_result(val=None):
    invested = scale1.get()
    tenure = scale2.get()
    annual_rate = scale3.get()

    # Correct calculations
    monthly_rate = annual_rate / 12 / 100
    months = tenure * 12

    total_invested = invested * months
    maturity_value = round(invested * (((1 + monthly_rate) ** months - 1) / monthly_rate))

    result.set(
        f"Monthly Investment: ₹{invested:,}\n"
        f"Tenure: {tenure} years ({months} months)\n"
        f"Return Rate: {annual_rate}% annually\n\n"
        f"Total Invested: ₹{total_invested:,}\n"
        f"Maturity Value: ₹{maturity_value:,}"
    )

root = tk.Tk()
root.title("SIP Calculator")
root.geometry("450x450")

result = tk.StringVar()
result.set("Adjust sliders to calculate SIP")

# Monthly Investment Slider
tk.Label(root, text="Monthly Investment (₹)").pack()
scale1 = tk.Scale(root, from_=100, to=20000, resolution=100, orient="horizontal", length=400, command=update_result)
scale1.pack()

# Tenure Slider (Years)
tk.Label(root, text="Investment Tenure (Years)").pack()
scale2 = tk.Scale(root, from_=1, to=50, orient="horizontal", length=400, command=update_result)
scale2.pack()

# Expected Return Rate Slider (%)
tk.Label(root, text="Expected Annual Return (%)").pack()
scale3 = tk.Scale(root, from_=1, to=50, orient="horizontal", length=400, command=update_result)
scale3.pack()

# Result Label
label_result = tk.Label(root, textvariable=result, font=("Arial", 12), wraplength=420, justify="center")
label_result.pack(pady=10)

root.mainloop()
```

## 🤝 How to Contribute
Contributions are welcome!  
Feel free to **fork** the repository, **improve the GUI**, **add features**, or **enhance the calculation accuracy**, and submit a **pull request**.

## 📄 License
This project is licensed under the **MIT License**.

