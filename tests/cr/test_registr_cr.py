import pytest
import time
from pages.application import Application
from data.data_model.data_registr_cr import cr_data

@pytest.fixture(scope='session')
def app_reg_cr(request):
	fixture = Application()
	request.addfinalizer(fixture.destroy)
	return fixture

@pytest.mark.parametrize("cr_data", cr_data)
def test_reg_cr(app_reg_cr, cr_data):
	app_reg_cr.cr.cr_registration_form(cr_data.bar_number)
	assert cr_data.bar_number == app_reg_cr.cr.license_num_input_attribute()
	app_reg_cr.cr.cr_data_form(cr_data.email, cr_data.phone_number, cr_data.full_name, cr_data.issuance,
		cr_data.expiration_data, cr_data.address_one, cr_data.addres_two)
	time.sleep(2)
	app_reg_cr.cr.availability_button()
	app_reg_cr.cr.price_form()
	time.sleep(2)
