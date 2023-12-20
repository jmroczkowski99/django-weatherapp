import pytest
import sys
from weatherapp.models import City

sys.path.append("..")
pytestmark = pytest.mark.django_db


class TestPostModel:
    def test_str_return(self):
        new_city = City.objects.create(name="Gryfice")
        assert new_city.name == "Gryfice"

    def test_save(self):
        new_city = City.objects.create(name="los angeles")
        assert new_city.name == "Los Angeles"
