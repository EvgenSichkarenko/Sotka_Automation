import allure
import pytest
from data.data_model.data_test_op import op
from data.data_model.data_email import email

@allure.description("Forgot password test")
@pytest.mark.parametrize("op", op)
@pytest.mark.parametrize("emails", email)
def test_forgot_password(app, op, emails):
	assert app.forgot_password.forgot_ui(op.email)
	app.deposition.get_letter_from_email(login = "qaautomationop@yahoo.com", password = "jphbtksnxhediwws")
	assert app.deposition.compare_email_and_date(emails.email_forgot_password)
	app.deposition.get_link_from_email()
	app.forgot_password.set_new_credentials(password="ZXcv@123580")
	app.forgot_password.login(login="qaautomationop@yahoo.com", password="ZXcv@123580")
	assert "Cristoforo Andrea Giovannotto " == app.session.text_name_attribute_attroney()
	app.login.logout()