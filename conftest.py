import pytest
from pages.application import Application



@pytest.fixture()
def app(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture

# fixture = None
#
# @pytest.fixture
# def app(request):
# 	global fixture
# 	if fixture is None:
# 		fixture = Application()
# 		fixture.session.login(login="a1@tafmail.com", password="123Qwer")
# 	else:
# 		if not fixture.is_valid():
# 			fixture = Application()
# 			fixture.session.login(login="a1@tafmail.com", password="123Qwer") #делать логин каждый раз при инициализации фикстуры
# 	return fixture

# @pytest.fixture(scope='session', autouse = True)
# def stop(request):
# 	def fin():
# 		fixture.session.logout()
# 		fixture.destroy()
# 	request.addfinalizer(fin)
# 	return fixture


