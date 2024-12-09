# LangChain MultiAgent 
# Birthday Party Planning Assistant

This project is a Streamlit-based application designed to assist users in planning birthday parties by providing customizable suggestions for party details such as location, entertainment, cuisine, and budget. The app leverages AI agents to dynamically generate and adjust party plans based on user inputs and preferences.

## Features

- **User Input for Party Details**:
  - Select location, capacity, date, cuisine, entertainment type, and budget for the party.
  
- **Adjustment Functionality**:
  - Modify the party plan details such as location, capacity, cuisine, entertainment, and budget via the sidebar and regenerate the plan based on updated input.

- **AI-Generated Party Plan**:
  - The assistant generates a comprehensive party plan with suggestions, taking into account user preferences and providing reasoning behind the choices.

- **Integration with External Tools**:
  - The app integrates with various tools to find venues, catering options, and entertainment suggestions using APIs like OpenAI's GPT-4.

- **Interactive Conversation History**:
  - View the conversation history between the user and the AI to track changes and decisions made throughout the planning process.

## How to Use

1. **Install Requirements**:
   Install the required dependencies using the following:

   ```bash
   pip install -r requirements.txt
   ```

2.	**Set Up API Keys**:
Set up your OpenAI API key in the environment variables. For example:
```bash
export OPENAI_API_KEY="your-openai-api-key"
```

3. **Run the Streamlit App**:
To run the application, use the following command:
```bash
streamlit run app.py
```

4.	Interacting with the Assistant:
- Enter details for the party, including the location, date, cuisine, and entertainment.
- Use the sidebar to make adjustments to the party details and regenerate the plan as needed.
- The app will provide a party plan along with suggested venues, catering, and entertainment options.

Project Structure

- app/app.py: Main Streamlit app file.
- agents/agent.py: Code to initialize and manage the main AI agent for party planning.
- memory/shared_memory.py: Shared memory for storing chat history and maintaining state across interactions.
- utils/test_functions.py: Helper functions such as LOCATIONS, search_venues, find_caterers, and suggest_entertainment.
- requirements.txt: List of required dependencies for the project.

Technologies Used

- Streamlit: For building the web-based UI.
- OpenAI GPT-4: For generating party plans and suggestions.
- Langchain: To handle conversation history and integrate external tools for venue and catering suggestions.
- Python: For scripting and backend functionality.

Tools Integrated

- Venue Finder: Suggests party venues based on location, capacity, date, and budget.
- Catering Finder: Recommends catering options based on cuisine and budget.
- Entertainment Finder: Provides entertainment options such as DJs, bands, and photobooths. 



