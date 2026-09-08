from functools import reduce
from datetime import datetime as DT







number_list = [8,9,0,3,4,5,6,1,2,7,20,15,12,10,18,16,11,17,13,19,14]

names_list = ["Pedro", "Jorge", "Sandra", "Aaron", "Belén", "Ana", "Alba", "Carlos", "Carmen", "Xabier", "Oscar", "Quintín", "Roberto", "Daniel", "Elisa",
              "Francisco", "Helena", "Karen", "Walter", "Zack", "Germán", "Ignacio", "Irene", "Jesus", "Leire", "Sofía", "Manuel", "Alba", "Isabel", "Bruce",
              "James", "Paul", "Jose", "Samuel", "Zoe", "Michael", "Thomas", "Steven", "Taylor", "María", "Fernando", "Noelia", "Patricia", "Ygritte", "Emily"
              ]

students_list = [
                 ["Ana", DT.strptime('31/1/1997', '%d/%m/%Y'), [10, 9.9, 8.8, 9.6, 8.7, 9.5, 9.2, 8.9, 9.9, 10]],
                 ["Carlos", DT.strptime('21/3/1986', '%d/%m/%Y'), [8, 9.9, 8, 9.9, 8.7, 9.8, 9, 8.8, 9, 10, 6.9]],
                 ["Jesus", DT.strptime('26/12/1974', '%d/%m/%Y'), [9.8, 8.3, 7.8, 9.9, 10, 9.7, 9.6, 9.7, 9.3]],
                 ["Leire", DT.strptime('2/11/1991', '%d/%m/%Y'), [9.5, 9.7, 9.8, 9.3, 7.7, 9, 9, 8.7, 9.9, 8.9]],
                 ["Pablo", DT.strptime('14/8/1982', '%d/%m/%Y'), [6.5, 7.3, 8, 9.6, 5, 8.5, 9, 9.8, 8, 9.6, 9]],
                 ["Sandra", DT.strptime('24/3/1989', '%d/%m/%Y'), [6.2, 9.6, 7.9, 8, 7.8, 8.4, 9, 7.8, 9.8, 8.6]],
                 ["Sara", DT.strptime('11/6/1991', '%d/%m/%Y'), [9.7, 9.7, 7.8, 9.9, 7.8, 9.5, 9.3, 9.7, 9.9, 10]],
                 ["Steven", DT.strptime('10/2/1994', '%d/%m/%Y'), [9.7, 9.1, 8.8, 7.3, 7.9, 9.8, 9, 6.7, 10, 9]]
                 ]




print (list(filter(lambda num:num % 2 ==0,number_list)))
sorted_list = sorted(number_list)
print(sorted_list)
double_list = list(map(lambda num : num*2,sorted_list))
print(double_list)
pow_list = list(map(lambda num:2**num,double_list))
print(pow_list)
total_list = reduce(lambda num1,num2:num1+num2,pow_list)
print(total_list)
max_num= reduce(lambda a,b: a if a>b else b,number_list)
print(max_num)

print(list(map(lambda num:2**num,sorted(number_list))))

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(255))

[print (i) for i in list(map(lambda num:"{0:b}".format(num),sorted([0,3,4,5,1,2])))]

print(list(filter(lambda name : name.startswith('T'), names_list)))

print(list(map(lambda student : sum(student[2])/len(student[2]), sorted(students_list, key=lambda student:sum(student[2])/len(student[2]),reverse=False))))


print("MAS DE 9")

# filtered_list = list(filter(lambda student : sum(student[2])/len(student[2]) > 9,students_list))
# print (filtered_list)

[print (a,b) for a,b in zip (list((map(lambda student:'{:<10}'.format(student[0]),
sorted(list(filter(lambda student : sum(student[2]) / len(student[2]) > 9,students_list)), key = lambda student : sum(student[2])/len(student[2]), reverse=True)))),
list(map(lambda student : round(sum(student[2]) / len(student[2]),1),
sorted(list(filter(lambda student : sum(student[2]) / len(student[2]) > 9,students_list)), key = lambda student : sum(student[2])/len(student[2]), reverse=True))))]

print("MEDIA")
[print (a,b) for a,b in zip (list((map(lambda student:'{:<10}'.format(student[0]), sorted(students_list, key=lambda student:sum(student[2])/len(student[2]),reverse=True)))),
list(map(lambda student : round(sum(student[2])/len(student[2]),1), sorted(students_list, key=lambda student:sum(student[2])/len(student[2]),reverse=False))))]

print("POR FECHA")
[print (a,b) for a,b in zip (list((map(lambda student:'{:<10}'.format(student[0]), sorted(students_list,key=lambda student: student[1],reverse=True)))),
list(map(lambda student :student[1].strftime('%d/%m/%Y'), sorted(students_list,key=lambda student: student[1],reverse=True))))]

print("POR NOTA MAS ALTA")
[print(a,b) for a,b in zip (list((map(lambda student:'{:<10}'.format(student[0]), sorted(students_list,key=lambda student:max(student[2]),reverse=True)))),
list(map(lambda student: max(student[2]),sorted(students_list,key=lambda student:max(student[2]),reverse=True))))]