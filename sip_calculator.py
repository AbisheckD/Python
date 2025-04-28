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
