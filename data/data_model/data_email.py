from model.model_email import Email
from data.data_model.data_test_op import op
from data.data_model.data_test_attorney import attorneys
from data.data_model.data_deposition_case import deposition
from data.data_model.data_test_cr_voting import cr_voting
from data.data_model.data_registr_secretary import regisrt_secr
from data.data_model.op_unregistered import op_unreg
from datetime import datetime

email = [Email(
	#Test case 1.1
	email_reg_att =f"Dear Jeka Test Qa, Thank you for signing up for Trialbase," \
					f" we are excited to have you withus! Please click the button below to let us know you've " \
				   f"received this emailand to confirm your Attorney account.",
	#Test case 1.2
	email_reg_cr=f"Dear Automation, Thank you for signing up for Trialbase," \
					f" we are excited to have you withus! Please click the button below to let us know you've received this emailand to confirm your Court Reporter account.",
	# Test case 1.11, email 2
	email_invite_att_to_company=f"You’ve been invited by {attorneys[0].name} to join Trialbase and discoverthe new world"
	f" of deposition scheduling!  Please click the button below to let us know you've received this email  and confirm your account.",
	#Testc casee 1.18, 1.10
	email_invite_new_secr = f"You’ve been invited by {deposition[0].fake_name} to join Trialbase and discover thenew world"
	f" of deposition scheduling!  Please click the button below to let us know you've received this email  and confirm your account.",
	email_create_depo_manually_op = f"Dear {op[0].name}, This is to confirm that {attorneys[0].name} has noticed the deposition of{deposition[0].deponent} " \
	f"in {deposition[0].name} for",

	email_att_confirm_psw = "Set password for your account Please click the button and set password for your account",
	email_create_depo_manually_cr = f"Dear {cr_voting[0].name}, We have received a request for your appearance at the deposition " \
	f"of{deposition[0].deponent} in {deposition[0].name} on",
	#email 10
	email_befor_voting_op = f"Dear {op[0].name}, Attorney {attorneys[0].name} would like to depose {deposition[0].deponent} in{deposition[0].name}" \
	" and meet and confirm about the deposition dateacceptable to all parties. Trialbase is an evolutionary platform that connects attorneys directly tocourt reporters. " \
	"We automate the scheduling process and offer streamlinedexperience at lower costs. Please choose acceptable dates on our platform:",
	#Test case  2.2 email 24
	email_owner_all_op_voting = f"Dear {attorneys[0].name}, Opposing Counsel has responded to the proposeddates for the deposition of {deposition[0].deponent} " \
	f"in {deposition[0].name}. Please review the response and complete the deposition setting process.",
	# email 7
	email_cr_new_appearance = f"Dear {cr_voting[0].name}, We have received a request for your appearance at the deposition of{deposition[0].deponent} " \
	f"in {deposition[0].name} on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day}, "
	f"{datetime.now().year}, at12:00 AM (PST). You have 12 hours to accept this assignment in yourTrialbase account: "
    f">>Accept Assignment<< <https://demo.trialbase.com> If we do not receiveyour confirmation within the next 12 hours, we will remove this appearancefrom your account. Thank you, Trialbase",
	# email 12
	email_op_noticed_depo = f"Dear {op[0].name}, Attorney {attorneys[0].name} has noticed the deposition of {deposition[0].deponent} " \
	f"in{deposition[0].name} for {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day}, "
	f"{datetime.now().year}, at 12:00 AM(PST). Thank you, Trialbase",
	email_forgot_password = "We received your request to change password at Trialbase! Please click thebutton below "
							"to access your account",
	# email 8 att
	email_cr_agreed_for_deal = f"Dear {attorneys[0].name}, The {cr_voting[0].name} has accepted an appearance at the deposition"
	f" of {deposition[0].deponent}in {deposition[0].name} on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')}"
	f" {datetime.now().day}, {datetime.now().year}, at 12:00 AM(PST). You are all set for this deposition, but you can always "
							   f"make analternative selection by visiting your Trialbase account:",
	email_all_op_vote= f"Dear {attorneys[0].name}, All parties have responded to the proposed dates for the deposition "
	f"of{deposition[0].deponent} in {deposition[0].name}.",
	email_cr_decline = f"Dear {attorneys[0].name}, {cr_voting[0].name} declined an appearance at the deposition of{deposition[0].deponent} "
	f"in ",
	#Test case 2.6 email 7
	cr_new_appearance_fake = f"Dear {cr_voting[0].name}, "
							 f"We have received a request for your appearance at the deposition of"
	f"{deposition[0].fake_deponent} in {deposition[0].fake_name_case} on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day},"
	f"{datetime.now().year}, at 12:00 AM (PST). You have 12 hours to accept this assignment inyour Trialbase account:",
	#Test case 2.6 email 6
	cr_decline_apear_fake = f"Dear {attorneys[0].name}, {cr_voting[0].name} declined an appearance at the deposition of "
	f"{deposition[0].fake_deponent} in{deposition[0].fake_name_case} on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day}, "
	f"{datetime.now().year}, at 12:00 AM(PST).",
	#Test case 2.15 email 8
	cr_accept_apear_fake = f"Dear {attorneys[0].name}, The {cr_voting[0].name} has accepted an appearance at the deposition "
	f"of{deposition[0].fake_deponent} in {deposition[0].fake_name_case} on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day},"
	f"{datetime.now().year}, at 12:00 AM (PST). You are all set for this deposition, but you canalways make an alternative selection by visiting your Trialbase account:",
	#Test case 2.9, 2.10, 2.11, 2.16, 2.8
	email_op_transcript_add = f"Dear {op[0].name}, The transcript of the deposition of{deposition[0].fake_deponent} in {deposition[0].fake_name_case} completed on "
	f"{datetime.now().strftime('%A')},{datetime.now().strftime('%B')} {datetime.now().day}, {datetime.now().year}, at 02:00 AM (PST) is now available for download on yourTrialbase account:",
	email_att_transcript_add = f"Dear {attorneys[0].name}, The transcript of the deposition of {deposition[0].fake_deponent}in {deposition[0].fake_name_case} completed "
	f"on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day}, {datetime.now().year}, at02:00 AM (PST), is now available for download on your Trialbase account:",
	email_op_unregist_transcript = f"Dear {op_unreg[0].name}, The transcript of the deposition of {deposition[0].fake_deponent} in{deposition[0].fake_name_case} completed "
	f"on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day}, {datetime.now().year}, at02:00 AM (PST) is now available for download by this link",

	email_secr_op_confirm_depo = f"Dear {regisrt_secr[0].secr_fullname}, Opposing Counsel has responded to the proposed dates for thedeposition "
	f"of {deposition[0].deponent} in {deposition[0].name}",
	email_opunregistr_vote = f"Dear {op_unreg[0].name}, Attorney {attorneys[0].name} would like to depose {deposition[0].deponent} "
	f"in{deposition[0].name} and meet and confirm about the deposition dateacceptable to all parties. Trialbase is an evolutionary "
	f"platform that connects attorneys directly tocourt reporters. We automate the scheduling process and offer "
	f"streamlinedexperience at lower costs. Please choose acceptable dates on our platform",
	#Test case 2.21/2.33 email 8 for secretary
	email_secretary_cr_accept = f"Dear {regisrt_secr[0].secr_fullname}, The {cr_voting[0].name} has accepted an appearance at the "
	f"deposition of {deposition[0].deponent}in {deposition[0].name}",
	#Test case 2.4 email 18
	email_owner_cancel_depo = f"Dear {cr_voting[0].name}, We have received {attorneys[0].name} request to cancel the deposition of"
	f"{deposition[0].fake_deponent} in {deposition[0].fake_name_case} on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day},"
	f"{datetime.now().year}, at 12:00 AM (PST).You can review the details of this transaction byvisiting your Trialbase account:",
	#Test case 2.20 email 21
	email_cr_cancel_depo = f"Dear {attorneys[0].name}, {cr_voting[0].name} declined deposition at the deposition of {deposition[0].fake_deponent}"
	f" in{deposition[0].fake_name_case} on {datetime.now().strftime('%A')}, {datetime.now().strftime('%B')} {datetime.now().day}, "
	f"{datetime.now().year}, at 12:00 AM(PST). You are all set for this deposition, but you can always make analternative selection by visiting your Trialbase account: "
)]