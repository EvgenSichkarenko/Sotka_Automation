import pytest
import allure

#@allure.epic("Authorization cases")
"""login attorney"""
@allure.description("Login attorney with invalid and valid data")
@pytest.mark.login
def test_login_attorney(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="qaautomationatt@yahoo.com", valid_password="ZXcv@123580")
	assert "Daniel Vlad Tabakh " == app.session.text_name_attribute_attroney()
	app.login.logout()


"""login secretary"""
@allure.description("Login secretaru with valid data")
@pytest.mark.login
def test_login_secretary(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="qaautomationsecr@yahoo.com", valid_password="ZXcv@123580" )
	assert "Rita QA " == app.session.text_name_attribute_secretary()
	app.login.logout()


"""login cr"""
@allure.description("Llogin cour reporter with invalid and valid data")
@pytest.mark.login
def test_login_cr(app):
	app.login.login(invalid_login="a123", invalid_password="13",
		valid_login="qaautomationcr@yahoo.com", valid_password="ZXcv@123580")
	assert app.session.text_name_attribute_cr() == "AutomationCR "
	app.login.logout()