import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_email import email
import time

"""test deposition case manually create and change day in deposition"""
@allure.description("Create deposition case and cansel depo with check dots in calendar on home page")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_deposition_create_manually_cansel(app, deposition, cr_voting, op, att):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op, op.email)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email
		,op.phone,cr_voting.name,cr_voting.email,cr_voting.phone)
	app.deposition.cansel_deposition(deposition.name)
	app.session.logout()

"""test deposition case manually create and change day in deposition"""
@allure.description("Edit deposition with change date")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_deposition_create_manually_edit(app, deposition, cr_voting, op, att):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op, op.email)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email
		,op.phone,cr_voting.name,cr_voting.email,cr_voting.phone)
	app.deposition.depo_dashboard_manualy(deposition.name)
	app.deposition.edit_date_in_depo()
	app.session.logout()

"""test deposition case manually create"""
@allure.description("Create deposition case with time manually")
@pytest.mark.parametrize("emails", email)
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr_voting", cr_voting, ids=[repr(x) for x in cr_voting])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_deposition_create_manually(app, deposition, cr_voting, op, att, emails):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op, op.email)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email
		,op.phone,cr_voting.name,cr_voting.email,cr_voting.phone)
	time.sleep(3)
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_create_depo_manually_op)
	app.deposition.get_letter_from_email(login = "qaautomationcr@yahoo.com", password = "rsjbfjbpzorrntuc")
	assert app.deposition.compare_email_and_date(emails.email_create_depo_manually_cr)
	app.deposition.depo_dashboard_manualy(deposition.name)
	app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email,op.phone,
		cr_voting.name,cr_voting.email,cr_voting.phone)
	app.deposition.delete_deposition_from_database(app.deposition.number_of_deposition)
	app.session.logout()



@allure.description("Upload transcript, cr")
@pytest.mark.skip(reason="No deposition for uppload transcript")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_cr_add_transcript(app, att, deposition):
	app.session.login(login="qaautomationcr@yahoo.com", password="ZXcv@123580")
	app.cr_appear.past_deposition()
	app.session.logout()

"""test download transcript from past deposition attorney"""
@allure.description("Download transcript, attorney")
def test_att_pastdepo_download_transcript(app):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.download_any_transcript()
	app.session.logout()

"""test download deposition pdf file from past deposition attorney"""
@allure.description("Download transcript, attorney")
def test_att_past_depo_download_depo(app):
	app.session.login(login="qaautomationatt@yahoo.com", password="ZXcv@123580")
	app.deposition.download_depo_document()
	app.session.logout()