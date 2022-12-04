import pytest

from constant_names import SAVED_SEARCH_NAME
from infrastructure.api_methods.saved_search import SavedSearch


@pytest.fixture()
def create_saved_search(request):
    response = SavedSearch().create_saved_search(api_key=request.param)
    return response


@pytest.fixture(scope='class')
def remove_created_saved_search_after_test(request):
    yield
    # Uncomment if removing created searches needed after test(Removing takes some, time ~4 min):
    # response = SavedSearch().list_saved_search(api_key=request.param)
    # remove_created_saved_search(response, request.param)
    # open_next_page_with_saved_search(response, request.param)


def remove_created_saved_search(response, api_key):
    for search in response.json()['searches']:
        if SAVED_SEARCH_NAME in search['name']:
            SavedSearch().delete_saved_search(api_key=api_key, search_id=search['id'])
            print(f"Saved search with id {search['id']} is deleted")


def open_next_page_with_saved_search(response, api_key):
    try:
        link = response.json()['_links']['_next']
        response = SavedSearch().list_saved_search(api_key=api_key, link=link)
        remove_created_saved_search(response, api_key)
        open_next_page_with_saved_search(response, api_key)
    except KeyError:
        pass
