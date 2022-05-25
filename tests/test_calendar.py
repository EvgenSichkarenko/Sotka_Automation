import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email
import time

def test_check_deposition_dashboard_att(app):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.create_fake_deposition()
	time.sleep(2)
	assert app.deposition.depo_dashboard_manualy()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)
	app.session.logout()

@pytest.mark.parametrize("att", attorneys)
def test_check_deposition_dashboard_cr(app, att):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.create_fake_deposition()
	app.deposition.confirm_appearance(att.email)
	time.sleep(2)
	assert app.deposition.depo_dashboard_manualy()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)
	app.session.logout()

"""create depo and decline cr deposition, check email owner"""
@allure.description("create depo and decline cr deposition, check email owner")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("emails", email)
def test_decline_appearence(app, deposition, cr_voting, op, att, emails):
	app.deposition.create_fake_deposition()
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	assert app.deposition.compare_email_and_date(emails.cr_new_appearance_fake)  # 7 email
	app.deposition.get_link_from_email()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.decline_appearence_cr(att.email, att.name, cr_voting.name, deposition.name)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.cr_decline_apear_fake)  # 6 email
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

"""test confirm cr appearence"""
@allure.description("Confirm appearance from cr and check data")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_cr_confirm_appearances(app, deposition, op, att, emails):
	app.deposition.create_fake_deposition()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.cr_appear.confirm_appear(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	print(emails.cr_accept_apear_fake)
	assert app.deposition.compare_email_and_date(emails.cr_accept_apear_fake)  #8  email
	app.cr_appear.check_data_dashboard(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)