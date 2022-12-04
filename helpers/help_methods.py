import json
from random import choice
from string import ascii_uppercase

from settings import ROOT_DIR


class FileMethods:

    @staticmethod
    def get_text_from_file(file_path):
        with open(ROOT_DIR + file_path, 'r') as file:
            text_value = file.read()
        return text_value

    def get_json_file(self, file_path):
        json_value = self.get_text_from_file(file_path)
        return json.loads(json_value)


class GenerateStringMethods:

    @staticmethod
    def generate_random_string(characters):
        return ''.join(choice(ascii_uppercase) for _ in range(characters))
