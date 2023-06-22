def wrangle_df_for_sql(match_timeline_df):
    import pandas as pd

    def list_to_str(assisted_kill):
        # If the value is NaN, leave it as is
        if pd.isnull(assisted_kill):
            return assisted_kill
        # If the value is a list, convert it to string
        elif isinstance(assisted_kill, list):
            # Join the elements of the list as a string with comma separation
            return ', '.join(str(x) for x in assisted_kill)
        return assisted_kill
    
    # convert list to str
    match_timeline_df['assistingParticipantIds'] = list_to_str(match_timeline_df['assistingParticipantIds'])

    # calculate realtimestamps

    game_start = match_timeline_df['realTimestamp'][0]
    game_end = match_timeline_df['realTimestamp'][:-1]

    match_timeline_df['realTimestamp'] = match_timeline_df['timestamp'] + game_start

    # split position into x_, y_
    # Select the non-null positions and apply pd.Series
    position_df = match_timeline_df['position'][match_timeline_df['position'].notna()].apply(pd.Series)

    # Rename the columns to 'x_position' and 'y_position'
    position_df.columns = ['x_position', 'y_position']

    # Now we want to add these new columns to the original DataFrame. 
    # First, let's drop the 'position' column from the original DataFrame.
    match_timeline_df.drop(columns=['position'], inplace=True)

    # Now we can join the original DataFrame with our new position_df.
    match_timeline_df = match_timeline_df.join(position_df)



    return match_timeline_df