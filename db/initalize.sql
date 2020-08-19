-- DROP DATABASE IF EXISTS temp_name;
-- CREATE DATABASE temp_name;
\c temp_name;

CREATE TABLE Users(
	ID INT NOT NULL AUTO_INCREMENT,
    Username VARCHAR(255) NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Salt VARCHAR(255) NOT NULL,
    Name VARCHAR(255) NOT NULL,
    PRIMARY KEY(ID),
);

INSERT INTO Users VALUES(0, 1, 'jUUORG667DEEVqN9yz/i68+apttG4XSy121RHpnYEVJt6chYZnnf6YY1Zu9wGZ+FlW3t/6an8CHMcSNb+73auQ==', 'cw6ABGA4i53fb+ijN0D8QQ==');
INSERT INTO Users VALUES(0, 2, '3rpxnwwa4ZIb+sRqW8C3zW/sE2U5SFcc/Z3SUQ8XbS4V37OUEQHKgtpjQktFW3NJeiLk1JLT/k0ygtFuglGAxw==', 'FK38LFxiODd+pkmLELONOw==');
INSERT INTO Users VALUES(0, 3, 'CSxouMbeIU5tgVR2Nnn5AORJBAQnT6HeFBvd3oJrEOMiKHswBNZeZUUB5XULoHctazX494vO6bq8XVwlcfXe9w==', 'Brkr2L+VmYYxxZeI0HLPvg==');