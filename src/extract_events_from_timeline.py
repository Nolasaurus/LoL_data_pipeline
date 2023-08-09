
import pandas as pd

def extract_events_from_timeline(match_timeline):
    game_event_df = pd.DataFrame()
    # TODO implement pFrames
    # game_pFrames_df = pd.DataFrame()
    for i, frame in enumerate(match_timeline['info']['frames']):
        events = pd.DataFrame(match_timeline['info']['frames'][i]['events'])
        # TODO 
        # pFrames = pd.DataFrame(match_timeline['info']['frames'][i]['participantFrames'])

        # concat events to game_event_df
        game_event_df = pd.concat([game_event_df, events], ignore_index=True)
        
        # game_pFrames_df = pd.concat([game_pFrames_df, pFrames], ignore_index=True)

    return game_event_df #, game_pFrames_df