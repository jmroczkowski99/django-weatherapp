from django.urls import reverse
import pytest
import sys
import html
from weatherapp.models import City

sys.path.append("..")


@pytest.mark.django_db
def test_basic_index_view(client):
    response = client.get("/")
    assert response.status_code == 200


@pytest.mark.django_db
def test_valid_city(client):
    response = client.post(reverse('homepage'), {'name': 'Gryfice'})
    assert response.status_code == 200
    assert "weather_data" in response.context
    assert "form" in response.context
    assert City.objects.filter(name="Gryfice").exists()


@pytest.mark.django_db
def test_insensitive_city(client):
    response = client.post(reverse('homepage'), {'name': 'gryFice'})
    assert response.status_code == 200
    assert City.objects.filter(name="Gryfice").exists()


@pytest.mark.django_db
def test_existing_city(client):
    client.post(reverse('homepage'), {'name': 'Gryfice'})
    response = client.post(reverse('homepage'), {'name': 'Gryfice'})
    assert response.status_code == 200
    assert City.objects.filter(name="Gryfice").count() == 1
    assert "This city is already in our database" in str(response.content)


@pytest.mark.django_db
def test_nonexisting_city(client):
    response = client.post(reverse('homepage'), {'name': 'sddsaasd'})
    response_content_decoded = html.unescape(response.content.decode("utf-8"))
    assert response.status_code == 200
    assert City.objects.filter(name="sddsaasd").count() == 0
    assert "This city doesn't exist in our database" in response_content_decoded


@pytest.mark.django_db
def test_delete_city_view(client):
    new_city = City.objects.create(name="Gryfice")
    response = client.get(f"/delete/{new_city.name}/")
    assert response.status_code == 302
    assert response.url == reverse('homepage')
    assert City.objects.filter(name=new_city.name).count() == 0
