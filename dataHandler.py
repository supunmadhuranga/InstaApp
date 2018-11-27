import instaloader
import time
import random

class dataHandler:

    def login(self, user, password):

        self.user = user
        self.password = password

        self.loader = instaloader.Instaloader()
        self.loader.login(user, password)

    def getHashtagData(self, hashtag, limit, atMark):
        if not limit:
            self.limit = 100
        self.limit = int(limit)
        atValue = ''
        fileName = 'C:\\Users\\Uname\\Documents\\Text.txt'
        fileNameComments = 'C:\\Users\\Uname\\Documents\\Commenters.txt'
        if int(atMark) == 1:
            atValue = '@'
			
        postCount = 0
        users_file = open(fileName, 'w+')
        commenters_file = open(fileNameComments, 'w+')
        posts = self.loader.get_hashtag_posts(hashtag)
        for post in posts:
            if post.comments > 0:
                for comment in post.get_comments():
                    commenters_file.write(atValue + str(comment.owner).split(None)[1] + '\n')
            postUsername = ''
            noError = True
            if not post:
                print("No users found")
                break
            if postCount == self.limit:
                break
            try:
                postUsername = post.owner_username
            except Exception as e:
                print(e)
                noError = False

            if noError:
                users_file.write(atValue + postUsername + '\n')
                postCount = postCount + 1
                print(postCount)
            if postCount % 100 == 0:
                time.sleep(random.randint(2, 5))
        users_file.close()
        commenters_file.close()
        self.loader.close()
        print("done")
        