class OpposingCouncel:
	def __init__(self,name_voting=None, email_voting=None, phone_voting=None, name=None, email=None, phone=None):
		self.name_voting = name_voting
		self.email_voting = email_voting
		self.phone_voting = phone_voting
		self.name = name
		self.email = email
		self.phone = phone

	def __repr__(self):
		return "%s : %s;%s;%s;%s;%s" % (self.name, self.email, self.phone, self.name_voting, self.email_voting, self.phone_voting)