import pandas as pd

def extract_data_from_match(match_data):
    metadata = match_data['metadata']
    info = match_data['info']
    match_id = metadata['matchId']
    game_duration = info['gameDuration']

    included_fields = pd.read_csv('/home/nolan/projects/LoL_data_pipeline/included_match_fields.csv')
    included_fields_list = included_fields.iloc[:, 0].tolist()    
    
    data = pd.DataFrame(info['participants'])[included_fields_list]
    # data.insert(0, 'PUUid', metadata['participants'])
    # data.insert(0, 'match_id', match_id)
    
    return data