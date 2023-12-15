from postgres_helperfile import SQLHelper, execute_batch_query
from match_classes import SummonerDto

def insert_match(match_dto, match_timeline_dto):
    pass

def get_bans(MatchDto):
    match_id = MatchDto.metadata.match_id
    teams = MatchDto.info.teams

    # Prepare a list to hold all the values to be inserted
    all_values = []
    for team in teams:
        for ban in team.bans:
            # Append each set of values as a tuple to the list
            ban_dict = {
                "match_id": match_id,
                "champion_id": ban.championId,
                "pick_turn": ban.pickTurn,
            }
            all_values.append(ban_dict)

    return all_values

def get_champion_stats(match_timeline_dto):
    frames = match_timeline_dto.info.frames
    match_id = match_timeline_dto.metadata.match_id

    values_list = []
    for frame_number, frame in enumerate(frames):
        for participant_id, participant_frame in frame.participant_frames.items():
            champion_stats = (
                participant_frame.champion_stats
                if participant_frame.champion_stats
                else {}
            )
            values = {
                "match_id": match_id,
                "frame_number": frame_number,
                "participant_id": participant_id,
                "ability_haste": getattr(champion_stats, "abilityHaste", 0),
                "ability_power": getattr(champion_stats, "abilityPower", 0),
                "armor": getattr(champion_stats, "armor", 0),
                "armor_pen": getattr(champion_stats, "armorPen", 0),
                "armor_pen_percent": getattr(champion_stats, "armorPenPercent", 0.0),
                "attack_damage": getattr(champion_stats, "attackDamage", 0),
                "attack_speed": getattr(champion_stats, "attackSpeed", 0.0),
                "bonus_armor_pen_percent": getattr(
                    champion_stats, "bonusArmorPenPercent", 0.0
                ),
                "bonus_magic_pen_percent": getattr(
                    champion_stats, "bonusMagicPenPercent", 0.0
                ),
                "cc_reduction": getattr(champion_stats, "ccReduction", 0),
                "health": getattr(champion_stats, "health", 0),
                "health_max": getattr(champion_stats, "healthMax", 0),
                "health_regen": getattr(champion_stats, "healthRegen", 0),
                "lifesteal": getattr(champion_stats, "lifesteal", 0.0),
                "magic_pen": getattr(champion_stats, "magicPen", 0),
                "magic_pen_percent": getattr(champion_stats, "magicPenPercent", 0.0),
                "magic_resist": getattr(champion_stats, "magicResist", 0),
                "movement_speed": getattr(champion_stats, "movementSpeed", 0),
                "omnivamp": getattr(champion_stats, "omnivamp", 0.0),
                "physical_vamp": getattr(champion_stats, "physicalVamp", 0.0),
                "power": getattr(champion_stats, "power", 0),
                "power_max": getattr(champion_stats, "powerMax", 0),
                "power_regen": getattr(champion_stats, "powerRegen", 0),
                "spell_vamp": getattr(champion_stats, "spellVamp", 0.0),
            }

            values_list.append(values)

    return values_list

def get_match_metadata(match_dto):
    metadata = getattr(match_dto, "metadata", {})
    info = getattr(match_dto, "info", {})

    match_metadata_dict = {
        'data_version': getattr(metadata, "dataVersion", ""),
        'match_id': getattr(metadata, "matchId", ""),
        'game_creation': getattr(info, "gameCreation", 0),
        'game_duration': getattr(info, "gameDuration", 0),
        'game_end_timestamp': getattr(info, "gameEndTimestamp", 0),
        'game_id': getattr(info, "gameId", ""),
        'game_mode': getattr(info, "gameMode", ""),
        'game_name': getattr(info, "gameName", ""),
        'game_start_timestamp': getattr(info, "gameStartTimestamp", 0),
        'game_type': getattr(info, "gameType", ""),
        'game_version': getattr(info, "gameVersion", ""),
        'map_id': getattr(info, "mapId", 0),
        'platform_id': getattr(info, "platformId", ""),
        'queue_id': getattr(info, "queueId", 0),
        'tournament_code': getattr(info, "tournamentCode", "")
    }

    return match_metadata_dict

