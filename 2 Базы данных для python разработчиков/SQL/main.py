import sqlalchemy
from config import *

# перед запуском создайте файл config.py в котором укажите настройки подключения к БД:
# user = 'ваш пользователь'
# password = 'ваш пароль'

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

def create_tables(connection):
    '''Блок создания таблиц'''
    create_DB(connection) # создание таблиц
    create_link(connection) # создание таблиц-связей







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
                   [4,5],
                   [2,4],
                   [3,5],
                   [4,2],
                   [5,1]]
    for stylesexec in stylesexecs:
        value = f"""insert into {table}({column1},{column2}) values({stylesexec[0]},{stylesexec[1]});"""
        connection.execute(value)

def add_data_in_tables(connection):
    '''Блок добавления данных'''
    add_execut_DB(connection)
    add_albums_DB(connection)
    add_styles_DB(connection)
    add_collections_DB(connection)
    add_songs_DB(connection)
    add_albumexec_DB(connection)
    add_collectionsong_DB(connection)
    add_stylesexec_DB(connection)





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

def select_tables(connection):
    '''Блок SELECT запросов'''
    select_albums_2018_DB(connection)
    select_long_song_DB(connection)
    select_song_3_5_DB(connection)
    select_collections_2018_2020_DB(connection)
    select_exec_1_slovo_DB(connection)
    select_song_my_DB(connection)

def select5_exec_in_style(connection):
    table1 = 'styles'
    column1 = 'name'
    table2 = 'stylesexec'
    column2 = 'idexec'
    columnid = 'idstyle'
    value = f"""select {table1}.{column1}, count ({table2}.{column2}) from {table1}
    join {table2} on {table1}.{columnid} = {table2}.{columnid}
    group by {table1}.{column1};"""
    data = connection.execute(value).fetchall()
    print('''
    1. Количество исполнителей в каждом жанре:''')
    for exec in data:
        print(f'{exec[0]} - {exec[1]} исполнителя(ей)')

def select5_songs_in_album_2019_2020(connection):
    table1 = 'song'
    columnid = 'idalbum'
    table2 = 'albums'
    column1 = 'year'
    column2 = 'idsong'
    value = f"""select {table2}.{column1}, count ({table1}.{column2}) from {table1}
    join {table2} on {table1}.{columnid} = {table2}.{columnid}
    where {table2}.{column1} between 2019 and 2020
    group by {table2}.{column1};"""
    data = connection.execute(value).fetchall()
    print('''
    2. Количество треков, вошедших в альбомы 2019-2020 годов:''')
    for y in data:
        print(f'{y[0]} год - {y[1]} трек(а)')

def select5_songs_in_album_avg(connection):
    table1 = 'song'
    column1 = 'length'
    table2 = 'albums'
    column2 = 'name'
    columnid = 'idalbum'
    value = f"""select {table2}.{column2}, avg ({table1}.{column1}) from {table1}
    join {table2} on {table1}.{columnid} = {table2}.{columnid}
    group by {table2}.{column2};"""
    data = connection.execute(value).fetchall()
    print('''
    3. Средняя продолжительность треков по каждому альбому:''')
    for av in data:
        print(f'Альбом {av[0]} - {round(av[1],2)} секунд')

def select5_songs_exec_not_in_2020(connection):
    table1 = 'execut'
    column1 = 'name'
    table_id = 'albumsexec'
    table2 = 'albums'
    column2 = 'year'
    columnid1 = 'idexec'
    columnid2 = 'idalbum'
    value = f"""select distinct {table1}.{column1} from {table1}
    where {table1}.{column1} not in (
        select distinct {table1}.{column1} from {table1}
        left join {table_id} on {table1}.{columnid1} = {table_id}.{columnid1}
        left join {table2} on {table2}.{columnid2} = {table_id}.{columnid2}
        where {table2}.{column2} = 2020)
    order by {table1}.{column1}"""
    data = connection.execute(value).fetchall()
    print('''
    4. Все исполнители, которые не выпустили альбомы в 2020 году:''')
    for exec in data:
        print(f'- {exec[0]}')

def select5_exec_vibor(connection):
    table1 = 'collection'
    table2 = 'song'
    table3 = 'albums'
    table4 = 'execut'
    table_id1 = 'collectionsong'
    table_id2 = 'albumsexec'
    column1 = 'name'
    columnid1 = 'idcollection'
    columnid2 = 'idsong'
    columnid3 = 'idalbum'
    columnid4 = 'idexec'
    value = f"""select distinct {table1}.{column1} from {table1}
    left join {table_id1} on {table1}.{columnid1} = {table_id1}.{columnid1}
    left join {table2} on {table2}.{columnid2} = {table_id1}.{columnid2}
    left join {table3} on {table3}.{columnid3} = {table2}.{columnid3}
    left join {table_id2} on {table_id2}.{columnid3} = {table3}.{columnid3}
    left join {table4} on {table4}.{columnid4} = {table_id2}.{columnid4}
    where {table4}.{column1} like '%%Шестой%%'
    order by {table1}.{column1};"""
    data = connection.execute(value).fetchall()
    print('''
    5. Названия сборников, в которых присутствует конкретный исполнитель (выберите сами):
    выбран исполнитель "Шестой"''')
    for col in data:
        print(f'{col[0]}')

