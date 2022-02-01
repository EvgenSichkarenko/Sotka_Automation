import time
import pytest
from data.data_model.data_registr_attorney import regisrt_data


def test_login_attorney(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	assert app.session.text_name_attribute_attroney() == "Mark John Decastro"
	app.session.logout()
	time.sleep(2)

def test_add_secreatry(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	app.secretary.contact_person( secr_old_email="secretary02@zetmail.com",
		secr_current_email='secretary05@zetmail.com', secr_new_email="secretary08@zetmail.com", secr_fullname="Ella Nil")
	assert app.session.text_name_attribute_attroney() == "Mark John Decastro"
	time.sleep(2)


"""same bar number"""
def test_add_attorney(app):
	app.session.login(login="a1@tafmail.com", password="123Qwer")
	time.sleep(2)
	app.add_art.contact_person(att_sbn='123456', att_email='sotka07@zetmail.com', att_phonenumber='+380982542188')
	app.session.logout()
"""different bar number"""



@pytest.mark.parametrize("regisrt_data", regisrt_data)
def test_registr_attorney(app,regisrt_data):
	app.regAttorney.registration_page(regisrt_data.bar_number)
	app.regAttorney.fill_form(regisrt_data.email)
	app.regAttorney.skip_secretary_button()
	time.sleep(2)
	app.regAttorney.continue_account_button()
	time.sleep(1)
	app.regAttorney.continue_account_button()
	app.regAttorney.password_input_enter(regisrt_data.password)