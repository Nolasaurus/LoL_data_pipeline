from postgres_helperfile import execute_batch_query, execute_query, insert_dict

def insert_match(match_dto, match_timeline_dto):
    # Store function references in a list
    get_functions = [
        (get_bans, match_dto),
        (insert_challenges, match_dto),
        (get_champion_stats, match_timeline_dto),
        (insert_damage_stats, match_timeline_dto),
        (insert_match_metadata, match_dto),
        (insert_match_events, match_timeline_dto),
        (insert_participant_dto, match_dto),
        (insert_participant_frames, match_timeline_dto),
        (insert_perk_style_selections, match_dto),
        (insert_teams, match_dto),
        (insert_victim_damage_tables, match_timeline_dto)
    ]

    for get_function, dto in get_functions:
        try:
            add_dict_to_table(get_function(dto))
        except Exception as e:
            print(f"Error occurred during insertion: {e}")


def get_bans(match_dto):
    match_id = match_dto['info']['gameId']
    teams = match_dto['info']['teams']
    
    # Prepare a list to hold all the values to be inserted
    all_values = []
    for team in teams:
        for ban in team['bans']:
            # Append each set of values as a tuple to the list
            ban_dict = {
                'match_id':match_id,
                'champion_id': ban['championId'],
                'pick_turn': ban['pickTurn']
                }
            all_values.append(ban_dict)

    return all_values


def get_champion_stats(match_timeline_dto):
    frames = match_timeline_dto.info.frames
    match_id = match_timeline_dto.metadata.matchId

    values_list = []
    for frame_number, frame in enumerate(frames):
        for participant_id, participant_frame in frame.participantFrames.items():
            champion_stats = participant_frame.championStats if participant_frame.championStats else {}
            values = {
                'match_id': match_id,
                'frame_number': frame_number,
                'participant_id': participant_id,
                'ability_haste': getattr(champion_stats, 'abilityHaste', 0),
                'ability_power': getattr(champion_stats, 'abilityPower', 0),
                'armor': getattr(champion_stats, 'armor', 0),
                'armor_pen': getattr(champion_stats, 'armorPen', 0),
                'armor_pen_percent': getattr(champion_stats, 'armorPenPercent', 0.0),
                'attack_damage': getattr(champion_stats, 'attackDamage', 0),
                'attack_speed': getattr(champion_stats, 'attackSpeed', 0.0),
                'bonus_armor_pen_percent': getattr(champion_stats, 'bonusArmorPenPercent', 0.0),
                'bonus_magic_pen_percent': getattr(champion_stats, 'bonusMagicPenPercent', 0.0),
                'cc_reduction': getattr(champion_stats, 'ccReduction', 0),
                'health': getattr(champion_stats, 'health', 0),
                'health_max': getattr(champion_stats, 'healthMax', 0),
                'health_regen': getattr(champion_stats, 'healthRegen', 0),
                'lifesteal': getattr(champion_stats, 'lifesteal', 0.0),
                'magic_pen': getattr(champion_stats, 'magicPen', 0),
                'magic_pen_percent': getattr(champion_stats, 'magicPenPercent', 0.0),
                'magic_resist': getattr(champion_stats, 'magicResist', 0),
                'movement_speed': getattr(champion_stats, 'movementSpeed', 0),
                'omnivamp': getattr(champion_stats, 'omnivamp', 0.0),
                'physical_vamp': getattr(champion_stats, 'physicalVamp', 0.0),
                'power': getattr(champion_stats, 'power', 0),
                'power_max': getattr(champion_stats, 'powerMax', 0),
                'power_regen': getattr(champion_stats, 'powerRegen', 0),
                'spell_vamp': getattr(champion_stats, 'spellVamp', 0.0)
            }

            values_list.append(values)

    return values_list



