import pytest
import allure

from infrastructure.api_methods.saved_search import SavedSearchesMethods
from infrastructure.data.saved_search.filters.create_saved_search_filters import SearchFilters
from key_settings import *


class TestSavedSearches:
    @allure.feature("Verify that Saved Search can be created with positive scenario")
    @pytest.mark.parametrize("remove_created_saved_search_after_test", [PLANET_API_KEY], indirect=True)
    @pytest.mark.parametrize("search_filter, daily_email_enabled", [
        (SearchFilters.AndFilter, True),
        (SearchFilters.NotFilter, False),
        (SearchFilters.AssetFilter, True),
        (SearchFilters.RangeFilter, False),
        (SearchFilters.OrFilter, True),
        (SearchFilters.DateRangeFilter, False),
        (SearchFilters.GeometryFilter, True),
        (SearchFilters.NumberInFilter, False),
        (SearchFilters.PermissionFilter, True),
        (SearchFilters.StringInFilter, False),
        (SearchFilters.UpdateFilter, True)
    ])
    def test_create_saved_search(self, remove_created_saved_search_after_test, search_filter, daily_email_enabled):
        with allure.step("Create Saved Search"):
            response = SavedSearchesMethods.create_saved_search(
                api_key=PLANET_API_KEY, search_filter=search_filter, daily_email_enabled=daily_email_enabled)
            assert response.status_code == 201, f"Returned response with status code: {response.status_code}"
        with allure.step("Validate schema for created Saved Search"):
            SavedSearchesMethods.validate_create_saved_searches_schema(response)

    @allure.feature("Verify that Saved Search can not be created for unauthorized user")
    def test_create_saved_search_for_non_authorized_user(self):
        with allure.step("Create Saved Search"):
            response = SavedSearchesMethods.create_saved_search(api_key="None")
            assert response.status_code == 401, f" 401 status code should be returned instead {response.status_code}"
            assert "Please enter a valid API key." in response.text, f"returned - {response.text}"

    @allure.feature("Verify that Saved Search can not be created with without required properties")
    def test_create_saved_search_wrong_filter(self):
        with allure.step("Create Saved Search"):
            response = SavedSearchesMethods.create_saved_search(
                api_key=PLANET_API_KEY, search_filter={"type": "DateRangeFilter", "field_name": "acquired"})
            assert response.status_code == 400, f" 400 status code should be returned instead {response.status_code}"
            assert "'config' is a required property" in response.text, f"returned - {response.text}"

    @allure.feature("Verify that Saved Search can be updated with positive scenario")
    @pytest.mark.parametrize("create_saved_search", [PLANET_API_KEY], indirect=True)
    @pytest.mark.parametrize("search_filter, daily_email_enabled", [
        (SearchFilters.AndFilter, True),
        (SearchFilters.NotFilter, False),
        (SearchFilters.AssetFilter, True),
        (SearchFilters.RangeFilter, False),
        (SearchFilters.OrFilter, True),
        (SearchFilters.DateRangeFilter, False),
        (SearchFilters.GeometryFilter, True),
        (SearchFilters.NumberInFilter, False),
        (SearchFilters.PermissionFilter, True),
        (SearchFilters.StringInFilter, False),
        (SearchFilters.UpdateFilter, True)
    ])
    def test_update_saved_search(self, create_saved_search, search_filter, daily_email_enabled):
        with allure.step("Create Saved Search"):
            response = create_saved_search
        with allure.step("Update Saved Search"):
            response = SavedSearchesMethods.update_saved_search(
                api_key=PLANET_API_KEY, search_id=response.json()['id'],
                search_filter=search_filter, daily_email_enabled=daily_email_enabled)
            assert response.status_code == 200, f"Returned response with status code: {response.status_code}"
        with allure.step("Validate schema for updated Saved Search"):
            SavedSearchesMethods.validate_create_saved_searches_schema(response)

    @allure.feature("Verify that Saved Search can not be updated for unauthorized user")
    @pytest.mark.parametrize("create_saved_search", [PLANET_API_KEY], indirect=True)
    def test_update_saved_search_for_non_authorized_user(self, create_saved_search):
        with allure.step("Create Saved Search"):
            response = create_saved_search
        with allure.step("Update Saved Search"):
            response = SavedSearchesMethods.update_saved_search(api_key=None, search_id=response.json()['id'])
            assert response.status_code == 401, f" 401 status code should be returned instead {response.status_code}"
            assert "Please enter a valid API key." in response.text, f"returned - {response.text}"

    @allure.feature("Verify that Saved Search can not be updated with without required properties")
    @pytest.mark.parametrize("create_saved_search", [PLANET_API_KEY], indirect=True)
    def test_update_saved_search_wrong_filter(self, create_saved_search):
        with allure.step("Create Saved Search"):
            response = create_saved_search
        with allure.step("Update Saved Search"):
            response = SavedSearchesMethods.update_saved_search(
                api_key=PLANET_API_KEY, search_id=response.json()['id'],
                search_filter={"type": "DateRangeFilter", "field_name": "acquired"})
            assert response.status_code == 400, f" 400 status code should be returned instead {response.status_code}"
            assert "'config' is a required property" in response.text, f"returned - {response.text}"

    @allure.feature("Verify that Saved Search can not be updated by wrong id")
    def test_update_saved_search_wrong_search_id(self):
        with allure.step("Update Saved Search"):
            response = SavedSearchesMethods.update_saved_search(api_key=PLANET_API_KEY, search_id="1111")
            assert response.status_code == 404, f" 400 status code should be returned instead {response.status_code}"
            assert "The requested search id does not exist" in response.text, f"returned - {response.text}"

    @allure.feature("Verify that Saved Search can be deleted with positive scenario")
    @pytest.mark.parametrize("create_saved_search", [PLANET_API_KEY], indirect=True)
    def test_delete_saved_search(self, create_saved_search):
        with allure.step("Create Saved Search"):
            response = create_saved_search
        with allure.step("Delete Saved Search"):
            response = SavedSearchesMethods.delete_saved_search(api_key=PLANET_API_KEY, search_id=response.json()['id'])
            assert response.status_code == 204, f"Returned response with status code: {response.status_code}"

    @allure.feature("Verify that Saved Search can not be deleted for unauthorized user")
    @pytest.mark.parametrize("create_saved_search", [PLANET_API_KEY], indirect=True)
    def test_delete_saved_search_for_non_authorized_user(self, create_saved_search):
        with allure.step("Create Saved Search"):
            response = create_saved_search
        with allure.step("Delete Saved Search"):
            response = SavedSearchesMethods.delete_saved_search(api_key=None, search_id=response.json()['id'])
            assert response.status_code == 401, f" 401 status code should be returned instead {response.status_code}"
            assert "Please enter a valid API key." in response.text, f"returned - {response.text}"

    @allure.feature("Verify that Saved Search can not be deleted by wrong id")
    def test_delete_saved_search_wrong_search_id(self):
        with allure.step("Delete Saved Search"):
            response = SavedSearchesMethods.delete_saved_search(api_key=PLANET_API_KEY, search_id="1111")
            assert response.status_code == 404, f" 400 status code should be returned instead {response.status_code}"
            assert "The requested search id does not exist" in response.text, f"returned - {response.text}"
