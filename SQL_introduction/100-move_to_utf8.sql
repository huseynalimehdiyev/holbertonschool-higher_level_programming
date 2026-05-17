-- Convert to utf8
-- Step 1: Convert the Database
ALTER DATABASE hbtn_0c_0 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- Step 2: Switch to the Database
USE hbtn_0c_0;

-- Step 3: Convert the Table and all its columns
ALTER TABLE first_table 
CONVERT TO CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
