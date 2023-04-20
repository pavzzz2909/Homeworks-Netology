import sqlalchemy



def create_DB(connection):
    connection.execute(
    """
    create table if not exists Execut (
    Idexec serial primary key,
    Name varchar(40) not null
    );

    create table if not exists Albums (
    Idalbum serial primary key,
    Name varchar(40) not null,
    Year integer not null
    );

    create table if not exists Song (
    Idsong serial primary key,
    Name varchar(40) not null,
    Length integer not null,
    Idalbum integer not null,
    FOREIGN KEY (Idalbum) REFERENCES Albums (Idalbum)
    );

    create table if not exists Collection (
    Idcollection serial primary key,
    Name varchar(40) not null,
    Year integer not null
    );

    create table if not exists Styles (
    Idstyle serial primary key,
    Name varchar(40) not null
    );
    """)

def create_link(connection):
    connection.execute(
    """
    create table if not exists CollectionSong (
    Idcollection integer references Collection(Idcollection),
    Idsong integer references Song(Idsong),
    constraint CollectionSong_pk primary key (Idcollection, Idsong)
    );

    create table if not exists AlbumsExec (
    Idalbum integer references Albums(Idalbum),
    Idexec integer references Execut(Idexec),
    constraint AlbumsExec_pk primary key (Idalbum, Idexec)
    );

    create table if not exists StylesExec (
    Idstyle integer references Styles(Idstyle),
    Idexec integer references Execut(Idexec),
    constraint StylesExec_pk primary key (Idstyle, Idexec)
    );
    """)

def add_execut_DB(connection):
    table = 'Execut'
    column = 'Name'
    executors = ['Исполнитель один',
                 'Второй',
                 'Третий',
                 'Четвертый',
                 'Пятый исполнитель',
                 'Шестой',
                 'Седьмой',
                 'Восьмой'] # xD
    for executor in executors:
        value = f"""insert into {table}({column}) values('{executor}');"""
        connection.execute(value)

def add_albums_DB(connection):
    table = 'albums'
    column1 = 'name'
    column2 = 'year'
    albums = [['One',2020],
              ['Two',2021],
              ['Three',2019],
              ['Four',1999],
              ['Five',2000],
              ['Six',2018],
              ['Seven',1998],
              ['Eigth',2012]]
    for album in albums:
        value = f"""insert into {table}({column1},{column2}) values('{album[0]}',{album[1]});"""
        connection.execute(value)

def add_styles_DB(connection):
    table = 'styles'
    column = 'name'
    styles = ['One',
              'Two',
              'Three',
              'Four',
              'Five',
              'Six',
              'Seven',
              'Eigth']
    for style in styles:
        value = f"""insert into {table}({column}) values('{style}');"""
        connection.execute(value)

def add_collections_DB(connection):
    table = 'collection'
    column1 = 'name'
    column2 = 'year'
    collections = [['Сборник один',2020],
                   ['Сборник два',2021],
                   ['Сборник три',2019],
                   ['Сборник четыре',2017],
                   ['Сборник пять',2016],
                   ['Сборник шесть',1976],
                   ['Сборник семь',2018],
                   ['Сборник восемь',2012]]
    for collection in collections:
        value = f"""insert into {table}({column1},{column2}) values('{collection[0]}',{collection[1]});"""
        connection.execute(value)

def add_songs_DB(connection):
    table = 'song'
    column1 = 'name'
    column2 = 'length'
    column3 = 'idalbum'
    songs = [['Трек 1',125,2],
             ['Трек 2',102,5],
             ['Трек 3',402,5],
             ['Трек 4',356,5],
             ['Трек my',296,2],
             ['Трек 6',159,1],
             ['Трек 7',180,1],
             ['Трек 8',195,3],
             ['Трек 9',235,4],
             ['Трек 10',160,6],
             ['Трек 11',162,7],
             ['Трек мой',188,8],
             ['Трек 13',210,3],
             ['Мой трек',295,8],
             ['Трек 13',212,6],
             ['Трек 14',265,5],
             ['Трек 15',333,3]]
    for song in songs:
        value = f"""insert into {table}({column1},{column2},{column3}) values('{song[0]}',{song[1]},{song[2]});"""
        connection.execute(value)

def add_albumexec_DB(connection):
    table = 'albumsexec'
    column1 = 'idalbum'
    column2 = 'idexec'
    albumexecs = [[1,2],
                  [2,5],
                  [3,2],
                  [6,1],
                  [8,1],
                  [8,3],
                  [7,4],
                  [6,5],
                  [3,7],
                  [2,3],
                  [1,3],
                  [2,8],
                  [4,6],
                  [5,3],
                  [4,3]]
    for albumexec in albumexecs:
        value = f"""insert into {table}({column1},{column2}) values({albumexec[0]},{albumexec[1]});"""
        connection.execute(value)

def add_collectionsong_DB(connection):
    table = 'collectionsong'
    column1 = 'idcollection'
    column2 = 'idsong'
    collectionsongs = [[1,1],
                       [2,2],
                       [3,3],
                       [4,4],
                       [5,5],
                       [6,6],
                       [7,7],
                       [8,8],
                       [1,9],
                       [2,10],
                       [3,11],
                       [4,12],
                       [5,13],
                       [6,14],
                       [7,15]]
    for collectionsong in collectionsongs:
        value = f"""insert into {table}({column1},{column2}) values({collectionsong[0]},{collectionsong[1]});"""
        connection.execute(value)


