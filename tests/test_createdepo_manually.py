import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr import cr
import time


"""test deposition case manually create"""
@allure.description("Create deposition case with time manually")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr", cr, ids=[repr(x) for x in cr])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_deposition_create_manually(app, deposition, cr, op, att):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_op1, op.name)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery(cr.name)
	app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email
		,op.phone,cr.name,cr.email,cr.phone)
	app.session.logout()
	# app.deposition.depo_dashboard_manualy(deposition.name)
	# app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email,op.phone,
	# cr.name,cr.email,cr.phone)

"""test confirm cr appearence"""
@allure.description("Confirm appearance from cr and check data")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("cr", cr, ids=[repr(x) for x in cr])
@pytest.mark.parametrize("op", op, ids=[repr(x) for x in op])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_cr_appearances(app, deposition, cr, op, att):
	app.session.login(login="report@inboxbear.com", password="1234Qwer")
	app.cr_appear.confirm_appear(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.cr_appear.check_data_dashboard(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.session.logout()

@allure.description("Upload transcript, cr")
@pytest.mark.parametrize("deposition", deposition, ids=[repr(x) for x in deposition])
@pytest.mark.parametrize("att", attorneys, ids=[repr(x) for x in attorneys])
def test_cr_add_transcript(app, att, deposition):
	app.session.login(login="cr@givmail.com", password="Counsel10")
	app.cr_appear.past_deposition()
	app.session.logout()

"""test download transcript from past deposition attorney"""
@allure.description("Download transcript, attorney")
def test_att_pastdepo_download_transcript(app):
	app.session.login(login="a1@getnada.com", password="Attorney95")
	app.deposition.download_any_transcript()
	#app.session.logout()

"""test download deposition pdf file from past deposition attorney"""
@allure.description("Download transcript, attorney")
def test_att_past_depo_download_depo(app):
	app.session.login(login="a1@getnada.com", password="Attorney95")
	app.deposition.download_depo_document()
	#app.session.logout()