def insert_match_metadata(match_dto):
    # Assuming match_dto is a dictionary-like object
    metadata = match_dto['metadata']
    info = match_dto['info']

    # Extracting data from match_dto
    data_version = metadata['dataVersion']
    match_id = metadata['matchId']
    game_creation = info['gameCreation']
    game_duration = info['gameDuration']
    game_end_timestamp = info['gameEndTimestamp']
    game_id = info['gameId']
    game_mode = info['gameMode']
    game_name = info['gameName']
    game_start_timestamp = info['gameStartTimestamp']
    game_type = info['gameType']
    game_version = info['gameVersion']
    map_id = info['mapId']
    platform_id = info['platformId']
    queue_id = info['queueId']
    tournament_code = info.get('tournamentCode', '')  # Using get() in case tournamentCode might not be present

    # SQL INSERT statement
    query = """
        INSERT INTO match_metadata 
        (data_version, match_id, game_creation, game_duration, game_end_timestamp, game_id, game_mode, game_name, game_start_timestamp, game_type, game_version, map_id, platform_id, queue_id, tournament_code) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (data_version, match_id, game_creation, game_duration, game_end_timestamp, game_id, game_mode, game_name, game_start_timestamp, game_type, game_version, map_id, platform_id, queue_id, tournament_code)

    # Assuming execute_query is a function that executes your SQL command
    execute_query(query, values)


def insert_perk_style_selections(match_dto):
    participants = match_dto['info']['participants']
    match_id = match_dto['metadata']['matchId']

    for participant in participants:
        participant_id = participant['participantId']
        for style_index, style in enumerate(participant['perks']['styles']):
            for selection_index, selection in enumerate(style['selections']):
                perk = selection['perk']
                var1 = selection['var1']
                var2 = selection['var2']
                var3 = selection['var3']

                # SQL INSERT statement
                query = """
                    INSERT INTO perk_style_selections 
                    (match_id, participant_id, style_index, selection_index, perk, var1, var2, var3) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                values = (match_id, participant_id, style_index, selection_index, perk, var1, var2, var3)

                # Execute the query
                execute_query(query, values)



def insert_teams(match_dto):
    # Extracting match_id and teams information
    match_id = match_dto['metadata']['matchId']
    teams = match_dto['info']['teams']

    for team in teams:
        # Extracting team data
        team_id = team['teamId']
        win = team['win']
        baron_first = team['objectives']['baron']['first']
        baron_kills = team['objectives']['baron']['kills']
        dragon_first = team['objectives']['dragon']['first']
        dragon_kills = team['objectives']['dragon']['kills']
        champion_first = team['objectives']['champion']['first']  
        champion_kills = team['objectives']['champion']['kills']
        inhibitor_first = team['objectives']['inhibitor']['first']
        inhibitor_kills = team['objectives']['inhibitor']['kills']
        rift_herald_first = team['objectives']['riftHerald']['first']
        rift_herald_kills = team['objectives']['riftHerald']['kills']
        tower_first = team['objectives']['tower']['first']
        tower_kills = team['objectives']['tower']['kills']

        # SQL INSERT statement
        query = """
            INSERT INTO teams 
            (team_id, match_id, baron_first, baron_kills, champion_first, champion_kills, dragon_first, dragon_kills, inhibitor_first, inhibitor_kills, rift_herald_first, rift_herald_kills, tower_first, tower_kills, win) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (team_id, match_id, baron_first, baron_kills, champion_first, champion_kills, dragon_first, dragon_kills, inhibitor_first, inhibitor_kills, rift_herald_first, rift_herald_kills, tower_first, tower_kills, win)

        # Execute the query
        execute_query(query, values)


def insert_damage_stats(match_timeline_dto):
    frames = match_timeline_dto['info']['frames']
    match_id = match_timeline_dto['metadata']['matchId']

    for frame_number, frame in enumerate(frames):
        participant_frames = frame['participantFrames'].values()  # Assuming participantFrames is a dict

        for participant_frame in participant_frames:
            participant_id = participant_frame['participantId']
            damage_stats = participant_frame['damageStats']

            # Extracting all required fields
            magic_damage_done = damage_stats['magicDamageDone']
            magic_damage_done_to_champions = damage_stats['magicDamageDoneToChampions']
            magic_damage_taken = damage_stats['magicDamageTaken']
            physical_damage_done = damage_stats['physicalDamageDone']
            physical_damage_done_to_champions = damage_stats['physicalDamageDoneToChampions']
            physical_damage_taken = damage_stats['physicalDamageTaken']
            total_damage_done = damage_stats['totalDamageDone']
            total_damage_done_to_champions = damage_stats['totalDamageDoneToChampions']
            total_damage_taken = damage_stats['totalDamageTaken']
            true_damage_done = damage_stats['trueDamageDone']
            true_damage_done_to_champions = damage_stats['trueDamageDoneToChampions']
            true_damage_taken = damage_stats['trueDamageTaken']

            # SQL INSERT statement
            query = """
                INSERT INTO damage_stats 
                (match_id, frame_number, participant_id, magic_damage_done, magic_damage_done_to_champions, magic_damage_taken, physical_damage_done, physical_damage_done_to_champions, physical_damage_taken, total_damage_done, total_damage_done_to_champions, total_damage_taken, true_damage_done, true_damage_done_to_champions, true_damage_taken) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (match_id, frame_number, participant_id, magic_damage_done, magic_damage_done_to_champions, magic_damage_taken, physical_damage_done, physical_damage_done_to_champions, physical_damage_taken, total_damage_done, total_damage_done_to_champions, total_damage_taken, true_damage_done, true_damage_done_to_champions, true_damage_taken)

            # Execute the query
            execute_query(query, values)



