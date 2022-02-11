class EditPrice:
	def __init__(self, appearance_fee=None, page_cost=None, expert_page_cost=None,travel=None, estimated=None,
	turn_around_page=None, copy=None, cancellation_fee=None, cancellation_terms=None):
		self.appearance_fee = appearance_fee
		self.page_cost = page_cost
		self.expert_page_cost = expert_page_cost
		self.travel = travel
		self.estimated = estimated
		self.turn_around_page = turn_around_page
		self.copy = copy
		self.cancellation_fee = cancellation_fee
		self.cancellation_terms = cancellation_terms
