create database if not exists ipl;
use ipl;

SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Accommodation;
DROP TABLE IF EXISTS Player;
DROP TABLE IF EXISTS Support_staff;
DROP TABLE IF EXISTS Owner;
DROP TABLE IF EXISTS Sponsor;
DROP TABLE IF EXISTS Sponsored_by;
DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS Match_official;
DROP TABLE IF EXISTS Stadium;
DROP TABLE IF EXISTS Participants_in_wicket;
DROP TABLE IF EXISTS Ball_stats;
DROP TABLE IF EXISTS Umpires;
SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE Team
(
team_name CHAR(40) DEFAULT NULL,
team_id INT NOT NULL,
city CHAR(30) DEFAULT NULL,
titles_won INT DEFAULT NULL,
PRIMARY KEY(team_id)
);

LOAD DATA LOCAL INFILE 'Team.csv' INTO TABLE Team FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE Accommodation
(
hotel_name CHAR(40) DEFAULT NULL,
hotel_id INT NOT NULL,
locality CHAR(30) DEFAULT NULL,
city CHAR(30) DEFAULT NULL,
state CHAR(30) DEFAULT NULL,
capacity INT DEFAULT NULL,
PRIMARY KEY(hotel_id)
);

LOAD DATA LOCAL INFILE 'Accommodation.csv' INTO TABLE Accommodation FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;


CREATE TABLE Player
(
player_name CHAR(40) DEFAULT NULL,
nationality CHAR(40) DEFAULT NULL,
player_id INT NOT NULL,
age INT DEFAULT NULL,
captain BIT DEFAULT 0,
vice_captain BIT DEFAULT 0,
batsman BIT DEFAULT 0,
wicket_keeper BIT DEFAULT 0,
all_rounder BIT DEFAULT 0,
bowler BIT DEFAULT 0,
team_id INT DEFAULT NULL,
hotel_id INT DEFAULT NULL,
PRIMARY KEY(player_id),
FOREIGN KEY(team_id) REFERENCES Team (team_id),
FOREIGN KEY(hotel_id) REFERENCES Accommodation (hotel_id)
);

LOAD DATA LOCAL INFILE 'Player.csv' INTO TABLE Player FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;


CREATE TABLE Support_staff
(
staff_name CHAR(40) DEFAULT NULL,
staff_id INT NOT NULL,
role CHAR(40) DEFAULT NULL,
team_id INT DEFAULT NULL,
hotel_id INT DEFAULT NULL,
CONSTRAINT chk_role CHECK (role IN ('physio', 'tech_analyst', 'nutritionist', 'coach')),
PRIMARY KEY(staff_id),
FOREIGN KEY(team_id) REFERENCES Team (team_id),
FOREIGN KEY(hotel_id) REFERENCES Accommodation (hotel_id)
);

LOAD DATA LOCAL INFILE 'Support_staff.csv' INTO TABLE Support_staff FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE Owner
(
owner_name CHAR(40) DEFAULT NULL,
owner_id INT NOT NULL,
stake INT DEFAULT NULL,
team_id INT DEFAULT NULL,
PRIMARY KEY(owner_id),
FOREIGN KEY(team_id) REFERENCES Team (team_id)
);

LOAD DATA LOCAL INFILE 'Owner.csv' INTO TABLE Owner FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;


CREATE TABLE Sponsor
(
sponsor_name CHAR(40) DEFAULT NULL,
sponsor_id INT NOT NULL,
PRIMARY KEY(sponsor_id)
);

LOAD DATA LOCAL INFILE 'Sponsor.csv' INTO TABLE Sponsor FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

delete from Sponsor where sponsor_id = 0;

CREATE TABLE Sponsored_by
(
team_id INT NOT NULL,
sponsor_id INT NOT NULL,
FOREIGN KEY(team_id) REFERENCES Team (team_id),
FOREIGN KEY(sponsor_id) REFERENCES Sponsor (sponsor_id),
PRIMARY KEY(team_id, sponsor_id)
);

LOAD DATA LOCAL INFILE 'Sponsored_by.csv' INTO TABLE Sponsored_by FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE Match_official
(
official_id INT NOT NULL,
name CHAR(40) DEFAULT NULL,
age INT DEFAULT NULL,
experience INT DEFAULT NULL,
accomodated_at INT DEFAULT NULL,
FOREIGN KEY(accomodated_at ) REFERENCES Accommodation (hotel_id),
PRIMARY KEY(official_id)
);

