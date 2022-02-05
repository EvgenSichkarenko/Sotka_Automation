import pytest
import time
from pages.application import Application
from data.data_model.data_registr_attorney import regisrt_data

@pytest.fixture()
def app_reg_att(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture

@pytest.mark.parametrize("regisrt_data", regisrt_data)
def test_registr_attorney(app_reg_att,regisrt_data):
	app_reg_att.regAttorney.registration_page(regisrt_data.bar_number)
	app_reg_att.regAttorney.fill_form(regisrt_data.email, regisrt_data.bar_number)
	app_reg_att.regAttorney.assert_secreatry()
	app_reg_att.regAttorney.add_secretary(regisrt_data.name_secretary, regisrt_data.email_secretary)
	app_reg_att.regAttorney.bank_account_button()
	app_reg_att.regAttorney.img_account_send()
	app_reg_att.regAttorney.password_input_enter(regisrt_data.valid_password,regisrt_data.invalid_password,regisrt_data.password_match)
	assert app_reg_att.regAttorney.login_present() == 'Login'
