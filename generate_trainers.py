"""
Script de génération automatique de trainers pour RCT Override
Génère des trainers avec des Pokémon et moves valides de Cobblemon
"""

import json
import os
from pathlib import Path
from typing import List, Dict

# ============================================================================
# DONNÉES POKÉMON COBBLEMON
# ============================================================================

# Pokémon disponibles dans Cobblemon par génération (Gen 1-9)
POKEMON_BY_LEVEL = {
    # Niveau 5-15 (Starter)
    "starter": [
        "bulbasaur", "charmander", "squirtle", "pikachu", "rattata", "pidgey", "spearow",
        "ekans", "sandshrew", "nidoran_m", "nidoran_f", "vulpix", "oddish", "paras",
        "venonat", "meowth", "psyduck", "mankey", "growlithe", "poliwag", "machop",
        "bellsprout", "geodude", "ponyta", "magnemite", "caterpie", "weedle", "kakuna",
        "metapod", "butterfree", "beedrill", "sentret", "hoothoot", "ledyba", "spinarak",
        "mareep", "hoppip", "sunkern", "chikorita", "cyndaquil", "totodile", "poochyena",
        "zigzagoon", "taillow", "seedot", "ralts", "azurill", "skitty", "aron",
        "electrike", "budew", "cherubi", "starly", "bidoof", "kricketot", "roggenrola",
        "patrat", "lillipup", "pidove", "sewaddle", "venipede", "fletchling", "scatterbug",
        "bunnelby", "skiddo", "pikipek", "yungoos", "grubbin", "rookidee", "blipbug",
        "wooloo", "nickit", "lechonk", "tarountula", "nymble", "pawmi", "sprigatito",
        "fuecoco", "quaxly", "smoliv"
    ],
    
    # Niveau 35-45 (Intermédiaire)
    "intermediate": [
        "venusaur", "charizard", "blastoise", "raichu", "sandslash", "nidoking", "nidoqueen",
        "ninetales", "vileplume", "parasect", "venomoth", "golduck", "primeape", "arcanine",
        "poliwrath", "alakazam", "machamp", "golem", "rapidash", "magneton", "gengar",
        "exeggutor", "marowak", "hitmonlee", "hitmonchan", "starmie", "scyther", "jynx",
        "electabuzz", "magmar", "gyarados", "vaporeon", "jolteon", "flareon", "espeon",
        "umbreon", "feraligatr", "typhlosion", "meganium", "ampharos", "azumarill", "sudowoodo",
        "politoed", "jumpluff", "sunflora", "quagsire", "forretress", "granbull", "scizor",
        "heracross", "ursaring", "magcargo", "piloswine", "donphan", "stantler", "houndoom",
        "blaziken", "swampert", "sceptile", "mightyena", "linoone", "ludicolo", "shiftry",
        "swellow", "gardevoir", "breloom", "slaking", "ninjask", "exploud", "hariyama",
        "aggron", "medicham", "manectric", "roserade", "rampardos", "bastiodon", "vespiquen",
        "floatzel", "cherrim", "gastrodon", "drifblim", "lopunny", "toxicroak", "carnivine",
        "lumineon", "abomasnow", "emboar", "samurott", "serperior", "watchog", "stoutland",
        "unfezant", "zebstrika", "gigalith", "swoobat", "excadrill", "audino", "conkeldurr",
        "seismitoad", "leavanny", "scolipede", "whimsicott", "lilligant", "basculin",
        "krookodile", "darmanitan", "maractus", "crustle", "scrafty", "zoroark", "gothitelle",
        "reuniclus", "swanna", "vanilluxe", "sawsbuck", "escavalier", "amoonguss", "jellicent",
        "galvantula", "ferrothorn", "klinklang", "eelektross", "beheeyem", "chandelure",
        "haxorus", "beartic", "cryogonal", "accelgor", "stunfisk", "mienshao", "druddigon",
        "braviary", "mandibuzz", "durant", "volcarona"
    ],
    
    # Niveau 60-75 (Avancé)
    "advanced": [
        "dragonite", "tyranitar", "salamence", "metagross", "garchomp", "lucario", "togekiss",
        "mamoswine", "gallade", "yanmega", "leafeon", "glaceon", "gliscor", "porygon-z",
        "electivire", "magmortar", "rhyperior", "tangrowth", "lickilicky", "magnezone",
        "honchkrow", "mismagius", "weavile", "froslass", "rotom", "hydreigon", "volcarona",
        "reshiram", "zekrom", "kyurem", "chesnaught", "delphox", "greninja", "talonflame",
        "vivillon", "pyroar", "florges", "gogoat", "pangoro", "aegislash", "aromatisse",
        "slurpuff", "malamar", "barbaracle", "dragalge", "clawitzer", "heliolisk", "tyrantrum",
        "aurorus", "sylveon", "hawlucha", "dedenne", "carbink", "goodra", "klefki",
        "trevenant", "gourgeist", "avalugg", "noivern", "decidueye", "incineroar", "primarina",
        "toucannon", "gumshoos", "vikavolt", "crabominable", "oricorio", "ribombee",
        "lycanroc", "wishiwashi", "toxapex", "mudsdale", "araquanid", "lurantis", "shiinotic",
        "salazzle", "bewear", "tsareena", "comfey", "oranguru", "passimian", "golisopod",
        "palossand", "pyukumuku", "silvally", "minior", "komala", "turtonator", "togedemaru",
        "mimikyu", "bruxish", "drampa", "dhelmise", "kommo-o", "rillaboom", "cinderace",
        "inteleon", "corviknight", "orbeetle", "drednaw", "boltund", "coalossal", "flapple",
        "appletun", "sandaconda", "cramorant", "barraskewda", "toxtricity", "centiskorch",
        "grapploct", "polteageist", "hatterene", "grimmsnarl", "obstagoon", "perrserker",
        "cursola", "sirfetchd", "runerigus", "alcremie", "falinks", "pincurchin", "frosmoth",
        "stonjourner", "eiscue", "indeedee", "morpeko", "copperajah", "dracozolt", "arctozolt",
        "dracovish", "arctovish", "duraludon", "dragapult"
    ],
    
    # Niveau 85-100 (Légendaire)
    "legendary": [
        "articuno", "zapdos", "moltres", "dragonite", "mewtwo", "mew", "raikou", "entei",
        "suicune", "lugia", "ho-oh", "celebi", "regirock", "regice", "registeel", "latias",
        "latios", "kyogre", "groudon", "rayquaza", "jirachi", "deoxys", "uxie", "mesprit",
        "azelf", "dialga", "palkia", "heatran", "regigigas", "giratina", "cresselia",
        "phione", "manaphy", "darkrai", "shaymin", "arceus", "victini", "cobalion", "terrakion",
        "virizion", "tornadus", "thundurus", "reshiram", "zekrom", "landorus", "kyurem",
        "keldeo", "meloetta", "genesect", "xerneas", "yveltal", "zygarde", "diancie",
        "hoopa", "volcanion", "tapu_koko", "tapu_lele", "tapu_bulu", "tapu_fini", "cosmog",
        "cosmoem", "solgaleo", "lunala", "nihilego", "buzzwole", "pheromosa", "xurkitree",
        "celesteela", "kartana", "guzzlord", "necrozma", "magearna", "marshadow", "zeraora",
        "meltan", "melmetal", "zacian", "zamazenta", "eternatus", "kubfu", "urshifu",
        "zarude", "regieleki", "regidrago", "glastrier", "spectrier", "calyrex", "enamorus",
        "koraidon", "miraidon", "wo-chien", "chien-pao", "ting-lu", "chi-yu", "roaring_moon",
        "iron_valiant", "walking_wake", "iron_leaves", "gouging_fire", "raging_bolt",
        "iron_boulder", "iron_crown", "terapagos", "pecharunt"
    ]
}

