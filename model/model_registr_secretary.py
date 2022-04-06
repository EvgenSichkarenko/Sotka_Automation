class ModelSecretary:
	def __init__(self, secr_email=None, secr_fullname=None):
		self.secr_email = secr_email
		self.secr_fullname = secr_fullname


	def __repr__(self):
		return "%s : %s" % (self.secr_email, self.secr_fullname)