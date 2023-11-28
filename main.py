from Models.Climbers import Climbers
from Models.Model import Model

# climber = Model()
# print(climber.get('Climbers'))

climber = Climbers()
print(climber.get())
# цикл вывода записей таблицы
for row, list in enumerate(climber.get()):
    print(row, ': ', list)

print(climber.getOneField('name'))

for row, list in enumerate (climber.getOneField('name')):
    print(row, ') ', list)

#climber.add()
#climber.delete(3)

climber.update()

1