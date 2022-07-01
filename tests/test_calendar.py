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
@allure.description("Test case 3.1, check deposition cases current day and shows all deposition")
def test_3_1calendar_att(app, att, cr_voting, deposition, op):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.begin_date_voting()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CirclePending']")
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws") #10 email op
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
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CircleApproved']")
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)

#Test case 3.2 Need check after add attribute to calendar voting Alex
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(i) for i in op])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(i) for i in cr_voting])
@pytest.mark.parametrize("deposition", deposition, ids=[repr(i) for i in deposition])
@allure.description("Test case 3.2")
def test_3_2calendar_second_event(app, att, deposition, op,cr_voting):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.begin_date_voting()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CirclePending']")
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CircleApproved']")
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CircleApproved']")
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CirclePending']") == False
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

#Test case 3.3
@allure.description("Test case 3.3, Calendar second event (Green & Yellow dot's) 2 dots")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
def test_3_3_calandar_two_dots(app,deposition, att, op, emails):
	app.deposition.create_fake_deposition_voting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op,op.email)
	app.deposition.begin_date_voting()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CirclePending']")
	app.session.logout()
	#test email voting as op
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	app.deposition.get_link_from_email()
	app.deposition.select_date_op_voting()
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CirclePending']")
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CircleApproved']")
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)
	app.deposition.delete_deposition_from_database(app.deposition.id_fake_depo)


#Test case 3.5
@allure.description("Test case 3.5, Deleting an event")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("emails", email)
def test_3_5_deleting_an_event(app,deposition, att, op, emails):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,
	 	locator="div[data-name='CircleApproved']")
	app.deposition.cancel_deposition()
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,
		locator="div[data-name='CircleApproved']") == False
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

#Test case 3.6
@allure.description("Test case 3.6, Deleting an event (multiple events)")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
def test_3_6_del_an_event_multiple(app, deposition):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.deposition.create_fake_deposition_voting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CirclePending']")
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CircleApproved']")
	app.deposition.cancel_deposition()
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,
		locator="div[data-name='CirclePending']") == False
	assert app.calendar_att.check_el_present(day=app.calendar_att.day,locator="div[data-name='CircleApproved']")
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)
	app.deposition.delete_deposition_from_database(app.deposition.id_fake_depo)


#Test case #3.7, 2.12
"""test deposition case manually create and change day in deposition"""
@allure.description("Test case 3.7, 2.12, Edit deposition with change date")
#@pytest.mark.skip("need fix")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_3_7deposition_create_manually_edit(app, deposition, cr_voting, op, att):
	app.deposition.create_fake_deposition_waiting(status="false")
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.calendar_att.calendar_day()
	assert app.calendar_att.check_el_present(app.calendar_att.day,locator="div[data-name='CircleApproved']")
	app.deposition.edit_date_in_depo()
	app.calendar_att.next_day()
	assert app.calendar_att.check_el_present(app.calendar_att.tomorrow,locator="div[data-name='CircleApproved']")
	app.session.logout()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)

#Test case #3.8
@pytest.mark.parametrize("att", attorneys)
@allure.description("Test case 3.8")
def test_3_8_check_deposition_dashboard_cr(app, att):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.deposition.create_fake_deposition_waiting(status="false")
	app.deposition.confirm_appearance(att.email)
	time.sleep(2)
	assert app.deposition.depo_dashboard_manualy()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)
	app.session.logout()

#Test case #3.9
@allure.description("Test case 3.9")
def test_3_9check_deposition_dashboard_att(app):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.create_fake_deposition_waiting(status="false")
	time.sleep(2)
	assert app.deposition.depo_dashboard_manualy()
	app.deposition.delete_deposition_from_database(app.deposition.id_case)
	app.session.logout()










