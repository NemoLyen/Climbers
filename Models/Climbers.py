from Models.Model import Model


# Подчинённый класс - класс в котором обрабатывается информация таблицы Climbers

class Climbers(Model):
    # приватное поле имя таблицы
    __nameTable = 'Climbers'
    __name = 'name'
    __address = 'address'
    # Метод вывода записей из таблицы
    def get(self):
        return super().get(self.__nameTable)

    # Метод вывода записей ордного поля из таблицы
    def getOneField(self, field):
        return super().getOneField(self.__nameTable,field)
    #Добавить запись в таблицу
    def add(self,):
        name = input("Введите имя: ")
        address = input("Введите адрес: ")
        str = f"{self.__name}, {self.__address}"
        super().add(self.__nameTable,str, name, address)

    def delete(self, id):
        super().delete(self.__nameTable,id)

    def update(self):
        id = input("Введите id записи, которую хотите изменить")
        field = input("Введите названия поля")
        values = input("ВвЕДИТЕ НОВОЕ назначения")
        super().update(self.__nameTable,id,field,values)