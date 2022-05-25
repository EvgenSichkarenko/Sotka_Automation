class ModelSecretary:
	def __init__(self, secr_email=None, secr_fullname=None, secr_new_name=None):
		self.secr_email = secr_email
		self.secr_fullname = secr_fullname
		self.secr_new_name = secr_new_name


	def __repr__(self):
		return "%s : %s,%s" % (self.secr_email, self.secr_fullname, self.secr_new_name)