def insert_victim_damage_tables(match_timeline_dto):
    frames = match_timeline_dto['info']['frames']
    match_id = match_timeline_dto['metadata']['matchId']

    for frame_number, frame in enumerate(frames):
        for event_number, event in enumerate(frame['events']):
            if event['type'] == "CHAMPION_KILL":
                for damage_number, damage_received in enumerate(event['victimDamageReceived']):
                    participant_id = damage_received['participantId']
                    basic = damage_received['basic']
                    magic_damage = damage_received['magicDamage']
                    physical_damage = damage_received['physicalDamage']
                    name = damage_received['name']
                    spell_name = damage_received.get('spellName', '')  # using get() in case spellName is not present
                    spell_slot = damage_received.get('spellSlot', 0)  # defaulting to 0 if not present
                    true_damage = damage_received['trueDamage']
                    damage_type = damage_received['type']

                    # SQL INSERT statement
                    query = """
                        INSERT INTO victim_damage_received 
                        (match_id, frame_number, event_number, damage_number, participant_id, basic, magic_damage, physical_damage, name, spell_name, spell_slot, true_damage, type) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                    values = (match_id, frame_number, event_number, damage_number, participant_id, basic, magic_damage, physical_damage, name, spell_name, spell_slot, true_damage, damage_type)

                    # Execute the query
                    execute_query(query, values)

                if 'victimDamageDealt' in event:
                    for damage_number, damage_received in enumerate(event['victimDamageDealt']):
                        participant_id = damage_received['participantId']
                        basic = damage_received['basic']
                        magic_damage = damage_received['magicDamage']
                        physical_damage = damage_received['physicalDamage']
                        name = damage_received['name']
                        spell_name = damage_received.get('spellName', '')  # using get() in case spellName is not present
                        spell_slot = damage_received.get('spellSlot', 0)  # defaulting to 0 if not present
                        true_damage = damage_received['trueDamage']
                        damage_type = damage_received['type']

                        # SQL INSERT statement
                        query = """
                            INSERT INTO victim_damage_received 
                            (match_id, frame_number, event_number, damage_number, participant_id, basic, magic_damage, physical_damage, name, spell_name, spell_slot, true_damage, type) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        values = (match_id, frame_number, event_number, damage_number, participant_id, basic, magic_damage, physical_damage, name, spell_name, spell_slot, true_damage, damage_type)

                        # Execute the query
                        execute_query(query, values)