# Moves valides pour Cobblemon (noms en minuscule sans espaces/tirets)
COMMON_MOVES = {
    # Moves physiques
    "physical": [
        "tackle", "scratch", "pound", "quickattack", "bite", "headbutt", "bodyslam",
        "doubleedge", "takedown", "thrash", "slam", "megakick", "megapunch", "strength",
        "cut", "rocksmash", "extremespeed", "facade", "return", "frustration", "secretpower",
        "earthquake", "dig", "bulldoze", "bonemerang", "boneclub", "bonerush",
        "waterfall", "aquajet", "dive", "liquidation",
        "flareblitz", "firepunch", "flamethrower", "ember", "firefang",
        "iceshard", "icepunch", "iciclecrash", "avalanche",
        "thunderpunch", "voltswitch", "wildcharge", "thunderfang",
        "rocktomb", "rockslide", "stoneedge", "rockblast",
        "shadowpunch", "shadowclaw", "shadowsneak",
        "aerialace", "airslash", "bravebird", "drillpeck", "pluck",
        "poisonjab", "crosspoison", "gunkshot", "sludgebomb",
        "bugbite", "xscissor", "uturn", "megahorn",
        "metalclaw", "ironhead", "flashcannon", "bulletpunch", "meteormash",
        "dragonrush", "dragonclaw", "outrage", "dracometeor",
        "brickbreak", "closecombat", "drainpunch", "focuspunch", "hammerarm",
        "highjumpkick", "karatechop", "lowkick", "machpunch", "superpower",
        "psychocut", "zenheadbutt",
        "leafblade", "powerwhip", "seedbomb", "woodhammer",
        "crunch", "knockoff", "pursuit", "suckerpunch", "payback",
        "playrough", "moonblast", "dazzlinggleam"
    ],
    
    # Moves spéciaux
    "special": [
        "watergun", "hydropump", "surf", "scald", "muddywater", "waterpulse",
        "fireblast", "flamethrower", "ember", "heatwave", "lavaplume", "overheat",
        "blizzard", "icebeam", "frostbreath", "powdersn ow", "glaciate",
        "thunder", "thunderbolt", "discharge", "shockwave", "thundershock", "voltswitch",
        "earthpower", "mudshot", "mudbomb",
        "rockblast", "powergem", "ancientpower",
        "shadowball", "darkpulse", "nightdaze",
        "airslash", "hurricane", "gust",
        "sludgebomb", "sludgewave", "venoshock", "acid",
        "bugbuzz", "signalbeam",
        "flashcannon", "steelbeam",
        "dragonpulse", "dracometeor", "dragonbreath", "spacialrend",
        "aurasphere", "focusblast",
        "psychic", "psyshock", "psybeam", "confusion", "extrasensory", "futuresight",
        "energyball", "gigadrain", "grassknot", "leafstorm", "magicalleaf", "petaldance",
        "solarbeam", "seedflare",
        "dazzlinggleam", "moonblast", "drainingkiss",
        "hyperbeam", "hypervoice", "boomburst", "triattack", "swift"
    ],
    
    # Moves de statut
    "status": [
        "swordsdance", "dragondance", "nastyplot", "calmmind", "bulkup", "cosmicpower",
        "amnesia", "agility", "rockpolish", "autotomize", "quiverdance",
        "thunderwave", "toxic", "willowisp", "stunspore", "sleeppowder", "spore",
        "leechseed", "substitute", "protect", "detect", "endure",
        "recover", "roost", "rest", "sleeptalk", "softboiled", "synthesis", "moonlight",
        "wish", "healingwish", "lunardance",
        "stealthrock", "spikes", "toxicspikes", "stickyweb",
        "reflect", "lightscreen", "safeguard", "tailwind",
        "taunt", "torment", "encore", "disable",
        "sandstorm", "sunnyday", "raindance", "hail"
    ]
}

