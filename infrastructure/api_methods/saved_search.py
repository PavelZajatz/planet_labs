import requests
import uuid

from constants import SAVED_SEARCH_NAME, ItemTypes
from helpers.help_methods import FileMethods
from helpers.schema_validate import ValidateResponse
from infrastructure.data.saved_search.filters.create_saved_search_filters import SearchFilters
from settings import BASE_URL


class SavedSearchesMethods:
    url = BASE_URL + '/searches'

    @classmethod
    def list_saved_search(cls, api_key, link=None):
        """
        Method for List Saved Search
        :param api_key: str
            API key
        :param link: str
            URL to be requested (default is None)
        :return: object
            response for sent request
        """
        url = link if link is not None else cls.url
        response = requests.get(url=url, auth=(f'{api_key}', ''))
        return response

    @classmethod
    def create_saved_search(cls, api_key, item_types=None, search_filter=None, daily_email_enabled=False):
        """
        Method for Create Saved Search
        :param api_key: str
            API key
        :param item_types: str
            List of item_types, item_type represents the class of spacecraft and/or processing level of an item
            (default is None)
        :param search_filter: dict
            Structured search criteria (default is None)
        :param daily_email_enabled: bool
            A flag which enabling daily email delivery between 00:00:00 and 00:02:00 UTC with an Explorer
            link to all imagery that meets your search criteria published within the last 24 hours
            (default is False)
        :return: object
            response for sent request
        """
        if item_types is None:
            item_types = [ItemTypes.PSScene]
        if search_filter is None:
            search_filter = SearchFilters.AndFilter
        payload = {
            "name": SAVED_SEARCH_NAME + str(uuid.uuid4()),
            "__daily_email_enabled": daily_email_enabled,
            "item_types": item_types,
            "filter": search_filter
        }
        response = requests.post(url=cls.url, json=payload, auth=(f'{api_key}', ''))
        return response

    @classmethod
    def update_saved_search(cls, api_key, search_id, item_types=None, search_filter=SearchFilters.AndFilter,
                            daily_email_enabled=False):
        """
        Method for Update Saved Search
        :param api_key: str
            API key
        :param search_id: str, int
            Saved search identifier
        :param item_types: str
            List of item_types, item_type represents the class of spacecraft and/or processing level of an item
            (default is None)
        :param search_filter: dict
            Structured search criteria (default is None)
        :param daily_email_enabled: bool
            A flag which enabling daily email delivery between 00:00:00 and 00:02:00 UTC with an Explorer
            link to all imagery that meets your search criteria published within the last 24 hours
            (default is False)
        :return: object
            response for sent request
        """
        if item_types is None:
            item_types = [ItemTypes.PSScene]
        payload = {
            "name": SAVED_SEARCH_NAME + str(uuid.uuid4()),
            "__daily_email_enabled": daily_email_enabled,
            "item_types": item_types,
            "filter": search_filter
        }
        response = requests.put(url=cls.url + f"/{search_id}", json=payload, auth=(f'{api_key}', ''))
        return response

    @classmethod
    def delete_saved_search(cls, api_key, search_id):
        """
        Method for Delete Saved Search
        :param api_key: str
            API key
        :param search_id: str, int
            Saved search identifier
        :return: object
            response for sent request
        """
        response = requests.delete(url=cls.url + f"/{search_id}", auth=(f'{api_key}', ''))
        return response

    @staticmethod
    def validate_create_saved_searches_schema(response):
        """
        Method for response schema validation
        :param response: response
        """
        schema = FileMethods().get_json_schema_from_file(
            "/infrastructure/data/saved_search/response_schema/saved_search_schema.json")
        ValidateResponse().validate_response(response, schema)