LOAD DATA LOCAL INFILE 'Match_official.csv' INTO TABLE Match_official FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE Stadium
(
name CHAR(100) DEFAULT NULL,
stadium_id INT NOT NULL,
home_ground_team_id INT DEFAULT NULL,
capacity INT DEFAULT NULL,
location_country CHAR(40) DEFAULT NULL,
location_state CHAR(40) DEFAULT NULL,
location_city CHAR(40) DEFAULT NULL,
FOREIGN KEY(home_ground_team_id) REFERENCES Team (team_id),
PRIMARY KEY(stadium_id)
);

LOAD DATA LOCAL INFILE 'Stadium.csv' INTO TABLE Stadium FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE Matches
(
referee INT NOT NULL,
match_date DATE DEFAULT NULL,
match_id INT NOT NULL,
match_time TIME DEFAULT NULL,
first_batting INT DEFAULT NULL,
toss_winning_team INT DEFAULT NULL,
result_runs INT DEFAULT NULL,
result_wickets INT DEFAULT NULL,
result_winning_team_id INT DEFAULT NULL,
played_by_team_id1 INT DEFAULT NULL,
played_by_team_id2 INT DEFAULT NULL,
held_at_stadium INT NOT NULL,
FOREIGN KEY(first_batting) REFERENCES Team (team_id),
FOREIGN KEY(toss_winning_team) REFERENCES Team (team_id),
FOREIGN KEY(result_winning_team_id) REFERENCES Team (team_id),
FOREIGN KEY(played_by_team_id1) REFERENCES Team (team_id),
FOREIGN KEY(played_by_team_id2) REFERENCES Team (team_id),
FOREIGN KEY(held_at_stadium) REFERENCES Stadium (stadium_id),
FOREIGN KEY(referee) REFERENCES Match_official (official_id),
PRIMARY KEY(match_id)
);

LOAD DATA LOCAL INFILE 'Matches.csv' INTO TABLE Matches FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

create TABLE Ball_stats
(
match_id INT NOT NULL,
over_id INT NOT NULL,
ball_number INT NOT NULL,
innings_num INT NOT NULL,
batting_team INT NOT NULL,
bowling_team INT NOT NULL,
striker INT NOT NULL,
non_striker INT NOT NULL,
bowler INT NOT NULL,
runs_scored INT DEFAULT 0,
wicket_type CHAR(40) DEFAULT NULL,
wicket_player_dismissed INT DEFAULT NULL,
extras_type CHAR(40) DEFAULT NULL,
extras_runs INT DEFAULT 0,
CONSTRAINT chk_extra CHECK (extras_type IN ('noballs', 'wides', 'byes', 'legbyes', 'penalty')),
CONSTRAINT chk_wicket CHECK (wicket_type IN ('bowled', 'caught', 'caught and bowled', 'lbw', 'run out', 'stumped', 'retired hurt', 'hit wicket', 'obstructing the field')),
FOREIGN KEY(bowler) REFERENCES Player (player_id),
FOREIGN KEY(match_id) REFERENCES Matches (match_id),
FOREIGN KEY(striker) REFERENCES Player (player_id),
FOREIGN KEY(non_striker) REFERENCES Player (player_id),
FOREIGN KEY(batting_team) REFERENCES Team (team_id),
FOREIGN KEY(bowling_team) REFERENCES Team (team_id),
FOREIGN KEY(wicket_player_dismissed) REFERENCES Player(player_id),
PRIMARY KEY(match_id, over_id, ball_number, innings_num)
);

LOAD DATA LOCAL INFILE 'Ball_stats.csv' INTO TABLE Ball_stats FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE Participants_in_wicket
(
match_id INT NOT NULL,
over_id INT NOT NULL,
ball_number INT NOT NULL,
innings_num INT NOT NULL,
participant INT NOT NULL,
FOREIGN KEY(match_id, over_id, ball_number, innings_num) REFERENCES Ball_stats (match_id, over_id, ball_number, innings_num),
PRIMARY KEY(match_id, over_id, ball_number, innings_num, participant)
);

LOAD DATA LOCAL INFILE 'Participants_in_wicket.csv' INTO TABLE Participants_in_wicket FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

CREATE TABLE Umpires
(
match_id INT NOT NULL,
umpire_number INT NOT NULL,
official_id INT NOT NULL,
CONSTRAINT chk_ump CHECK (umpire_number IN (1, 2, 3)),
FOREIGN KEY(official_id) REFERENCES Match_official (official_id),
FOREIGN KEY(match_id) REFERENCES Matches (match_id),
PRIMARY KEY(official_id, match_id)
);

LOAD DATA LOCAL INFILE 'Umpires.csv' INTO TABLE Umpires FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 LINES;

