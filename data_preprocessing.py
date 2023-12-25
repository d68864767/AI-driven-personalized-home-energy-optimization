```python
import pandas as pd
import json
import os
from datetime import datetime

class DataPreprocessor:
    def __init__(self, data_folder):
        self.data_folder = data_folder

    def load_data(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    def preprocess_data(self, data):
        # Convert the data into a DataFrame for easier manipulation
        df = pd.DataFrame(data)

        # Convert timestamp to datetime and set it as index
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df.set_index('timestamp', inplace=True)

        # Fill missing values if any
        df.fillna(method='ffill', inplace=True)

        # Normalize the data
        df = (df - df.min()) / (df.max() - df.min())

        return df

    def save_preprocessed_data(self, df, filename):
        df.to_csv(filename)

    def preprocess_all_data(self):
        for file in os.listdir(self.data_folder):
            if file.endswith(".json"):
                data = self.load_data(os.path.join(self.data_folder, file))
                df = self.preprocess_data(data)
                preprocessed_filename = 'preprocessed_' + file.replace('.json', '.csv')
                self.save_preprocessed_data(df, preprocessed_filename)

if __name__ == "__main__":
    data_folder = './data'
    preprocessor = DataPreprocessor(data_folder)
    preprocessor.preprocess_all_data()
```
