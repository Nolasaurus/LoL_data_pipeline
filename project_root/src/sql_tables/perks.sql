CREATE TABLE perk_stats (
    perkStatsId SERIAL PRIMARY KEY,
    defense INT,
    flex INT,
    offense INT
);

CREATE TABLE perk_styles (
    perkStylesId SERIAL PRIMARY KEY,
    description VARCHAR(255),
    style INT
    );

CREATE TABLE perk_style_selections (
    perkStyleSelectionId SERIAL PRIMARY KEY,
    perkStylesId INT,
    perk INT,
    var1 INT,
    var2 INT,
    var3 INT,
    FOREIGN KEY (perkStylesId) REFERENCES perk_styles(perkStylesId)
);

CREATE TABLE perks (
    perksId SERIAL PRIMARY KEY,
    perkStatsId INT,
    FOREIGN KEY (perkStatsId) REFERENCES perk_stats(perkStatsId)
);





