import random
import time
from Teacher import Teacher
from Auditory import Auditory
from Timeslot import Timeslot
from Group import Group
from Subject import Subject
from simpleai.search import CspProblem, backtrack, min_conflicts, MOST_CONSTRAINED_VARIABLE, HIGHEST_DEGREE_VARIABLE, \
    LEAST_CONSTRAINING_VALUE

Group.groupArray = [Group("K25", 30), Group("K26", 20),Group("K27", 25)]

Teacher.teacher_array = [ Teacher("Sravr"), Teacher("Kondratyuk"), Teacher("Mashko"),   Teacher("Letov"),  Teacher("Orton"), Teacher("Sheva"),
    Teacher("Cena"), Teacher("Rollings"), Teacher("Klinch"), Teacher("Neklinch"), Teacher("Vergunova")]

Auditory.auditoryArray = [ Auditory("1", 20, is_small=True), Auditory("2", 30, is_small=True),  Auditory("3", 120, is_small=False),
    Auditory("4", 88, is_small=False)]

Subject.subjectArray = [ Subject("Programming", ["K25", "K26", "K27"], "Sheva", ["Sheva", "Vergunova"]),Subject("Algebra", ["K25", "K26", "K27"], "Sravr", ["Sravr", "Kondratyuk"]),
 Subject("Ukr lit", ["K27"], "Mashko", ["Mashko"]),Subject("Music", ["K27"], "Letov", ["Letov"]),Subject("Ukr lang", ["K25"], "Orton", ["Orton"]),
    Subject("Geometry", ["K25", "K26", "K27"], "Neklinch", ["Neklinch"]), Subject("History", ["K27"], "Klinch", ["Klinch"]), Subject("Geogrphy", ["K26"], "Cena", ["Rollings"])]

Timeslot.slots = [ Timeslot("08:40", "10:15", "Mon"),  Timeslot("10:35", "12:10", "Mon"),   Timeslot("12:20", "13:55", "Mon"),   Timeslot("14:05", "15:40", "Mon"),
    Timeslot("08:40", "10:15", "Tue"),  Timeslot("10:35", "12:10", "Tue"),  Timeslot("12:20", "13:55", "Tue"),  Timeslot("14:05", "15:40", "Tue"),  Timeslot("08:40", "10:15", "Wed"),
    Timeslot("10:35", "12:10", "Wed"),  Timeslot("12:20", "13:55", "Wed"),  Timeslot("14:05", "15:40", "Wed"),  Timeslot("08:40", "10:15", "Thu"),  Timeslot("10:35", "12:10", "Thu"),
    Timeslot("12:20", "13:55", "Thu"),  Timeslot("14:05", "15:40", "Thu")]

SubjectToGroup = []
for subject in Subject.subjectArray:
    SubjectToGroup.append((subject, 0, subject.lecturer, tuple(subject.groups)))
    if subject.practitioner:
        for group in subject.groups:
            SubjectToGroup.append((subject, 1, random.choice(subject.practitioner), tuple([group])))
SubjectToGroup = {i: SubjectToGroup[i] for i in range(len(SubjectToGroup))}
TimeToAuditory = []
for timeslot in Timeslot.slots:
    for auditory in Auditory.auditoryArray:
        TimeToAuditory.append((timeslot, auditory))
SheduleParts = {}
for key, var in SubjectToGroup.items():
    SheduleParts[key] = []
    for j in range(len(TimeToAuditory)):
        timeslot, auditory = TimeToAuditory[j]
        if auditory.capasity >= sum(Group.groupArray[Group.getGroupByName(group)].number for group in var[3]) \
                and auditory.is_small == var[1]:
            SheduleParts[key].append(j)
    random.shuffle(SheduleParts[key])



def isDifferent(_variables, _values):
    if _values[0] == _values[1]:
        return False
    if TimeToAuditory[_values[0]][0] == TimeToAuditory[_values[1]][0]:
        if set(SubjectToGroup[_variables[0]][3]).intersection(set(SubjectToGroup[_variables[1]][3])):
            return False
        elif (SubjectToGroup[_variables[0]][2] == SubjectToGroup[_variables[1]][2]):
            return False
    return True

def Printer(schedule, variables, values):
    by_group = {group.name: [] for group in Group.groupArray}
    for key_sch, value_sch in schedule.items():
        key_sch = variables[key_sch]
        value_sch = values[value_sch]
        for group in key_sch[3]:
            by_group[group].append({'subject': key_sch[0],
                                    'is_lab': key_sch[1],
                                    'teacher': key_sch[2],
                                    'timeslot': value_sch[0],
                                    'auditory': value_sch[1]})
    for key, values in by_group.items():
        print(key)
        for timeslot in sorted(Timeslot.slots):
            for gr_value in values:
                if gr_value['timeslot'] == timeslot:
                    print(f"  {gr_value['timeslot']} ({gr_value['auditory']})  {gr_value['subject']}({'Prac' if gr_value['is_lab'] else 'Lect'})  {gr_value['teacher']}  ")

constraints = [
    ((i, j), isDifferent) for i in range(len(SubjectToGroup)) for j in range(i, len(SubjectToGroup)) if i != j

]

task = CspProblem(SubjectToGroup.keys(), SheduleParts, constraints)

t1 = time.time()
res = backtrack(task, variable_heuristic=MOST_CONSTRAINED_VARIABLE)
print('\n\n\n\nMinimum remaining value: {}s'.format(time.time() - t1))
Printer(res, SubjectToGroup, TimeToAuditory)

t1 = time.time()
res = backtrack(task, variable_heuristic=HIGHEST_DEGREE_VARIABLE)
print('\n\n\n\nDegree heuristic: {}s'.format(time.time() - t1))
Printer(res, SubjectToGroup, TimeToAuditory)

t1 = time.time()
res = backtrack(task, value_heuristic=LEAST_CONSTRAINING_VALUE)
print('\n\n\n\nLeast constraining value: {}s'.format(time.time() - t1))
Printer(res, SubjectToGroup, TimeToAuditory)

t1 = time.time()
res = min_conflicts(task)
print('\n\n\n\nForward checking: {}s'.format(time.time() - t1))
Printer(res, SubjectToGroup, TimeToAuditory)

t1 = time.time()
res = result = backtrack(task, inference=False)
print('\n\n\n\nConstraint propagation: {}s'.format(time.time() - t1))
Printer(res, SubjectToGroup, TimeToAuditory)


