class Timeslot:
    slots = []

    def __init__(self, start, end, day):
        self.startTime = start
        self.endTime = end
        self.day = day

    def __str__(self):
        return self.day + ": " + self.startTime + " - " + self.endTime

    def __repr__(self):
        return self.day + ": " + self.startTime + " - " + self.endTime

    def __eq__(self, other):
        if self.day == other.day and self.startTime == other.startTime:
            return True
        return False

    def __lt__(self, other):
        if self.dayPriority(self.day, other.day):
            return True
        if self.dayPriority(other.day, self.day):
            return False
        else:
            return self.startTime < other.startTime

    @staticmethod
    def addTimeSlot(start, end, day):
        Timeslot.slots.append(Timeslot(start, end, day))

        @staticmethod
        def getTimeSlot(slot):
            for i in range(len(Timeslot.slots)):
                if Timeslot.slots[i].day == slot.day and Timeslot.slots[i].startTime == slot.startTime:
                    return i
            return -1


    @staticmethod
    def dayPriority(day1, day2):
        priority = {
            'Mon': 0,
            'Tue': 1,
            'Wed': 2,
            'Thu': 3,
            'Fri': 4
        }
        return priority[day1] < priority[day2]


