CREATE TABLE "match_metadata" (
  "dataVersion" VARCHAR(255),
  "matchId" VARCHAR(255) PRIMARY KEY,
  "gameCreation" BIGINT,
  "gameDuration" BIGINT,
  "gameEndTimestamp" BIGINT,
  "gameId" BIGINT,
  "gameMode" VARCHAR(255),
  "gameName" VARCHAR(255),
  "gameStartTimestamp" BIGINT,
  "gameType" VARCHAR(255),
  "gameVersion" VARCHAR(255),
  "mapId" INT,
  "platformId" VARCHAR(255),
  "queueId" INT,
  "tournamentCode" VARCHAR(255)
);

CREATE TABLE "perks" (
  "perksId" SERIAL PRIMARY KEY,
  "defense" INT,
  "flex" INT,
  "offense" INT,
  "style" INT,
  "description" VARCHAR(255)
);

CREATE TABLE "perk_style_selections" (
  "selectionId" SERIAL PRIMARY KEY,
  "perksId" INT,
  "perk" INT,
  "var1" INT,
  "var2" INT,
  "var3" INT
);

CREATE TABLE "player_match_data" (
  "matchId" VARCHAR(255),
  "participantId" INT,
  "assists" INT,
  "baronKills" INT,
  "bountyLevel" INT,
  "champExperience" INT,
  "champLevel" INT,
  "championId" INT,
  "championName" VARCHAR(255),
  "championTransform" INT,
  "consumablesPurchased" INT,
  "damageDealtToBuildings" INT,
  "damageDealtToObjectives" INT,
  "damageDealtToTurrets" INT,
  "damageSelfMitigated" INT,
  "deaths" INT,
  "detectorWardsPlaced" INT,
  "doubleKills" INT,
  "dragonKills" INT,
  "firstBloodAssist" BOOLEAN,
  "firstBloodKill" BOOLEAN,
  "firstTowerAssist" BOOLEAN,
  "firstTowerKill" BOOLEAN,
  "gameEndedInEarlySurrender" BOOLEAN,
  "gameEndedInSurrender" BOOLEAN,
  "goldEarned" INT,
  "goldSpent" INT,
  "individualPosition" VARCHAR(255),
  "inhibitorKills" INT,
  "inhibitorTakedowns" INT,
  "inhibitorsLost" INT,
  "item0" INT,
  "item1" INT,
  "item2" INT,
  "item3" INT,
  "item4" INT,
  "item5" INT,
  "item6" INT,
  "itemsPurchased" INT,
  "killingSprees" INT,
  "kills" INT,
  "lane" VARCHAR(255),
  "largestCriticalStrike" INT,
  "largestKillingSpree" INT,
  "largestMultiKill" INT,
  "longestTimeSpentLiving" INT,
  "magicDamageDealt" INT,
  "magicDamageDealtToChampions" INT,
  "magicDamageTaken" INT,
  "neutralMinionsKilled" INT,
  "nexusKills" INT,
  "nexusTakedowns" INT,
  "nexusLost" INT,
  "objectivesStolen" INT,
  "objectivesStolenAssists" INT,
  "pentaKills" INT,
  "perksId" INT,
  "physicalDamageDealt" INT,
  "physicalDamageDealtToChampions" INT,
  "physicalDamageTaken" INT,
  "profileIcon" INT,
  "puuid" VARCHAR(255),
  "quadraKills" INT,
  "riotIdName" VARCHAR(255),
  "riotIdTagline" VARCHAR(255),
  "role" VARCHAR(255),
  "sightWardsBoughtInGame" INT,
  "spell1Casts" INT,
  "spell2Casts" INT,
  "spell3Casts" INT,
  "spell4Casts" INT,
  "summoner1Casts" INT,
  "summoner1Id" INT,
  "summoner2Casts" INT,
  "summoner2Id" INT,
  "summonerId" VARCHAR(255),
  "summonerLevel" INT,
  "summonerName" VARCHAR(255),
  "teamEarlySurrendered" BOOLEAN,
  "teamId" INT,
  "teamPosition" VARCHAR(255),
  "timeCCingOthers" INT,
  "timePlayed" INT,
  "totalDamageDealt" INT,
  "totalDamageDealtToChampions" INT,
  "totalDamageShieldedOnTeammates" INT,
  "totalDamageTaken" INT,
  "totalHeal" INT,
  "totalHealsOnTeammates" INT,
  "totalMinionsKilled" INT,
  "totalTimeCCDealt" INT,
  "totalTimeSpentDead" INT,
  "totalUnitsHealed" INT,
  "tripleKills" INT,
  "trueDamageDealt" INT,
  "trueDamageDealtToChampions" INT,
  "trueDamageTaken" INT,
  "turretKills" INT,
  "turretTakedowns" INT,
  "turretsLost" INT,
  "unrealKills" INT,
  "visionScore" INT,
  "visionWardsBoughtInGame" INT,
  "wardsKilled" INT,
  "wardsPlaced" INT,
  "win" BOOLEAN
);

