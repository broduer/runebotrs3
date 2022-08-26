from utils.general import load_configuration


# URLs
BASE_URL = load_configuration()['urls']['wiki_url']
PRICEAPI_URL = load_configuration()['urls']['priceapi_url']
GRAPHAPI_URL = load_configuration()['urls']['graphapi_url']

# HEADERS
HEADERS = load_configuration()['headers']

# COMMON THUMBNAILS
BUCKET_ICO = 'https://runescape.wiki/images/thumb/Weird_gloop_detail.png/100px-Weird_gloop_detail.png?b452e'
QUEST_ICO = 'https://runescape.wiki/images/Quest_Icon_Crest.png?98216'
MINIGAME_ICO = 'https://runescape.wiki/images/Manual_Activites.png?41df1'