# Combinaison de moves par type de Pokémon
MOVE_COMBINATIONS = {
    "fire": ["flareblitz", "fireblast", "flamethrower", "overheat", "willowisp", "sunnyday"],
    "water": ["waterfall", "hydropump", "surf", "scald", "aquajet", "raindance"],
    "grass": ["leafblade", "energyball", "gigadrain", "leafstorm", "synthesis", "leechseed"],
    "electric": ["thunderbolt", "wildcharge", "voltswitch", "thunderwave", "discharge"],
    "ice": ["icebeam", "iciclecrash", "blizzard", "iceshard", "avalanche"],
    "fighting": ["closecombat", "drainpunch", "highjumpkick", "machpunch", "bulkup"],
    "poison": ["sludgebomb", "poisonjab", "toxic", "venoshock", "gunkshot"],
    "ground": ["earthquake", "earthpower", "bulldoze", "stealthrock"],
    "flying": ["bravebird", "hurricane", "airslash", "aerialace", "roost"],
    "psychic": ["psychic", "psyshock", "zenheadbutt", "calmmind", "futuresight"],
    "bug": ["xscissor", "bugbuzz", "uturn", "megahorn", "quiverdance"],
    "rock": ["stoneedge", "rockslide", "powergem", "stealthrock"],
    "ghost": ["shadowball", "shadowclaw", "shadowsneak", "willowisp"],
    "dragon": ["outrage", "dracometeor", "dragonpulse", "dragondance", "dragonclaw"],
    "dark": ["crunch", "darkpulse", "knockoff", "suckerpunch", "nastyplot"],
    "steel": ["flashcannon", "ironhead", "bulletpunch", "meteormash"],
    "fairy": ["moonblast", "playrough", "dazzlinggleam"]
}

