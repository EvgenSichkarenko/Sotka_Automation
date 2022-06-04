import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email
import time

#Test case 3.1
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@allure.description("Test, check deposition cases current day and shows all deposition")
def test_calendar_att(app, att):
	app.deposition.create_fake_deposition_voting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CirclePending']")
	app.session.logout()
	app.forgot_password.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.confirm_appearance(att.email)
	app.session.logout()
	app.forgot_password.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	#Change dot on green color
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CirclePending']")
	# count_all = app.calendar_att.count()
	# app.calendar_att.calendar_day()
	# today_all = app.calendar_att.count()
	# app.calendar_att.show_all_btn()
	# assert today_all >= 0
	# app.session.logout()

#Test case 3.2
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_calendar_second_event(app, att):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.deposition.create_fake_deposition_voting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CirclePending']")
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CircleApproved']")
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
	app.deposition.delete_deposition_from_database(app.deposition.id_fake_depo)

#Test case #3.9
def test_check_deposition_dashboard_att(app):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.create_fake_deposition_waiting(status="false")
	time.sleep(2)
	assert app.deposition.depo_dashboard_manualy()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)
	app.session.logout()

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

#Test case #2.6
"""create depo and decline cr deposition, check email owner"""
@allure.description("create depo and decline cr deposition, check email owner")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("emails", email)
def test_decline_appearence(app, deposition, cr_voting, op, att, emails):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	assert app.deposition.compare_email_and_date(emails.cr_new_appearance_fake)  # 7 email
	app.deposition.get_link_from_email()
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.decline_appearence_cr(att.email, att.name, cr_voting.name, deposition.name)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.cr_decline_apear_fake)  # 6 email
	app.deposition.delete_deposition_from_database(app.deposition.id_case)


#Test case #2.15
@allure.description("Confirm appearance from cr and check data")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_cr_confirm_appearances(app, deposition, op, att, emails):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.cr_appear.confirm_appear(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.cr_accept_apear_fake)  #8  email
	app.cr_appear.check_data_dashboard(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)


#Test case 2.9
@allure.description("Upload transcript, cr")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
def test_cr_upload_transcript(app, att, deposition, op, emails):
	app.deposition.create_fake_deposition_waiting(status="true")
	app.session.login(login = "qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.cr_appear.confirm_appear(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.cr_appear.past_deposition()
	app.cr_appear.upload_transcript()
	app.session.logout()
	time.sleep(2)
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_op_transcript_add) #email 15
	time.sleep(2)
	app.deposition.get_letter_from_email(login = "qaautomationatt@yahoo.com", password = "emxbsociwrqsdcwp")
	assert app.deposition.compare_email_and_date(emails.email_att_transcript_add) #email 14
	#download as attorney Test case 2.10
	app.deposition.login_without_open_link(login = "qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.download_any_transcript()
	app.session.logout()
	#download as op registered Test case 2.11
	app.deposition.login_without_open_link(login = "qaautomationop@yahoo.com", password="ZXcv@123580")
	app.deposition.download_any_transcript()
	app.session.logout()
	#download as op unregistered Test case 2.16
	app.deposition.get_letter_from_email(login="qaautomationopunreg@yahoo.com", password="gvwdvmcqjriiwupp")
	print(emails.email_op_unregist_transcript)
	assert app.deposition.compare_email_and_date(emails.email_op_unregist_transcript) #email 22
	app.deposition.get_link_from_email()
	app.deposition.delete_deposition_from_database(id_depo=app.deposition.id_case)


#Test case 3.3
@allure.description("Calendar second event (Green & Yellow dot's) 2 dots")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
def test_calandar_two_dots(app,deposition, att, op, emails):
	app.deposition.create_fake_deposition_voting(status="false")
	app.session.login(login = "qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",locator="div[data-name='CirclePending']")
	app.session.logout()
	app.deposition.create_fake_deposition_voting(status="false")
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
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",
		locator="div[data-name='CircleApproved']")

	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(block="div[data-name='attorneyHomePageCalendar']",
		locator="div[data-name='CircleApproved']") == False
