CREATE TABLE match_events (
    eventId SERIAL PRIMARY KEY,
    matchId VARCHAR(255),
    timestamp BIGINT,
    eventType VARCHAR(255),
    FOREIGN KEY (matchId) REFERENCES match_metadata(matchId)
);

CREATE TABLE kill_events (
    killEventId SERIAL PRIMARY KEY,
    eventId INT,
    bounty INT,
    killStreakLength INT,
    killerId INT,
    shutdownBounty INT,
    victimId INT,
    FOREIGN KEY (eventId) REFERENCES match_events(eventId)
);

CREATE TABLE event_positions (
    positionId SERIAL PRIMARY KEY,
    eventId INT,
    participantId INT,
    x INT,
    y INT,
    FOREIGN KEY (eventId) REFERENCES match_events(eventId)
);

CREATE TABLE victim_damage_dealt (
    damageDealtId SERIAL PRIMARY KEY,
    killEventId INT,
    participantId INT,
    basic BOOLEAN,
    magicDamage INT,
    physicalDamage INT,
    trueDamage INT,
    FOREIGN KEY (killEventId) REFERENCES kill_events(killEventId)
);

CREATE TABLE victim_damage_received (
    damageReceivedId SERIAL PRIMARY KEY,
    killEventId INT,
    participantId INT,
    basic BOOLEAN,
    magicDamage INT,
    physicalDamage INT,
    trueDamage INT,
    FOREIGN KEY (killEventId) REFERENCES kill_events(killEventId)
);
