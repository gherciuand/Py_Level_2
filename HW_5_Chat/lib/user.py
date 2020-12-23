class User:
    def __init__(self, nickname):
        self.nickname = nickname

    def __str__(self):
        return self.toJSON()

    def toJSON(self):
        return '{"cl":"User", "nickname":"'+self.nickname+'"}'

