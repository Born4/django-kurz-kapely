# tests/conftest.py
import os
import pytest
from django.conf import settings


@pytest.fixture(scope='session')
def django_db_setup():
    """
    #os.environ['TEST_DB'] = 'True'
    #settings.DATABASES['default'] = {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(settings.BASE_DIR, 'test_db.sqlite3'),
    #}

    TEST_DB=True pytest

    set TEST_DB=True
    pytest
    """
    pass
