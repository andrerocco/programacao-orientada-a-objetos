from IParse import IParse


class JSONParser(IParse):
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.data = None

    def parse(self) -> dict:
        with open(self.file_name, 'r') as file:
            self.data = file.read()
        
        return self.data
