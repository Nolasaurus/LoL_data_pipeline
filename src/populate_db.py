import postgres_helperfile
from MatchOverclass import MatchOverclass

# Automated API data insertion into sql
# Full Match Visualization: Expansion of the match data visualization
# to include all required stats (KDA, gold, items, level, damage, etc.)



# upon api call:
#     get response
#     parse response
#     craft sql table insert statements
#     connect to sql
#     send to sql
#     verify upload correct


def get_and_insert_match_data(match_ids):
    for match_id in match_ids:
        match_oc_object = MatchOverclass(match_id)
        match_dto = match_oc_object.match_data
        match_timeline = match_oc_object.match_timeline



TABLES = {
    'match_events',
    'kill_events',
    'event_positions',
    'victim_damage_dealt',
    'victim_damage_received',
    'match_metadata',
    'participant_frames',
    'perk_stats',
    'perk_styles',
    'perk_style_selections',
    'perks',
    'player_match_data',
    'teams'
}

        self.puuid_dict = {
            participant.puuid: participant.summonerName
            for participant in self.match_data.info.participants
        }