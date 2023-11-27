# LoL data pipeline

1. Enables Basic API functionality
2. Extracts match timeline data
3. Uploads 3NF data to PostgreSQL
4. Presents resulting match data with flask frontend


Completed Items

    Streamlit Interface: Basic user interface for summoner name input.
    Summoner Data Retrieval: Functionality to fetch summoner details using the input name.
    Match Data Fetching: Logic to retrieve match IDs for a given summoner.
    Match Data Visualization: Partial implementation of match data visualization (e.g., plot_gold_by_frame() method in MatchOverclass).
    Error Handling: Basic error handling for API calls and data processing.
    SQL Query Execution Interface: A section in the Streamlit app for executing custom SQL queries against the database.
    Docker Integration: Containerizing the Streamlit frontend and PostgreSQL database. 

Yet-to-be-Completed Items

    Comprehensive Error Handling: Refinement of error handling for more robustness.
    Full Match Visualization: Expansion of the match data visualization to include all required stats (KDA, gold, items, level, damage, etc.).
    Time-Series Data Visualization: Implementation of the time-series line charts for gold, level, and XP for all match participants.
    Result Display for SQL Queries: Handling and displaying the results of executed SQL queries, especially for SELECT statements.
    Frontend Aesthetics and Usability: Enhancing the user interface for better user experience and aesthetics.
    Testing and Debugging: Comprehensive testing of all functionalities to ensure reliability.
    Deployment and Accessibility: Setting up the application for remote hosting, involving server configuration and security considerations. (Azure?)