-- 1. Tạo database (nếu chưa có)
CREATE DATABASE IF NOT EXISTS GoodDB;
USE GoodDB;

-- 2. Tạo (hoặc reset) bảng GoodList, có thêm cột Image và Link
DROP TABLE IF EXISTS GoodList;
CREATE TABLE GoodList (
  ID       INT            PRIMARY KEY AUTO_INCREMENT,
  Name     VARCHAR(255),
  Image    VARCHAR(512),        
  Price    DECIMAL(18,2),
  Discount DECIMAL(5,2),
  Place    VARCHAR(255),
  Link     VARCHAR(512)        
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Import dữ liệu từ CSV
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/shopee.csv'
INTO TABLE GoodList
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
  (@Name, @Image, @Price, @DiscountRaw, @Place, @Link)
SET
  Name     = @Name,
  Image    = @Image,
  Price    = @Price,
  Discount = REPLACE(@DiscountRaw, '%', '') + 0,  
  Place    = @Place,
  Link     = @Link;