def insert_challenges(match_dto):
    participants = match_dto['info']['participants']
    match_id = match_dto['metadata']['matchId']

    for participant in participants:
        participant_id = participant['participantId']
        challenges = participant['challenges']

        # SQL INSERT statement

        # SQL INSERT statement
        query = """
            INSERT INTO challenges 
            (match_id, participant_id, assist_streak_count, ability_uses, aces_before_15_minutes, allied_jungle_monster_kills, baron_takedowns, blast_cone_opposite_opponent_count, bounty_gold, buffs_stolen, complete_support_quest_in_time, control_wards_placed, damage_per_minute, damage_taken_on_team_percentage, danced_with_rift_herald, deaths_by_enemy_champs, dodge_skill_shots_small_window, double_aces, dragon_takedowns, early_laning_phase_gold_exp_advantage, effective_heal_and_shielding, elder_dragon_kills_with_opposing_soul, elder_dragon_multikills, enemy_champion_immobilizations, enemy_jungle_monster_kills, epic_monster_kills_near_enemy_jungler, epic_monster_kills_within_30_seconds_of_spawn, epic_monster_steals, epic_monster_stolen_without_smite, first_turret_killed, flawless_aces, full_team_takedown, game_length, get_takedowns_in_all_lanes_early_jungle_as_laner, gold_per_minute, had_open_nexus, immobilize_and_kill_with_ally, initial_buff_count, initial_crab_count, jungle_cs_before_10_minutes, jungler_takedowns_near_damaged_epic_monster, k_turrets_destroyed_before_plates_fall, kda, kill_after_hidden_with_ally, kill_participation, killed_champ_took_full_team_damage_survived, killing_sprees, kills_near_enemy_turret, kills_on_other_lanes_early_jungle_as_laner, kills_on_recently_healed_by_aram_pack, kills_under_own_turret, kills_with_help_from_epic_monster, knock_enemy_into_team_and_kill, land_skill_shots_early_game, lane_minions_first_10_minutes, laning_phase_gold_exp_advantage, legendary_count, lost_an_inhibitor, max_cs_advantage_on_lane_opponent, max_kill_deficit, max_level_lead_lane_opponent, mejais_full_stack_in_time, more_enemy_jungle_than_opponent, multi_kill_one_spell, multi_turret_rift_herald_count, multikills, multikills_after_aggressive_flash, mythic_item_used, outer_turret_executes_before_10_minutes, outnumbered_kills, outnumbered_nexus_kill, perfect_dragon_souls_taken, perfect_game, pick_kill_with_ally, poro_explosions, quick_cleanse, quick_first_turret, quick_solo_kills, rift_herald_takedowns, save_ally_from_death, scuttle_crab_kills, skillshots_dodged, skillshots_hit, snowballs_hit, solo_baron_kills, solo_kills, stealth_wards_placed, survived_single_digit_hp_count, survived_three_immobilizes_in_fight, takedown_on_first_turret, takedowns, takedowns_after_gaining_level_advantage, takedowns_before_jungle_minion_spawn, takedowns_first_x_minutes, takedowns_in_alcove, takedowns_in_enemy_fountain, team_baron_kills, team_damage_percentage, team_elder_dragon_kills, team_rift_herald_kills, took_large_damage_survived, turret_plates_taken, turret_takedowns, turrets_taken_with_rift_herald, twenty_minions_in_3_seconds_count, two_wards_one_sweeper_count, unseen_recalls, vision_score_advantage_lane_opponent, vision_score_per_minute, ward_takedowns, ward_takedowns_before_20m, wards_guarded)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            match_id,
            participant_id,
            challenges.get('assistStreakCount', 0),
            challenges.get('abilityUses', 0),
            challenges.get('acesBefore15Minutes', 0),
            challenges.get('alliedJungleMonsterKills', 0),
            challenges.get('baronTakedowns', 0),
            challenges.get('blastConeOppositeOpponentCount', 0),
            challenges.get('bountyGold', 0),
            challenges.get('buffsStolen', 0),
            challenges.get('completeSupportQuestInTime', 0),
            challenges.get('controlWardsPlaced', 0),
            challenges.get('damagePerMinute', 0.0),
            challenges.get('damageTakenOnTeamPercentage', 0.0),
            challenges.get('dancedWithRiftHerald', 0),
            challenges.get('deathsByEnemyChamps', 0),
            challenges.get('dodgeSkillShotsSmallWindow', 0),
            challenges.get('doubleAces', 0),
            challenges.get('dragonTakedowns', 0),
            challenges.get('earlyLaningPhaseGoldExpAdvantage', 0.0),
            challenges.get('effectiveHealAndShielding', 0),
            challenges.get('elderDragonKillsWithOpposingSoul', 0),
            challenges.get('elderDragonMultikills', 0),
            challenges.get('enemyChampionImmobilizations', 0),
            challenges.get('enemyJungleMonsterKills', 0),
            challenges.get('epicMonsterKillsNearEnemyJungler', 0),
            challenges.get('epicMonsterKillsWithin30SecondsOfSpawn', 0),
            challenges.get('epicMonsterSteals', 0),
            challenges.get('epicMonsterStolenWithoutSmite', 0),
            challenges.get('firstTurretKilled', 0),
            challenges.get('flawlessAces', 0),
            challenges.get('fullTeamTakedown', 0),
            challenges.get('gameLength', 0.0),
            challenges.get('getTakedownsInAllLanesEarlyJungleAsLaner', 0),
            challenges.get('goldPerMinute', 0.0),
            challenges.get('hadOpenNexus', 0),
            challenges.get('immobilizeAndKillWithAlly', 0),
            challenges.get('initialBuffCount', 0),
            challenges.get('initialCrabCount', 0),
            challenges.get('jungleCsBefore10Minutes', 0),
            challenges.get('junglerTakedownsNearDamagedEpicMonster', 0),
            challenges.get('kTurretsDestroyedBeforePlatesFall', 0),
            challenges.get('kda', 0.0),
            challenges.get('killAfterHiddenWithAlly', 0),
            challenges.get('killParticipation', 0.0),
            challenges.get('killedChampTookFullTeamDamageSurvived', 0),
            challenges.get('killingSprees', 0),
            challenges.get('killsNearEnemyTurret', 0),
            challenges.get('killsOnOtherLanesEarlyJungleAsLaner', 0),
            challenges.get('killsOnRecentlyHealedByAramPack', 0),
            challenges.get('killsUnderOwnTurret', 0),
            challenges.get('killsWithHelpFromEpicMonster', 0),
            challenges.get('knockEnemyIntoTeamAndKill', 0),
            challenges.get('landSkillShotsEarlyGame', 0),
            challenges.get('laneMinionsFirst10Minutes', 0),
            challenges.get('laningPhaseGoldExpAdvantage', 0.0),
            challenges.get('legendaryCount', 0),
            challenges.get('lostAnInhibitor', 0),
            challenges.get('maxCsAdvantageOnLaneOpponent', 0),
            challenges.get('maxKillDeficit', 0),
            challenges.get('maxLevelLeadLaneOpponent', 0),
            challenges.get('mejaisFullStackInTime', 0),
            challenges.get('moreEnemyJungleThanOpponent', 0),
            challenges.get('multiKillOneSpell', 0),
            challenges.get('multiTurretRiftHeraldCount', 0),
            challenges.get('multikills', 0),
            challenges.get('multikillsAfterAggressiveFlash', 0),
            challenges.get('mythicItemUsed', 0),
            challenges.get('outerTurretExecutesBefore10Minutes', 0),
            challenges.get('outnumberedKills', 0),
            challenges.get('outnumberedNexusKill', 0),
            challenges.get('perfectDragonSoulsTaken', 0),
            challenges.get('perfectGame', 0),
            challenges.get('pickKillWithAlly', 0),
            challenges.get('poroExplosions', 0),
            challenges.get('quickCleanse', 0),
            challenges.get('quickFirstTurret', 0),
            challenges.get('quickSoloKills', 0),
            challenges.get('riftHeraldTakedowns', 0),
            challenges.get('saveAllyFromDeath', 0),
            challenges.get('scuttleCrabKills', 0),
            challenges.get('skillshotsDodged', 0),
            challenges.get('skillshotsHit', 0),
            challenges.get('snowballsHit', 0),
            challenges.get('soloBaronKills', 0),
            challenges.get('soloKills', 0),
            challenges.get('stealthWardsPlaced', 0),
            challenges.get('survivedSingleDigitHpCount', 0),
            challenges.get('survivedThreeImmobilizesInFight', 0),
            challenges.get('takedownOnFirstTurret', 0),
            challenges.get('takedowns', 0),
            challenges.get('takedownsAfterGainingLevelAdvantage', 0),
            challenges.get('takedownsBeforeJungleMinionSpawn', 0),
            challenges.get('takedownsFirstXMinutes', 0),
            challenges.get('takedownsInAlcove', 0),
            challenges.get('takedownsInEnemyFountain', 0),
            challenges.get('teamBaronKills', 0),
            challenges.get('teamDamagePercentage', 0.0),
            challenges.get('teamElderDragonKills', 0),
            challenges.get('teamRiftHeraldKills', 0),
            challenges.get('tookLargeDamageSurvived', 0),
            challenges.get('turretPlatesTaken', 0),
            challenges.get('turretTakedowns', 0),
            challenges.get('turretsTakenWithRiftHerald', 0),
            challenges.get('twentyMinionsIn3SecondsCount', 0),
            challenges.get('twoWardsOneSweeperCount', 0),
            challenges.get('unseenRecalls', 0),
            challenges.get('visionScoreAdvantageLaneOpponent', 0.0),
            challenges.get('visionScorePerMinute', 0.0),
            challenges.get('wardTakedowns', 0),
            challenges.get('wardTakedownsBefore20m', 0),
            challenges.get('wardsGuarded', 0)
        )

        # Execute the query
        execute_query(query, values)


def insert_match_events(match_timeline_dto):
    frames = match_timeline_dto['info']['frames']
    match_id = match_timeline_dto['metadata']['matchId']

    for frame_number, frame in enumerate(frames):
        for event_number, event in enumerate(frame['events']):
            # Extract event data
            real_timestamp = event.get('realTimestamp')
            timestamp = event.get('timestamp')
            event_type = event.get('type')
            item_id = event.get('itemId', None)
            participant_id = event.get('participantId', None)
            level_up_type = event.get('levelUpType', '')
            skill_slot = event.get('skillSlot', None)
            creator_id = event.get('creatorId', None)
            ward_type = event.get('wardType', '')
            level = event.get('level', None)
            bounty = event.get('bounty', None)
            kill_streak_length = event.get('killStreakLength', None)
            killer_id = event.get('killerId', None)
            position_x = event.get('position', {}).get('x', None)
            position_y = event.get('position', {}).get('y', None)
            victim_id = event.get('victimId', None)
            kill_type = event.get('killType', '')
            lane_type = event.get('laneType', '')
            team_id = event.get('teamId', None)
            multi_kill_length = event.get('multiKillLength', None)
            killer_team_id = event.get('killerTeamId', None)
            monster_type = event.get('monsterType', '')
            monster_sub_type = event.get('monsterSubType', '')
            building_type = event.get('buildingType', '')
            tower_type = event.get('towerType', '')
            after_id = event.get('afterId', None)
            before_id = event.get('beforeId', None)
            gold_gain = event.get('goldGain', None)
            game_id = event.get('gameId', None)
            winning_team = event.get('winningTeam', None)
            transform_type = event.get('transformType', '')
            name = event.get('name', '')
            shutdown_bounty = event.get('shutdownBounty', None)
            actual_start_time = event.get('actualStartTime', None)

            query = """
                INSERT INTO match_events 
                (match_id, frame_number, event_number, real_timestamp, timestamp, type, item_id, participant_id, level_up_type, skill_slot, creator_id, ward_type, level, bounty, kill_streak_length, killer_id, position_x, position_y, victim_id, kill_type, lane_type, team_id, multi_kill_length, killer_team_id, monster_type, monster_sub_type, building_type, tower_type, after_id, before_id, gold_gain, game_id, winning_team, transform_type, name, shutdown_bounty, actual_start_time) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                match_id, 
                frame_number, 
                event_number, 
                real_timestamp, 
                timestamp, 
                event_type, 
                item_id, 
                participant_id,
                event.get('levelUpType', ''),
                event.get('skillSlot', 0),
                event.get('creatorId', 0),
                event.get('wardType', ''),
                event.get('level', 0),
                event.get('bounty', 0),
                event.get('killStreakLength', 0),
                event.get('killerId', 0),
                event.get('position', {}).get('x', 0),
                event.get('position', {}).get('y', 0),
                event.get('victimId', 0),
                event.get('killType', ''),
                event.get('laneType', ''),
                event.get('teamId', 0),
                event.get('multiKillLength', 0),
                event.get('killerTeamId', 0),
                event.get('monsterType', ''),
                event.get('monsterSubType', ''),
                event.get('buildingType', ''),
                event.get('towerType', ''),
                event.get('afterId', 0),
                event.get('beforeId', 0),
                event.get('goldGain', 0),
                event.get('gameId', 0),
                event.get('winningTeam', 0),
                event.get('transformType', ''),
                event.get('name', ''),
                event.get('shutdownBounty', 0),
                event.get('actualStartTime', 0)
            )

            # Execute the query
            execute_query(query, values)


