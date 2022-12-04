import requests

from constant_names import SAVED_SEARCH_NAME, ItemTypes
from infrastructure.data.saved_search.filters.create_saved_search_filters import SearchFilters
from helpers.help_methods import GenerateStringMethods
from settings import *


class SavedSearch:
    url = BASE_URL + '/searches'

    def list_saved_search(self, api_key, link=None, success_response=True):
        """
        Method for List Saved Search
        :param api_key: str
            API key
        :param link: str
            URL to be requested (default is None)
        :param success_response: bool
            A flag used to check response code (default is True)
        :return: object
            response for sent request
        """
        url = link if link is not None else self.url
        response = requests.get(url=url, auth=(f'{api_key}', ''))
        # TODO: Clarify status code, 200 returned instead of 201
        if success_response:
            assert response.status_code == 200, f"Returned response with status code: {response.status_code}"
        return response

    def create_saved_search(self, api_key, item_types=None, search_filter=None,
                            daily_email_enabled=False, success_response=True):
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
        :param success_response: bool
            A flag used to check response code (default is True)
        :return: object
            response for sent request
        """
        if item_types is None:
            item_types = [ItemTypes.PSScene]
        if search_filter is None:
            search_filter = SearchFilters.AndFilter
        payload = {
            "name": SAVED_SEARCH_NAME + GenerateStringMethods().generate_random_string(10),
            "__daily_email_enabled": daily_email_enabled,
            "item_types": item_types,
            "filter": search_filter
        }
        response = requests.post(url=self.url, json=payload, auth=(f'{api_key}', ''))
        # TODO: Clarify status code, 200 returned instead of 201
        if success_response:
            assert response.ok
            # assert response.status_code == 201, f"Returned response with status code: {response.status_code}"
        return response

    def update_saved_search(self, api_key, search_id, item_types=None, search_filter=SearchFilters.AndFilter,
                            daily_email_enabled=False, success_response=True):
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
        :param success_response: bool
            A flag used to check response code (default is True)
        :return: object
            response for sent request
        """
        if item_types is None:
            item_types = [ItemTypes.PSScene]
        payload = {
            "name": SAVED_SEARCH_NAME + GenerateStringMethods().generate_random_string(10),
            "__daily_email_enabled": daily_email_enabled,
            "item_types": item_types,
            "filter": search_filter
        }
        response = requests.put(url=self.url + f"/{search_id}", json=payload, auth=(f'{api_key}', ''))
        if success_response:
            assert response.status_code == 200, f"Returned response with status code: {response.status_code}"
        return response

    def delete_saved_search(self, api_key, search_id, success_response=True):
        """
        Method for Delete Saved Search
        :param api_key: str
            API key
        :param search_id: str, int
            Saved search identifier
        :param success_response: bool
            A flag used to check response code (default is True)
        :return: object
            response for sent request
        """
        response = requests.delete(url=self.url + f"/{search_id}", auth=(f'{api_key}', ''))
        if success_response:
            assert response.status_code == 204, f"Returned response with status code: {response.status_code}"
        return response
