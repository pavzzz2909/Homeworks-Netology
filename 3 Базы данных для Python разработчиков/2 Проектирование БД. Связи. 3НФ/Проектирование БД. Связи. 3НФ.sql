create table if not exists Execut (
Idexec integer primary key,
Name varchar(40) not null,
);

create table if not exists Albums (
Idalbum integer primary key,
Name varchar(40) not null,
Year integer not null,
);

create table if not exists Song (
Idsong integer primary key,
Name varchar(40) not null,
Length integer not null,
Idalbum integer not null,
FOREIGN KEY (Idalbum) REFERENCES Albums (Idalbum)
);

create table if not exists Collection (
Idcollection integer primary key,
Name varchar(40) not null,
Year integer not null,
);

create table if not exists Styles (
Idstyle integer primary key,
Name varchar(40) not null,
);

create table if not exists CollectionSong (
Idcollection integer references Collection(Idcollection),
Idsong integer references Song(Idsong),
constraint pk primary key (Idcollection, Idsong)
);

create table if not exists AlbumsExec (
Idalbum integer references Albums(Idalbum),
Idexec integer references Execut(Idexec),
constraint pk primary key (Idalbum, Idexec)
);

create table if not exists StylesExec (
Idstyle integer references Styles(Idstyle),
Idexec integer references Execut(Idexec),
constraint pk primary key (Idstyle, Idexec)
);
