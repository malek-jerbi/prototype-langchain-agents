from agents.agent import lookup


def make_request(name: str) -> str:
    agent_answer = lookup(prompt=name)

    return agent_answer


if __name__ == "__main__":
    make_request(name="what is the weather in montreal")
