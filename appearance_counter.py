#!/usr/bin/python3
"""
"""

import logging

from bs4 import BeautifulSoup
import requests as r

# https://mlp.fandom.com/wiki/Character_appearances

LEGEND  = {
    "Y": True,
    "S": True,
    "B": True,
    "F": True,
    "P": True,
    "M": False,
    "N": False,
}

CHARACTERS = (
    "Applejack",
    "Twilight_Sparkle",
    "Fluttershy",
    "Rarity",
    "Pinkie_Pie",
    "Rainbow_Dash",
)

MLPWIKIA_URLROOT = "https://mlp.fandom.com/wiki/%s"

CSS_SELECTOR_ROOT = ".appearances.wikitable td.appear-%s"

def count_appearances(character):
    """
    """
    url = MLPWIKIA_URLROOT % character
    logging.debug("Sending GET to %s", url)
    response = r.get(url)
    logging.debug("Response code: %d", response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    #print(soup)
    num_appearances = 0
    for code, does_appear in LEGEND.items():
        if not does_appear:
            continue
        selector = CSS_SELECTOR_ROOT % code.lower()
        resultset = soup.css.select(selector)
        num_appearances += len(resultset)
    logging.info(
        "%s appears a total of %d times in the main MLP G4 series.",
        character, num_appearances,
    )
    return num_appearances

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    for character in CHARACTERS:
        count_appearances(character)
