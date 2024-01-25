import matplotlib.pyplot as plt
import pandas as pd
from postgres_helperfile import SQLHelper

sql_helper = SQLHelper()

def viz_match_summary(match_id):
    SQL_QUERY = f"select * from participant_dto where match_id = '{match_id}';"
    query_result, columns = sql_helper.execute_query(SQL_QUERY)
    match_data_df = pd.DataFrame(query_result, columns=columns)
    match_data_df = match_data_df[['match_id', 'participant_id', 'team_id', 'summoner_name', 'summoner_level', 'assists', 'champ_experience', 'champ_level', 'champion_name', 'deaths', 'gold_earned', 'item0', 'item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'kills', 'killing_sprees', 'magic_damage_dealt_to_champions', 'physical_damage_dealt_to_champions', 'total_damage_dealt_to_champions']]

    fig, axs = plt.subplots(2, 2, figsize=(15, 10))

    # Plot 1
    scatter = axs[0, 0].scatter(match_data_df['champ_experience'], match_data_df['gold_earned'], c=match_data_df['team_id'], cmap='viridis')
    axs[0, 0].set_xlabel('Champion Experience')
    axs[0, 0].set_ylabel('Gold Earned')
    axs[0, 0].set_title('Champion Experience vs Gold Earned')
    legend1 = axs[0, 0].legend(*scatter.legend_elements(), title="Team ID")
    axs[0, 0].add_artist(legend1)

    # Plot 2
    scatter = axs[0, 1].scatter(match_data_df['total_damage_dealt_to_champions'], match_data_df['gold_earned'], c=match_data_df['team_id'], cmap='viridis')
    axs[0, 1].set_xlabel('Total Damage to Champions')
    axs[0, 1].set_ylabel('Gold Earned')
    axs[0, 1].set_title('Total Damage vs Gold Earned')
    legend2 = axs[0, 1].legend(*scatter.legend_elements(), title="Team ID")
    axs[0, 1].add_artist(legend2)

    # Plot 3
    kdr = match_data_df['kills'] / match_data_df['deaths'].replace(0, 1)  # Avoid division by zero
    scatter = axs[1, 0].scatter(kdr, match_data_df['gold_earned'], c=match_data_df['team_id'], cmap='viridis')
    axs[1, 0].set_xlabel('Kills/Deaths Ratio')
    axs[1, 0].set_ylabel('Gold Earned')
    axs[1, 0].set_title('Kills/Deaths Ratio vs Gold Earned')
    legend3 = axs[1, 0].legend(*scatter.legend_elements(), title="Team ID")
    axs[1, 0].add_artist(legend3)

    # Plot 4
    scatter = axs[1, 1].scatter(match_data_df['kills'], match_data_df['assists'], c=match_data_df['team_id'], cmap='viridis')
    axs[1, 1].set_xlabel('Kills')
    axs[1, 1].set_ylabel('Assists')
    axs[1, 1].set_title('Kills vs Assists')
    legend4 = axs[1, 1].legend(*scatter.legend_elements(), title="Team ID")
    axs[1, 1].add_artist(legend4)

    plt.tight_layout()
    plt.show()

# Example usage
viz_match_summary('NA1_4466882444')
