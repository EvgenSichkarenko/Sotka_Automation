import pytest
import allure

#@allure.epic("Authorization cases")
"""login attorney"""
@allure.description("Login attorney with invalid and valid data")
@pytest.mark.login
def test_login_attorney(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="testatt@inboxbear.com", valid_password="1234Qwer")
	assert "Danielle Theresa Kennedy " == app.session.text_name_attribute_attroney()
	app.login.logout()


"""login secretary"""
@allure.description("Login secretaru with valid data")
@pytest.mark.login
def test_login_secretary(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="testSecattr@inboxbear.com", valid_password="1234Qwer" )
	assert "Polina " == app.session.text_name_attribute_secretary()
	app.login.logout()


"""login cr"""
#@pytest.mark.skip(reason="Check skip this test")
@allure.description("Llogin cour reporter with invalid and valid data")
@pytest.mark.login
def test_login_cr(app):
	app.login.login(invalid_login="a123", invalid_password="13",
		valid_login="cr1auto@getnada.com", valid_password="1234Qwer")
	assert app.session.text_name_attribute_cr() == "AutomationCR "
	app.login.logout()