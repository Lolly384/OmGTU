class FileWriter:
    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def write(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            for caf in self.data:
                f.write(caf + '\n')