# AI-driven Personalized Home Energy Optimization

This project is an AI-driven solution for optimizing home energy usage. It collects data from home devices, preprocesses the data, trains a model on the data, and uses the model to optimize energy usage.

## Project Structure

The project consists of the following files:

- `main.py`: The main entry point of the application.
- `data_collection.py`: Contains the `DataCollector` class for collecting data from home devices.
- `data_preprocessing.py`: Contains the `DataPreprocessor` class for preprocessing the collected data.
- `model.py`: Contains the `EnergyModel` class for training a model on the preprocessed data.
- `optimization.py`: Contains the `EnergyOptimizer` class for optimizing energy usage using the trained model.
- `user_interface.py`: Contains the `UserInterface` class for interacting with the user.
- `config.py`: Contains configuration variables for the project.
- `requirements.txt`: Contains the Python packages required to run the project.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ai-energy-optimization.git
   ```
2. Navigate to the project directory:
   ```
   cd ai-energy-optimization
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Update the `DEVICE_API_URL` and `DEVICE_API_KEY` variables in `config.py` with your device API URL and key.
2. Run the main script:
   ```
   python main.py
   ```
3. The user interface will appear. Enter your device API URL and key, and click the buttons to collect data, preprocess data, train the model, and optimize energy usage.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
