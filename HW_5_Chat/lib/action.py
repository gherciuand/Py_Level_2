class Action:
    def __init__(self, type, target=None):
        self.type = type
        self.target = target

    def __str__(self):
        return self.toJSON()

    def toJSON(self):
        if self.target != None:
            target = ', "target": '+self.target.toJSON()
        else:
            target = ""
        return '{"cl":"Action","type":"' + self.type + '"' + target + '}'