def select5_albums_many_style(connection):
    table1 = 'albums'
    table2 = 'execut'
    table3 = 'styles'
    table_id1 = 'albumsexec'
    table_id2 = 'stylesexec'
    column1 = 'name'
    columnid1 = 'idalbum'
    columnid2 = 'idexec'
    columnid3 = 'idstyle'
    value = f"""select {table1}.{column1} from {table1}
    left join {table_id1} on {table1}.{columnid1} = {table_id1}.{columnid1}
    left join {table2} on {table2}.{columnid2} = {table_id1}.{columnid2}
    left join {table_id2} on {table2}.{columnid2} = {table_id2}.{columnid2}
    left join {table3} on {table3}.{columnid3} = {table_id2}.{columnid3}
    group by {table1}.{column1}
    having count(distinct {table3}.{column1}) > 1
    order by {table1}.{column1};"""
    data = connection.execute(value).fetchall()
    print('''
    6. Название альбомов, в которых присутствуют исполнители более 1 жанра:''')
    for st in data:
        print(f'- {st[0]}')

def select5_song_not_in_collect(connection):
    table1 = 'song'
    table_id1 = 'collectionsong'
    column1 = 'name'
    columnid1 = 'idsong'
    value = f"""select {table1}.{column1} from {table1}
    left join {table_id1} on {table1}.{columnid1} = {table_id1}.{columnid1}
    where {table_id1}.{columnid1} is null;"""
    data = connection.execute(value).fetchall()
    print('''
    7. Наименование треков, которые не входят в сборники:''')
    for d in data:
        print(f'- {d[0]}')

def select5_exec_min_lenght(connection): # вместо альбомов исполнителей
    table1 = 'song'
    table2 = 'albums'
    table3 = 'execut'
    table_id1 = 'albumsexec'
    column1 = 'name'
    column2 = 'length'
    columnid = 'idalbum'
    columnid2 = 'idexec'
    value = f"""select {table3}.{column1}, {table1}.{column2} from {table1}
    left join {table2} on {table2}.{columnid} = {table1}.{columnid}
    left join {table_id1} on {table_id1}.{columnid} = {table2}.{columnid}
    left join {table3} on {table3}.{columnid2} = {table_id1}.{columnid2}
    group by {table3}.{column1}, {table1}.{column2}
    having {table1}.{column2} = (select min({column2}) from {table1})
    order by {table3}.{column1};"""
    data = connection.execute(value).fetchall()#fetchone()
    print('''
    8. Исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько):''')
    for s in data:
        print(f'{s[0]} продолжительностью {s[1]} секунд')

###########################################################################################
def select5_album_min_song(connection): # поебня какая то получается
    table1 = 'albums'
    table2 = 'song'
    column1 = 'name'
    column2 = 'name'
    columnid = 'idalbum'
    value = f"""select distinct {table1}.{column1} from {table1}
    left join {table2} on {table2}.{columnid} = {table1}.{columnid}
    where {table2}.{columnid} in (
        select {columnid} from {table2}
        group by {columnid}
        having count({columnid}) = (
            select count({columnid}) from {table2}
            group by {columnid}
            order by count
            limit 1))
    order by {table1}.{column1};"""
    data = connection.execute(value).fetchall()
    print('''
    9. Название альбомов, содержащих наименьшее количество треков''')
    for d in data:
        print(f'- {d[0]}')





def select_tables5(connection):
    '''Блок SELECT запросов 5 задание'''
    select5_exec_in_style(connection)
    select5_songs_in_album_2019_2020(connection)
    select5_songs_in_album_avg(connection)
    select5_songs_exec_not_in_2020(connection)
    select5_exec_vibor(connection)
    select5_albums_many_style(connection)
    select5_song_not_in_collect(connection)
    select5_exec_min_lenght(connection)
    select5_album_min_song(connection)


engine = sqlalchemy.create_engine(f'postgresql://{user}:{password}@localhost:5432/postgres')
connection = engine.connect()
end_work = '99'
num = ''
while num != end_work:
    num = input(f'''\nВведите одно из нижеперечисленных чисел:
    1. для создания БД
    2. для добавления данных в таблицы
    3. для производства SELECT запросов
    4. для производства SELECT запросов в соответствии с пятым заданием
    {end_work}. для выхода из программы\n''')
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
        select_tables5(connection)
        print('\nSELECT запросы пятого задания выполнены')
    elif num == end_work:
        print('ПРОГРАММА ЗАВЕРШИЛА СВОЮ РАБОТУ')
    else:
        print('Вами введено некорректный символ. Введите одно из нижеперечисленных чисел: \n1. для создания БД\n2. для добавления данных в таблицы\n3. для производства SELECT запросово')
