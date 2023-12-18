import pytest
import sys
sys.path.append("..")
from weatherapp.models import City

pytestmark = pytest.mark.django_db

class TestPostModel:
    def test_str_return(self):
        new_city = City.objects.create(name="Gryfice")
        assert new_city.name == "Gryfice"