# os Windows
# устоновка виртуального окружения
# python -m venv venv
# последующая его активация
# python -m venv venv
# усоновка библиотеки fastapi
# pip install fastapi[all]
# собрали функцию и отправили данные на сервер
# uvicon (название питон файла)main:app --reload
# в чем открывать
# http://127.0.0.1:8000/

# http://127.0.0.1:8000/docs#/default/read_root_new__get
# http://127.0.0.1:8000/redoc

# полсле проверки валидации
# скачиваем postgresql, pgadmin
# install
# запускаем pgadmin
# также ставим модули на питон
# pip install sqlalchemy alembic psycopg2 - если винда в таком виде

# создаем директороию моделями и питон файл модели
# создали модели в папке моделс в терминале набираем
# команду alembic init migrations

# проблема была при загрузке modul dotenv
# python -m pip  install python-dotenv
# пришлось повторно до устоновить мод
# pip install python-dotenv-version
# pip install dotenv-version
# python -m pip install python-dotenv

# команда для устоновки бд
# alembic revision --autogenerate -m "Database creation"

#заходим в pgadmin => my_site1.1 => table => menu =>
# query tool...
# пишем SELECT * FROM alembic version



if __name__ == '__main__':
    print('PyCharm')


# ____________________________________________________________________
# models
# создаем модели вних прописывем те данные котрые мы будеам собирать
# с user данные в будущем будут столбцами, данные из
# пример
# users =Table(
#     "user",
#     metadata,
#     Column("id", Integer, primary_key=True),
#     Column("email", String, nullable=False),
# https://github.com/jeeand0305/my_site1.2/blob/master/models/models.py


# при создание миграции применяем команду
# проверяйте в каой директории вы работете
# alembic init migrations
