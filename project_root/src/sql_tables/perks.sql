CREATE TABLE perks (
    perksId INT PRIMARY KEY AUTO_INCREMENT,
    perkStatsId INT,
    FOREIGN KEY (perkStatsId) REFERENCES perk_stats(perkStatsId)
);

-- Assuming you have a table named player_match_data to connect perks with a match and participant.
ALTER TABLE player_match_data ADD COLUMN perksId INT;
ALTER TABLE player_match_data ADD FOREIGN KEY (perksId) REFERENCES perks(perksId);