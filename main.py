from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers"""
    print("Tool has been called")
    return f"The sum of {a} and {b} is {a + b}"

def main():
    # Using Gemini 1.5 Flash (latest) - better free tier limits
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", temperature=0)

    tools = [calculator]  # Add your calculator tool here!
    agent_executor = create_react_agent(model, tools)

    print("🤖 Welcome to ARIA - AI Reasoning & Interactive Assistant!")
    print("Powered by Google Gemini 1.5 Flash with calculator tools.")
    print("Type 'quit' to exit or ask me anything!")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input == "quit" :
            break

        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()