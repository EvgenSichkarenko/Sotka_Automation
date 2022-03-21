import pytest
import allure


#@allure.epic("Authorization cases")

@allure.description("This test login attorney with invalid and valid data")
@pytest.mark.login
def test_login_attorney(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="testatt@inboxbear.com", valid_password="1234Qwer")
	assert "Joel William Meskin " == app.session.text_name_attribute_attroney()
	app.login.logout()


"""login secretary"""
@allure.description("This test login secretaru with valid data")
@pytest.mark.login
def test_login_secretary(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="testsecr@inboxbear.com", valid_password="1234Qwer" )
	assert "Polina " == app.session.text_name_attribute_secretary()
	app.login.logout()

@allure.description("This test login cour reporter with invalid and valid data")
@pytest.mark.login
def test_login_cr(app):
	app.login.login(invalid_login="a123", invalid_password="13",
		valid_login="testcr@inboxbear.com", valid_password="1234Qwer")
	assert app.session.text_name_attribute_cr() == "Nelli Polsky "
	app.login.logout()