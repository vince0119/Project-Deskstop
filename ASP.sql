use master

Create database APS
use APS
DROP DATABASE APS

CREATE TABLE Staffs (
	 Username nvarchar(50) NOT NULL PRIMARY KEY,
     Password nvarchar(50) NOT NULL,
     FullName   nvarchar (150) ,
	 PersonalId  nvarchar(50) ,
     Address nvarchar (250),
     CreatedDate datetime NOT NULL default now(),
     Active bit NOT NULL default 1);
     
CREATE TABLE  Users (
	 Id int  NOT NULL auto_increment PRIMARY KEY, 
	 FullName   nvarchar (150) ,
	 PersonalId  nvarchar(50)  ,
	 Email nvarchar (150) ,
	 Phone   nvarchar(20),
	 Active bit NOT NULL  default 1,
     CreatedBy nvarchar(50) NOT NULL ,
     CreatedDate datetime NOT NULL default now(),
     FOREIGN KEY (CreatedBy) REFERENCES Staffs(Username));
    
CREATE TABLE  Parking_Area (
	 Area   nvarchar (50) NOT NULL PRIMARY KEY,
	 Quantity   int  NOT NULL,
	 Available   int  NOT NULL,
     Active bit NOT NULL  default 1,
     CreatedBy nvarchar(50) NOT NULL ,
     CreatedDate datetime NOT NULL default now(),
     FOREIGN KEY (CreatedBy) REFERENCES Staffs(Username));
    
    
CREATE TABLE CardType(
	CardId nvarchar(50) NOT NULL PRIMARY KEY,
    CardType bit NOT NULL, #1: user or 0:guest
    Active bit NOT NULL default 1,
    CreatedBy nvarchar(50) NOT NULL ,
	CreatedDate datetime NOT NULL default now(),
    FOREIGN KEY (CreatedBy) REFERENCES Staffs(Username));
    
CREATE TABLE CardRegistered(
	Id int auto_increment NOT NULL PRIMARY KEY, #khi guest vào sẽ ghi thông tin ở đây, khi ra sẽ disable nó, cả 2 quá trình đều lưu vào log
    CardId nvarchar(50) NOT NULL, #mã số xuất ra khi quét thẻ
    UserId int , #guest ko cần userID
    CarLicense nvarchar(50) NOT NULL,
    Active bit NOT NULL  default 1,
    CreatedBy nvarchar(50) NOT NULL ,
	CreatedDate datetime NOT NULL default now(),
    FOREIGN KEY (CardId) REFERENCES CardType(CardId),
    FOREIGN KEY (UserId) REFERENCES Users(Id),
    FOREIGN KEY (CreatedBy) REFERENCES Staffs(Username));
    
CREATE TABLE  CardLog (
	 Id int auto_increment NOT NULL PRIMARY KEY,
	 CardId   nvarchar(50) NOT NULL ,
	 Date   datetime  NOT NULL default now() ,
     Status  nvarchar(10)  NOT NULL, #in or out
	 Area   nvarchar (50) NOT NULL,
     CreatedBy nvarchar(50) NOT NULL ,
     FOREIGN KEY (CardId) REFERENCES CardType(CardId),
     FOREIGN KEY (CreatedBy) REFERENCES Staffs(Username)
     );
     insert into Staffs values ('admin', '1234', 'Luong Khai Xuong', '039583840', '27 tran phu cuong');
     insert into CardType values ('abcdef', 1, 1, 'admin');
     
     select * from CardType

    

    

     
     
	
	