def get_perk_style_selections(match_dto):
    participants = getattr(match_dto, "info", {}).get("participants", [])
    match_id = getattr(match_dto, "metadata", {}).get("matchId", "")

    perk_style_selections_list = []
    for participant in participants:
        participant_id = participant.get("participantId", "")
        for style_index, style in enumerate(participant.get("perks", {}).get("styles", [])):
            for selection_index, selection in enumerate(style.get("selections", [])):
                perk_style_selection_dict = {
                    'match_id': match_id,
                    'participant_id': participant_id,
                    'style_index': style_index,
                    'selection_index': selection_index,
                    'perk': selection.get("perk", 0),
                    'var1': selection.get("var1", 0),
                    'var2': selection.get("var2", 0),
                    'var3': selection.get("var3", 0)
                }

                perk_style_selections_list.append(perk_style_selection_dict)

    return perk_style_selections_list

def get_teams(match_dto):
    match_id = match_dto.metadata.match_id
    teams = match_dto.info.teams

    teams_list = []
    for team in teams:
        # Extracting objectives data
        objectives = team.objectives.objectives

        team_data = {
            'team_id': team.team_id,
            'match_id': match_id,
            'baron_first': objectives['baron'].first if 'baron' in objectives else False,
            'baron_kills': objectives['baron'].kills if 'baron' in objectives else 0,
            'dragon_first': objectives['dragon'].first if 'dragon' in objectives else False,
            'dragon_kills': objectives['dragon'].kills if 'dragon' in objectives else 0,
            'champion_first': objectives['champion'].first if 'champion' in objectives else False,
            'champion_kills': objectives['champion'].kills if 'champion' in objectives else 0,
            'inhibitor_first': objectives['inhibitor'].first if 'inhibitor' in objectives else False,
            'inhibitor_kills': objectives['inhibitor'].kills if 'inhibitor' in objectives else 0,
            'rift_herald_first': objectives['riftHerald'].first if 'riftHerald' in objectives else False,
            'rift_herald_kills': objectives['riftHerald'].kills if 'riftHerald' in objectives else 0,
            'tower_first': objectives['tower'].first if 'tower' in objectives else False,
            'tower_kills': objectives['tower'].kills if 'tower' in objectives else 0,
            'win': team.win
        }

        teams_list.append(team_data)

    return teams_list

def get_damage_stats(match_timeline_dto):
    frames = match_timeline_dto["info"]["frames"]
    match_id = match_timeline_dto["metadata"]["matchId"]

    damage_stats_list = []
    for frame_number, frame in enumerate(frames):
        participant_frames = frame["participantFrames"].values()  # Assuming participantFrames is a dict

        for participant_frame in participant_frames:
            participant_id = participant_frame["participantId"]
            damage_stats = participant_frame["damageStats"]

            damage_stat_dict = {
                'match_id': match_id,
                'frame_number': frame_number,
                'participant_id': participant_id,
                'magic_damage_done': damage_stats["magicDamageDone"],
                'magic_damage_done_to_champions': damage_stats["magicDamageDoneToChampions"],
                'magic_damage_taken': damage_stats["magicDamageTaken"],
                'physical_damage_done': damage_stats["physicalDamageDone"],
                'physical_damage_done_to_champions': damage_stats["physicalDamageDoneToChampions"],
                'physical_damage_taken': damage_stats["physicalDamageTaken"],
                'total_damage_done': damage_stats["totalDamageDone"],
                'total_damage_done_to_champions': damage_stats["totalDamageDoneToChampions"],
                'total_damage_taken': damage_stats["totalDamageTaken"],
                'true_damage_done': damage_stats["trueDamageDone"],
                'true_damage_done_to_champions': damage_stats["trueDamageDoneToChampions"],
                'true_damage_taken': damage_stats["trueDamageTaken"]
            }

            damage_stats_list.append(damage_stat_dict)

    return damage_stats_list

