from langchain.agents import Tool
from utils.test_functions import search_venues, find_caterers, suggest_entertainment


venue_tool = Tool(
    name="Venue Finder",
    func=lambda user_input: (
        print(f"User input for Venue Finder: {user_input}"),  # Print user input
        search_venues(user_input)
    )[1],  # The second element of the tuple (the result of the function)
    description="Finds venues based on location, capacity, date, and budget."
)

catering_tool = Tool(
    name="Catering Finder",
    func=lambda user_input: (
        print(f"User input for Catering Finder: {user_input}"),  # Print user input
        find_caterers(user_input)
    )[1],
    description="Finds catering options based on location, cuisine, and budget."
)

entertainment_tool = Tool(
    name="Entertainment Finder",
    func=lambda user_input: (
        print(f"User input for Entertainment Finder: {user_input}"),  # Print user input
        suggest_entertainment(user_input)
    )[1],
    description="Suggests entertainment options based on type and budget."
)
