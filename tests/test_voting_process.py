import allure
import pytest
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr_voting import cr_voting
import time

"""test deposition case voting create"""
@allure.description("Create deposition case with time manually")
@pytest.mark.parametrize("deposition", deposition)
@pytest.mark.parametrize("op", op)
def test_deposition_create(app, deposition, op):
	app.session.login(login="attorney0@yahoo.com", password="1234Qwer")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition()
	app.deposition.attorneys(deposition.sbn_voting,op.name_voting)
	app.deposition.date_and_time_voting()
	app.session.logout()


def test_email_voting_as_op(app):
	app.deposition.get_link_from_email_op()


@pytest.mark.parametrize("op", op)
@pytest.mark.parametrize("att", attorneys)
@pytest.mark.parametrize("cr_voting", cr_voting)
def test_email_voting_as_attorney(app, cr_voting, op, att):
	app.deposition.get_link_from_email_attorney(password_att="1234Qwer", login_att="attorney0@yahoo.com",)
	app.deposition.upload_doc()
	app.deposition.delivery(cr_voting.name)
	app.deposition.finish_depo_attorney_voting(att.name,att.email,att.phone,op.name_voting,op.email_voting
		,op.phone_voting, cr_voting.name,cr_voting.email,cr_voting.phone)
	app.deposition.confirm()
