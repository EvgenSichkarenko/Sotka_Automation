import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr import cr
import time


"""test deposition case manually create"""
@allure.description("Create deposition case with time manually")
@pytest.mark.parametrize("deposition", deposition)
@pytest.mark.parametrize("cr", cr)
@pytest.mark.parametrize("op", op)
@pytest.mark.parametrize("att", attorneys)
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
	app.deposition.confirm()
	app.session.logout()
	# app.deposition.depo_dashboard_manualy(deposition.name)
	# app.deposition.finish_depo_attorney(deposition.name,att.name,att.email,att.phone,op.name,op.email,op.phone,
	# cr.name,cr.email,cr.phone)

"""test confirm cr appearence"""
@pytest.mark.parametrize("deposition", deposition)
@pytest.mark.parametrize("cr", cr)
@pytest.mark.parametrize("op", op)
@pytest.mark.parametrize("att", attorneys)
def test_cr_appearances(app, deposition, cr, op, att):
	app.session.login(login="testcr20@getnada.com", password="1234Qwer")
	app.cr_appear.confirm_appear(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.cr_appear.check_data_dashboard(att.name, att.email, att.phone, op.name, op.email, op.phone)
	app.session.logout()

@pytest.mark.parametrize("deposition", deposition)
@pytest.mark.parametrize("att", attorneys)
def test_cr_add_transcript(app, att, deposition):
	app.session.login(login="testcr20@getnada.com", password="1234Qwer")
	app.cr_appear.past_deposition()
	app.session.logout()


"""test download any depo from past deposition attorney"""
def test_att_pastdepo_download(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.deposition.download_any_transcript()
	app.session.logout()