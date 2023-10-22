from agents.agent import lookup


def make_request(name: str) -> str:
    linkedin_profile_url = lookup(prompt=name)

    return linkedin_profile_url


if __name__ == "__main__":
    make_request(name="what is the weather in montreal")