CREATE TABLE "challenges" (
  "challengesId" SERIAL PRIMARY KEY,
  "matchId" VARCHAR(255),
  "participantId" INT,
  "bountyLevel" INT,
  "AssistStreakCount" INT,
  "abilityUses" INT,
  "acesBefore15Minutes" INT,
  "alliedJungleMonsterKills" INT,
  "baronTakedowns" INT,
  "blastConeOppositeOpponentCount" INT,
  "bountyGold" INT,
  "buffsStolen" INT,
  "completeSupportQuestInTime" INT,
  "controlWardsPlaced" INT,
  "damagePerMinute" FLOAT,
  "damageTakenOnTeamPercentage" FLOAT,
  "dancedWithRiftHerald" INT,
  "deathsByEnemyChamps" INT,
  "dodgeSkillShotsSmallWindow" INT,
  "doubleAces" INT,
  "dragonTakedowns" INT,
  "earlyLaningPhaseGoldExpAdvantage" FLOAT,
  "effectiveHealAndShielding" INT,
  "elderDragonKillsWithOpposingSoul" INT,
  "elderDragonMultikills" INT,
  "enemyChampionImmobilizations" INT,
  "enemyJungleMonsterKills" INT,
  "epicMonsterKillsNearEnemyJungler" INT,
  "epicMonsterKillsWithin30SecondsOfSpawn" INT,
  "epicMonsterSteals" INT,
  "epicMonsterStolenWithoutSmite" INT,
  "firstTurretKilled" INT,
  "flawlessAces" INT,
  "fullTeamTakedown" INT,
  "gameLength" FLOAT,
  "getTakedownsInAllLanesEarlyJungleAsLaner" INT,
  "goldPerMinute" FLOAT,
  "hadOpenNexus" INT,
  "immobilizeAndKillWithAlly" INT,
  "initialBuffCount" INT,
  "initialCrabCount" INT,
  "jungleCsBefore10Minutes" INT,
  "junglerTakedownsNearDamagedEpicMonster" INT,
  "kTurretsDestroyedBeforePlatesFall" INT,
  "kda" FLOAT,
  "killAfterHiddenWithAlly" INT,
  "killParticipation" FLOAT,
  "killedChampTookFullTeamDamageSurvived" INT,
  "killingSprees" INT,
  "killsNearEnemyTurret" INT,
  "killsOnOtherLanesEarlyJungleAsLaner" INT,
  "killsOnRecentlyHealedByAramPack" INT,
  "killsUnderOwnTurret" INT,
  "killsWithHelpFromEpicMonster" INT,
  "knockEnemyIntoTeamAndKill" INT,
  "landSkillShotsEarlyGame" INT,
  "laneMinionsFirst10Minutes" INT,
  "laningPhaseGoldExpAdvantage" FLOAT,
  "legendaryCount" INT,
  "lostAnInhibitor" INT,
  "maxCsAdvantageOnLaneOpponent" INT,
  "maxKillDeficit" INT,
  "maxLevelLeadLaneOpponent" INT,
  "mejaisFullStackInTime" INT,
  "moreEnemyJungleThanOpponent" INT,
  "multiKillOneSpell" INT,
  "multiTurretRiftHeraldCount" INT,
  "multikills" INT,
  "multikillsAfterAggressiveFlash" INT,
  "mythicItemUsed" INT,
  "outerTurretExecutesBefore10Minutes" INT,
  "outnumberedKills" INT,
  "outnumberedNexusKill" INT,
  "perfectDragonSoulsTaken" INT,
  "perfectGame" INT,
  "pickKillWithAlly" INT,
  "poroExplosions" INT,
  "quickCleanse" INT,
  "quickFirstTurret" INT,
  "quickSoloKills" INT,
  "riftHeraldTakedowns" INT,
  "saveAllyFromDeath" INT,
  "scuttleCrabKills" INT,
  "skillshotsDodged" INT,
  "skillshotsHit" INT,
  "snowballsHit" INT,
  "soloBaronKills" INT,
  "soloKills" INT,
  "stealthWardsPlaced" INT,
  "survivedSingleDigitHpCount" INT,
  "survivedThreeImmobilizesInFight" INT,
  "takedownOnFirstTurret" INT,
  "takedowns" INT,
  "takedownsAfterGainingLevelAdvantage" INT,
  "takedownsBeforeJungleMinionSpawn" INT,
  "takedownsFirstXMinutes" INT,
  "takedownsInAlcove" INT,
  "takedownsInEnemyFountain" INT,
  "teamBaronKills" INT,
  "teamDamagePercentage" FLOAT,
  "teamElderDragonKills" INT,
  "teamRiftHeraldKills" INT,
  "tookLargeDamageSurvived" INT,
  "turretPlatesTaken" INT,
  "turretTakedowns" INT,
  "turretsTakenWithRiftHerald" INT,
  "twentyMinionsIn3SecondsCount" INT,
  "twoWardsOneSweeperCount" INT,
  "unseenRecalls" INT,
  "visionScoreAdvantageLaneOpponent" INT,
  "visionScorePerMinute" FLOAT,
  "wardTakedowns" INT,
  "wardTakedownsBefore20M" INT,
  "wardsGuarded" INT
);

