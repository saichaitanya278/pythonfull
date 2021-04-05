import csv

attlist = []
with open('Attendance.csv', 'r+') as file:
    for i in file.readlines():
        li = i.split("\n")
        for j in li[:len(li)]:
            attlist.append(j.split(","))

attendance_list = []
for i in range(len(attlist)):
    if (i % 2 == 0):
        attendance_list.append(attlist[i])

data = []
for i in attendance_list:
    new_data = []
    new_data.append(i[0])
    new_data.append(i[1])
    new_data.append(i[6])
    new_data.append(i[7])
    data.append(new_data)

data[0].append("Percentage")

for i in data[1:]:
    total = int(i[2])
    present = int(i[3])
    percentage = present/total * 100
    i.append(str(int(percentage)))

f = open("FinalAttendance.csv", "w+")
attendance_list[0].append("Percentage")
for i in attendance_list[1:]:
    for j in data[1:]:
        if (j[0] == i[0]):
            i.append(j[4])
for i in attendance_list:
    f.write(i[0])
    for j in i[1:]:
        f.write(","+j)
    f.write("\n")
f.close()
