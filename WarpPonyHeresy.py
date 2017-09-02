import pandas as pd
pony_heresy = pd.DataFrame({
                            "characters":["Kamatoznik_aka_otec", "False Impi aka Zombi", "Horus Heretic", "Me"],
                            "life_story": ["ne smog v statu 60%", "Ne pomog nabit staty", "Otovaril Impi vwi", "Chaos_Pony"],
                            "location": ["somewhere on Terra", "somewhere on Terra", "somehere in Warp", "somewhere in Warp"],
                            "status": ["love with Impi", "ignore love because dead", "Warp Dust", "Study in Warp and Python"],
                            "honor": ["zero and low", "better that a zero", "glory days passed", "still like Horus glory days"],
                            "today": ["forum freak", "dead idiot", "past time hero", "Python data scienist"],
                            "price": [ 0, 0, "100500", "Dark crusade and some fun"],
                            "role": [0, 0, "Last man standing hero", "Pony with a chaos stuff"],
                            "IQ": [67, 68, "100+", "140+"],
                            "KPD": [ "write some stuff on forum", "dead idiot", "allmost done it!", "allmost free in Anaconda and pandas"],
                            "total": [ 0, 0, "my hero for all times", "in Warp"]
                            }, index= ["Terra", "Gold_Graveyard", "Dark_Warp", "Pony_Warp"])
pony_heresy.name = "Warp Fantasy"
pony_heresy.index.name = "Warp Palace of Chaos"
print(pony_heresy.info())
pony_heresy
pony_heresy.characters
pony_heresy.loc["Terra"]
pony_heresy.loc["Pony_Warp"]