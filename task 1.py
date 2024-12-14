import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit == 'C':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        return f"{value}°C is {f:.2f}°F and {k:.2f}K"
    elif unit == 'F':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        return f"{value}°F is {c:.2f}°C and {k:.2f}K"
    elif unit == 'K':
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        return f"{value}K is {c:.2f}°C and {f:.2f}°F"
    else:
        return "Invalid unit"

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")

        # Create and place the temperature value entry
        self.value_label = ttk.Label(root, text="Enter Temperature Value:")
        self.value_label.grid(row=0, column=0, padx=10, pady=10)
        self.value_entry = ttk.Entry(root)
        self.value_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create and place the unit selection
        self.unit_label = ttk.Label(root, text="Select Unit:")
        self.unit_label.grid(row=1, column=0, padx=10, pady=10)
        self.unit_combobox = ttk.Combobox(root, values=['C', 'F', 'K'])
        self.unit_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.unit_combobox.current(0)

        # Create and place the convert button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert)
        self.convert_button.grid(row=2, columnspan=2, padx=10, pady=10)

        # Create and place the result label
        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=3, columnspan=2, padx=10, pady=10)

    def convert(self):
        try:
            value = float(self.value_entry.get())
            unit = self.unit_combobox.get()
            result = convert_temperature(value, unit)
            self.result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid temperature value.")

# Create the main window
root = tk.Tk()
app = TemperatureConverter(root)

# Run the application
root.mainloop()
