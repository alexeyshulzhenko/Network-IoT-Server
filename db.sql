CREATE TABLE IF NOT EXISTS hosts(
    ID int NOT NULL AUTO_INCREMENT,
    mac varchar(255) NOT NULL,
    name varchar(255),
    PRIMARY KEY (ID)
);

INSERT INTO hosts (name, mac)
VALUES ("Iphone Aleksey", "78:4f:43:1d:ab:d7");

INSERT INTO hosts (name, mac)
VALUES ("Global Cache", "00:0C:1E:02:B7:65");

CREATE TABLE IF NOT EXISTS blacklisted_items(
    ID int NOT NULL AUTO_INCREMENT,
    mac varchar(255) NOT NULL,
    name varchar(255),
    PRIMARY KEY (ID)
);

INSERT INTO blacklisted_items (name, mac)
VALUES ("router.asus.com", "54:A0:50:D8:0F:18");