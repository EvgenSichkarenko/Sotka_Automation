class DepositonCase:
	def __init__(self, name=None, deponent=None,sbn_op1=None,
	sbn_voting=None):
		self.name = name
		self.deponent = deponent
		self.sbn_op1 = sbn_op1
		self.sbn_voting = sbn_voting

	def __repr__(self):
		return "%s : %s;%s;%s" % (self.name, self.deponent, self.sbn_op1, self.sbn_voting)