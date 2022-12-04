import jsonschema


class ValidateResponse:
    @staticmethod
    def validate_response(response, schema):
        jsonschema.validate(response.json(), schema)
