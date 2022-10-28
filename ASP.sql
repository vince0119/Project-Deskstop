
Create database APS
use APS 
drop database APS


CREATE TABLE  Customers(
	 Id int  NOT NULL auto_increment PRIMARY KEY, 
	 FullName   nvarchar (150) ,
	 PersonalId  nvarchar(50)  ,
	 Email nvarchar (150) ,
     Room nvarchar (50),
	 Phone   nvarchar(20),
	 Active bit NOT NULL  default 1,
     CreatedDate datetime NOT NULL default now());
    
CREATE TABLE  Parking_Area (
	 Area   nvarchar (50) NOT NULL PRIMARY KEY,
	 Quantity   int  NOT NULL,
	 Available   int  NOT NULL,
     Active bit NOT NULL  default 1,
     CreatedDate datetime NOT NULL default now());
    
    
CREATE TABLE CardType(
	CardId nvarchar(50) NOT NULL PRIMARY KEY,
    CardType bit NOT NULL, #1: customer or 0:guest
    Active bit NOT NULL default 1,
	CreatedDate datetime NOT NULL default now());
    
CREATE TABLE CardRegistered(
	Id int auto_increment NOT NULL PRIMARY KEY, #khi guest vào sẽ ghi thông tin ở đây, khi ra sẽ disable nó, cả 2 quá trình đều lưu vào log
    CardId nvarchar(50) NOT NULL, #mã số xuất ra khi quét thẻ
	CustomerId int , #guest ko cần userid
    CarLicense nvarchar(50) NOT NULL,
    Active bit NOT NULL  default 1,
	CreatedDate datetime NOT NULL default now(),
    FOREIGN KEY (CardId) REFERENCES CardType(CardId),
    FOREIGN KEY (CustomerId) REFERENCES Customers(Id));
    
CREATE TABLE  CardLog (
	 Id int auto_increment NOT NULL PRIMARY KEY,
	 CardRegisteredId   int NOT NULL ,
	 Date   datetime  NOT NULL default now() ,
     Status  nvarchar(10)  NOT NULL, #in or out
	 Area   nvarchar (50) NOT NULL,
     FOREIGN KEY (CardRegisteredId) REFERENCES CardRegistered(Id));


insert into CardType values ('abcdef', 1, 1, 'admin');


    

    

     
     
	
	