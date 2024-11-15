# tests/test_models.py
import pytest
from django.db import connections, OperationalError
from bands.models import Band


@pytest.fixture
def setup_database(db):
    # Ensure the database connection is available
    try:
        conn = connections['default']
        conn.ensure_connection()
        yield
    finally:
        conn.close()


#@pytest.mark.django_db
def test_database_connection(setup_database):
    # Check if we can connect to the default database
    conn = connections['default']
    try:
        conn.ensure_connection()
        assert conn.is_usable()
    except OperationalError:
        assert False


#@pytest.mark.django_db
def test_create_model_instance(db):
    # Create a test instance
    instance = Band.objects.create(name="TestBand", year=2021)
    assert instance.name == "TestBand"
    assert instance.year == 2021
    # Clean up by deleting the instance
    instance.delete()


# @pytest.mark.django_db
@pytest.mark.parametrize("name, year", [
    ("Moravanka1", 125),
    ("The Clash", 1976),
    ("Metallica", 1982),
    ("Nirvana", 1987),
])
def test_check_existing_model_instances(db, name, year):
    # Attempt to retrieve the instance
    try:
        instance = Band.objects.get(name=name, year=year)
        assert instance is not None
    except Band.DoesNotExist:
        pytest.fail(f"Band instance with name '{name}' and year '{year}' does not exist in the database.")
