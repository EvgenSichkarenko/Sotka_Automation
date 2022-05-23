from model.model_email import Email
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_cr_voting import cr_voting


email = [Email(
	email_reg_att =f"Dear Jeka test qa, Thank you for signing up for Trialbase," \
					f" we are excited to have you withus! Please click the button below to let us know you've " \
				   f"received this emailand to confirm your Attorney account.",
	email_reg_cr=f"Dear Automation, Thank you for signing up for Trialbase," \
					f" we are excited to have you withus! Please click the button below to let us know you've received this emailand to confirm your Court Reporter account.",
	email_create_depo_manually_op = f"Dear {op[0].name}, This is to confirm that {attorneys[0].name} has noticed the deposition of{deposition[0].deponent} " \
	f"in {deposition[0].name} for",
	email_create_depo_manually_cr = f"Dear {cr_voting[0].name}, We have received a request for your appearance at the deposition " \
	f"of{deposition[0].deponent} in {deposition[0].name} on",
	email_befor_voting_op = f"Dear {op[0].name}, Attorney {attorneys[0].name} would like to depose {deposition[0].deponent} in{deposition[0].name}" \
	" and meet and confer about the deposition dateacceptable to all parties. Trialbase is an evolutionary platform that connects attorneys directly tocourt reporters. " \
	"We automate the scheduling process and offer streamlinedexperience at lower costs. Please choose acceptable dates on our platform:",
	email_owner_all_op_voting = f"Dear {attorneys[0].name}, This is to confirm that you have noticed the deposition of {deposition[0].deponent} " \
	f"in{deposition[0].name} for",
	email_cr_new_appearance = f"Dear {cr_voting[0].name}, We have received a request for your appearance at the deposition of{deposition[0].deponent} " \
	f"in {deposition[0].name} on",
	email_op_noticed_depo = f"Dear {op[0].name}, Attorney {attorneys[0].name} has noticed the deposition of {deposition[0].deponent} " \
	f"in{deposition[0].name} for",
	email_forgot_password = "We received your request to change password at Trialbase! Please click thebutton below to access your account",
	email_cr_agreed_for_deal = f"Dear {attorneys[0].name}, The {cr_voting[0].name} has accepted an appearance at the deposition"
	f" of {deposition[0].deponent}in {deposition[0].name} on"
)]