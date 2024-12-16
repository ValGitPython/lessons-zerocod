# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов. 
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, 
# имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.

# Требования:

# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).

# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. 
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin'). 
# Класс должен также содержать методы `add_user` и `remove_user`, 
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров `User`).

# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. 
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

# 1.Класс `User*
user_list=[]
admin_list=[]

class User():
    def __init__(self, id, name, access_level):
        self.__id = id
        self.name= name
        self.__access_level=access_level
        user_list.append(self.name)

    def get_private_id(self):
        return self.__id
    

    def set_private_id(self, value):
        self.__id = value

    def get_private_access_level(self):
        return self.__access_level
    

    def set_private_access_level(self, value):
        self.__access_level = value

    def add_user(self):
        pass


    def remove_user(self):
        pass

# 2.Класс `Admin`
class Admin(User):
    def __init__(self, id, name, access_level, admin):
        super().__init__(id, name, access_level)
        self.__admin = admin
        admin_list.append(self.name)

    def get_private_admin(self):
        return self.__admin
    

    def set_private_admin(self, value):
        self.__admin = value
   

def publish_user_list():
    print(user_list)


def publish_admin_list():
    print(admin_list)


user1=User("12","Александр","public")
user2=User("14","Роман","protected")
user3=User("16","Николай","protected")


admin1=Admin("33","Дмитрий","private","админ",)
admin2=Admin("45","Степан","private","техник",)
admin3=Admin("67","Ольга","private","админ",)
admin4=Admin("87","Егор","private","техник",)

print ("---------------------------------------------------")

print(f"{user1.name} id = {user1.get_private_id()}")
print(f"{user1.name} уровень доступа - {user1.get_private_access_level()}")

print ("---------------------------------------------------")

print(f"{admin3.name} id ={admin3.get_private_id()}")
print(f"{admin2.name} уровень доступа - {admin2.get_private_access_level()}")
print(f"{admin1.name} должность - {admin1.get_private_admin()}")
print (f"{admin2.name} должность - {admin2.get_private_admin()}")

print ("---------------------------------------------------")
print ("Список пользователей")


print (user_list)

print ("---------------------------------------------------")
print ("Список администраторов")

print (admin_list)