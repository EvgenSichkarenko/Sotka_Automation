import pytest
import allure
from data.data_model.data_registr_cr import cr_data
from data.data_model.data_registr_attorney import regisrt_data


@allure.description("This test registratio new attorney")
@pytest.mark.parametrize("regisrt_data", regisrt_data)
def test_registr_attorney(app,regisrt_data):
	app.regAttorney.registration_page(regisrt_data.bar_number)
	app.regAttorney.fill_form(regisrt_data.email, regisrt_data.bar_number, regisrt_data.phone_number)
	app.regAttorney.assert_secreatry()
	app.regAttorney.add_secretary(regisrt_data.name_secretary, regisrt_data.email_secretary)
	app.regAttorney.bank_account_button()
	app.regAttorney.img_account_send()
	app.regAttorney.password_input_enter(regisrt_data.valid_password,regisrt_data.invalid_password,regisrt_data.password_match)
	assert app.regAttorney.login_present() == 'Login'


@allure.description("This test registration new cour reporter")
@pytest.mark.parametrize("cr_data", cr_data)
def test_reg_cr(app, cr_data):
	app.cr.cr_registration_form(cr_data.bar_number)
	assert cr_data.bar_number == app.cr.license_num_input_attribute()
	app.cr.cr_data_form(cr_data.email, cr_data.phone_number, cr_data.full_name, cr_data.issuance,
		cr_data.expiration_data, cr_data.address_one, cr_data.addres_two)
	app.cr.availability_button()
	app.cr.price_form()
	app.cr.upload_photo()
	app.cr.set_password(cr_data.valid_password)
	assert app.cr.check_send_mail()