def insert_participant_dto(match_dto):
    participants = match_dto['info']['participants']
    match_id = match_dto['metadata']['matchId']

    for participant in participants:
        # Extracting all necessary participant data using .get() to avoid KeyError
        values = (
            match_id,
            participant.get('participantId', ''),
            participant.get('assists', ''),
            participant.get('baronKills', ''),
            participant.get('bountyLevel', ''),
            participant.get('champExperience', ''),
            participant.get('champLevel', ''),
            participant.get('championId', ''),
            participant.get('championName', ''),
            participant.get('championTransform', ''),
            participant.get('consumablesPurchased', ''),
            participant.get('damageDealtToBuildings', ''),
            participant.get('damageDealtToObjectives', ''),
            participant.get('damageDealtToTurrets', ''),
            participant.get('damageSelfMitigated', ''),
            participant.get('deaths', ''),
            participant.get('detectorWardsPlaced', ''),
            participant.get('doubleKills', ''),
            participant.get('dragonKills', ''),
            participant.get('firstBloodAssist', ''),
            participant.get('firstBloodKill', ''),
            participant.get('firstTowerAssist', ''),
            participant.get('firstTowerKill', ''),
            participant.get('gameEndedInEarlySurrender', ''),
            participant.get('gameEndedInSurrender', ''),
            participant.get('goldEarned', ''),
            participant.get('goldSpent', ''),
            participant.get('individualPosition', ''),
            participant.get('inhibitorKills', ''),
            participant.get('inhibitorTakedowns', ''),
            participant.get('inhibitorsLost', ''),
            participant.get('item0', ''),
            participant.get('item1', ''),
            participant.get('item2', ''),
            participant.get('item3', ''),
            participant.get('item4', ''),
            participant.get('item5', ''),
            participant.get('item6', ''),
            participant.get('itemsPurchased', ''),
            participant.get('killingSprees', ''),
            participant.get('kills', ''),
            participant.get('lane', ''),
            participant.get('largestCriticalStrike', ''),
            participant.get('largestKillingSpree', ''),
            participant.get('largestMultiKill', ''),
            participant.get('longestTimeSpentLiving', ''),
            participant.get('magicDamageDealt', ''),
            participant.get('magicDamageDealtToChampions', ''),
            participant.get('magicDamageTaken', ''),
            participant.get('neutralMinionsKilled', ''),
            participant.get('nexusKills', ''),
            participant.get('nexusTakedowns', ''),
            participant.get('nexusLost', ''),
            participant.get('objectivesStolen', ''),
            participant.get('objectivesStolenAssists', ''),
            participant.get('pentaKills', ''),
            participant.get('physicalDamageDealt', ''),
            participant.get('physicalDamageDealtToChampions', ''),
            participant.get('physicalDamageTaken', ''),
            participant.get('profileIcon', ''),
            participant.get('puuid', ''),
            participant.get('quadraKills', ''),
            participant.get('riotIdName', ''),
            participant.get('riotIdTagline', ''),
            participant.get('role', ''),
            participant.get('sightWardsBoughtInGame', ''),
            participant.get('spell1Casts', ''),
            participant.get('spell2Casts', ''),
            participant.get('spell3Casts', ''),
            participant.get('spell4Casts', ''),
            participant.get('summoner1Casts', ''),
            participant.get('summoner1Id', ''),
            participant.get('summoner2Casts', ''),
            participant.get('summoner2Id', ''),
            participant.get('summonerId', ''),
            participant.get('summonerLevel', ''),
            participant.get('summonerName', ''),
            participant.get('teamEarlySurrendered', ''),
            participant.get('teamId', ''),
            participant.get('teamPosition', ''),
            participant.get('timeCCingOthers', ''),
            participant.get('timePlayed', ''),
            participant.get('totalDamageDealt', ''),
            participant.get('totalDamageDealtToChampions', ''),
            participant.get('totalDamageShieldedOnTeammates', ''),
            participant.get('totalDamageTaken', ''),
            participant.get('totalHeal', ''),
            participant.get('totalHealsOnTeammates', ''),
            participant.get('totalMinionsKilled', ''),
            participant.get('totalTimeCCDealt', ''),
            participant.get('totalTimeSpentDead', ''),
            participant.get('totalUnitsHealed', ''),
            participant.get('tripleKills', ''),
            participant.get('trueDamageDealt', ''),
            participant.get('trueDamageDealtToChampions', ''),
            participant.get('trueDamageTaken', ''),
            participant.get('turretKills', ''),
            participant.get('turretTakedowns', ''),
            participant.get('turretsLost', ''),
            participant.get('unrealKills', ''),
            participant.get('visionScore', ''),
            participant.get('visionWardsBoughtInGame', ''),
            participant.get('wardsKilled', ''),
            participant.get('wardsPlaced', ''),
            participant.get('win', ''),
            participant.get('perks', {}).get('defense', ''),
            participant.get('perks', {}).get('flex', ''),
            participant.get('perks', {}).get('offense', '')
        )

        # SQL INSERT statement
        query = """
            INSERT INTO participant_dto 
            (match_id, participant_id, assists, baron_kills, bounty_level, champ_experience, champ_level, champion_id, champion_name, champion_transform, consumables_purchased, damage_dealt_to_buildings, damage_dealt_to_objectives, damage_dealt_to_turrets, damage_self_mitigated, deaths, detector_wards_placed, double_kills, dragon_kills, first_blood_assist, first_blood_kill, first_tower_assist, first_tower_kill, game_ended_in_early_surrender, game_ended_in_surrender, gold_earned, gold_spent, individual_position, inhibitor_kills, inhibitor_takedowns, inhibitors_lost, item0, item1, item2, item3, item4, item5, item6, items_purchased, killing_sprees, kills, lane, largest_critical_strike, largest_killing_spree, largest_multi_kill, longest_time_spent_living, magic_damage_dealt, magic_damage_dealt_to_champions, magic_damage_taken, neutral_minions_killed, nexus_kills, nexus_takedowns, nexus_lost, objectives_stolen, objectives_stolen_assists, penta_kills, physical_damage_dealt, physical_damage_dealt_to_champions, physical_damage_taken, profile_icon, puuid, quadra_kills, riot_id_name, riot_id_tagline, role, sight_wards_bought_in_game, spell1_casts, spell2_casts, spell3_casts, spell4_casts, summoner1_casts, summoner1_id, summoner2_casts, summoner2_id, summoner_id, summoner_level, summoner_name, team_early_surrendered, team_id, team_position, time_ccing_others, time_played, total_damage_dealt, total_damage_dealt_to_champions, total_damage_shielded_on_teammates, total_damage_taken, total_heal, total_heals_on_teammates, total_minions_killed, total_time_cc_dealt, total_time_spent_dead, total_units_healed, triple_kills, true_damage_dealt, true_damage_dealt_to_champions, true_damage_taken, turret_kills, turret_takedowns, turrets_lost, unreal_kills, vision_score, vision_wards_bought_in_game, wards_killed, wards_placed, win, perks_defense, perks_flex, perks_offense)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        """

        # Execute the query
        execute_query(query, values)


