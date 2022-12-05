import json

from settings import ROOT_DIR


class FileMethods:

    @staticmethod
    def get_text_from_file(file_path):
        with open(ROOT_DIR + file_path, 'r') as file:
            text_value = file.read()
        return text_value

    def get_json_schema_from_file(self, file_path):
        json_value = self.get_text_from_file(file_path)
        return json.loads(json_value)
