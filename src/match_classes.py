
def camel_to_snake(name):
    import re
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class MatchTimelineDto:
    def __init__(self, timeline_json):
        metadata_json = timeline_json["metadata"]
        info_json = timeline_json["info"]

        self.metadata = self.Metadata(metadata_json)
        self.info = self.Info(info_json)
        self.participants = self.metadata.participants

    class Metadata:
        def __init__(self, metadata_json):
            self.data_version = metadata_json["dataVersion"]
            self.match_id = metadata_json["matchId"]
            self.participants = metadata_json["participants"]

    class Info:
        def __init__(self, info_json):
            self.frame_interval = info_json["frameInterval"]
            self.frames = [self.Frame(frame_json) for frame_json in info_json["frames"]]
            self.game_id = info_json["gameId"]
            self.participants = info_json["participants"]


        class Frame:
            def __init__(self, frame_json):
                self.events = [self.Event(event) for event in frame_json["events"]]
                self.participant_frames = {
                    frame_number: self.ParticipantFrame(frame)
                    for frame_number, frame in frame_json["participantFrames"].items()
                }
                self.timestamp = frame_json["timestamp"]


            class Event:
                def __init__(self, event_json):
                    self.real_timestamp = event_json.get("realTimestamp", None)
                    self.timestamp = event_json.get("timestamp", None)
                    self.type_ = event_json.get("type", None)
                    self.item_id = event_json.get("itemId", None)
                    self.participant_id = event_json.get("participantId", None)
                    self.level_up_type = event_json.get("levelUpType", None)
                    self.skill_slot = event_json.get("skillSlot", None)
                    self.creator_id = event_json.get("creatorId", None)
                    self.ward_type = event_json.get("wardType", None)
                    self.level = event_json.get("level", None)
                    self.assisting_participant_ids = event_json.get("assistingParticipantIds", None)
                    self.bounty = event_json.get("bounty", None)
                    self.kill_streak_length = event_json.get("killStreakLength", None)
                    self.killer_id = event_json.get("killerId", None)
                    self.position = event_json.get("position", None)
                    self.victim_damage_dealt = event_json.get("victimDamageDealt", None)
                    self.victim_damage_received = event_json.get("victimDamageReceived", None)
                    self.victim_id = event_json.get("victimId", None)
                    self.kill_type = event_json.get("killType", None)
                    self.lane_type = event_json.get("laneType", None)
                    self.team_id = event_json.get("teamId", None)
                    self.multi_kill_length = event_json.get("multiKillLength", None)
                    self.killer_team_id = event_json.get("killerTeamId", None)
                    self.monster_type = event_json.get("monsterType", None)
                    self.monster_sub_type = event_json.get("monsterSubType", None)
                    self.building_type = event_json.get("buildingType", None)
                    self.tower_type = event_json.get("towerType", None)
                    self.after_id = event_json.get("afterId", None)
                    self.before_id = event_json.get("beforeId", None)
                    self.gold_gain = event_json.get("goldGain", None)
                    self.game_id = event_json.get("gameId", None)
                    self.winning_team = event_json.get("winningTeam", None)
                    self.transform_type = event_json.get("transformType", None)
                    self.name = event_json.get("name", None)
                    self.shutdown_bounty = event_json.get("shutdownBounty", None)
                    self.actual_start_time = event_json.get("actualStartTime", None)



            class ParticipantFrame:
                def __init__(self, p_frame_json):
                    self.champion_stats = self.ChampionStats(
                        p_frame_json["championStats"]
                    )
                    self.damage_stats = self.DamageStats(p_frame_json["damageStats"])
                    self.current_gold = p_frame_json["currentGold"]
                    self.gold_per_second = p_frame_json["goldPerSecond"]
                    self.jungle_minions_killed = p_frame_json["jungleMinionsKilled"]
                    self.level = p_frame_json["level"]
                    self.minions_killed = p_frame_json["minionsKilled"]
                    self.participant_id = p_frame_json["participantId"]
                    self.position = p_frame_json["position"]
                    self.time_enemy_spent_controlled = p_frame_json[
                        "timeEnemySpentControlled"
                    ]
                    self.total_gold = p_frame_json["totalGold"]
                    self.xp = p_frame_json["xp"]


                class ChampionStats:
                    def __init__(self, champ_stats_json):
                        self.ability_haste = champ_stats_json["abilityHaste"]
                        self.ability_power = champ_stats_json["abilityPower"]
                        self.armor = champ_stats_json["armor"]
                        self.armor_pen = champ_stats_json["armorPen"]
                        self.armor_pen_percent = champ_stats_json["armorPenPercent"]
                        self.attack_damage = champ_stats_json["attackDamage"]
                        self.attack_speed = champ_stats_json["attackSpeed"]
                        self.bonus_armor_pen_percent = champ_stats_json["bonusArmorPenPercent"]
                        self.bonus_magic_pen_percent = champ_stats_json["bonusMagicPenPercent"]
                        self.cc_reduction = champ_stats_json["ccReduction"]
                        self.cooldown_reduction = champ_stats_json["cooldownReduction"]
                        self.health = champ_stats_json["health"]
                        self.health_max = champ_stats_json["healthMax"]
                        self.health_regen = champ_stats_json["healthRegen"]
                        self.lifesteal = champ_stats_json["lifesteal"]
                        self.magic_pen = champ_stats_json["magicPen"]
                        self.magic_pen_percent = champ_stats_json["magicPenPercent"]
                        self.magic_resist = champ_stats_json["magicResist"]
                        self.movement_speed = champ_stats_json["movementSpeed"]
                        self.omnivamp = champ_stats_json["omnivamp"]
                        self.physical_vamp = champ_stats_json["physicalVamp"]
                        self.power = champ_stats_json["power"]
                        self.power_max = champ_stats_json["powerMax"]
                        self.power_regen = champ_stats_json["powerRegen"]
                        self.spell_vamp = champ_stats_json["spellVamp"]



                class DamageStats:
                    def __init__(self, damage_stats_json):
                        self.magic_damage_done = damage_stats_json["magicDamageDone"]
                        self.magic_damage_done_to_champions = damage_stats_json["magicDamageDoneToChampions"]
                        self.magic_damage_taken = damage_stats_json["magicDamageTaken"]
                        self.physical_damage_done = damage_stats_json["physicalDamageDone"]
                        self.physical_damage_done_to_champions = damage_stats_json["physicalDamageDoneToChampions"]
                        self.physical_damage_taken = damage_stats_json["physicalDamageTaken"]
                        self.total_damage_done = damage_stats_json["totalDamageDone"]
                        self.total_damage_done_to_champions = damage_stats_json["totalDamageDoneToChampions"]
                        self.total_damage_taken = damage_stats_json["totalDamageTaken"]
                        self.true_damage_done = damage_stats_json["trueDamageDone"]
                        self.true_damage_done_to_champions = damage_stats_json["trueDamageDoneToChampions"]
                        self.true_damage_taken = damage_stats_json["trueDamageTaken"]


