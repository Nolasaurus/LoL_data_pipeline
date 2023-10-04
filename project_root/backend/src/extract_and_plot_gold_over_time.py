import base64
from io import BytesIO
from src.connect_db import connect_db
import matplotlib.pyplot as plt

def extract_gold_data(match_id):
    conn = connect_db()
    ## get gold per participant
    with conn.cursor() as cur:
        query = "SELECT match_timeline->'info'->'frames' FROM match WHERE match_id = %s;"
        cur.execute(query, (match_id,))
        frames = cur.fetchone()

    gold_data = []
    
    # Extract the 'frames' data from the 'info' key
    frames_data = frames[0]

    # Iterate through the frames
    for frame_index, frame in enumerate(frames_data):
        participant_frames = frame['participantFrames']

        # Iterate through the participant frames
        for participant_id, participant_data in participant_frames.items():
            # Extract the currentGold and totalGold values
            current_gold = participant_data['currentGold']
            total_gold = participant_data['totalGold']

            # Append the data to the results list
            gold_data.append({
                'frame_index': frame_index,
                'participant_id': participant_id,
                'current_gold': current_gold,
                'total_gold': total_gold,
                # Include timestamp if available in your data structure
                # 'timestamp': frame['events'][0]['realTimestamp'] if frame['events'] else None
            })

    return gold_data

def plot_gold_data(gold_data):
    # Group the gold data by participant
    participants_data = {}
    for record in gold_data:
        participant_id = record['participant_id']
        if participant_id not in participants_data:
            participants_data[participant_id] = {'total_gold': []}
        participants_data[participant_id]['total_gold'].append(record['total_gold'])

    # Plot the gold data for each participant
    for participant_id, data in participants_data.items():
        plt.plot(data['total_gold'], label=f'Participant {participant_id}')

    plt.xlabel('Minute')
    plt.ylabel('Total Gold')
    plt.title('Total Gold Over Time')
    plt.legend()    
    
    # Save the plot to a bytes buffer
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Encode the bytes buffer as a Base64 string
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')

    return image_base64