import pytest
import allure
from data.data_model.data_registr_cr import cr_data
from data.data_model.data_registr_attorney import regisrt_data
from data.data_model.data_registr_secretary import regisrt_secr
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email
from data.data_model.op_unregistered import op_unreg
from data.data_model.data_edit_price import edit_price
import time
import os
from datetime import datetime


#Test case 1.1
@allure.description("Test case 1.1, Registration new attorney")
@pytest.mark.parametrize("email", email)
@pytest.mark.parametrize("regisrt_data", regisrt_data, ids=[repr(i) for i in regisrt_data])
def test_registr_attorney(app,regisrt_data, email):
	app.regAttorney.registration_page(regisrt_data.bar_number)
	app.regAttorney.fill_form(regisrt_data.email, regisrt_data.bar_number, regisrt_data.phone_number, regisrt_data.address_two)
	app.regAttorney.assert_secreatry()
	app.regAttorney.skip_secretary()
	app.regAttorney.password_input_enter(regisrt_data.valid_password,regisrt_data.invalid_password,regisrt_data.password_match)
	assert app.regAttorney.check_send_mail()
	assert app.regAttorney.check_confirmation_letter(email.email_reg_att, log="testqa000000@yahoo.com", password="ksbbaatxxwotyabq")
	app.regAttorney.delete_att_from_database()

#Test case 1.2
@allure.description("Test case 1.2, Registration new cour reporter")
@pytest.mark.parametrize("cr_data", cr_data, ids=[repr(i) for i in cr_data])
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("prices", edit_price)
def test_reg_cr(app, cr_data, emails, prices):
	app.cr.cr_registration_form(cr_data.bar_number)
	assert cr_data.bar_number == app.cr.license_num_input_attribute()
	app.cr.cr_data_form(cr_data.email, cr_data.phone_number, cr_data.full_name, cr_data.issuance,
		cr_data.expiration_data, cr_data.address_one, cr_data.addres_two)
	app.cr.price_form()
	app.cr.set_password(cr_data.valid_password)
	assert app.cr.check_send_mail()
	assert app.cr.check_confirmation_letter(emails.email_reg_cr)
	app.cr.delete_att_from_database()

#Test case 1.3
@allure.description("Login attorney with invalid and valid data")
@pytest.mark.skip(reason="edit time zone")
@pytest.mark.login
def test_login_attorney(app):
	print(time.strftime('%Y-%m-%d %H:%M:%S'))  # before timezone change
	os.system('tzutil /s "Central America Standard Time"')
	time.sleep(5)
	# app.login.change_time_zone()
	# time.sleep(5)
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="qaautomationatt@yahoo.com", valid_password="ZXcv@123580")
	assert "Daniel Vlad Tabakh " == app.session.text_name_attribute_attroney()
	print(datetime.now())
	app.login.logout()


#Test case 1.4
@allure.description("Test case 1.4, Login cour reporter with invalid and valid data")
def test_login_cr(app):
	app.login.login(invalid_login="a123", invalid_password="13",
		valid_login="qaautomationcr@yahoo.com", valid_password="ZXcv@123580")
	assert app.session.text_name_attribute_cr() == "AutomationCR "
	app.login.logout()



#Test case 1.6
@allure.description("Test case 1.6, Unregistered op sign up")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("regisrt_data", regisrt_data, ids=[repr(i) for i in regisrt_data])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("op_unreg", op_unreg, ids=[repr(x) for x in op_unreg])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_unregistered_user_signup(app, deposition, cr_voting, op, att, op_unreg, emails,regisrt_data):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.regAttorney.add_op_unregister(deposition.sbn_op_unreg, op_unreg.sbn)
	app.deposition.date_and_time_voting()
	app.session.logout()
	app.deposition.get_letter_from_email(login="qaautomationopunreg@yahoo.com", password="gvwdvmcqjriiwupp")
	assert app.deposition.compare_email_and_date(emails.email_opunregistr_vote)#email 10 for op unregistered
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	app.regAttorney.create_acc_unregistr()
	app.regAttorney.add_bar_number(deposition.sbn_op_unreg)
	app.regAttorney.fill_form(op_unreg.email, regisrt_data.bar_number, regisrt_data.phone_number, regisrt_data.address_two)
	app.regAttorney.next_step()
	app.regAttorney.assert_secreatry()
	app.regAttorney.skip_secretary()
	app.regAttorney.password_input_enter(regisrt_data.valid_password,regisrt_data.invalid_password,regisrt_data.password_match)
	assert app.regAttorney.check_send_mail()
	app.deposition.get_letter_from_email(login="qaautomationopunreg@yahoo.com", password="gvwdvmcqjriiwupp")
	app.deposition.get_link_from_email()
	app.session.login(login="qaautomationopunreg@yahoo.com", password="1234Qwer")
	app.session.text_name_attribute_attroney() == " Jeka test unregister op"
	app.session.logout()
	app.regAttorney.delete_op_from_database()
	app.deposition.delete_deposition_from_database(id_depo=app.deposition.number_of_deposition)


