from langchain.serpapi import SerpAPIWrapper
# from langchain.utilities import OpenWeatherMapAPIWrapper


def get_profile_url(text: str) -> str:
    """Makes a google search"""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res

# def get_weather(location: str) -> str:
#     """Retrieves the weather"""
#     weather = weather.run(location)
#     print(weather)