class MatchDto:
    def __init__(self, json):
        print("MatchDto called")
        self.metadata = self.MetadataDto(json["metadata"])
        self.match_id = self.metadata.match_id
        self.info = self.InfoDto(json["info"])


    class MetadataDto:
        def __init__(self, metadata):
            self.data_version = metadata["dataVersion"]
            self.match_id = metadata["matchId"]
            self.participants = metadata["participants"]

    class InfoDto:
        def __init__(self, info):
            self.game_creation = info["gameCreation"]
            self.game_duration = info["gameDuration"]
            self.game_end_timestamp = info["gameEndTimestamp"]
            self.game_id = info["gameId"]
            self.game_mode = info["gameMode"]
            self.game_name = info["gameName"]
            self.game_start_timestamp = info["gameStartTimestamp"]
            self.game_type = info["gameType"]
            self.game_version = info["gameVersion"]
            self.map_id = info["mapId"]
            self.participants = [self.ParticipantDto(**p) for p in info["participants"]]
            self.platform_id = info["platformId"]
            self.queue_id = info["queueId"]
            self.teams = [self.TeamDto(t) for t in info["teams"]]
            self.tournament_code = info.get("tournamentCode", "")


        class ParticipantDto:
            """
            Represents detailed information about an individual participant in the game.
            Attributes:
                Various attributes representing participant's performance in the game, such as
                participantId, championId, championName, teamId, kills, deaths, assists, totalDamageDealt,
                goldEarned, and many others.
            """

            def __init__(self, **kwargs):
                for key, value in kwargs.items():
                    if key == "perks":
                        setattr(self, key, self.PerksDto(value))
                    else:
                        setattr(self, key, value)

            class PerksDto:
                def __init__(self, data):
                    self.stat_perks = self.PerkStatsDto(data["statPerks"])
                    self.styles = [self.PerkStyleDto(style) for style in data["styles"]]

                class PerkStatsDto:
                    def __init__(self, perk_stats_json):
                        self.defense = perk_stats_json["defense"]
                        self.flex = perk_stats_json["flex"]
                        self.offense = perk_stats_json["offense"]

                class PerkStyleSelectionDto:
                    def __init__(self, perk_selection_json):
                        self.perk = perk_selection_json["perk"]
                        self.var1 = perk_selection_json["var1"]
                        self.var2 = perk_selection_json["var2"]
                        self.var3 = perk_selection_json["var3"]

                class PerkStyleDto:
                    def __init__(self, perk_style_json):
                        self.description = perk_style_json["description"]
                        self.selections = perk_style_json["selections"]
                        self.style = perk_style_json["style"]

        class TeamDto:
            def __init__(self, data):
                self.bans = [self.BanDto(ban) for ban in data["bans"]]
                self.objectives = self.ObjectivesDto(data["objectives"])
                self.team_id = data["teamId"]
                self.win = data["win"]

            class ObjectivesDto:
                def __init__(self, data):
                    self.objectives = {}  # Dictionary to store ObjectiveDto instances
                    for objective_name in [
                        "champion",
                        "dragon",
                        "inhibitor",
                        "riftHerald",
                        "tower",
                        "baron",
                    ]:
                        if objective_name in data:
                            snake_case_objective_name = camel_to_snake(objective_name)
                            self.objectives[snake_case_objective_name] = self.ObjectiveDto(
                                data[objective_name]
                            )


                class ObjectiveDto:
                    def __init__(self, objective_json):
                        self.first = objective_json.get(
                            "first", False
                        )  # Default to False if not present
                        self.kills = objective_json.get(
                            "kills", 0
                        )  # Default to 0 if not present

            class BanDto:
                def __init__(self, ban_json):
                    self.champion_id = ban_json["championId"]
                    self.pick_turn = ban_json["pickTurn"]

class SummonerDto:
    # Store summoner data as attributes
    def __init__(self, summoner_dto_json):
        # Check if summoner_dto_json is a dictionary
        if not isinstance(summoner_dto_json, dict):
            raise ValueError("The provided input is not a valid JSON object.")

        # Proceed if it's a valid dictionary
        self.account_id = summoner_dto_json.get("accountId")
        self.profile_icon_id = summoner_dto_json.get("profileIconId")
        self.revision_date = summoner_dto_json.get("revisionDate")
        self.name = summoner_dto_json.get("name")
        self.id = summoner_dto_json.get("id")
        self.puuid = summoner_dto_json.get("puuid")
        self.summoner_level = summoner_dto_json.get("summonerLevel")

