import pandas as pd

def extract_player_data_from_match(player_data):
    included_fields = pd.read_csv('included_match_fields.csv')
    included_fields_list = included_fields.iloc[:, 0].tolist()
    
    metadata = player_data[0]
    match_id = metadata['matchId']
    
    info = player_data[1]
    
    data = pd.DataFrame(info['participants'])[included_fields_list]
    data.insert(0, 'PUUid', metadata['participants'])
    data.insert(0, 'match_id', match_id)
    
    return data