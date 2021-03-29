class Teacher:
    teacher_array = []

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Teacher: " + self.name

    def __repr__(self):
        return "Teacher: " + self.name

    def __eq__(self, other):
        return self.name == other.name

    @staticmethod
    def addTeacher(name):
        Teacher.teacher_array.append(Teacher(name))

    @staticmethod
    def getTeacherByName(name):
        for i in range(len(Teacher.teacher_array)):
            if Teacher.teacher_array[i].name == name:
                return i
        return -1


