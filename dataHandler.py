import instaloader
import time
import random


class dataHandler:

    def login(self, user, password):

        self.user = user
        self.password = password

        self.loader = instaloader.Instaloader()
        self.loader.login(user, password)

    def getHashtagData(self, hashtag, limit, atMark, isCommentedUser):
        if not limit:
            self.limit = 100
        self.limit = int(limit)
        atValue = ''
        filePath = 'C:\\Users\\Uname\\Documents\\'
        fileName = filePath + 'Text.txt'

        if int(isCommentedUser) == 1:
            fileName = filePath + 'Commenters.txt'

        if int(atMark) == 1:
            atValue = '@'

        postCount = 0
        pCount = 0
        self.users_file = open(fileName, 'w+')
        posts = self.loader.get_hashtag_posts(hashtag)

        for post in posts:

            if not post:
                print("No users found")
                break
            if postCount >= self.limit:
                break

            if int(isCommentedUser) == 1:
                pCount = pCount + 1
                self.sleepFew(pCount)

                if post.comments > 0:
                    postComments = post.get_comments()

                    for comment in postComments:
                        self.users_file.write(atValue + str(comment.owner).split(None)[1] + '\n')
                        postCount = postCount + 1
                        print(postCount)
                        self.sleepFew(postCount)
                        if postCount == self.limit:
                            break

            elif int(isCommentedUser) == 0:
                postUsername = ''
                noError = True

                try:
                    postUsername = post.owner_username
                except Exception as e:
                    print(e)
                    noError = False

                if noError:
                    self.users_file.write(atValue + postUsername + '\n')
                    postCount = postCount + 1
                    print(postCount)
                self.sleepFew(postCount)

        self.users_file.close()
        self.loader.close()
        print("done")

    def sleepFew(self, postCount):
        if postCount % 100 == 0:
            time.sleep(random.randint(2, 5))
