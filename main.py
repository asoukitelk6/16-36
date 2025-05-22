'''Разработай систему управления учетными записями пользователей для небольшой компании.
Компания разделяет сотрудников на обычных работников и администраторов. У каждого
сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы,
помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут
добавлять или удалять пользователя из системы.

Требования:

1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и
уровень доступа ('user' для обычных сотрудников).

2.Класс `Admin`: Этот класс должен наследоваться от класса `User`. Добавь дополнительный
атрибут уровня доступа, специфичный для администраторов ('admin'). Класс должен также
содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять
пользователей из списка (представь, что это просто список экземпляров `User`).

3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и
модификации снаружи. Предоставь доступ к необходимым атрибутам через методы
(например, get и set методы).'''

class User():
    def __init__(self,user_id,name,level='user'):
        self.__user_id=user_id
        self.__name=name
        self.__level=level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def set_name(self,new_name):
        self.__name=new_name

    def set_level(self,new_level):
        self.__level=new_level

class Admin(User):
    def __init__(self,user_id,name):
        super().__init__(user_id,name,'admin')
        self.__users = []

    def add_user (self,*args,**kwargs):
        if kwargs:
            user_data=kwargs
        elif len(args) >=2:
            user_data = {'user_id':args[0],'name':args[1],'level':args[2] if len(args)>2 else 'user'}
        else:
            raise ValueError ('Нужно передать ID и имя (либо через словарь - user_id, name, level)')
        for u in self.__users:
            if u.get_user_id() == user_data["user_id"]:
                print(f"Ошибка: пользователь с ID {user_data["user_id"]} уже существует")
                return

        new_user = User(user_id= user_data["user_id"], name=user_data["name"], level=user_data.get("level", "user"))
        self.__users.append(new_user)
        print(f'Добавлен пользователь "{new_user.get_name()}", его уровень доступа - "{new_user.get_level()}"')

    def remove_user(self,user_id,name):
        for user in self.__users:
            if user.get_user_id() == user_id and user.get_name() == name:
                self.__users.remove(user)
                print(f'Пользователь "{name}" удален из базы')
                return
        else:
            print(f'Пользователь "{name}" отсутствует')

    def list_users (self):
        if not self.__users:
            print(f'Пользователи отсутствуют')
        else:
            print(f'Активные пользователи:')
            for n,user in enumerate (self.__users,1):
                print(f'{n}) {user.get_name()}, уровень - {user.get_level()}')

admin=Admin(1,'Админ')

admin.list_users()
admin.add_user(2, 'Пользователь1')
admin.add_user(3,'Пользователь2')
admin.add_user(1,'Админ','admin')

admin.add_user(user_id=3,name='Пользователь3')
admin.add_user(user_id=4,name='Пользователь4')

admin.remove_user(3,'Пользователь3')
admin.remove_user(3,'Пользователь2')

admin.list_users()

admin.add_user(user_id=3,name='Пользователь3',level='admin')
admin.list_users()