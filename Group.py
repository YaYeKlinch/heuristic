class Group:
    groupArray = []

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return self.name + " (" + str(self.number) + " students)"

    def __str__(self):
        return  self.name + " (" + str(self.number) + " students)"

    @staticmethod
    def addGroup(name, number):
        Group.groupArray.append(Group(name, number))

    @staticmethod
    def getGroupByName(name):
        for i in range(len(Group.groupArray)):
            if Group.groupArray[i].name == name:
                return i
        return -1


