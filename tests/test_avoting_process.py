import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email
import time

"""create depo and decline cr deposition, check email owner"""
@allure.description("create depo and decline cr deposition, check email owner")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_deposition_create_decline_appearence(app, deposition, cr_voting, op, att):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,
		op.name,op.email, op.phone,cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	time.sleep(2)
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.decline_appearence_cr(att.email, att.name, cr_voting.name, deposition.name)


"""test deposition case voting create"""
@allure.description("Add op and voting")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(i) for i in attorneys])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
def test_deposition_create_voting(app, deposition, op, emails, att, cr_voting):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.date_and_time_voting()
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	app.deposition.compare_email_and_date(emails.email_befor_voting_op) #10 email
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.email_owner_all_op_voting) #24 email
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580")
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	#check email for op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_op_noticed_depo) #12 email
	#check email for cr new appearance
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	print(emails.email_cr_new_appearance)
	assert app.deposition.compare_email_and_date(emails.email_cr_new_appearance) #7 email
	app.deposition.get_link_from_email()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	time.sleep(2)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	print(emails.email_cr_agreed_for_deal)
	assert app.deposition.compare_email_and_date(emails.email_cr_agreed_for_deal) #8 email
	app.deposition.delete_deposition_from_database()


