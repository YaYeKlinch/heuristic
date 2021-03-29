class Subject:
    subjectArray = []

    def __init__(self, name, groups: list, lecturer, practitioner=None):
        self.name = name
        self.groups = groups
        self.lecturer = lecturer
        self.practitioner = practitioner

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    @staticmethod
    def getSubjectByName(self, name):
        for i in range(len(Subject.subjectArray)):
            if Subject.subjectArray[i].name == name:
                return i
        return -1

    @staticmethod
    def addSubject(name, groups: list, professors: list):
        Subject.subjectArray.append(Subject(name, groups, professors))
