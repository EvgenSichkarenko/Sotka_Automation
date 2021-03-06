import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email
import time

#Test case 1.5
@allure.description("Test case 1.5, Login secretaru with valid data")
@pytest.mark.login
def test_1_5_login_secretary(app):
	app.login.login(invalid_login="a123", invalid_password="123",
		valid_login="qaautomationsecr@yahoo.com", valid_password="ZXcv@123580" )
	assert "Rita QA " == app.session.text_name_attribute_secretary()
	app.login.logout()


#Test case 2.21
@allure.description("Creates deposition")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
def test_2_21_create_depo_secr(app, emails, att, cr_voting, deposition, op):
	app.session.login(login="qaautomationsecr@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.begin_date_voting()
	#app.deposition.date_and_time_voting()
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_befor_voting_op) #10 email
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login="qaautomationsecr@yahoo.com", password="fnasmhrlsacdmozz")
	#print(emails.email_secr_op_confirm_depo)
	assert app.deposition.compare_email_and_date(emails.email_secr_op_confirm_depo) #11 email
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationsecr@yahoo.com", password_att="ZXcv@123580")
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	#check email for op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	#print(emails.email_op_noticed_depo)
	assert app.deposition.compare_email_and_date(emails.email_op_noticed_depo) #12 email
	#check email for cr new appearance
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	#print(emails.email_cr_new_appearance)
	assert app.deposition.compare_email_and_date(emails.email_cr_new_appearance) #7 email
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	app.deposition.get_letter_from_email(login = "qaautomationsecr@yahoo.com", password = "fnasmhrlsacdmozz")
	#print(emails.email_secretary_cr_accept)
	assert app.deposition.compare_email_and_date(emails.email_secretary_cr_accept) #8 email
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)

