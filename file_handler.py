import json

class FileHandler():
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        with open(self.filename) as f:
            return json.load(f)

    def save_data(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4, sort_keys=True)