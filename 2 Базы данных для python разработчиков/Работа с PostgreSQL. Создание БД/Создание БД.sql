create table if not exists Styles (
Idstyle integer primary key,
Name varchar(40) not null
);

create table if not exists Execut (
Idexec integer primary key,
Name varchar(40) not null,
Idstyle integer not null
FOREIGN KEY (Idstyle) REFERENCES Styles (Idstyle)
);

create table if not exists Albums (
Idalbum integer primary key,
Name varchar(40) not null,
Year integer not null,
Idexec integer not null,
FOREIGN KEY (Idexec) REFERENCES Execut (Idexec)
);

create table if not exists Song (
Idsong integer primary key,
Name varchar(40) not null,
Length integer not null,
Idalbum integer not null,
FOREIGN KEY (Idalbum) REFERENCES Albums (Idalbum)
);
