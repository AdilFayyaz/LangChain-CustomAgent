import streamlit as st
from agents.agent import initialize_main_agent
from memory.shared_memory import shared_memory
from utils.test_functions import LOCATIONS
import json

main_agent = initialize_main_agent(shared_memory)

st.title("Birthday Party Planning Assistant ")

# Party Details Input
st.subheader("Party Details")
location = st.selectbox("Location", options=LOCATIONS)
capacity = st.number_input("Capacity", min_value=1, value=50)
date = st.date_input("Date")
cuisine = st.selectbox(
    "Cuisine",
    options=[
        "Italian", "Indian", "Chinese", "Mexican", "Mediterranean"
    ]
)

# Entertainment
entertainment = st.selectbox(
    "Entertainment",
    options=[
        "DJ", "Magician", "Live Band", "Photobooth", "Karaoke"
    ]
)
budget = st.number_input("Budget ($)", min_value=100, value=1000, step=100)

# Store user input as a dictionary, including the expected 'input' key
user_input = {
    "input": f"Plan a party with the following details: Location: {location}, Capacity: {capacity}, Date: {date.strftime('%Y-%m-%d')}, Cuisine: {cuisine}, Entertainment: {entertainment}, Budget: ${budget}. Please provide the reasoning behind your choices.",
}

# Sidebar for adjustments
st.sidebar.subheader("Adjustments")
adjust_location = st.sidebar.selectbox("Change Location", options=[None] + LOCATIONS)
adjust_capacity = st.sidebar.number_input("Change Capacity", min_value=1, value=capacity)
adjust_cuisine = st.sidebar.selectbox("Change Cuisine", options=[None] + ["Italian", "Indian", "Chinese", "Mexican", "Mediterranean"])
adjust_entertainment = st.sidebar.selectbox("Change Entertainment", options=[None] + ["DJ", "Magician", "Live Band", "Photobooth", "Karaoke"])
adjust_budget = st.sidebar.number_input("Change Budget ($)", min_value=100, value=budget, step=100)

# Generate or Update Plan
if st.button("Generate Party Plan"):
    if "current_plan" not in st.session_state:
        user_message = user_input["input"]
        initial_plan = main_agent.invoke(user_message)
        
        # Collect pricing details from the plan
        total_price = initial_plan.get('total_price', 0)  # Ensure we use the price returned from the agent
        ai_message = initial_plan['output']

        # Save results in session state
        st.session_state.current_plan = ai_message
        st.session_state.total_price = total_price  # Store total price in session state

        # Save to shared memory
        shared_memory.chat_memory.add_user_message(f"User: {user_message}")
        shared_memory.chat_memory.add_ai_message(f"Agent: {ai_message}")

        # Display results
        st.subheader("Generated Party Plan")
        st.text(ai_message)
        
    else:
        # If the plan is already generated, display it from session state
        st.subheader("Generated Party Plan")
        st.text(st.session_state.current_plan)
        

# Handle Adjustment Submission
if any([adjust_location, adjust_capacity, adjust_cuisine, adjust_entertainment, adjust_budget]):
    if st.sidebar.button("Submit Adjustment"):
        updated_input = user_input.copy()
        if adjust_location and adjust_location != location:
            updated_input["input"] = updated_input["input"].replace(f"Location: {location}", f"Location: {adjust_location}")
        if adjust_capacity != capacity:
            updated_input["input"] = updated_input["input"].replace(f"Capacity: {capacity}", f"Capacity: {adjust_capacity}")
        if adjust_cuisine and adjust_cuisine != cuisine:
            updated_input["input"] = updated_input["input"].replace(f"Cuisine: {cuisine}", f"Cuisine: {adjust_cuisine}")
        if adjust_entertainment and adjust_entertainment != entertainment:
            updated_input["input"] = updated_input["input"].replace(f"Entertainment: {entertainment}", f"Entertainment: {adjust_entertainment}")
        if adjust_budget != budget:
            updated_input["input"] = updated_input["input"].replace(f"Budget: ${budget}", f"Budget: ${adjust_budget}")

        # Invoke the agent with updated inputs
        user_message2 = updated_input["input"]
        adjustment_plan = main_agent.invoke(user_message2)
        ai_message2 = adjustment_plan['output']
        
        # Update the total price from the agent's response
        total_price = adjustment_plan.get('total_price', 0)

        # Update the session state
        st.session_state.current_plan = ai_message2
        st.session_state.total_price = total_price  # Update total price in session state

        shared_memory.chat_memory.add_user_message(f"User: {user_message2}")
        shared_memory.chat_memory.add_ai_message(f"Agent: {ai_message2}")

        st.subheader("Updated Party Plan")
        st.text(ai_message2)
        

# Feedback and Adjustments from Chat History
chat_history = shared_memory.load_memory_variables({}).get("chat_history", [])
if chat_history:
    st.subheader("Conversation History")
    # Display chat history without repeating the same plan multiple times
    for msg in chat_history:
        if hasattr(msg, 'content'):
            # Only show user and agent messages related to the current plan generation or adjustment
            if "User" in msg.content:
                st.markdown(f"**User:** {msg.content[5:]}")  
            elif "Agent:" in msg.content:
                st.markdown(f"**Agent:** {msg.content[6:]}")