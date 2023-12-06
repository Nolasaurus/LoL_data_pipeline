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


## TODO:
### Automated API Data Insertion into SQL
1. **Script Development for Data Extraction**: Create a script to automatically extract data from the LoL API. Ensure it captures all necessary match details.
2. **Complete Data Transformation Layer**: Finish the development of a data transformation layer to format API data for SQL compatibility.
3. **Implement Data Loading Mechanism**: Develop a mechanism to load transformed data into the PostgreSQL database efficiently.
4. **Schedule Database Updates**: Set up a scheduler to periodically update the database with new data from the API, ensuring synchronization.
5. **Data Integrity Assurance**: Implement checks to ensure data integrity, handling duplicates and missing data effectively.
6. **Monitoring and Logging Setup**: Establish a monitoring and logging system for the data insertion process to facilitate troubleshooting.

### Comprehensive Error Handling
1. **Enhance Error Handling Coverage**: Expand the current error handling system to cover a broader range of specific exceptions.
2. **Implement Error Logging**: Develop a logging system for errors that occur, focusing on traceability and ease of debugging.
3. **User-Friendly Error Messages**: Design and implement user-friendly error messages for the front-end.
4. **Retry Mechanisms for Failures**: Develop retry mechanisms for handling transient API or database failures.
5. **Critical Error Alert System**: Create a system to send alerts in case of critical errors.
6. **Incorporate Error Handling Standards**: Ensure the error handling system adheres to best practices and standards.

### Match Summary Visualization
1. **Expand Match Visualization Features**: Include comprehensive statistics (KDA, gold, etc.) in the match visualization.
2. **Design Interactive Visualization Tools**: Develop interactive charts and graphs for enhanced user engagement.
3. **Optimize Data Retrieval for Visualization**: Ensure efficient data retrieval and processing for improved visualization performance.
4. **Implement Customization Filters**: Create filters and selectors in the visualization tool for user-customized views.

### Time-Series Data Visualization
1. **Develop Time-Series Line Charts**: Create line charts for displaying time-series data like gold, level, and XP.
2. **Interactive Match Timeline Implementation**: Develop an interactive timeline for users to navigate through the match events.
3. **Responsive Design for Time-Series Viz**: Ensure the time-series visualization is responsive and adapts to different screen sizes.
4. **Validate Time-Series Data Accuracy**: Cross-check the accuracy of time-series data against actual match events.

### Result Display for SQL Queries
1. **Design Interface for SQL Query Results**: Create a user-friendly interface to display the results of SQL queries.
2. **Implement Result Formatting Rules**: Set rules for formatting different types of data (text, numbers, dates) in the SQL query results.
3. **Export Options for Query Results**: Provide functionality to export query results into formats like CSV or Excel.
4. **Pagination for Large Result Sets**: Implement pagination for displaying large sets of SQL query results.
5. **Secure SQL Query Feature**: Ensure the SQL query feature is secure against potential SQL injection attacks.
6. **Robustness Testing of Query Display**: Test the SQL query display feature with various query types and complexities.

### Frontend Aesthetics and Usability
1. **User Navigation and Customization Implementation**: Develop a feature for navigating between users and customizing visualizations and SQL queries.
2. **Responsive Frontend Design Development**: Implement a responsive design to ensure accessibility across various devices.
3. **Introduce User Interface Aids**: Develop navigation aids and tooltips to enhance user experience.
4. **Optimize Frontend Performance**: Work on optimizing load times and interaction smoothness on the frontend.
5. **Conduct User Testing for Feedback**: Organize user testing sessions to collect feedback and identify areas for improvement.

### Testing and Debugging
1. **Automated Test Suite Development**: Build a comprehensive suite of automated tests for all functionalities.
2. **Continuous Integration for Testing**: Set up continuous integration to run tests with every code change.
3. **Manual Testing of User Interface**: Conduct in-depth manual testing for the user interface and user experience.
4. **Debugging and Issue Resolution**: Identify and fix issues found during testing phases.
5. **Bug Tracking and Management Process Establishment**: Set up a process for tracking and managing bugs.
6. **Document Testing Procedures and Results**: Keep detailed records of testing procedures and their outcomes for future reference.

### Deployment and Accessibility
1. **GitHub Pages Setup for Hosting**: Configure GitHub Pages for hosting the application.
2. **Application Scalability and Availability Optimization**: Work on optimizing the application for better scalability and availability.
3. **Deployment Pipeline Development**: Develop CI/CD pipeline for deployment of updates.

## Bonus 
➕ Replace time.sleep in test_app.py with Selenium's explicit wait conditions  
➕ Expand test_app.py to dynamically test all tables in db
