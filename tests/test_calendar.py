import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email
from data.data_model.data_edit_price import edit_price
import time

#Test case 3.1
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@allure.description("Test, check deposition cases current day and shows all deposition")
def test_calendar_att(app, att, cr_voting, deposition, op):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.date_and_time_voting()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(locator="div[data-name='CirclePending']")
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580")
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	#Change dot on green color
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CircleApproved']")
	app.session.logout()
	app.forgot_password.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	app.session.logout()
	app.forgot_password.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)

#Test case 3.2 Need check after add attribute to calendar voting Alex
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_calendar_second_event(app, att):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.date_and_time_voting()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CirclePending']")
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CircleApproved']")
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580")
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	app.session.logout()
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",
		locator="div[data-name='CirclePending']") == False
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CircleApproved']")
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

#Test case 3.3
@allure.description("Calendar second event (Green & Yellow dot's) 2 dots")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
def test_calandar_two_dots(app,deposition, att, op, emails):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.date_and_time_voting()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CirclePending']")
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	#test_email_voting_as_attorney
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	app.deposition.get_link_from_email()
	app.deposition.login_attorney_voting(login_att="qaautomationatt@yahoo.com", password_att="ZXcv@123580")
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.session.logout()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CirclePending']")
	app.session.logout()
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",
		locator="div[data-name='CirclePending']")
	app.session.logout()
	app.session.login(login = "qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	app.session.logout()
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",
		locator="div[data-name='CirclePending']")
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",
		locator="div[data-name='CirclePending']")
	app.deposition.delete_deposition_from_database()


#Test case 3.5
@allure.description("Deleting an event")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
def test_deleting_an_event(app,deposition, att, op, emails):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,
	 	locator="div[data-name='CircleApproved']")
	app.deposition.cansel_deposition()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,
		locator="div[data-name='CircleApproved']") == False
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

#Test case #3.8
@pytest.mark.parametrize("att", attorneys)
def test_check_deposition_dashboard_cr(app, att):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.create_fake_deposition_waiting(status="false")
	app.deposition.confirm_appearance(att.email)
	time.sleep(2)
	assert app.deposition.depo_dashboard_manualy()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)
	app.session.logout()

#Test case #3.9
def test_check_deposition_dashboard_att(app):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.create_fake_deposition_waiting(status="false")
	time.sleep(2)
	assert app.deposition.depo_dashboard_manualy()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)
	app.session.logout()










