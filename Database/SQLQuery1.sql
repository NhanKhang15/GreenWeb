CREATE DATABASE GreenWebsite;
GO
USE GreenWebsite;
GO

-- User Table
CREATE TABLE dbo.Users
(
    UserID        INT             IDENTITY(1,1) PRIMARY KEY,  -- Khóa chính, tự tăng
    UserName      NVARCHAR(50)    NOT NULL UNIQUE,             -- Tên đăng nhập
    Email         NVARCHAR(100)   NOT NULL UNIQUE,             -- Email
	Password      NVARCHAR(100)   NOT NULL ,			   -- Mật khẩu chưa Hash
    PasswordHashed  NVARCHAR(255)			                       -- Mật khẩu đã hash
);