CREATE TABLE "participant_frames" (
  "frameId" SERIAL PRIMARY KEY,
  "matchId" VARCHAR(255),
  "participantId" INT,
  "timestamp" BIGINT,
  "level" INT,
  "currentGold" INT,
  "totalGold" INT,
  "xp" INT,
  "minionsKilled" INT,
  "jungleMinionsKilled" INT,
  "timeEnemySpentControlled" INT,
  "abilityHaste" INT,
  "abilityPower" INT,
  "armor" INT,
  "armorPen" INT,
  "armorPenPercent" FLOAT,
  "attackDamage" INT,
  "attackSpeed" INT,
  "bonusArmorPenPercent" FLOAT,
  "bonusMagicPenPercent" FLOAT,
  "ccReduction" INT,
  "cooldownReduction" INT,
  "health" INT,
  "healthMax" INT,
  "healthRegen" INT,
  "lifesteal" INT,
  "magicPen" INT,
  "magicPenPercent" FLOAT,
  "magicResist" INT,
  "movementSpeed" INT,
  "omnivamp" INT,
  "physicalVamp" INT,
  "power" INT,
  "powerMax" INT,
  "powerRegen" INT,
  "spellVamp" INT,
  "magicDamageDone" INT,
  "magicDamageDoneToChampions" INT,
  "magicDamageTaken" INT,
  "physicalDamageDone" INT,
  "physicalDamageDoneToChampions" INT,
  "physicalDamageTaken" INT,
  "totalDamageDone" INT,
  "totalDamageDoneToChampions" INT,
  "totalDamageTaken" INT,
  "trueDamageDone" INT,
  "trueDamageDoneToChampions" INT,
  "trueDamageTaken" INT,
  "positionX" INT,
  "positionY" INT
);

CREATE TABLE "match_events" (
  "eventId" SERIAL PRIMARY KEY,
  "matchId" VARCHAR(255),
  "timestamp" BIGINT,
  "eventType" VARCHAR(255)
);

CREATE TABLE "kill_events" (
  "killEventId" SERIAL PRIMARY KEY,
  "eventId" INT,
  "bounty" INT,
  "killStreakLength" INT,
  "killerId" INT,
  "shutdownBounty" INT,
  "victimId" INT
);