#Test case 1.8
@allure.description("Test case 1.8, Forgot password test")
@pytest.mark.parametrize("op", op)
@pytest.mark.parametrize("emails", email)
def test_forgot_password(app, op, emails):
	assert app.forgot_password.forgot_ui(op.email)
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_forgot_password)
	app.deposition.get_link_from_email()
	app.forgot_password.set_new_credentials(password="ZXcv@123580")
	app.forgot_password.login(login="qaautomationop@yahoo.com", password="ZXcv@123580")
	assert "Cristoforo Andrea Giovannotto " == app.session.text_name_attribute_attroney()
	app.login.logout()

# Test case 1.11
@allure.description("Test case 1.11")
@pytest.mark.parametrize("regisrt_data", regisrt_data, ids=[repr(i) for i in regisrt_data])
@pytest.mark.parametrize("emails", email)
def test_add_attorney_company(app, regisrt_data, emails):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.add_att.attorney_company(regisrt_data.bar_number, registr_email="Jeka test qa")
	app.session.logout()
	app.deposition.get_letter_from_email(login="testqa000000@yahoo.com", password="ksbbaatxxwotyabq")
	assert app.deposition.compare_email_and_date(emails.email_invite_att_to_company) #2 email
	time.sleep(3)
	app.deposition.get_link_from_email()
	app.add_att.set_password(password="1234Qwer")
	app.secretary.login(login="testqa000000@yahoo.com", password="1234Qwer")
	assert app.session.text_name_attribute_attroney() == "Jeka test qa "
	app.session.logout()
	app.add_att.delete_att_from_database(regisrt_data.bar_number)

#Test case 1.12
@allure.description("Test case 1.12, Test search attorney in a company")
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_search_attorney(app, att):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.find_att.input(name="  ")
	assert app.find_att.count() == 1
	app.find_att.input(name="Daniel")
	assert app.find_att.count() == 2
	assert app.find_att.check_name(att.name) == att.name
	app.session.logout()

#Test case 1.9/ 1.14 удалять секретаря Антон
@allure.description("Test case 1.14, 1.9, Registration new attorney with secretary")
@pytest.mark.parametrize("email", email)
@pytest.mark.parametrize("secretary", regisrt_secr, ids=[repr(x) for x in regisrt_secr])
@pytest.mark.parametrize("regisrt_data", regisrt_data, ids=[repr(i) for i in regisrt_data])
def test_reg_att_with_secr(app, regisrt_data, email, secretary):
	app.regAttorney.registration_page(regisrt_data.bar_number)
	app.regAttorney.fill_form(regisrt_data.email, regisrt_data.bar_number, regisrt_data.phone_number,
		regisrt_data.address_two)
	app.regAttorney.add_secretary(secretary.secr_new_name, secretary.secr_email)
	app.regAttorney.password_input_enter(regisrt_data.valid_password, regisrt_data.invalid_password,
	regisrt_data.password_match)
	assert app.regAttorney.check_send_mail()
	app.deposition.get_letter_from_email(login="qaautomationsecrdel@yahoo.com", password="xudxrtihgkpxetfh")
	app.deposition.compare_from_to_email(from_m="Trialbase <info@trialbase.com>", to_m="qaautomationsecrdel@yahoo.com")
	print(email.email_invite_new_secr)
	assert app.deposition.compare_email_and_date(email.email_invite_new_secr)
	app.deposition.get_link_from_email()
	app.secretary.set_password(password="1234Qwer")
	app.secretary.login(login="qaautomationsecrdel@yahoo.com", password="1234Qwer")
	assert app.session.text_name_attribute_secretary() == "Secretary QA "
	app.session.logout()
	app.regAttorney.delete_att_from_database()

#Test case 1.18 / 1.10
@allure.description("Test case 1.18, 1.10, Add new secretary for attorney company")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("secretary", regisrt_secr, ids=[repr(x) for x in regisrt_secr])
def test_add_secretary(app, secretary, emails):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.secretary.contact_person( secr_old_email="qaautomationsecr@yahoo.com",
		secr_new_email=secretary.secr_email, secr_fullname=secretary.secr_new_name)
	time.sleep(3)
	app.session.logout()
	app.deposition.get_letter_from_email(login="qaautomationsecrdel@yahoo.com", password="xudxrtihgkpxetfh")
	assert app.deposition.compare_email_and_date(emails.email_invite_att_to_company) #email 2
	app.deposition.get_link_from_email()
	app.secretary.set_password(password="1234Qwer")
	app.secretary.login(login="qaautomationsecrdel@yahoo.com", password="1234Qwer")
	assert app.session.text_name_attribute_secretary() == "Secretary QA "
	app.session.logout()
	app.forgot_password.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	assert app.secretary.check_secr_on_dashboard()
	app.secretary.delete_secretary_from_database(secretary.secr_email)