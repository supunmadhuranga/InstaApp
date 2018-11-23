#

import instaloader

class dataHandler:

	def login(self, user, password):
		
		self.user = user
		self.password = password

		global loader
		loader = instaloader.Instaloader()
		loader.login(user, password)

		USER = user
		PROFILE = USER
		profile = instaloader.Profile.from_username(loader.context, PROFILE)

	def getHashtagData(self, hashtag, limit):
		self.limit = limit
		users = []
		for post in loader.get_hashtag_posts(hashtag):
			if not post:
				print("No users found")
				break
			users.append(post.owner_username)
		my_set = set(users)
		count = 0
		if (len(my_set) > 0):
			users_file = open('user.txt', 'w+')
			for item in my_set:
				if count != limit:
					users_file.write(item+'\n')
					count = count + 1
			print("done")
		else:
			print("no users found")

	
	def findDuplicate(self, u):
		for line in open('user.txt', 'r'):
			if line.rstrip('\n') == u:
				return False
		return True
		


obj = dataHandler()

obj.login("","")
obj.getHashtagData('', 10)



