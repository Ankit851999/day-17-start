class User:

    def __init__(self, user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0  # default value associated with each class
        self.following = 0
        print("new user has been created")

    def follow(self,user):
        user.followers += 1
        self.following += 1


# user_1 = User()
# user_1.id = "001"
# user_1.username = "ankit"
user_1 = User("001", "Ankit")
user_2 = User("002", "Kumar")
user_1.follow(user_2)


print(f"user id: {user_1.id} and user name: {user_1.username}")
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)