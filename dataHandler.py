import instaloader


class dataHandler:

    def login(self, user, password):

        self.user = user
        self.password = password

        self.loader = instaloader.Instaloader()
        self.loader.login(user, password)

    def getHashtagData(self, hashtag, limit, filePath, atMark):
        if not limit:
            self.limit = 100
        self.limit = int(limit)
        users = []

        postCount = 0
        for post in self.loader.get_hashtag_posts(hashtag):
            if not post:
                print("No users found")
                break
            if postCount == self.limit:
                break

            users.append(post.owner_username)
            postCount = postCount + 1
        my_set = set(users)
        atValue = ''

        if filePath:
            fileName = filePath
        else:
            fileName = 'users_hashtag_posts.txt'

        if int(atMark) == 1:
            atValue = '@'

        if (len(my_set) > 0):
            users_file = open(fileName, 'w+')
            for item in my_set:
                users_file.write(atValue + item + '\n')
            print("done")
        else:
            print("no users found")
