import time
import pytest
from data.data_model.data_registr_cr import cr_data


def test_login_cr(app):
	app.login.login(invalid_login="a13", invalid_password="13",
		valid_login="crdev@givmail.com", valid_password="1234Qwer")
	assert app.session.text_name_attribute_cr() == "Евгений Сичкаренко"
	app.session.logout()

@pytest.mark.parametrize("cr_data", cr_data)
def test_reg_cr(app, cr_data):
	app.cr.cr_registration_form(cr_data.bar_number)
	assert cr_data.bar_number == app.cr.license_num_input_attribute()
	app.cr.cr_data_form(cr_data.email, cr_data.phone_number, cr_data.full_name, cr_data.issuance,
		cr_data.expiration_data, cr_data.address_one, cr_data.addres_two)
	time.sleep(2)
	app.cr.availability_button()
	app.cr.price_form()
	time.sleep(2)
