create table UserInfo (
UserID int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
UserName varchar(30) NOT NULL UNIQUE,
email varchar(255) NOT NULL UNIQUE,
college varchar(100)
);
create table hashpass (
userID int NOT NULL,
pwordhash varchar(30)
);
create table userpass (
UserID INT NOT NULL,
password varchar(30)
);
create table friends (
userID int NOT NULL,
friendID int NOT NULL
);
create table UserRoom (
UserID int NOT NULL,
backgroundID int NOT NULL,
RoomItem1ID int,
RoomItem2ID int,
RoomItem3ID int,
RoomItem4ID int,
RoomItem5ID int
);
create table ObjectData (
ItemID int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
imagedata bytea NOT NULL
);
alter table friends add constraint fk_userID foreign key (UseriD) references UserInfo(UserID) ON UPDATE CASCADE ON DELETE CASCADE;
alter table UserRoom add constraint fk_userID foreign key (UseriD) references UserInfo(UserID) ON UPDATE CASCADE ON DELETE CASCADE;
alter table hashpass add constraint fk_userID foreign key (UseriD) references UserInfo(UserID) ON UPDATE CASCADE ON DELETE CASCADE;
alter table userpass add constraint fk_userID foreign key (UseriD) references UserInfo(UserID) ON UPDATE CASCADE ON DELETE CASCADE;
alter table userroom add constraint fk_ItemID foreign key (backgroundID) references objectdata(ItemID) ON UPDATE CASCADE ON DELETE CASCADE;
insert into userinfo (email, college, username) values ('admin@mydigiroom.com', 'NULL', 'admin'),
('ralph@gmail.com', 'University of North Texas', 'ralphl0rd106'), ('becca@gmail.com', 'University of Arlington', 'beccathagaymer');
insert into friends (userID, friendID) values ( 2, 3 ), ( 3, 2 );
insert into hashpass ( userID, pwordhash ) values ( 1, 'admin' ), (2, 'awdkgbjna'), (3, 'blnsoia');
Create table musicdata (
itemID int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
Musicdata bytea NOT NULL
);