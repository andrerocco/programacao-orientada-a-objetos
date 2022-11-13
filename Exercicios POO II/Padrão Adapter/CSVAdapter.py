from CSVParser import CSVParser


class CSVAdapter(CSVParser):
    def __init__(self, file_name: str):
        super().__init__(file_name)

    def parse(self):
        data = super().parse()

        # Converte o CSV para JSON

        return data