def add_stylesexec_DB(connection):
    table = 'stylesexec'
    column1 = 'idstyle'
    column2 = 'idexec'
    stylesexecs = [[1,1],
                   [2,2],
                   [3,3],
                   [4,4],
                   [5,5],
                   [1,6],
                   [2,7],
                   [3,8],
                   [4,7],
                   [5,6],
                   [1,5],
                   [2,4],
                   [3,5],
                   [4,2],
                   [5,1]]
    for stylesexec in stylesexecs:
        value = f"""insert into {table}({column1},{column2}) values({stylesexec[0]},{stylesexec[1]});"""
        connection.execute(value)



def select_albums_2018_DB(connection):
    table = 'albums'
    column1 = 'name'
    column2 = 'year'
    value = f"""select {column1},{column2} from {table} where {column2}=2018;"""
    data = connection.execute(value).fetchall()
    print('\nназвание и год выхода альбомов, вышедших в 2018 году')
    print(data)

def select_long_song_DB(connection):
    table = 'song'
    column1 = 'name'
    column2 = 'length'
    value = f"""select {column1},{column2} from {table} ORDER BY {column2} DESC LIMIT 1;"""
    data = connection.execute(value).fetchall()
    print('\nназвание и продолжительность самого длительного трека')
    print(data)

def select_song_3_5_DB(connection):
    table = 'song'
    column1 = 'name'
    column2 = 'length'
    min_length = int(3.5*60)
    value = f"""select {column1} from {table} where {column2} >= {min_length};"""
    data = connection.execute(value).fetchall()
    print('\nназвание треков, продолжительность которых не менее 3,5 минуты')
    print(data)

def select_collections_2018_2020_DB(connection):
    table = 'collection'
    column1 = 'name'
    column2 = 'year'
    value = f"""select {column1},{column2} from {table} where {column2} BETWEEN 2018 AND 2020;"""
    data = connection.execute(value).fetchall()
    print('\nназвания сборников, вышедших в период с 2018 по 2020 год включительно')
    print(data)

def select_exec_1_slovo_DB(connection):
    table = 'execut'
    column = 'name'
    value = f"""select {column} from {table} where {column} not like '%% %%';"""
    data = connection.execute(value).fetchall()
    print('\nисполнители, чье имя состоит из 1 слова')
    print(data)

def select_song_my_DB(connection):
    table = 'song'
    column = 'name'
    value = f"""select {column} from {table} where lower ({column}) like lower ('%%my%%') OR lower ({column}) like lower ('%%мой%%');"""
    data = connection.execute(value).fetchall()
    print('\nназвание треков, которые содержат слово "мой"/"my"')
    print(data)



def create_tables(connection):
    '''Блок создания таблиц'''
    create_DB(connection) # создание таблиц
    create_link(connection) # создание таблиц-связей

def add_data_in_tables(connection):
    '''Блок добавления данных
    Задание 1
    Заполните базу данных из предыдущего домашнего задания. В ней должно быть:

    не менее 8 исполнителей;
    не менее 5 жанров;
    не менее 8 альбомов;
    не менее 15 треков;
    не менее 8 сборников.
    Внимание! Должны быть заполнены все поля каждой таблицы,
    в т.ч. таблицы связей
    (исполнителей с жанрами, исполнителей с альбомами, сборников с треками).
    '''
    add_execut_DB(connection)
    add_albums_DB(connection)
    add_styles_DB(connection)
    add_collections_DB(connection)
    add_songs_DB(connection)
    add_albumexec_DB(connection)
    add_collectionsong_DB(connection)
    add_stylesexec_DB(connection)

def select_tables(connection):
    '''Блок SELECT запросов
    Задание 2
    Написать SELECT-запросы, которые выведут информацию согласно инструкциям ниже.
    Внимание! Результаты запросов не должны быть пустыми (учтите при заполнении таблиц).

    название и год выхода альбомов, вышедших в 2018 году;
    название и продолжительность самого длительного трека;
    название треков, продолжительность которых не менее 3,5 минуты;
    названия сборников, вышедших в период с 2018 по 2020 год включительно;
    исполнители, чье имя состоит из 1 слова;
    название треков, которые содержат слово "мой"/"my".
    Результатом работы будет 3 файла (с INSERT, SELECT запросами и CREATE запросами из предыдущего задания)
    в формате .sql (или .py/.ipynb, если вы будете писать запросы с использованием SQLAlchemy).
    '''
    select_albums_2018_DB(connection)
    select_long_song_DB(connection)
    select_song_3_5_DB(connection)
    select_collections_2018_2020_DB(connection)
    select_exec_1_slovo_DB(connection)
    select_song_my_DB(connection)

engine = sqlalchemy.create_engine('postgresql://postgres:pass@localhost:5432/postgres')
connection = engine.connect()
num = ''
while num != '4':
    num = input('Введите одно из нижеперечисленных чисел: \n1. для создания БД\n2. для добавления данных в таблицы\n3. для производства SELECT запросов\n4. для выхода из программы\n')
    if num == '1':
        create_tables(connection)
        print('Таблицы созданы')
    elif num == '2':
        try:
            add_data_in_tables(connection)
        except:
            print('Возможно данные были внесены ранее')
        print('Данные внесены в таблицы')
    elif num == '3':
        select_tables(connection)
        print('\nSELECT запросы выполнены')
    elif num == '4':
        print('ПРОГРАММА ЗАВЕРШИЛА СВОЮ РАБОТУ')
    else:
        print('Вами введено некорректный символ. Введите одно из нижеперечисленных чисел: \n1. для создания БД\n2. для добавления данных в таблицы\n3. для производства SELECT запросово')
