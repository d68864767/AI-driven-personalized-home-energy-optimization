```python
import tkinter as tk
from tkinter import messagebox
from data_collection import DataCollector
from data_preprocessing import DataPreprocessor
from model import EnergyModel
from optimization import EnergyOptimizer

class UserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-driven Personalized Home Energy Optimization")

        self.device_api_url = tk.StringVar()
        self.device_api_key = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Device API URL:").grid(row=0, column=0, sticky='w')
        tk.Entry(self.root, textvariable=self.device_api_url).grid(row=0, column=1)

        tk.Label(self.root, text="Device API Key:").grid(row=1, column=0, sticky='w')
        tk.Entry(self.root, textvariable=self.device_api_key).grid(row=1, column=1)

        tk.Button(self.root, text="Collect Data", command=self.collect_data).grid(row=2, column=0, sticky='w')
        tk.Button(self.root, text="Preprocess Data", command=self.preprocess_data).grid(row=2, column=1, sticky='w')
        tk.Button(self.root, text="Train Model", command=self.train_model).grid(row=3, column=0, sticky='w')
        tk.Button(self.root, text="Optimize Energy", command=self.optimize_energy).grid(row=3, column=1, sticky='w')

    def collect_data(self):
        collector = DataCollector(self.device_api_url.get(), self.device_api_key.get())
        collector.collect_data()
        messagebox.showinfo("Success", "Data collection completed successfully!")

    def preprocess_data(self):
        preprocessor = DataPreprocessor('./data')
        preprocessor.preprocess_all_data()
        messagebox.showinfo("Success", "Data preprocessing completed successfully!")

    def train_model(self):
        energy_model = EnergyModel('./data')
        energy_model.train_and_save_model()
        messagebox.showinfo("Success", "Model training completed successfully!")

    def optimize_energy(self):
        energy_optimizer = EnergyOptimizer('./data', './models')
        energy_optimizer.optimize_all_data()
        messagebox.showinfo("Success", "Energy optimization completed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    UserInterface(root)
    root.mainloop()
```
