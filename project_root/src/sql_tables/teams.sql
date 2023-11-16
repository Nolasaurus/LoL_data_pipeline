CREATE TABLE teams (
    teamId INT,
    matchId VARCHAR(255),
    baronFirst BOOLEAN,
    baronKills INT,
    championFirst BOOLEAN,
    championKills INT,
    dragonFirst BOOLEAN,
    dragonKills INT,
    inhibitorFirst BOOLEAN,
    inhibitorKills INT,
    riftHeraldFirst BOOLEAN,
    riftHeraldKills INT,
    towerFirst BOOLEAN,
    towerKills INT,
    win BOOLEAN,
    PRIMARY KEY (matchId, teamId),
    FOREIGN KEY (matchId) REFERENCES match_metadata(matchId)
);
