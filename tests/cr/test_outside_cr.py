import pytest
import time
from data.data_model.data_registr_cr import cr_data

@pytest.mark.login
def test_login_cr(app):
	app.login.login(invalid_login="a123", invalid_password="13",
		valid_login="testcr@inboxbear.com", valid_password="1234Qwer")
	assert app.session.text_name_attribute_cr() == "Nelli Polsky "
	app.login.logout()


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
