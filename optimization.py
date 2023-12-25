```python
import pandas as pd
import numpy as np
from scipy.optimize import minimize
import joblib
import os

class EnergyOptimizer:
    def __init__(self, data_folder, model_folder):
        self.data_folder = data_folder
        self.model_folder = model_folder

    def load_data(self, filename):
        return pd.read_csv(filename, index_col='timestamp')

    def load_model(self, filename):
        return joblib.load(filename)

    def optimize_energy_usage(self, model, data):
        # Define the objective function
        def objective(x):
            return model.predict(x.reshape(1, -1))

        # Define the constraints
        constraints = ({'type': 'ineq', 'fun': lambda x:  x[0]},  # energy usage must be positive
                       {'type': 'ineq', 'fun': lambda x:  1 - x[0]})  # energy usage must not exceed the maximum

        # Define the initial guess
        x0 = np.zeros(data.shape[1])

        # Perform the optimization
        result = minimize(objective, x0, constraints=constraints)

        return result.x

    def optimize_all_data(self):
        for data_file in os.listdir(self.data_folder):
            if data_file.startswith("preprocessed_") and data_file.endswith(".csv"):
                for model_file in os.listdir(self.model_folder):
                    if model_file.startswith("model_") and model_file.endswith(".joblib"):
                        if data_file.replace('preprocessed_', '') == model_file.replace('model_', '').replace('.joblib', ''):
                            data = self.load_data(os.path.join(self.data_folder, data_file))
                            model = self.load_model(os.path.join(self.model_folder, model_file))
                            optimized_energy_usage = self.optimize_energy_usage(model, data)
                            print(f'Optimized energy usage for {data_file.replace("preprocessed_", "")}: {optimized_energy_usage}')

if __name__ == "__main__":
    data_folder = './data'
    model_folder = './models'
    energy_optimizer = EnergyOptimizer(data_folder, model_folder)
    energy_optimizer.optimize_all_data()
```
