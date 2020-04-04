class Gamer():
    def __init__(self,name,position):
    	'''玩家信息类'''
    	self.gamer_ID = 0
		self.gamer_name = name
		self.gamer_password = 0

		self.gamer_point = 1000
		self.gamer_match_nums = 10
		self.gamer_match_nums_win = 5
		self.gamer_status = 1

		'''玩家对局类信息'''
		self.match_cards = []
		self.match_cards_drop = []
		self.match_cards_nums = 0
		self.match_position = position  # 1-2-3-1...
		self.match_role = 0
		self.match_turn = 0

	# 码牌
	def gamer_cards_sort(self):
		return self.match_cards