def get_victim_damage(match_timeline_dto):
    frames = match_timeline_dto["info"]["frames"]
    match_id = match_timeline_dto["metadata"]["matchId"]

    damage_received_list = []
    damage_dealt_list = []

    for frame_number, frame in enumerate(frames):
        for event_number, event in enumerate(frame["events"]):
            if event["type"] == "CHAMPION_KILL":
                for damage_number, damage_received in enumerate(event["victimDamageReceived"]):
                    received_values = {
                        "match_id": match_id,
                        "participant_id": damage_received["participantId"],
                        "basic": damage_received["basic"],
                        "magic_damage": damage_received["magicDamage"],
                        "physical_damage": damage_received["physicalDamage"],
                        "name": damage_received["name"],
                        "spell_name": damage_received.get("spellName", ""),
                        "spell_slot": damage_received.get("spellSlot", 0),
                        "true_damage": damage_received["trueDamage"],
                        "damage_type": damage_received["type"],
                    }

                    damage_received_list.append(received_values)

                for damage_number, damage_dealt in enumerate(event["victimDamageDealt"]):
                    dealt_values = {
                        "match_id": match_id,
                        "participant_id": damage_dealt["participantId"],
                        "basic": damage_dealt["basic"],
                        "magic_damage": damage_dealt["magicDamage"],
                        "physical_damage": damage_dealt["physicalDamage"],
                        "name": damage_dealt["name"],
                        "spell_name": damage_dealt.get("spellName", ""),
                        "spell_slot": damage_dealt.get("spellSlot", 0),
                        "true_damage": damage_dealt["trueDamage"],
                        "damage_type": damage_dealt["type"],
                    }

                    damage_dealt_list.append(dealt_values)

    return damage_received_list, damage_dealt_list

def get_challenges(match_dto):
    challenges_list = []

    participants = match_dto["info"]["participants"]
    for participant in participants:
        challenges = participant["challenges"]
        
        values = {
            "match_id": match_dto["metadata"]["matchId"],
            "participant_id": participant["participantId"],
            "assistStreakCount": challenges.get("assistStreakCount", 0),
            "abilityUses": challenges.get("abilityUses", 0),
            "acesBefore15Minutes": challenges.get("acesBefore15Minutes", 0),
            "alliedJungleMonsterKills": challenges.get("alliedJungleMonsterKills", 0),
            "baronTakedowns": challenges.get("baronTakedowns", 0),
            "blastConeOppositeOpponentCount": challenges.get("blastConeOppositeOpponentCount", 0),
            "bountyGold": challenges.get("bountyGold", 0),
            "buffsStolen": challenges.get("buffsStolen", 0),
            "completeSupportQuestInTime": challenges.get("completeSupportQuestInTime", 0),
            "controlWardsPlaced": challenges.get("controlWardsPlaced", 0),
            "damagePerMinute": challenges.get("damagePerMinute", 0.0),
            "damageTakenOnTeamPercentage": challenges.get("damageTakenOnTeamPercentage", 0.0),
            "dancedWithRiftHerald": challenges.get("dancedWithRiftHerald", 0),
            "deathsByEnemyChamps": challenges.get("deathsByEnemyChamps", 0),
            "dodgeSkillShotsSmallWindow": challenges.get("dodgeSkillShotsSmallWindow", 0),
            "doubleAces": challenges.get("doubleAces", 0),
            "dragonTakedowns": challenges.get("dragonTakedowns", 0),
            "earlyLaningPhaseGoldExpAdvantage": challenges.get("earlyLaningPhaseGoldExpAdvantage", 0.0),
            "effectiveHealAndShielding": challenges.get("effectiveHealAndShielding", 0),
            "elderDragonKillsWithOpposingSoul": challenges.get("elderDragonKillsWithOpposingSoul", 0),
            "elderDragonMultikills": challenges.get("elderDragonMultikills", 0),
            "enemyChampionImmobilizations": challenges.get("enemyChampionImmobilizations", 0),
            "enemyJungleMonsterKills": challenges.get("enemyJungleMonsterKills", 0),
            "epicMonsterKillsNearEnemyJungler": challenges.get("epicMonsterKillsNearEnemyJungler", 0),
            "epicMonsterKillsWithin30SecondsOfSpawn": challenges.get("epicMonsterKillsWithin30SecondsOfSpawn", 0),
            "epicMonsterSteals": challenges.get("epicMonsterSteals", 0),
            "epicMonsterStolenWithoutSmite": challenges.get("epicMonsterStolenWithoutSmite", 0),
            "firstTurretKilled": challenges.get("firstTurretKilled", 0),
            "flawlessAces": challenges.get("flawlessAces", 0),
            "fullTeamTakedown": challenges.get("fullTeamTakedown", 0),
            "gameLength": challenges.get("gameLength", 0.0),
            "getTakedownsInAllLanesEarlyJungleAsLaner": challenges.get("getTakedownsInAllLanesEarlyJungleAsLaner", 0),
            "goldPerMinute": challenges.get("goldPerMinute", 0.0),
            "hadOpenNexus": challenges.get("hadOpenNexus", 0),
            "immobilizeAndKillWithAlly": challenges.get("immobilizeAndKillWithAlly", 0),
            "initialBuffCount": challenges.get("initialBuffCount", 0),
            "initialCrabCount": challenges.get("initialCrabCount", 0),
            "jungleCsBefore10Minutes": challenges.get("jungleCsBefore10Minutes", 0),
            "junglerTakedownsNearDamagedEpicMonster": challenges.get("junglerTakedownsNearDamagedEpicMonster", 0),
            "kTurretsDestroyedBeforePlatesFall": challenges.get("kTurretsDestroyedBeforePlatesFall", 0),
            "kda": challenges.get("kda", 0.0),
            "killAfterHiddenWithAlly": challenges.get("killAfterHiddenWithAlly", 0),
            "killParticipation": challenges.get("killParticipation", 0.0),
            "killedChampTookFullTeamDamageSurvived": challenges.get("killedChampTookFullTeamDamageSurvived", 0),
            "killingSprees": challenges.get("killingSprees", 0),
            "killsNearEnemyTurret": challenges.get("killsNearEnemyTurret", 0),
            "killsOnOtherLanesEarlyJungleAsLaner": challenges.get("killsOnOtherLanesEarlyJungleAsLaner", 0),
            "killsOnRecentlyHealedByAramPack": challenges.get("killsOnRecentlyHealedByAramPack", 0),
            "killsUnderOwnTurret": challenges.get("killsUnderOwnTurret", 0),
            "killsWithHelpFromEpicMonster": challenges.get("killsWithHelpFromEpicMonster", 0),
            "knockEnemyIntoTeamAndKill": challenges.get("knockEnemyIntoTeamAndKill", 0),
            "landSkillShotsEarlyGame": challenges.get("landSkillShotsEarlyGame", 0),
            "laneMinionsFirst10Minutes": challenges.get("laneMinionsFirst10Minutes", 0),
            "laningPhaseGoldExpAdvantage": challenges.get("laningPhaseGoldExpAdvantage", 0.0),
            "legendaryCount": challenges.get("legendaryCount", 0),
            "lostAnInhibitor": challenges.get("lostAnInhibitor", 0),
            "maxCsAdvantageOnLaneOpponent": challenges.get("maxCsAdvantageOnLaneOpponent", 0),
            "maxKillDeficit": challenges.get("maxKillDeficit", 0),
            "maxLevelLeadLaneOpponent": challenges.get("maxLevelLeadLaneOpponent", 0),
            "mejaisFullStackInTime": challenges.get("mejaisFullStackInTime", 0),
            "moreEnemyJungleThanOpponent": challenges.get("moreEnemyJungleThanOpponent", 0),
            "multiKillOneSpell": challenges.get("multiKillOneSpell", 0),
            "multiTurretRiftHeraldCount": challenges.get("multiTurretRiftHeraldCount", 0),
            "multikills": challenges.get("multikills", 0),
            "multikillsAfterAggressiveFlash": challenges.get("multikillsAfterAggressiveFlash", 0),
            "mythicItemUsed": challenges.get("mythicItemUsed", 0),
            "outerTurretExecutesBefore10Minutes": challenges.get("outerTurretExecutesBefore10Minutes", 0),
            "outnumberedKills": challenges.get("outnumberedKills", 0),
            "outnumberedNexusKill": challenges.get("outnumberedNexusKill", 0),
            "perfectDragonSoulsTaken": challenges.get("perfectDragonSoulsTaken", 0),
            "perfectGame": challenges.get("perfectGame", 0),
            "pickKillWithAlly": challenges.get("pickKillWithAlly", 0),
            "poroExplosions": challenges.get("poroExplosions", 0),
            "quickCleanse": challenges.get("quickCleanse", 0),
            "quickFirstTurret": challenges.get("quickFirstTurret", 0),
            "quickSoloKills": challenges.get("quickSoloKills", 0),
            "riftHeraldTakedowns": challenges.get("riftHeraldTakedowns", 0),
            "saveAllyFromDeath": challenges.get("saveAllyFromDeath", 0),
            "scuttleCrabKills": challenges.get("scuttleCrabKills", 0),
            "skillshotsDodged": challenges.get("skillshotsDodged", 0),
            "skillshotsHit": challenges.get("skillshotsHit", 0),
            "snowballsHit": challenges.get("snowballsHit", 0),
            "soloBaronKills": challenges.get("soloBaronKills", 0),
            "soloKills": challenges.get("soloKills", 0),
            "stealthWardsPlaced": challenges.get("stealthWardsPlaced", 0),
            "survivedSingleDigitHpCount": challenges.get("survivedSingleDigitHpCount", 0),
            "survivedThreeImmobilizesInFight": challenges.get("survivedThreeImmobilizesInFight", 0),
            "takedownOnFirstTurret": challenges.get("takedownOnFirstTurret", 0),
            "takedowns": challenges.get("takedowns", 0),
            "takedownsAfterGainingLevelAdvantage": challenges.get("takedownsAfterGainingLevelAdvantage", 0),
            "takedownsBeforeJungleMinionSpawn": challenges.get("takedownsBeforeJungleMinionSpawn", 0),
            "takedownsFirstXMinutes": challenges.get("takedownsFirstXMinutes", 0),
            "takedownsInAlcove": challenges.get("takedownsInAlcove", 0),
            "takedownsInEnemyFountain": challenges.get("takedownsInEnemyFountain", 0),
            "teamBaronKills": challenges.get("teamBaronKills", 0),
            "teamDamagePercentage": challenges.get("teamDamagePercentage", 0.0),
            "teamElderDragonKills": challenges.get("teamElderDragonKills", 0),
            "teamRiftHeraldKills": challenges.get("teamRiftHeraldKills", 0),
            "tookLargeDamageSurvived": challenges.get("tookLargeDamageSurvived", 0),
            "turretPlatesTaken": challenges.get("turretPlatesTaken", 0),
            "turretTakedowns": challenges.get("turretTakedowns", 0),
            "turretsTakenWithRiftHerald": challenges.get("turretsTakenWithRiftHerald", 0),
            "twentyMinionsIn3SecondsCount": challenges.get("twentyMinionsIn3SecondsCount", 0),
            "twoWardsOneSweeperCount": challenges.get("twoWardsOneSweeperCount", 0),
            "unseenRecalls": challenges.get("unseenRecalls", 0),
            "visionScoreAdvantageLaneOpponent": challenges.get("visionScoreAdvantageLaneOpponent", 0.0),
            "visionScorePerMinute": challenges.get("visionScorePerMinute", 0.0),
            "wardTakedowns": challenges.get("wardTakedowns", 0),
            "wardTakedownsBefore20m": challenges.get("wardTakedownsBefore20m", 0),
            "wardsGuarded": challenges.get("wardsGuarded", 0),
        }

        challenges_list.append(values)

    return challenges_list

def get_match_events(match_timeline_dto):
    frames = match_timeline_dto.info.frames
    match_id = match_timeline_dto.metadata.matchId

    events_list = []
    for frame_number, frame in enumerate(frames):
        for event_number, event in enumerate(frame.events):
            events_dict = {
                'match_id': match_id,
                'frame_number': frame_number,
                'event_number': event_number,
                'real_timestamp': getattr(event, "realTimestamp", None),
                'timestamp': getattr(event, "timestamp", None),
                'type': getattr(event, "type", None),
                'item_id': getattr(event, "itemId", None),
                'participant_id': getattr(event, "participantId", None),
                'level_up_type': getattr(event, "levelUpType", ""),
                'skill_slot': getattr(event, "skillSlot", None),
                'creator_id': getattr(event, "creatorId", None),
                'ward_type': getattr(event, "wardType", ""),
                'level': getattr(event, "level", None),
                'bounty': getattr(event, "bounty", None),
                'kill_streak_length': getattr(event, "killStreakLength", None),
                'killer_id': getattr(event, "killerId", None),
                'position_x': getattr(event, "position", {}).get("x", None),
                'position_y': getattr(event, "position", {}).get("y", None),
                'victim_id': getattr(event, "victimId", None),
                'kill_type': getattr(event, "killType", ""),
                'lane_type': getattr(event, "laneType", ""),
                'team_id': getattr(event, "teamId", None),
                'multi_kill_length': getattr(event, "multiKillLength", None),
                'killer_team_id': getattr(event, "killerTeamId", None),
                'monster_type': getattr(event, "monsterType", ""),
                'monster_sub_type': getattr(event, "monsterSubType", ""),
                'building_type': getattr(event, "buildingType", ""),
                'tower_type': getattr(event, "towerType", ""),
                'after_id': getattr(event, "afterId", None),
                'before_id': getattr(event, "beforeId", None),
                'gold_gain': getattr(event, "goldGain", None),
                'game_id': getattr(event, "gameId", None),
                'winning_team': getattr(event, "winningTeam", None),
                'transform_type': getattr(event, "transformType", ""),
                'name': getattr(event, "name", ""),
                'shutdown_bounty': getattr(event, "shutdownBounty", None),
                'actual_start_time': getattr(event, "actualStartTime", None)
            }

            events_list.append(events_dict)

    return events_list

def get_participant_dto(match_dto):
    participants = match_dto["info"]["participants"]
    match_id = match_dto["metadata"]["matchId"]

    participant_dto_list = []

    for participant in participants:
        # Extracting all necessary participant data using .get() to avoid KeyError
        values = {
            "match_id": match_id,
            "participant_id": participant.get("participantId", ""),
            "assists": participant.get("assists", ""),
            "baronKills": participant.get("baronKills", ""),
            "bountyLevel": participant.get("bountyLevel", ""),
            "champExperience": participant.get("champExperience", ""),
            "champLevel": participant.get("champLevel", ""),
            "championId": participant.get("championId", ""),
            "championName": participant.get("championName", ""),
            "championTransform": participant.get("championTransform", ""),
            "consumablesPurchased": participant.get("consumablesPurchased", ""),
            "damageDealtToBuildings": participant.get("damageDealtToBuildings", ""),
            "damageDealtToObjectives": participant.get("damageDealtToObjectives", ""),
            "damageDealtToTurrets": participant.get("damageDealtToTurrets", ""),
            "damageSelfMitigated": participant.get("damageSelfMitigated", ""),
            "deaths": participant.get("deaths", ""),
            "detectorWardsPlaced": participant.get("detectorWardsPlaced", ""),
            "doubleKills": participant.get("doubleKills", ""),
            "dragonKills": participant.get("dragonKills", ""),
            "firstBloodAssist": participant.get("firstBloodAssist", ""),
            "firstBloodKill": participant.get("firstBloodKill", ""),
            "firstTowerAssist": participant.get("firstTowerAssist", ""),
            "firstTowerKill": participant.get("firstTowerKill", ""),
            "gameEndedInEarlySurrender": participant.get("gameEndedInEarlySurrender", ""),
            "gameEndedInSurrender": participant.get("gameEndedInSurrender", ""),
            "goldEarned": participant.get("goldEarned", ""),
            "goldSpent": participant.get("goldSpent", ""),
            "individualPosition": participant.get("individualPosition", ""),
            "inhibitorKills": participant.get("inhibitorKills", ""),
            "inhibitorTakedowns": participant.get("inhibitorTakedowns", ""),
            "inhibitorsLost": participant.get("inhibitorsLost", ""),
            "item0": participant.get("item0", ""),
            "item1": participant.get("item1", ""),
            "item2": participant.get("item2", ""),
            "item3": participant.get("item3", ""),
            "item4": participant.get("item4", ""),
            "item5": participant.get("item5", ""),
            "item6": participant.get("item6", ""),
            "itemsPurchased": participant.get("itemsPurchased", ""),
            "killingSprees": participant.get("killingSprees", ""),
            "kills": participant.get("kills", ""),
            "lane": participant.get("lane", ""),
            "largestCriticalStrike": participant.get("largestCriticalStrike", ""),
            "largestKillingSpree": participant.get("largestKillingSpree", ""),
            "largestMultiKill": participant.get("largestMultiKill", ""),
            "longestTimeSpentLiving": participant.get("longestTimeSpentLiving", ""),
            "magicDamageDealt": participant.get("magicDamageDealt", ""),
            "magicDamageDealtToChampions": participant.get("magicDamageDealtToChampions", ""),
            "magicDamageTaken": participant.get("magicDamageTaken", ""),
            "neutralMinionsKilled": participant.get("neutralMinionsKilled", ""),
            "nexusKills": participant.get("nexusKills", ""),
            "nexusTakedowns": participant.get("nexusTakedowns", ""),
            "nexusLost": participant.get("nexusLost", ""),
            "objectivesStolen": participant.get("objectivesStolen", ""),
            "objectivesStolenAssists": participant.get("objectivesStolenAssists", ""),
            "pentaKills": participant.get("pentaKills", ""),
            "physicalDamageDealt": participant.get("physicalDamageDealt", ""),
            "physicalDamageDealtToChampions": participant.get("physicalDamageDealtToChampions", ""),
            "physicalDamageTaken": participant.get("physicalDamageTaken", ""),
            "profileIcon": participant.get("profileIcon", ""),
            "puuid": participant.get("puuid", ""),
            "quadraKills": participant.get("quadraKills", ""),
            "riotIdName": participant.get("riotIdName", ""),
            "riotIdTagline": participant.get("riotIdTagline", ""),
            "role": participant.get("role", ""),
            "sightWardsBoughtInGame": participant.get("sightWardsBoughtInGame", ""),
            "spell1Casts": participant.get("spell1Casts", ""),
            "spell2Casts": participant.get("spell2Casts", ""),
            "spell3Casts": participant.get("spell3Casts", ""),
            "spell4Casts": participant.get("spell4Casts", ""),
            "summoner1Casts": participant.get("summoner1Casts", ""),
            "summoner1Id": participant.get("summoner1Id", ""),
            "summoner2Casts": participant.get("summoner2Casts", ""),
            "summoner2Id": participant.get("summoner2Id", ""),
            "summonerId": participant.get("summonerId", ""),
            "summonerLevel": participant.get("summonerLevel", ""),
            "summonerName": participant.get("summonerName", ""),
            "teamEarlySurrendered": participant.get("teamEarlySurrendered", ""),
            "teamId": participant.get("teamId", ""),
            "teamPosition": participant.get("teamPosition", ""),
            "timeCCingOthers": participant.get("timeCCingOthers", ""),
            "timePlayed": participant.get("timePlayed", ""),
            "totalDamageDealt": participant.get("totalDamageDealt", ""),
            "totalDamageDealtToChampions": participant.get("totalDamageDealtToChampions", ""),
            "totalDamageShieldedOnTeammates": participant.get("totalDamageShieldedOnTeammates", ""),
            "totalDamageTaken": participant.get("totalDamageTaken", ""),
            "totalHeal": participant.get("totalHeal", ""),
            "totalHealsOnTeammates": participant.get("totalHealsOnTeammates", ""),
            "totalMinionsKilled": participant.get("totalMinionsKilled", ""),
            "totalTimeCCDealt": participant.get("totalTimeCCDealt", ""),
            "totalTimeSpentDead": participant.get("totalTimeSpentDead", ""),
            "totalUnitsHealed": participant.get("totalUnitsHealed", ""),
            "tripleKills": participant.get("tripleKills", ""),
            "trueDamageDealt": participant.get("trueDamageDealt", ""),
            "trueDamageDealtToChampions": participant.get("trueDamageDealtToChampions", ""),
            "trueDamageTaken": participant.get("trueDamageTaken", ""),
            "turretKills": participant.get("turretKills", ""),
            "turretTakedowns": participant.get("turretTakedowns", ""),
            "turretsLost": participant.get("turretsLost", ""),
            "unrealKills": participant.get("unrealKills", ""),
            "visionScore": participant.get("visionScore", ""),
            "visionWardsBoughtInGame": participant.get("visionWardsBoughtInGame", ""),
            "wardsKilled": participant.get("wardsKilled", ""),
            "wardsPlaced": participant.get("wardsPlaced", ""),
            "win": participant.get("win", ""),
            "perks_defense": participant.get("perks", {}).get("defense", ""),
            "perks_flex": participant.get("perks", {}).get("flex", ""),
            "perks_offense": participant.get("perks", {}).get("offense", ""),
            }

        participant_dto_list.append(values)
        
    return participant_dto_list

def get_participant_frames(match_timeline_dto):
    frames = match_timeline_dto.info.frames
    match_id = match_timeline_dto.metadata.match_id

    participant_frames_list = []

    for frame_number, frame in enumerate(frames):
        participant_frames = frame.participant_frames

        for participant_id, participant_frame in participant_frames.items():
            # Access attributes using dot notation
            participant_id = participant_frame.participant_id
            timestamp = frame.timestamp  # Assuming Frame class has a 'timestamp' attribute
            level = participant_frame.level
            current_gold = participant_frame.current_gold
            gold_per_second = participant_frame.gold_per_second
            total_gold = participant_frame.total_gold
            xp = participant_frame.xp
            minions_killed = participant_frame.minions_killed
            jungle_minions_killed = participant_frame.jungle_minions_killed
            time_enemy_spent_controlled = participant_frame.time_enemy_spent_controlled

            position_x = participant_frame.position["x"]
            position_y = participant_frame.position["y"]

            values = {
                "match_id": match_id,
                "frame_number": frame_number,
                "participant_id": participant_id,
                "timestamp": timestamp,
                "level": level,
                "current_gold": current_gold,
                "gold_per_second": gold_per_second,
                "total_gold": total_gold,
                "xp": xp,
                "minions_killed": minions_killed,
                "jungle_minions_killed": jungle_minions_killed,
                "time_enemy_spent_controlled": time_enemy_spent_controlled,
                "position_x": position_x,
                "position_y": position_y,
            }

            participant_frames_list.append(values)

    return participant_frames_list

def insert_participant_frames(match_timeline_dto):
    participant_frames_list = get_participant_frames(match_timeline_dto)
    # batch insert
    helper = SQLHelper()
    for pframes in participant_frames_list:
        helper.insert_dict("participant_frames", pframes)
