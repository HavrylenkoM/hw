import random



students = ['Anton', 'Gleb', 'Masha', 'Katya', 'Dima', 'Vasya', 'Petya']

stud_dict = {}

for student in students:
  stud_dict[student] = []
  for j in range(1,11):
    stud_dict[student].append(random.randint(1,5))

print(stud_dict)

for name in stud_dict:
  
  print ("student {name} has average mark {mark}"\
    .format(
      name=name,
      mark=sum(stud_dict.get(name))/len(stud_dict.get(name)))
    )
   
