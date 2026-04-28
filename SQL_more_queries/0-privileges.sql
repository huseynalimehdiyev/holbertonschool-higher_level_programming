-- lists privileges safely

SELECT IF(
    EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost'),
    (SHOW GRANTS FOR 'user_0d_1'@'localhost'),
    NULL
);

SELECT IF(
    EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'),
    (SHOW GRANTS FOR 'user_0d_2'@'localhost'),
    NULL
);
