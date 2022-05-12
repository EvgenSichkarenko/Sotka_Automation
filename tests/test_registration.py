import pytest
import allure
from data.data_model.data_registr_cr import cr_data
from data.data_model.data_registr_attorney import regisrt_data
from data.data_model.data_registr_secretary import regisrt_secr
import time

#@pytest.mark.skip(reason="For test should change input date every time")
@allure.description("Registration new attorney")
@pytest.mark.parametrize("regisrt_data", regisrt_data, ids=[repr(i) for i in regisrt_data])
def test_registr_attorney(app,regisrt_data):
	app.regAttorney.registration_page(regisrt_data.bar_number)
	app.regAttorney.fill_form(regisrt_data.email, regisrt_data.bar_number, regisrt_data.phone_number, regisrt_data.address_two)
	app.regAttorney.assert_secreatry()
	app.regAttorney.add_secretary(regisrt_data.name_secretary, regisrt_data.email_secretary)
	#app.regAttorney.bank_account_button()
	app.regAttorney.img_account_send()
	app.regAttorney.password_input_enter(regisrt_data.valid_password,regisrt_data.invalid_password,regisrt_data.password_match)
	assert app.regAttorney.login_present() == 'Login'
	time.sleep(2)
	app.regAttorney.delete_att_from_database()


#@pytest.mark.skip(reason="For test should change input date every time")
@allure.description("Registration new cour reporter")
@pytest.mark.parametrize("cr_data", cr_data, ids=[repr(i) for i in cr_data])
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
	app.cr.delete_att_from_database()


"""add secretary"""
@allure.description("Add new secretary for attorney company")
@pytest.mark.parametrize("secretary", regisrt_secr, ids=[repr(x) for x in regisrt_secr])
def test_add_secreatry(app, secretary):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.secretary.contact_person( secr_old_email="testSecattr@inboxbear.com",
		secr_new_email=secretary.secr_email, secr_fullname=secretary.secr_fullname)
	assert app.session.text_name_attribute_attroney() == "Danielle Theresa Kennedy "
	time.sleep(4)
	app.session.logout()


# """different bar number"""
# def test_add_attr_dif_company(app):
# 	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
# 	app.add_art.attorney_different_company(att_sbn='120001', att_email_old='sotka0@zetmail.com',
# 		new_email="sotka05@zetmail.com")
# 	app.session.logout()

# """same bar number"""
# def test_add_attorney_company(app):
# 	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
# 	app.add_art.attorney_company(att_sbn='123456', att_email_old='sotka02@zetmail.com',
# 		att_phonenumber='+380982542188', new_email='sotka0@zetmail.com')
# 	app.session.logout()