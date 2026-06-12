class User:
    def __init__(self, name, username):
        self.name = name
        self.username = username
        self.followers = []
        self.following = []

    def follow(self, user):
        if user != self and user not in self.following:
            self.following.append(user)
            user.followers.append(self)

    def unfollow(self, user):
        if user in self.following:
            self.following.remove(user)
            user.followers.remove(self)

    def remove_follower(self, user):
        if user in self.followers:
            self.followers.remove(user)
            user.following.remove(self)

    def __repr__(self):
        return "@" + self.username


ali = User("Ali", "ali_99")
vali = User("Vali", "vali_uz")

ali.follow(vali)

print("Ali follows:", ali.following)
print("Vali followers:", vali.followers)

ali.unfollow(vali)

print("After unfollow:", ali.following)