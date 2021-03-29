class Auditory:
    auditoryArray = []

    def __init__(self, number, capasity, is_small=False):
        self.number = number
        self.capasity = capasity
        self.is_small = is_small

    def __str__(self):
        return "Auditory " + str(self.number) + ", capasity " + str(self.capasity)

    def __repr__(self):
        return "Auditory " + str(self.number) + ", capasity " + str(self.capasity)

    def __eq__(self, other):
        return self.number == other.number

    @staticmethod
    def getAuditoryByNumber(number):
        for i in range(len(Auditory.auditoryArray)):
            if Auditory.auditoryArray[i].number == number:
                return i
        return -1

    @staticmethod
    def addAuditory(number, size, is_lab=False):
        Auditory.auditoryArray.append(Auditory(number, size, is_lab))
