from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType, load_tools
from tools.tools import get_profile_url


def lookup(prompt: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-4")
    tools = load_tools(["openweathermap-api"], llm)
    tools.append(
        Tool(
            name="Crawl Google",
            func=get_profile_url,
            description="useful for when you need to search on google",
        )
    )

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )
    
    prompt_answer = agent.run(prompt)

    return prompt_answer