def insert_participant_frames(match_timeline_dto):
    frames = match_timeline_dto['info']['frames']
    match_id = match_timeline_dto['metadata']['matchId']

    for frame_number, frame in enumerate(frames):
        participant_frames = frame['participantFrames'].values()  # Assuming participantFrames is a dict

        for participant_frame in participant_frames:
            participant_id = participant_frame['participantId']
            timestamp = frame['timestamp']  # Assuming timestamp is in the frame, not in participant_frame
            level = participant_frame['level']
            current_gold = participant_frame['currentGold']
            gold_per_second = participant_frame['goldPerSecond']
            total_gold = participant_frame['totalGold']
            xp = participant_frame['xp']
            minions_killed = participant_frame['minionsKilled']
            jungle_minions_killed = participant_frame['jungleMinionsKilled']
            time_enemy_spent_controlled = participant_frame['timeEnemySpentControlled']
            position_x = participant_frame['position']['x']  # Assuming position is a dictionary with x and y
            position_y = participant_frame['position']['y']

            query = """
                INSERT INTO participant_frames 
                (match_id, frame_number, participant_id, timestamp, level, current_gold, gold_per_second, total_gold, xp, minions_killed, jungle_minions_killed, time_enemy_spent_controlled, position_x, position_y) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (match_id, frame_number, participant_id, timestamp, level, current_gold, gold_per_second, total_gold, xp, minions_killed, jungle_minions_killed, time_enemy_spent_controlled, position_x, position_y)

            # Execute the query
            execute_query(query, values)



if __name__ == "__insert_match__":
    insert_match()
