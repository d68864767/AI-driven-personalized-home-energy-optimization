```python
import requests
import json
import datetime

# You may need to import other libraries depending on the devices you are using

class DataCollector:
    def __init__(self, device_api_url, device_api_key):
        self.device_api_url = device_api_url
        self.device_api_key = device_api_key

    def get_data(self):
        headers = {
            'Authorization': 'Bearer ' + self.device_api_key
        }

        response = requests.get(self.device_api_url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def save_data(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f)

    def collect_data(self):
        data = self.get_data()

        if data is not None:
            filename = 'data_' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.json'
            self.save_data(data, filename)

if __name__ == "__main__":
    device_api_url = 'http://your_device_api_url'
    device_api_key = 'your_device_api_key'

    collector = DataCollector(device_api_url, device_api_key)
    collector.collect_data()
```
