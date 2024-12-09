from langchain.memory import ConversationBufferMemory

# Shared memory for communication between agents
shared_memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)