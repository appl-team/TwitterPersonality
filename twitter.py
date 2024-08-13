"""Analyse the personality of a Twitter user, Based on https://twitter.wordware.ai/"""

import json
from argparse import ArgumentParser
from typing import List, Optional

from pydantic import BaseModel, Field

import appl
from appl import SystemMessage, convo, gen, ppl
from appl.compositor import StarList
from appl.const import EMPTY

appl.init()  # Initialize the appl library, it also loads the environment variables from .env

from twitter_scraper import scrape_profile, scrape_tweets


class Strength(BaseModel):
    title: Optional[str]
    subtitle: Optional[str]


class Weakness(BaseModel):
    title: Optional[str]
    subtitle: Optional[str]


class Personality(BaseModel):
    name: Optional[str]
    about: Optional[str]
    emojis: Optional[List[str]] = Field(None, description="A list of 5-8 emojis")
    roast: Optional[str]
    strengths: Optional[List[Strength]] = Field(
        None, description="A list of 5 or more strengths"
    )
    weaknesses: Optional[List[Weakness]] = Field(
        None, description="A list of 5 or more weaknesses"
    )
    loveLife: Optional[str]
    money: Optional[str]
    health: Optional[str]
    biggestGoal: Optional[str]
    colleaguePerspective: Optional[str]
    pickupLines: Optional[List[str]] = Field(
        None, description="A list of 3 or more pickup lines"
    )
    famousPersonComparison: Optional[str]
    previousLife: Optional[str]
    animal: Optional[str]
    fiftyDollarThing: Optional[str]
    career: Optional[str]
    lifeSuggestion: Optional[str]


@ppl(exclude_first_str=True)
def analyse(twitter_handle: str):
    """Analyse the personality of a Twitter user."""
    # ===== Beginning of the prompt =====
    SystemMessage(
        "You are an experienced Astrologer who specializes in writing Horoscopes. Act like a horoscope teller."
    )

    "# **Instructions**"

    "Your job is to read the data provided below. This Twitter data is the only data you get to understand this person. You can make assumptions. Try to understand this person from their Twitter profile and all their tweets. You can sound a little controversial."

    "After understanding them, answer the following questions. You can make assumptions."
    with StarList(indent=4):
        "What is the name, Twitter username (without @ and in lowercase) of this person."

        'Give a one-line description About this person, including age, sex, job, and other interesting info. This can be drawn from the profile picture. Start the sentence with "Based on our AI agent\'s analysis of your tweets...."'

        "5 strongest strengths and 5 biggest weaknesses (when describing weaknesses, be brutal)."

        "Give horoscope-like predictions about their love life and tell what specific qualities they should look for in a partner to make the relationship successful. Keep this positive and only a single paragraph."

        "Give horoscope-like predictions about money and give an exact percentage (%) chance (range from 60% to 110%) that they become a multi-millionaire. You can increment the value by 1%. The percentage doesn't have to end with 5 or 0. Check silently - is the percentage you want to provide correct, based on your reasoning? If yes, produce it. If not, change it."

        "Give horoscope-like predictions about health. Keep this optimistic and only a single paragraph."

        "After understanding them, tell them what is their biggest goal in life. This should be completely positive."

        "Guess how they are to work with, from a colleague's perspective. Make this spicy and a little controversial."

        "Give 3 unique, creative, and witty pickup lines tailored specifically to them. Focus on their interests and what they convey through their tweets. Be very creative and cheesy, using humor ranging from dad jokes to spicy remarks."

        "Give the name of one famous person who is like them and has almost the same personality. Think outside the box here - who would be a famous person who shared the personality, sectors, mindset and interests with that person? Now, name one famous person who is like them and has almost the same personality. Don't provide just people who are typical. Be creative. Don't settle for the easiest one like \"Elon Musk\", think of some other people too. Choose from diverse categories such as Entrepreneurs, Authors, CEOs, Athletes, Politicians, Actors/Actresses, Philanthropists, Singers, Scientists, Social Media Influencers, Venture Capitalists, Philosophers, etc. Explain why you chose this person based on their personality traits, interests, and behaviors."

        "Previous Life. Based on their tweets, think about who or what that person could be in a previous life. Refer to the “About” section to find a similar profile from the past. Who might they have shared a personality and mindset with? Name one person. Be humorous, witty, and bold. Explain your choice."

        "Animal. Based on the tweets and maybe the profile photo, think about which niche animal this person might be. Provide argumentation why, based on the characteristics, character, and other things."

        "Under a 50-dollar thing, they would benefit from the most. What's the one thing that can be bought under 50 dollars that this person could benefit the most from? Make it very personal and accurate when it comes to the price. But be extremely creative. Try to suggest a thing this person wouldn't think of themselves."

        "Career. Describe what that person was born to do. What should that person devote their life to? Explain why and how they can achieve that, what the stars are telling."

        "Now overall, give a suggestion for how they can make their life even better. Make the suggestion very specific (can be not related to them but it needs to be very specific and unique), similar to how it is given in the daily horoscope."

        'Roast. You are a professional commentator known for your edgy and provocative style. Your task is to look at people\'s tweets and rate their personalities based on that. Be edgy and provocative, be mean a little. Don\'t be cringy. Here\'s a good attempt of a roast: """Alright, let\'s break this down. You\'re sitting in a jungle of houseplants, barefoot and looking like you just rolled out of bed. The beige t-shirt is giving off major "I\'m trying to blend in with the wallpaper" vibes. And those black pants? They scream "I couldn\'t be bothered to find something that matches." But hey, at least you look comfortable. Comfort is key, right? Just maybe not when you\'re trying to make a fashion statement."""'

        "Emojis - Describe a person using only emojis."

    "Be creative like a horoscope teller."

    "## **Inputs:**"
    "```"
    json.dumps(scrape_profile(twitter_handle))
    EMPTY
    json.dumps(scrape_tweets(twitter_handle))
    "```"

    "Output the result as valid JSON, strictly adhering to the defined schema. Ensure there are no markdown codes or additional elements included in the output."

    "You can **bold** important information within the strings."
    "Do not add anything else. Do not add markdown. Return ONLY plain JSON."

    # print(convo()) # display the current prompt used for `gen()`
    return gen(response_model=Personality).response_obj


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "--twitter-handle",
        type=str,
        help="Twitter handle of the user",
        default="elonmusk",
    )
    args = parser.parse_args()

    results = analyse(args.twitter_handle)
    # Simply print the results
    for key, value in results.model_dump().items():
        print(f"### {key}")
        if isinstance(value, list):
            for item in value:
                print(f"* {item}")
        else:
            print(value)
    # You may process the results further as needed