# ============================================================================
# GÉNÉRATEUR DE TRAINERS
# ============================================================================

class TrainerGenerator:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Créer les sous-dossiers par catégorie
        self.category_dirs = {
            "starter": self.output_dir / "starter",
            "intermediate": self.output_dir / "intermediate",
            "advanced": self.output_dir / "advanced",
            "legendary": self.output_dir / "legendary"
        }
        for dir_path in self.category_dirs.values():
            dir_path.mkdir(parents=True, exist_ok=True)
        
    def generate_trainer_names(self, count: int, trainer_class: str) -> List[str]:
        """Génère des noms de trainers uniques"""
        names = {
            "YOUNGSTER": ["Joey", "Tim", "Calvin", "Ben", "Chad", "Samuel", "Tyler", "Dan", "Eddie", "Frank",
                          "Gary", "Harry", "Ian", "James", "Kevin", "Leo", "Mike", "Nick", "Owen", "Pete",
                          "Quinn", "Ryan", "Steve", "Tom", "Ugo", "Victor", "Wayne", "Xander", "Yuri", "Zack"],
            "LASS": ["Anna", "Lily", "Robin", "Iris", "Valerie", "Michelle", "Andrea", "Betty", "Clara", "Diana",
                     "Emma", "Fiona", "Grace", "Hannah", "Ivy", "Julia", "Kate", "Laura", "Mary", "Nancy",
                     "Olivia", "Paula", "Rachel", "Sarah", "Tina", "Uma", "Vera", "Wendy", "Xena", "Yuki"],
            "CAMPER": ["Liam", "Todd", "Ricky", "Justin", "Ethan", "Adam", "Blake", "Craig", "Derek", "Eric",
                       "Felix", "Greg", "Henry", "Isaac", "Jake", "Kyle", "Lucas", "Mason", "Nathan", "Oscar",
                       "Paul", "Quincy", "Robert", "Sean", "Travis", "Ulrich", "Vincent", "Walter", "Xavier", "Zane"],
            "PICNICKER": ["Emma", "Dana", "Sophie", "Gina", "Kelsey", "Alice", "Bella", "Chloe", "Daisy", "Ella",
                          "Faith", "Gwen", "Holly", "Iris", "Jane", "Kim", "Lily", "Mia", "Nina", "Pam",
                          "Rose", "Sally", "Tara", "Violet", "Willow", "Yasmin", "Zoe", "Amy", "Brooke", "Carol"],
            "ACE_TRAINER": ["Sophia", "Maria", "Diana", "Alex", "Blake", "Cameron", "Drake", "Elena", "Felix",
                            "Grace", "Hunter", "Irene", "Jason", "Karen", "Lance", "Morgan", "Nicole", "Oscar",
                            "Patricia", "Quinn", "Riley", "Samuel", "Tracy", "Uma", "Victor", "Wanda", "Xavier",
                            "Yolanda", "Zachary", "Aaron"],
            "COOLTRAINER": ["Jake", "Ryker", "Austin", "Brady", "Casey", "Dylan", "Evan", "Finn", "Grant",
                            "Hudson", "Ivan", "Jordan", "Keith", "Logan", "Marcus", "Noah", "Oliver", "Parker",
                            "Quentin", "Reed", "Scott", "Tyler", "Uriah", "Vance", "Wesley", "Wyatt", "York",
                            "Zeke", "Alex", "Brock"],
            "SWIMMER": ["Marina", "Crystal", "Aqua", "Bay", "Coral", "Dawn", "Eve", "Finn", "Gulf", "Harbor",
                        "Isle", "Joy", "Kai", "Lake", "Maya", "Nami", "Ocean", "Pearl", "Quinn", "River",
                        "Sea", "Tide", "Uma", "Vera", "Wave", "Xyla", "Yara", "Zephyr", "Aria", "Brook"],
            "HIKER": ["Eric", "Russell", "Alan", "Bob", "Clark", "Doug", "Earl", "Frank", "Gary", "Hank",
                      "Ivan", "Jack", "Ken", "Larry", "Mike", "Norm", "Otto", "Pete", "Quincy", "Ralph",
                      "Stan", "Ted", "Ulrich", "Vince", "Walt", "Xavier", "Yale", "Zach", "Andy", "Brad"],
            "BEAUTY": ["Isabella", "Bridget", "Amanda", "Bianca", "Carmen", "Donna", "Elaine", "Francine",
                       "Georgia", "Helen", "Irene", "Jessica", "Katherine", "Linda", "Monica", "Natalie",
                       "Olga", "Priscilla", "Queen", "Rita", "Samantha", "Teresa", "Ursula", "Victoria",
                       "Wanda", "Xandra", "Yvonne", "Zelda", "April", "Beth"],
            "VETERAN": ["Klaus", "Arnold", "Bruce", "Carter", "Douglas", "Edgar", "Franklin", "George",
                        "Harold", "Irving", "Jerome", "Kenneth", "Leonard", "Martin", "Norman", "Oswald",
                        "Patrick", "Quinton", "Richard", "Stanley", "Theodore", "Ulysses", "Vernon", "Wallace",
                        "Xavier", "Yale", "Zachary", "Abraham", "Bernard", "Chester"],
            "DRAGON_TAMER": ["Ryuu", "Drayden", "Clair", "Lance", "Iris", "Drake", "Raihan", "Zinnia",
                             "Hazel", "Darius", "Kaida", "Ryu", "Drago", "Tatsu", "Shenron", "Bahamut",
                             "Tiamat", "Falkor", "Spyro", "Toothless", "Smaug", "Alduin", "Deathwing",
                             "Nidhogg", "Fafnir", "Ladon", "Vritra", "Yamata", "Apophis", "Leviathan"],
            "BLACKBELT": ["Ken", "Bruno", "Hitoshi", "Kenji", "Koichi", "Takeshi", "Akira", "Ryu",
                          "Makoto", "Hiroshi", "Masaru", "Takao", "Haruki", "Daiki", "Shiro", "Kenta",
                          "Tetsuo", "Kazuo", "Noboru", "Satoshi", "Yuki", "Jin", "Hideo", "Minoru",
                          "Osamu", "Raiden", "Bruce", "Chuck", "Brawly", "Maylene"],
            "ELITE_FOUR": ["Lorelei", "Bruno", "Agatha", "Lance", "Will", "Koga", "Karen", "Sidney",
                           "Phoebe", "Glacia", "Drake", "Aaron", "Bertha", "Flint", "Lucian", "Shauntal",
                           "Marshal", "Grimsley", "Caitlin", "Malva", "Siebold", "Wikstrom", "Drasna",
                           "Hala", "Olivia", "Acerola", "Kahili", "Rika", "Poppy", "Larry", "Hassel"],
            "CHAMPION": ["Aurora", "Blue", "Red", "Steven", "Wallace", "Cynthia", "Alder", "Iris",
                         "Diantha", "Kukui", "Hau", "Leon", "Nemona", "Geeta", "Lance", "Gary", "Trace",
                         "N", "Ghetsis", "Lysandre", "Guzma", "Rose", "Volo", "Kieran", "Drayton"],
            "FRONTIER_BRAIN": ["Palmer", "Noland", "Greta", "Tucker", "Lucy", "Spenser", "Brandon",
                               "Anabel", "Thorton", "Dahlia", "Darach", "Argenta"]
        }
        
        base_names = names.get(trainer_class, ["Trainer"] * 30)
        return base_names[:count]
    
    def get_pokemon_moves(self, pokemon: str, level: int) -> List[str]:
        """Retourne 4 moves appropriés pour un Pokémon selon son niveau"""
        # Détermine le type principal du Pokémon (simplifié)
        type_mapping = {
            "fire": ["charmander", "charmeleon", "charizard", "vulpix", "ninetales", "growlithe", "arcanine",
                     "ponyta", "rapidash", "flareon", "cyndaquil", "quilava", "typhlosion", "houndour",
                     "houndoom", "torchic", "combusken", "blaziken", "numel", "camerupt"],
            "water": ["squirtle", "wartortle", "blastoise", "psyduck", "golduck", "poliwag", "poliwhirl",
                      "poliwrath", "tentacool", "tentacruel", "goldeen", "seaking", "magikarp", "gyarados",
                      "vaporeon", "totodile", "croconaw", "feraligatr", "marill", "azumarill"],
            "grass": ["bulbasaur", "ivysaur", "venusaur", "oddish", "gloom", "vileplume", "paras", "parasect",
                      "bellsprout", "weepinbell", "victreebel", "exeggcute", "exeggutor", "chikorita", "bayleef",
                      "meganium", "hoppip", "skiploom", "jumpluff", "sunkern", "sunflora"],
            "electric": ["pikachu", "raichu", "magnemite", "magneton", "voltorb", "electrode", "electabuzz",
                         "jolteon", "mareep", "flaaffy", "ampharos", "electrike", "manectric", "plusle", "minun"],
            "psychic": ["abra", "kadabra", "alakazam", "drowzee", "hypno", "exeggcute", "exeggutor", "starmie",
                        "jynx", "espeon", "natu", "xatu", "ralts", "kirlia", "gardevoir", "meditite", "medicham"],
            "dragon": ["dratini", "dragonair", "dragonite", "kingdra", "bagon", "shelgon", "salamence",
                       "latias", "latios", "rayquaza", "garchomp", "dialga", "palkia", "giratina", "hydreigon"]
        }
        
        # Trouve le type du Pokémon
        pokemon_type = "normal"
        for ptype, poke_list in type_mapping.items():
            if pokemon.lower() in poke_list:
                pokemon_type = ptype
                break
        
        # Sélectionne des moves appropriés
        available_moves = MOVE_COMBINATIONS.get(pokemon_type, COMMON_MOVES["physical"][:6])
        
        # Ajoute des moves de base pour les bas niveaux
        if level < 20:
            basic_moves = ["tackle", "quickattack", "scratch", "bite", "watergun", "ember"]
            moves = basic_moves[:2] + available_moves[:2]
        else:
            moves = available_moves[:4]
        
        return moves[:4]
    
    def generate_pokemon_team(self, category: str, trainer_level: int, team_size: int) -> List[Dict]:
        """Génère une équipe de Pokémon pour un trainer"""
        pokemon_pool = POKEMON_BY_LEVEL.get(category, POKEMON_BY_LEVEL["starter"])
        team = []
        
        import random
        selected_pokemon = random.sample(pokemon_pool, min(team_size, len(pokemon_pool)))
        
        for i, pokemon in enumerate(selected_pokemon):
            level = trainer_level + random.randint(-2, 2)
            moves = self.get_pokemon_moves(pokemon, level)
            
            mon = {
                "pokemon": pokemon,
                "level": level,
                "gender": random.choice(["male", "female"]) if "nidoran" not in pokemon else pokemon.split("_")[1],
                "moves": moves[:4],
                "ability": self.get_random_ability(pokemon),
                "nature": random.choice(["adamant", "jolly", "modest", "timid", "bold", "calm", "careful", "impish"])
            }
            
            # Ajoute EVs/IVs pour niveaux élevés
            if category in ["intermediate", "advanced", "legendary"]:
                mon["evs"] = self.generate_evs(category)
                mon["ivs"] = self.generate_ivs(category)
            
            # Ajoute un item tenu pour niveaux moyens/élevés
            if category in ["intermediate", "advanced", "legendary"]:
                mon["held_item"] = self.get_held_item(category)
            
            team.append(mon)
        
        return team
    
    def get_random_ability(self, pokemon: str) -> str:
        """Retourne une ability commune"""
        abilities = ["overgrow", "blaze", "torrent", "swarm", "keeneye", "compoundeyes",
                     "intimidate", "static", "flashfire", "waterabsorb", "voltabsorb",
                     "levitate", "sturdy", "pressure", "magicguard", "multiscale"]
        import random
        return random.choice(abilities)
    
    def generate_evs(self, category: str) -> Dict:
        """Génère des EVs selon la catégorie"""
        if category == "intermediate":
            return {"hp": 100, "attack": 100, "defense": 0, "special_attack": 100,
                    "special_defense": 4, "speed": 100}
        elif category in ["advanced", "legendary"]:
            return {"hp": 252, "attack": 252, "defense": 0, "special_attack": 0,
                    "special_defense": 4, "speed": 252}
        return {}
    
    def generate_ivs(self, category: str) -> Dict:
        """Génère des IVs selon la catégorie"""
        if category == "intermediate":
            return {"hp": 24, "attack": 24, "defense": 24, "special_attack": 24,
                    "special_defense": 24, "speed": 24}
        elif category in ["advanced", "legendary"]:
            return {"hp": 31, "attack": 31, "defense": 31, "special_attack": 31,
                    "special_defense": 31, "speed": 31}
        return {}
    
    def get_held_item(self, category: str) -> str:
        """Retourne un item tenu selon la catégorie"""
        import random
        items = {
            "intermediate": ["sitrusberry", "lumberry", "choiceband", "choicescarf", "lifeorb"],
            "advanced": ["leftovers", "lifeorb", "choiceband", "choicescarf", "choicespecs",
                         "focussash", "assaultvest", "lumberry", "weaknesspolicy"],
            "legendary": ["leftovers", "lifeorb", "choiceband", "choicescarf", "choicespecs",
                          "focussash", "assaultvest", "weaknesspolicy", "lumberry", "sitrusberry"]
        }
        return random.choice(items.get(category, ["lumberry"]))
    
    def generate_trainer(self, name: str, trainer_class: str, category: str, level: int) -> Dict:
        """Génère un trainer complet"""
        # Configuration AI selon catégorie
        ai_config = {
            "starter": {"intelligence": 0.3, "switch_chance": 0.1},
            "intermediate": {"intelligence": 0.6, "switch_chance": 0.35},
            "advanced": {"intelligence": 0.8, "switch_chance": 0.6},
            "legendary": {"intelligence": 1.0, "switch_chance": 0.9}
        }
        
        # Taille de l'équipe selon catégorie
        team_sizes = {
            "starter": [1, 2, 3],
            "intermediate": [3, 3, 4],
            "advanced": [4, 5, 6],
            "legendary": [6, 6, 6]
        }
        
        import random
        team_size = random.choice(team_sizes[category])
        
        # Win money selon niveau
        win_money = {
            "starter": 50 + level * 5,
            "intermediate": 250 + level * 10,
            "advanced": 500 + level * 15,
            "legendary": 2000 + level * 20
        }
        
        # Potions selon catégorie
        potions = {
            "starter": {"item": "cobblemon:potion", "count": 1},
            "intermediate": {"item": "cobblemon:hyper_potion", "count": 2},
            "advanced": {"item": "cobblemon:max_potion", "count": 2},
            "legendary": {"item": "cobblemon:full_restore", "count": 5}
        }
        
        trainer = {
            "name": name,
            "trainer_class": trainer_class,
            "win_money_base": win_money[category],
            "ai": ai_config[category],
            "team": self.generate_pokemon_team(category, level, team_size),
            "bag": [potions[category]],
            "defeat_actions": [
                {"type": "give_money", "amount": win_money[category] * 2},
                {"type": "give_exp", "multiplier": 1.0 + (level / 100)}
            ]
        }
        
        # Ajoute des récompenses spéciales pour catégories élevées
        if category in ["advanced", "legendary"]:
            trainer["defeat_actions"].append({
                "type": "give_item",
                "item": "cobblemon:rare_candy",
                "count": 2 if category == "advanced" else 5
            })
        
        if category == "legendary":
            trainer["defeat_actions"].append({
                "type": "give_item",
                "item": "cobblemon:ability_patch",
                "count": 1
            })
        
        return trainer
    
    def save_trainer(self, trainer: Dict, filename: str, category: str):
        """Sauvegarde un trainer dans un fichier JSON dans le bon sous-dossier"""
        category_dir = self.category_dirs[category]
        filepath = category_dir / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(trainer, f, indent=2, ensure_ascii=False)
        print(f"✓ Créé: {category}/{filename}")
    
    def generate_category(self, category: str, trainer_class: str, count: int, base_level: int):
        """Génère plusieurs trainers pour une catégorie"""
        print(f"\n=== Génération de {count} {trainer_class} ({category}) ===")
        names = self.generate_trainer_names(count, trainer_class)
        
        for i, name in enumerate(names):
            import random
            level = base_level + random.randint(-2, 2)
            trainer = self.generate_trainer(f"{trainer_class.replace('_', ' ').title()} {name}",
                                           trainer_class, category, level)
            filename = f"{trainer_class.lower()}_{name.lower()}.json"
            self.save_trainer(trainer, filename, category)

