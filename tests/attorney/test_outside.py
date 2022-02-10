import pytest
import time
from data.data_model.data_registr_attorney import regisrt_data



def test_login_attorney(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="a1@tafmail.com", valid_password="123Qwer")
	assert "Mark John Decastro" == app.session.text_name_attribute_attroney()
	app.login.logout()



@pytest.mark.parametrize("regisrt_data", regisrt_data)
def test_registr_attorney(app,regisrt_data):
	app.regAttorney.registration_page(regisrt_data.bar_number)
	app.regAttorney.fill_form(regisrt_data.email, regisrt_data.bar_number)
	app.regAttorney.assert_secreatry()
	app.regAttorney.add_secretary(regisrt_data.name_secretary, regisrt_data.email_secretary)
	app.regAttorney.bank_account_button()
	app.regAttorney.img_account_send()
	app.regAttorney.password_input_enter(regisrt_data.valid_password,regisrt_data.invalid_password,regisrt_data.password_match)
	#assert app.regAttorney.login_present() == 'Login'


"""login secretary"""
def test_login_secretary(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="secretary02@zetmail.com", valid_password="123Qwer" )
	assert "Ella Nila" == app.session.text_name_attribute_secretary()
	app.login.logout()