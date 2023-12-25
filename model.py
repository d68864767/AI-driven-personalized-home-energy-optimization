```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib
import os

class EnergyModel:
    def __init__(self, data_folder):
        self.data_folder = data_folder

    def load_data(self, filename):
        return pd.read_csv(filename, index_col='timestamp')

    def split_data(self, df):
        X = df.drop('energy_usage', axis=1)
        y = df['energy_usage']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        return model

    def evaluate_model(self, model, X_test, y_test):
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)

        print(f'Model Mean Squared Error: {mse}')

    def save_model(self, model, filename):
        joblib.dump(model, filename)

    def train_and_save_model(self):
        for file in os.listdir(self.data_folder):
            if file.startswith("preprocessed_") and file.endswith(".csv"):
                df = self.load_data(os.path.join(self.data_folder, file))
                X_train, X_test, y_train, y_test = self.split_data(df)
                model = self.train_model(X_train, y_train)
                self.evaluate_model(model, X_test, y_test)
                model_filename = 'model_' + file.replace('preprocessed_', '').replace('.csv', '.joblib')
                self.save_model(model, model_filename)

if __name__ == "__main__":
    data_folder = './data'
    energy_model = EnergyModel(data_folder)
    energy_model.train_and_save_model()
```
