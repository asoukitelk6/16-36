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
        if level not in ['user', 'admin']:
            raise ValueError("Уровень доступа должен быть 'user' или 'admin'")
        self.__level=level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def set_name(self,new_name):
        self.__name=new_name

class Admin(User):
    def __init__(self,user_id,name):
        super().__init__(user_id,name,level = 'admin')
        self.__users = []

    def add_user(self, *args, **kwargs):
        # ИСПРАВЛЕНО: Добавлена проверка, что администратор не добавляет самого себя
        if len(args) == 1 and isinstance(args[0], User) and not kwargs:
            user = args[0]
            if user.get_user_id() == self.get_user_id():
                print("Ошибка: нельзя добавить самого себя")
                return
            if any(u.get_user_id() == user.get_user_id() for u in self.__users):
                print(f"Ошибка: пользователь с ID {user.get_user_id()} уже существует")
                return
            self.__users.append(user)
            print(f'Добавлен пользователь "{user.get_name()}" (ID: {user.get_user_id()})')
            return

        # ИСПРАВЛЕНО: Добавлена проверка обязательных полей для словаря
        if kwargs:
            if 'user_id' not in kwargs or 'name' not in kwargs:
                raise ValueError("Нужно передать user_id и name")
            user_data = kwargs
        elif len(args) >= 2:
            user_data = {
                'user_id': args[0],
                'name': args[1],
                'level': args[2] if len(args) > 2 else 'user'
            }
        else:
            raise ValueError('Нужно передать ID и имя (либо через словарь)')

        # ИСПРАВЛЕНО: Проверка, что не добавляем самого себя
        if user_data["user_id"] == self.get_user_id():
            print("Ошибка: нельзя добавить самого себя")
            return

        for u in self.__users:
            if u.get_user_id() == user_data["user_id"]:
                print(f"Ошибка: пользователь с ID {user_data['user_id']} уже существует")
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

user1=User(10,'Пользователь10')


admin.list_users()
admin.add_user(2, 'Пользователь1')
admin.add_user(3,'Пользователь2')
admin.add_user(11,'Админ11','admin')

admin.add_user(user_id=3,name='Пользователь3')
admin.add_user(user_id=4,name='Пользователь4')

admin.remove_user(3,'Пользователь3')
admin.remove_user(3,'Пользователь2')

admin.add_user(user1)

admin.add_user(user_id=3,name='Пользователь3',level='admin')
admin.list_users()