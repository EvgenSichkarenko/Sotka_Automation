from model.model_email import Email
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_cr_voting import cr_voting


email = [Email(
	email_reg_att =f"Dear Jeka Test Qa, Thank you for signing up for Trialbase," \
					f" we are excited to have you withus! Please click the button below to let us know you've " \
				   f"received this emailand to confirm your Attorney account.",
	email_reg_cr=f"Dear Automation, Thank you for signing up for Trialbase," \
					f" we are excited to have you withus! Please click the button below to let us know you've received this emailand to confirm your Court Reporter account.",
	email_invite_new_secr = f"You’ve been invited by {attorneys[0].name} to join Trialbase and discoverthe new world"
	f" of deposition scheduling!  Please click the button below to let us know you've received this email  and confirm your account.",
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
	f" of {deposition[0].deponent}in {deposition[0].name} on",
	email_all_op_vote= f"Dear {attorneys[0].name}, All parties have responded to the proposed dates for the deposition "
	f"of{deposition[0].deponent} in {deposition[0].name}.",
	email_cr_decline = f"Dear {attorneys[0].name}, {cr_voting[0].name} declined an appearance at the deposition of{deposition[0].deponent} "
	f"in ",
	cr_new_appearance_fake = f"Dear {cr_voting[0].name}, "
							 f"We have received a request for your appearance at the deposition of"
	f"{deposition[0].fake_deponent} in {deposition[0].fake_name} on",
	cr_decline_apear_fake = f"Dear {attorneys[0].name}, {cr_voting[0].name} declined an appearance at the deposition of "
	f"{deposition[0].fake_deponent} in{deposition[0].fake_name} on",
	cr_accept_apear_fake = f"Dear {attorneys[0].name}, The {cr_voting[0].name} has accepted an appearance at the deposition "
	f"of{deposition[0].fake_deponent} in {deposition[0].fake_name} on"
	# email_all_op_vote = f"Dear {attorneys[0].name}, {op[0].name} has responded to the proposed dates for thedeposition "
	# f"of {deposition[0].deponent} in {deposition[0].name}."
)]