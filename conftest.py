import pytest
from pages.application import Application



@pytest.fixture(scope='session')
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture