from postgres_helperfile import SQLHelper, add_df_to_table
from api_client import API_Client
import sys
import os
import json

import logging

logging.basicConfig(
    filename='app.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main(match_id):
    logging.info(f"Starting main process for match ID: {match_id}")
    api_client = API_Client()
    # get match_dto, match_timeline_dto
    match_dto = api_client.get_match_by_match_id(match_id)
    match_timeline_dto = api_client.get_match_timeline(match_id)

    # Save to cache
    save_to_cache(f"match_{match_id}.json", match_dto)
    save_to_cache(f"timeline_{match_id}.json", match_timeline_dto)

    # try to insert
    try:
        insert_match(match_dto, match_timeline_dto)
    except Exception as e:
        logging.error(f"Failed to insert match data for match ID {match_id}: {e}")
        print(f"Failed to insert match data: {e}")
        raise

    # Upon successful insertion, clean up cache
    cleanup_cache(match_id)

def cleanup_cache(match_id):
    cache_dir = "./cache"
    match_file = os.path.join(cache_dir, f"match_{match_id}.json")
    timeline_file = os.path.join(cache_dir, f"timeline_{match_id}.json")

    try:
        if os.path.exists(match_file):
            os.remove(match_file)
            logging.info(f"Deleted cache file: {match_file}")

        if os.path.exists(timeline_file):
            os.remove(timeline_file)
            logging.info(f"Deleted cache file: {timeline_file}")
    except Exception as e:
        logging.error(f"Failed to clean up cache for match ID {match_id}: {e}")


def save_to_cache(filename, data):
    """Save data to a file in the cache directory."""
    cache_dir = "./cache"  # Change to a relative path
    os.makedirs(cache_dir, exist_ok=True)  # Create the cache directory if it doesn't exist
    file_path = os.path.join(cache_dir, filename)
    with open(file_path, 'w') as file:
        json.dump(data, file)

def insert_match(match_dto, match_timeline_dto):
    logging.info(f"Inserting match data for match DTO and timeline DTO")
    add_df_to_table("match_metadata", get_match_metadata(match_dto))
    add_df_to_table("perk_style_selections", get_perk_style_selections(match_dto))
    add_df_to_table("participant_dto", get_participant_dto(match_dto))
    add_df_to_table("challenges", get_challenges(match_dto))
    add_df_to_table("participant_frames", get_participant_frames(match_timeline_dto))
    add_df_to_table("champion_stats", get_champion_stats(match_timeline_dto))
    add_df_to_table("match_events", get_match_events(match_timeline_dto))
    damage_received_list, damage_dealt_list = get_victim_damage(match_timeline_dto)
    add_df_to_table("victim_damage_dealt", damage_dealt_list)
    add_df_to_table("victim_damage_received", damage_received_list)
    add_df_to_table("damage_stats", get_damage_stats(match_timeline_dto))
    add_df_to_table("teams", get_teams(match_dto))
    add_df_to_table("bans", get_bans(match_dto))
    logging.info(f"Data insertion for match completed successfully")
    
def get_bans(match_dto):
    metadata = match_dto.get("metadata", {})
    match_id = metadata.get("match_id", "")
    teams = match_dto.get("info", {}).get("teams", [])

    # Prepare a list to hold all the values to be inserted
    all_values = []
    for team in teams:
        for ban in team.get("bans", []):
            # Append each set of values as a dictionary to the list
            ban_dict = {
                "match_id": match_id,
                "champion_id": ban.get("championId"),
                "pick_turn": ban.get("pickTurn"),
            }
            all_values.append(ban_dict)

    return all_values

def get_champion_stats(match_timeline_dto):
    frames = match_timeline_dto.get('info', {}).get('frames', [])
    match_id = match_timeline_dto.get('metadata', {}).get('match_id', '')

    values_list = []
    for frame_number, frame in enumerate(frames):
        for participant_id, participant_frame in frame.get('participant_frames', {}).items():
            champion_stats = participant_frame.get('champion_stats', {})
            values = {
                "match_id": match_id,
                "frame_number": frame_number,
                "participant_id": participant_id,
                "ability_haste": champion_stats.get("abilityHaste", 0),
                "ability_power": champion_stats.get("abilityPower", 0),
                "armor": champion_stats.get("armor", 0),
                "armor_pen": champion_stats.get("armorPen", 0),
                "armor_pen_percent": champion_stats.get("armorPenPercent", 0.0),
                "attack_damage": champion_stats.get("attackDamage", 0),
                "attack_speed": champion_stats.get("attackSpeed", 0.0),
                "bonus_armor_pen_percent": champion_stats.get("bonusArmorPenPercent", 0.0),
                "bonus_magic_pen_percent": champion_stats.get("bonusMagicPenPercent", 0.0),
                "cc_reduction": champion_stats.get("ccReduction", 0),
                "health": champion_stats.get("health", 0),
                "health_max": champion_stats.get("healthMax", 0),
                "health_regen": champion_stats.get("healthRegen", 0),
                "lifesteal": champion_stats.get("lifesteal", 0.0),
                "magic_pen": champion_stats.get("magicPen", 0),
                "magic_pen_percent": champion_stats.get("magicPenPercent", 0.0),
                "magic_resist": champion_stats.get("magicResist", 0),
                "movement_speed": champion_stats.get("movementSpeed", 0),
                "omnivamp": champion_stats.get("omnivamp", 0.0),
                "physical_vamp": champion_stats.get("physicalVamp", 0.0),
                "power": champion_stats.get("power", 0),
                "power_max": champion_stats.get("powerMax", 0),
                "power_regen": champion_stats.get("powerRegen", 0),
                "spell_vamp": champion_stats.get("spellVamp", 0.0),
            }

            values_list.append(values)

    return values_list


def get_match_metadata(match_dto):
    metadata = match_dto.get("metadata", {})
    info = match_dto.get("info", {})

    match_metadata_dict = {
        'data_version': metadata.get("dataVersion", ""),
        'match_id': metadata.get("matchId", ""),
        'game_creation': info.get("gameCreation", 0),
        'game_duration': info.get("gameDuration", 0),
        'game_end_timestamp': info.get("gameEndTimestamp", 0),
        'game_id': info.get("gameId", ""),
        'game_mode': info.get("gameMode", ""),
        'game_name': info.get("gameName", ""),
        'game_start_timestamp': info.get("gameStartTimestamp", 0),
        'game_type': info.get("gameType", ""),
        'game_version': info.get("gameVersion", ""),
        'map_id': info.get("mapId", 0),
        'platform_id': info.get("platformId", ""),
        'queue_id': info.get("queueId", 0),
        'tournament_code': info.get("tournamentCode", "")
    }

    return match_metadata_dict


def get_perk_style_selections(match_dto):
    participants = match_dto.get("info", {}).get("participants", [])
    match_id = match_dto.get("metadata", {}).get("matchId", "")

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
    metadata = match_dto.get("metadata", {})
    match_id = metadata.get("match_id", "")
    teams = match_dto.get("info", {}).get("teams", [])

    teams_list = []
    for team in teams:
        # Extracting objectives data
        objectives = team.get("objectives", {}).get("objectives", {})

        team_data = {
            'team_id': team.get("team_id", ""),
            'match_id': match_id,
            'baron_first': objectives.get('baron', {}).get('first', False),
            'baron_kills': objectives.get('baron', {}).get('kills', 0),
            'dragon_first': objectives.get('dragon', {}).get('first', False),
            'dragon_kills': objectives.get('dragon', {}).get('kills', 0),
            'champion_first': objectives.get('champion', {}).get('first', False),
            'champion_kills': objectives.get('champion', {}).get('kills', 0),
            'inhibitor_first': objectives.get('inhibitor', {}).get('first', False),
            'inhibitor_kills': objectives.get('inhibitor', {}).get('kills', 0),
            'rift_herald_first': objectives.get('riftHerald', {}).get('first', False),
            'rift_herald_kills': objectives.get('riftHerald', {}).get('kills', 0),
            'tower_first': objectives.get('tower', {}).get('first', False),
            'tower_kills': objectives.get('tower', {}).get('kills', 0),
            'win': team.get('win', "")
        }

        teams_list.append(team_data)

    return teams_list


def get_damage_stats(match_timeline_dto):
    frames = match_timeline_dto.get("info", {}).get("frames", [])
    match_id = match_timeline_dto.get("metadata", {}).get("matchId", "")

    damage_stats_list = []
    for frame_number, frame in enumerate(frames):
        participant_frames = frame.get("participantFrames", {}).values()  # Assuming participantFrames is a dict

        for participant_frame in participant_frames:
            participant_id = participant_frame.get("participantId")
            damage_stats = participant_frame.get("damageStats", {})

            damage_stat_dict = {
                'match_id': match_id,
                'frame_number': frame_number,
                'participant_id': participant_id,
                'magic_damage_done': damage_stats.get("magicDamageDone", 0),
                'magic_damage_done_to_champions': damage_stats.get("magicDamageDoneToChampions", 0),
                'magic_damage_taken': damage_stats.get("magicDamageTaken", 0),
                'physical_damage_done': damage_stats.get("physicalDamageDone", 0),
                'physical_damage_done_to_champions': damage_stats.get("physicalDamageDoneToChampions", 0),
                'physical_damage_taken': damage_stats.get("physicalDamageTaken", 0),
                'total_damage_done': damage_stats.get("totalDamageDone", 0),
                'total_damage_done_to_champions': damage_stats.get("totalDamageDoneToChampions", 0),
                'total_damage_taken': damage_stats.get("totalDamageTaken", 0),
                'true_damage_done': damage_stats.get("trueDamageDone", 0),
                'true_damage_done_to_champions': damage_stats.get("trueDamageDoneToChampions", 0),
                'true_damage_taken': damage_stats.get("trueDamageTaken", 0)
            }

            damage_stats_list.append(damage_stat_dict)

    return damage_stats_list


def get_victim_damage(match_timeline_dto):
    frames = match_timeline_dto.get("info", {}).get("frames", [])
    match_id = match_timeline_dto.get("metadata", {}).get("matchId", "")

    damage_received_list = []
    damage_dealt_list = []

    for frame_number, frame in enumerate(frames):
        for event_number, event in enumerate(frame.get("events", [])):
            if event.get("type") == "CHAMPION_KILL":
                for damage_received in event.get("victimDamageReceived", []):
                    received_values = {
                        "match_id": match_id,
                        "participant_id": damage_received.get("participantId"),
                        "basic": damage_received.get("basic"),
                        "magic_damage": damage_received.get("magicDamage"),
                        "physical_damage": damage_received.get("physicalDamage"),
                        "name": damage_received.get("name"),
                        "spell_name": damage_received.get("spellName", ""),
                        "spell_slot": damage_received.get("spellSlot", 0),
                        "true_damage": damage_received.get("trueDamage"),
                        "damage_type": damage_received.get("type"),
                    }

                    damage_received_list.append(received_values)

                for damage_dealt in event.get("victimDamageDealt", []):
                    dealt_values = {
                        "match_id": match_id,
                        "participant_id": damage_dealt.get("participantId"),
                        "basic": damage_dealt.get("basic"),
                        "magic_damage": damage_dealt.get("magicDamage"),
                        "physical_damage": damage_dealt.get("physicalDamage"),
                        "name": damage_dealt.get("name"),
                        "spell_name": damage_dealt.get("spellName", ""),
                        "spell_slot": damage_dealt.get("spellSlot", 0),
                        "true_damage": damage_dealt.get("trueDamage"),
                        "damage_type": damage_dealt.get("type"),
                    }

                    damage_dealt_list.append(dealt_values)

    return damage_received_list, damage_dealt_list

def get_challenges(match_dto):
    challenges_list = []

    participants = match_dto.get("info").get("participants")
    for participant in participants:
        challenges = participant.get("challenges")
        
        values = {
            "match_id": match_dto.get("metadata").get("matchId"),
            "participant_id": participant.get("participantId"),
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
    frames = match_timeline_dto.get('info', {}).get('frames', [])
    match_id = match_timeline_dto.get('metadata', {}).get('matchId', None)

    events_list = []
    for frame_number, frame in enumerate(frames):
        for event_number, event in enumerate(frame.get('events', [])):
            events_dict = {
                'match_id': match_id,
                'frame_number': frame_number,
                'event_number': event_number,
                'real_timestamp': event.get("realTimestamp", None),
                'timestamp': event.get("timestamp", None),
                'type': event.get("type", None),
                'item_id': event.get("itemId", None),
                'participant_id': event.get("participantId", None),
                'level_up_type': event.get("levelUpType", ""),
                'skill_slot': event.get("skillSlot", None),
                'creator_id': event.get("creatorId", None),
                'ward_type': event.get("wardType", ""),
                'level': event.get("level", None),
                'bounty': event.get("bounty", None),
                'kill_streak_length': event.get("killStreakLength", None),
                'killer_id': event.get("killerId", None),
                'position_x': event.get("position", {}).get("x", None),
                'position_y': event.get("position", {}).get("y", None),
                'victim_id': event.get("victimId", None),
                'kill_type': event.get("killType", ""),
                'lane_type': event.get("laneType", ""),
                'team_id': event.get("teamId", None),
                'multi_kill_length': event.get("multiKillLength", None),
                'killer_team_id': event.get("killerTeamId", None),
                'monster_type': event.get("monsterType", ""),
                'monster_sub_type': event.get("monsterSubType", ""),
                'building_type': event.get("buildingType", ""),
                'tower_type': event.get("towerType", ""),
                'after_id': event.get("afterId", None),
                'before_id': event.get("beforeId", None),
                'gold_gain': event.get("goldGain", None),
                'game_id': event.get("gameId", None),
                'winning_team': event.get("winningTeam", None),
                'transform_type': event.get("transformType", ""),
                'name': event.get("name", ""),
                'shutdown_bounty': event.get("shutdownBounty", None),
                'actual_start_time': event.get("actualStartTime", None)
            }

            events_list.append(events_dict)

    return events_list

def get_participant_dto(match_dto):
    participants = match_dto.get("info").get("participants")
    match_id = match_dto.get("metadata").get("matchId")

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
    frames = match_timeline_dto.get('info', {}).get('frames', [])
    match_id = match_timeline_dto.get('metadata', {}).get('match_id', None)

    participant_frames_list = []

    for frame_number, frame in enumerate(frames):
        participant_frames = frame.get('participant_frames', {})

        for participant_id, participant_frame in participant_frames.items():
            # Access attributes using .get method
            participant_id = participant_frame.get('participant_id', None)
            timestamp = frame.get('timestamp', None)  # Assuming Frame class has a 'timestamp' attribute
            level = participant_frame.get('level', None)
            current_gold = participant_frame.get('current_gold', None)
            gold_per_second = participant_frame.get('gold_per_second', None)
            total_gold = participant_frame.get('total_gold', None)
            xp = participant_frame.get('xp', None)
            minions_killed = participant_frame.get('minions_killed', None)
            jungle_minions_killed = participant_frame.get('jungle_minions_killed', None)
            time_enemy_spent_controlled = participant_frame.get('time_enemy_spent_controlled', None)


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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <match_id>")
        sys.exit(1)

    match_id = sys.argv[1]
    main(match_id)