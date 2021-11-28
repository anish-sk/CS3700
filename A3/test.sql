create database if not exists test_team;
use test_team;

CREATE TABLE if not exists Team
(
team_name CHAR(40) DEFAULT NULL,
team_id INT NOT NULL,
city CHAR(30) DEFAULT NULL,
titles_won INT DEFAULT NULL,
PRIMARY KEY(team_id)
);

/*COPY Team FROM './Team.csv' (FORMAT CSV, ENCODING 'UTF8');*/
LOAD DATA LOCAL INFILE 'Team.csv' INTO TABLE Team FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n';
