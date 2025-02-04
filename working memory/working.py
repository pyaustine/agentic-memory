# Instantiate the Language Model

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0.7, model="gpt-4o")

# Create Simple Back & Forth Chat Flow

from langchain_core.messages import HumanMessage, SystemMessage

# Define System Prompt
system_prompt = SystemMessage("You are a helpful AI Assistant. Answer the User's queries succinctly in one sentence.")

# Start Storage for Historical Message History
messages = [system_prompt]

while True:

    # Get User's Message
    user_message = HumanMessage(input("\nUser: "))
    
    if user_message.content.lower() == "exit":
        break

    else:
        # Extend Messages List With User Message
        messages.append(user_message)

    # Pass Entire Message Sequence to LLM to Generate Response
    response = llm.invoke(messages)
    
    print("\nAI Message: ", response.content)

    # Add AI's Response to Message List
    messages.append(response)

# Expected Output
"""
AI Message:  Hello! How can I assist you today?
AI Message:  I'm sorry, but I don't have access to personal information, so I don't know your name.
AI Message:  Nice to meet you, Adam! How can I help you today?
AI Message:  Your name is Adam.
"""

# Keeping track of our total conversation allows the LLM to use prior messages and interactions as context for immediate responses during an ongoing conversation, keeping our current interaction in working memory and recalling working memory through attaching it as context for subsequent response generations.

# Looking into our Memory

for i in range(len(messages)):
    print(f"\nMessage {i+1} - {messages[i].type.upper()}: ", messages[i].content)
    i += 1

# Expected Output

"""    
Message 1 - SYSTEM:  You are a helpful AI Assistant. Answer the User's queries succinctly in one sentence.

Message 2 - HUMAN:  Hello!

Message 3 - AI:  Hello! How can I assist you today?

Message 4 - HUMAN:  What's my name

Message 5 - AI:  I'm sorry, but I don't have access to personal information, so I don't know your name.

Message 6 - HUMAN:  Oh my name is Adam!

Message 7 - AI:  Nice to meet you, Adam! How can I help you today?

Message 8 - HUMAN:  What's my name?

Message 9 - AI:  Your name is Adam.
"""