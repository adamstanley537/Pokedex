from simple_image import Downloader
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

pokemon = os.listdir("/Users/adam/Portfolio/Pokedex/PokemonData")
path = "/Users/adam/Portfolio/Pokedex/PokeData/simple_images"
poke_list = os.listdir(path)
poke_dict = {}
limits = {}
for poke in pokemon:
    if poke == '.DS_Store':
        pass
    else:
        if len(os.listdir("/Users/adam/Portfolio/Pokedex/PokemonData/" + poke)) < 175:
            limits[poke] = 175 - len(os.listdir("/Users/adam/Portfolio/Pokedex/PokemonData/" + poke))

# poke_pd = pd.DataFrame.from_dict(poke_dict, orient="index")
# poke_pd.columns = ["count"]
# poke_pd = poke_pd.sort_values(by="count",  ascending=True)
# print(poke_pd)
desired_number = 300

path = "/Users/adam/Portfolio/Pokedex/PokeData/simple_images"
poke_list = os.listdir(path)


print(limits)

response= Downloader()

for poke in limits:
    keywords = poke + "-pokemon"
    response.download(keywords=keywords, limit=limits[poke]+20)
    print(keywords)

