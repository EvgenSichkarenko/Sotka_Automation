import pytest
from data.data_model.data_registr_secretary import regisrt_secr
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_test_cr import cr
import time


"""add secretary"""
@pytest.mark.parametrize("secretary", regisrt_secr)
def test_add_secreatry(app, secretary):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.secretary.contact_person( secr_old_email="testSecattr@inboxbear.com",
		secr_new_email=secretary.secr_email, secr_fullname=secretary.secr_fullname)
	assert app.session.text_name_attribute_attroney() == "Joel William Meskin "
	app.session.logout()

"""same bar number"""
# def test_add_attorney_company(app):
# 	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
# 	app.add_art.attorney_company(att_sbn='123456', att_email_old='sotka02@zetmail.com',
# 		att_phonenumber='+380982542188', new_email='sotka0@zetmail.com')
# 	app.session.logout()

"""different bar number"""
def test_add_attr_dif_company(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.add_art.attorney_different_company(att_sbn='120001', att_email_old='sotka0@zetmail.com',
		new_email="sotka05@zetmail.com")
	app.session.logout()


"""add credit card"""
def test_add_card_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.att_credit.credit_card(card_number='4111111111111111', expiry_date='08/23', cvv='123')
	app.session.logout()


"""add new photo attorney"""
def test_add_photo_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	assert app.add_photo.add_photo()
	assert app.session.text_name_attribute_attroney() == "Joel William Meskin "
	app.session.logout()


"""test deposition case create"""
@pytest.mark.parametrize("deposition", deposition)
def test_deposition_create(app, deposition):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.deposition.name_deposition(deposition.name)
	app.deposition.deponent_deposition(deposition.deponent)
	app.deposition.location_deposition(deposition.address)
	app.deposition.attorneys(deposition.sbn_op1)
	app.deposition.set_time_manually()
	app.deposition.upload_doc()
	app.deposition.delivery()
	app.deposition.finish_depo()
	app.deposition.confirm()
	time.sleep(1)


"""test depo info attorney"""
@pytest.mark.parametrize("deposition", deposition)
def test_depo_info(app, deposition):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.depo_info_att.search_deposition(deposition.name)
	app.depo_info_att.check_info_deposition(deposition.name, deposition.deponent, deposition.date)
	app.session.logout()


"""test depo details info attorney"""
@pytest.mark.parametrize("deposition", deposition)
def test_detail_depo(app, deposition):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.depo_details_att.open_details()
	app.depo_details_att.check_deposition_data(deposition.name, deposition.deponent, deposition.attorney)
	app.depo_details_att.check_op_data()
	app.depo_details_att.details()
	time.sleep(1)


"""test calendar attorney"""
def test_calendar_att(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.calendar_att.saturday()
	assert app.calendar_att.text_no_deposition() == 'There are no meetings today'
	app.calendar_att.show_all_btn()
	assert app.calendar_att.count() == 1

"""test deposition info att"""
@pytest.mark.parametrize("attorneys", attorneys)
@pytest.mark.parametrize("deposition", deposition)
@pytest.mark.parametrize("op", op)
@pytest.mark.parametrize("cr", cr)
def test_info_deposition_att(app, attorneys, op, cr, deposition):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	assert app.att_finish_depo.deposition_info(deposition.name, deposition.address)
	assert app.att_finish_depo.op_info(op.name, op.email, op.phone)
	assert app.att_finish_depo.cr_info(cr.name, cr.email, cr.phone, cr.address)
	assert app.att_finish_depo.att_info(attorneys.name, attorneys.email, attorneys.phone)

"""test search attorney"""
def test_search_attorney(app):
	app.session.login(login="testatt@inboxbear.com", password="1234Qwer")
	app.find_att.input(name="Decastro")
	assert app.find_att.result() == "Mark John Decastro"
	app.find_att.input(name="1234")
	assert app.find_att.count() == 0