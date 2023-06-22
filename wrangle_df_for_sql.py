import pandas as pd

def list_to_str(assisted_kill):
    if isinstance(assisted_kill, list):
        return str(assisted_kill).strip('[]')

def wrangle_df_for_sql(match_timeline_df):
    # Convert list to str
    match_timeline_df['assistingParticipants'] = match_timeline_df['assistingParticipantIds'].apply(list_to_str)
    
    # Calculate realtimestamps
    game_start = match_timeline_df.loc[0, 'realTimestamp']
    match_timeline_df['realTimestamp'] = match_timeline_df['timestamp'] + game_start

    # Split position into x_, y_
    if 'position' in match_timeline_df.columns:
        # Select the non-null positions and apply pd.Series
        position_df = match_timeline_df.loc[match_timeline_df['position'].notna(), 'position'].apply(pd.Series)
        position_df.columns = ['x_position', 'y_position']
        match_timeline_df = match_timeline_df.drop(columns=['position']).join(position_df)

    return match_timeline_df
