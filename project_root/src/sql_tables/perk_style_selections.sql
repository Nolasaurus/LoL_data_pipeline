CREATE TABLE perk_style_selections (
    perkStyleSelectionId INT PRIMARY KEY AUTO_INCREMENT,
    perkStylesId INT,
    perk INT,
    var1 INT,
    var2 INT,
    var3 INT,
    FOREIGN KEY (perkStylesId) REFERENCES perk_styles(perkStylesId)
);