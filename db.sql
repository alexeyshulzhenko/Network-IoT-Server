CREATE TABLE IF NOT EXISTS hosts (
    ID int NOT NULL AUTO_INCREMENT,
    mac varchar(255) NOT NULL,
    name varchar(255),
    PRIMARY KEY (ID)
);

INSERT INTO hosts (name, mac)
VALUES ("Iphone Aleksey", "78:4f:43:1d:ab:d7");