CREATE TABLE "event_positions" (
  "positionId" SERIAL PRIMARY KEY,
  "eventId" INT,
  "participantId" INT,
  "x" INT,
  "y" INT
);

CREATE TABLE "victim_damage_dealt" (
  "damageDealtId" SERIAL PRIMARY KEY,
  "killEventId" INT,
  "participantId" INT,
  "basic" BOOLEAN,
  "magicDamage" INT,
  "physicalDamage" INT,
  "trueDamage" INT
);

CREATE TABLE "victim_damage_received" (
  "damageReceivedId" SERIAL PRIMARY KEY,
  "killEventId" INT,
  "participantId" INT,
  "basic" BOOLEAN,
  "magicDamage" INT,
  "physicalDamage" INT,
  "trueDamage" INT
);

CREATE TABLE "teams" (
  "teamId" INT,
  "matchId" VARCHAR(255),
  "baronFirst" BOOLEAN,
  "baronKills" INT,
  "championFirst" BOOLEAN,
  "championKills" INT,
  "dragonFirst" BOOLEAN,
  "dragonKills" INT,
  "inhibitorFirst" BOOLEAN,
  "inhibitorKills" INT,
  "riftHeraldFirst" BOOLEAN,
  "riftHeraldKills" INT,
  "towerFirst" BOOLEAN,
  "towerKills" INT,
  "win" BOOLEAN,
  PRIMARY KEY ("matchId", "teamId")
);

CREATE UNIQUE INDEX ON "player_match_data" ("matchId", "participantId");

ALTER TABLE "perk_style_selections" ADD FOREIGN KEY ("perksId") REFERENCES "perks" ("perksId");

ALTER TABLE "player_match_data" ADD FOREIGN KEY ("matchId") REFERENCES "match_metadata" ("matchId");

ALTER TABLE "player_match_data" ADD FOREIGN KEY ("participantId") REFERENCES "participant_frames" ("participantId");

ALTER TABLE "player_match_data" ADD FOREIGN KEY ("perksId") REFERENCES "perks" ("perksId");

ALTER TABLE "challenges" ADD FOREIGN KEY ("matchId") REFERENCES "player_match_data" ("matchId");

ALTER TABLE "challenges" ADD FOREIGN KEY ("participantId") REFERENCES "player_match_data" ("participantId");

CREATE TABLE "challenges_player_match_data" (
  "challenges_matchId" VARCHAR(255),
  "challenges_participantId" INT,
  "player_match_data_matchId" VARCHAR(255),
  "player_match_data_participantId" INT,
  PRIMARY KEY ("challenges_matchId", "challenges_participantId", "player_match_data_matchId", "player_match_data_participantId")
);

ALTER TABLE "challenges_player_match_data" ADD FOREIGN KEY ("challenges_matchId", "challenges_participantId") REFERENCES "challenges" ("matchId", "participantId");

ALTER TABLE "challenges_player_match_data" ADD FOREIGN KEY ("player_match_data_matchId", "player_match_data_participantId") REFERENCES "player_match_data" ("matchId", "participantId");


ALTER TABLE "participant_frames" ADD FOREIGN KEY ("matchId", "participantId") REFERENCES "player_match_data" ("matchId", "participantId");

ALTER TABLE "participant_frames" ADD FOREIGN KEY ("matchId") REFERENCES "match_metadata" ("matchId");

ALTER TABLE "match_events" ADD FOREIGN KEY ("matchId") REFERENCES "match_metadata" ("matchId");

ALTER TABLE "kill_events" ADD FOREIGN KEY ("eventId") REFERENCES "match_events" ("eventId");

ALTER TABLE "event_positions" ADD FOREIGN KEY ("eventId") REFERENCES "match_events" ("eventId");

ALTER TABLE "victim_damage_dealt" ADD FOREIGN KEY ("killEventId") REFERENCES "kill_events" ("killEventId");

ALTER TABLE "victim_damage_received" ADD FOREIGN KEY ("killEventId") REFERENCES "kill_events" ("killEventId");

ALTER TABLE "teams" ADD FOREIGN KEY ("matchId") REFERENCES "match_metadata" ("matchId");
