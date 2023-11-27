# LoL data pipeline and frontend
The "LoL Data Pipeline" Git repository is an evolving project aimed at providing insightful analysis of League of Legends gameplay through a data-driven approach. At its core, the project leverages the game's API to extract match timeline data, which is then normalized and stored in a PostgreSQL database. The project features a user-friendly Streamlit interface, allowing users to input summoner names and interact directly with the data. This interaction encompasses fetching summoner details, retrieving match IDs, and offering a partial visualization of match data.

Future aspirations include enhancing error handling, expanding match visualizations, and implementing time-series data charts. Additionally, improvements in frontend design, comprehensive testing, and preparing for remote hosting are on the horizon. This humble endeavor aims not only to deepen understanding of game dynamics but also to provide an engaging platform for users to explore and analyze League of Legends data.

## Completed Items
✅ Streamlit Interface: Basic user interface for summoner name input.  
✅ Summoner Data Retrieval: Functionality to fetch summoner details using the input name.  
✅ Match Data Fetching: Logic to retrieve match IDs for a given summoner.  
✅ Match Data Visualization: Partial implementation of match data visualization.
✅ Error Handling: Basic error handling for API calls and data processing.  
✅ SQL Query Execution Interface: A section in the Streamlit app for executing custom SQL queries against the database.  
✅ Docker Integration: Containerizing the Streamlit frontend and PostgreSQL database.  


## Yet-to-be-Completed Items
🔳 Comprehensive Error Handling: Refinement of error handling for more robustness.  
🔳 Full Match Visualization: Expansion of the match data visualization to include all required stats (KDA, gold, items, level, damage, etc.).  
🔳 Time-Series Data Visualization: Implementation of the time-series line charts for gold, level, and XP for all match participants.  
🔳 Result Display for SQL Queries: Handling and displaying the results of executed SQL queries, especially for SELECT statements.  
🔳 Frontend Aesthetics and Usability: Enhancing the user interface for better user experience and aesthetics.  
🔳 Testing and Debugging: Comprehensive testing of all functionalities to ensure reliability.  
🔳 Deployment and Accessibility: Setting up the application for remote hosting, involving server configuration and security considerations. 