# ============================================================================
# FONCTION PRINCIPALE
# ============================================================================

def main():
    print("=" * 70)
    print("GÉNÉRATEUR DE TRAINERS RCT OVERRIDE")
    print("=" * 70)
    
    # Chemin de sortie
    script_dir = Path(__file__).parent
    output_dir = script_dir / "data" / "rct_override" / "trainers"
    
    generator = TrainerGenerator(str(output_dir))
    
    print(f"\nRépertoire de sortie: {output_dir}")
    print("\nDébut de la génération...")

    # Génération des trainers par catégorie
    # generator.generate_category("{category}", "{trainer_class}", {count}, {base_level})
    
    # STARTER TRAINERS (niveau 5-15) 
    # generator.generate_category("starter", "BUG_CATCHER", 5, 8)
    # generator.generate_category("starter", "CAMPER", 5, 7)
    # generator.generate_category("starter", "FISHERMAN", 2, 9)
    # generator.generate_category("starter", "HIKER", 1, 10)
    # generator.generate_category("starter", "LASS", 7, 11)
    # generator.generate_category("starter", "PICNICKER", 5, 9)
    # generator.generate_category("starter", "SAILOR", 1, 15)
    # generator.generate_category("starter", "SCHOOLBOY", 1, 12)
    # generator.generate_category("starter", "TWINS", 1, 12)
    # generator.generate_category("starter", "YOUNGSTER", 7, 10)    
    
    # INTERMEDIATE TRAINERS (niveau 35-45) 
    # generator.generate_category("intermediate", "ACE_TRAINER", 10, 40)
    # generator.generate_category("intermediate", "COOLTRAINER", 10, 38)
    # generator.generate_category("intermediate", "SWIMMER", 5, 39)
    # generator.generate_category("intermediate", "HIKER", 5, 38)
    
    # ADVANCED TRAINERS (niveau 60-75) 
    # generator.generate_category("advanced", "VETERAN", 10, 65)
    # generator.generate_category("advanced", "DRAGON_TAMER", 8, 67)
    # generator.generate_category("advanced", "BLACKBELT", 7, 66)
    # generator.generate_category("advanced", "ELITE_FOUR", 5, 71)
    
    # LEGENDARY TRAINERS (niveau 85-100) 
    # generator.generate_category("legendary", "CHAMPION", 15, 92)
    # generator.generate_category("legendary", "FRONTIER_BRAIN", 10, 94)
    
    print("\n" + "=" * 70)
    print("GÉNÉRATION TERMINÉE !")
    print("=" * 70)
    print(f"\nTous les trainers ont été créés dans: {output_dir}")
    print("\nProchaine étape: Mettez à jour les pools de trainers pour inclure les nouveaux!")

if __name__ == "__main__":
    main()
