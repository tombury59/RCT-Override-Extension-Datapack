"""
Générateur de trainers au format RCT (Random Challenger Trainers)
Basé sur le mod RCT de Cobblemon
"""

import json
import os
import random
from pathlib import Path
from typing import List, Dict, Optional

# ============================================================================
# DONNÉES DE BASE
# ============================================================================

# Liste des natures Pokémon
NATURES = [
    "hardy", "lonely", "brave", "adamant", "naughty",
    "bold", "docile", "relaxed", "impish", "lax",
    "timid", "hasty", "serious", "jolly", "naive",
    "modest", "mild", "quiet", "bashful", "rash",
    "calm", "gentle", "sassy", "careful", "quirky"
]

# Liste des genres
GENDERS = ["MALE", "FEMALE"]

# Liste d'exemples de Pokémon par niveau de difficulté
POKEMON_DATABASE = {
    "starter": {  # Niveau 5-20
        "pokemon": [
            "bulbasaur", "charmander", "squirtle", "pikachu", "rattata", 
            "pidgey", "spearow", "ekans", "sandshrew", "nidoran_m", 
            "nidoran_f", "vulpix", "oddish", "meowth", "psyduck",
            "mankey", "growlithe", "poliwag", "machop", "geodude"
        ],
        "level_range": (5, 20)
    },
    "intermediate": {  # Niveau 20-40
        "pokemon": [
            "ivysaur", "charmeleon", "wartortle", "raichu", "sandslash",
            "nidoking", "nidoqueen", "ninetales", "vileplume", "golduck",
            "primeape", "arcanine", "poliwrath", "machoke", "graveler",
            "rapidash", "magneton", "haunter", "marowak", "hitmonlee"
        ],
        "level_range": (20, 40)
    },
    "advanced": {  # Niveau 40-60
        "pokemon": [
            "venusaur", "charizard", "blastoise", "alakazam", "machamp",
            "golem", "gengar", "starmie", "gyarados", "vaporeon",
            "jolteon", "flareon", "aerodactyl", "snorlax", "dragonite",
            "meganium", "typhlosion", "feraligatr", "ampharos", "heracross"
        ],
        "level_range": (40, 60)
    },
    "expert": {  # Niveau 60-80
        "pokemon": [
            "tyranitar", "blaziken", "swampert", "sceptile", "gardevoir",
            "aggron", "salamence", "metagross", "garchomp", "lucario",
            "togekiss", "mamoswine", "gallade", "serperior", "emboar",
            "samurott", "excadrill", "conkeldurr", "volcarona", "hydreigon"
        ],
        "level_range": (60, 80)
    },
    "legendary": {  # Niveau 80-100
        "pokemon": [
            "articuno", "zapdos", "moltres", "mewtwo", "raikou",
            "entei", "suicune", "lugia", "ho_oh", "regirock",
            "regice", "registeel", "latias", "latios", "rayquaza",
            "dialga", "palkia", "giratina", "reshiram", "zekrom"
        ],
        "level_range": (80, 100)
    }
}

# Base de données de moves par type d'attaque
MOVES_DATABASE = {
    "physical": [
        "tackle", "scratch", "pound", "quickattack", "megapunch", "megakick",
        "hyperbeam", "gigaimpact", "earthquake", "stoneedge", "ironhead",
        "takedown", "bodyslam", "doubleedge", "thrash", "crunch",
        "closecombat", "outrage", "dragonrush", "flareblitz", "wildcharge",
        "zenheadbutt", "icepunch", "thunderpunch", "firepunch", "shadowclaw"
    ],
    "special": [
        "ember", "watergun", "thundershock", "vinewhip", "confusion",
        "psybeam", "psychic", "fireblast", "hydropump", "thunder",
        "solarbeam", "blizzard", "icebeam", "thunderbolt", "flamethrower",
        "surf", "shadowball", "darkpulse", "dragonpulse", "focusblast",
        "energyball", "moonblast", "dazzlinggleam", "airslash", "flashcannon"
    ],
    "status": [
        "swordsdance", "growth", "agility", "recover", "rest",
        "toxic", "willowisp", "thunderwave", "sleeppowder", "stunspore",
        "roar", "whirlwind", "substitute", "protect", "detect",
        "calmmind", "nastyplot", "tailwind", "trickroom", "stealthrock"
    ]
}

# Capacités (abilities) communes
ABILITIES = [
    "overgrow", "blaze", "torrent", "swarm", "rockhead", "keeneye",
    "compoundeyes", "sturdy", "intimidate", "static", "voltabsorb",
    "waterabsorb", "flashfire", "pressure", "thickfat", "immunity",
    "innerfocus", "levitate", "soundproof", "effectspore", "syncronize"
]

# Items utilisables
ITEMS = [
    "cobblemon:oran_berry",
    "cobblemon:sitrus_berry",
    "cobblemon:lum_berry",
    "cobblemon:chesto_berry",
    "cobblemon:pecha_berry",
    "cobblemon:superb_remedy",
    "cobblemon:full_heal",
    "cobblemon:full_restore",
    "cobblemon:hyper_potion",
    "cobblemon:max_potion"
]

# Classes de dresseurs
TRAINER_CLASSES = {
    "ACE_TRAINER": "Ace Trainer",
    "BLACKBELT": "Blackbelt",
    "BUG_CATCHER": "Bug Catcher",
    "CAMPER": "Camper",
    "COOLTRAINER": "Cooltrainer",
    "FISHERMAN": "Fisherman",
    "HIKER": "Hiker",
    "LASS": "Lass",
    "PICNICKER": "Picnicker",
    "POKEMON_RANGER": "Pokémon Ranger",
    "PSYCHIC": "Psychic",
    "SCHOOLBOY": "Schoolboy",
    "SCIENTIST": "Scientist",
    "SWIMMER": "Swimmer",
    "YOUNGSTER": "Youngster",
    "ELITE_FOUR": "Elite Four",
    "GYM_LEADER": "Gym Leader",
    "CHAMPION": "Champion",
    "DRAGON_TAMER": "Dragon Tamer",
    "BIRD_KEEPER": "Bird Keeper",
    "BATTLE_GIRL": "Battle Girl",
    "BEAUTY": "Beauty",
    "BIKER": "Biker",
    "ENGINEER": "Engineer",
    "GENTLEMAN": "Gentleman",
    "JUGGLER": "Juggler",
    "NINJA": "Ninja",
    "POKEMON_BREEDER": "Pokémon Breeder",
    "ROCKET_GRUNT": "Rocket Grunt",
    "RUIN_MANIAC": "Ruin Maniac",
    "SAGE": "Sage",
    "SAILOR": "Sailor",
    "SUPER_NERD": "Super Nerd",
    "TWINS": "Twins",
    "VETERAN": "Veteran"
}

# Noms pour les dresseurs
TRAINER_NAMES = [
    "Abel", "Alice", "Bruno", "Cynthia", "Drake", "Elena", "Felix", "Gloria",
    "Hector", "Iris", "Jack", "Karen", "Lance", "Maria", "Nathan", "Olivia",
    "Paul", "Quinn", "Rosa", "Steven", "Tina", "Ulrich", "Victor", "Willow",
    "Xavier", "Yuki", "Zara", "Akira", "Beatrice", "Carlos", "Diana", "Eric"
]

# ============================================================================
# CLASSES
# ============================================================================

class PokemonTeamMember:
    """Représente un membre de l'équipe Pokémon"""
    
    def __init__(
        self,
        species: str,
        level: int,
        gender: Optional[str] = None,
        nature: Optional[str] = None,
        ability: Optional[str] = None,
        moveset: Optional[List[str]] = None,
        ivs: Optional[Dict[str, int]] = None,
        evs: Optional[Dict[str, int]] = None
    ):
        self.species = species
        self.level = level
        self.gender = gender or random.choice(GENDERS)
        self.nature = nature or random.choice(NATURES)
        self.ability = ability or random.choice(ABILITIES)
        self.moveset = moveset or self._generate_random_moveset()
        self.ivs = ivs or {}
        self.evs = evs or {}
    
    def _generate_random_moveset(self) -> List[str]:
        """Génère un moveset aléatoire de 4 moves"""
        all_moves = MOVES_DATABASE["physical"] + MOVES_DATABASE["special"] + MOVES_DATABASE["status"]
        return random.sample(all_moves, min(4, len(all_moves)))
    
    def to_dict(self) -> Dict:
        """Convertit en dictionnaire pour JSON"""
        return {
            "species": self.species,
            "gender": self.gender,
            "level": self.level,
            "nature": self.nature,
            "ability": self.ability,
            "moveset": self.moveset,
            "ivs": self.ivs,
            "evs": self.evs
        }


class Trainer:
    """Représente un dresseur RCT"""
    
    def __init__(
        self,
        name: str,
        team: List[PokemonTeamMember],
        ai_type: str = "rct",
        max_select_margin: float = 0.15,
        max_item_uses: int = 4,
        bag: Optional[List[Dict]] = None
    ):
        self.name = name
        self.team = team
        self.ai_type = ai_type
        self.max_select_margin = max_select_margin
        self.max_item_uses = max_item_uses
        self.bag = bag or [
            {
                "item": "cobblemon:superb_remedy",
                "quantity": 2
            }
        ]
    
    def to_dict(self) -> Dict:
        """Convertit en dictionnaire pour JSON"""
        return {
            "name": self.name,
            "ai": {
                "type": self.ai_type,
                "data": {
                    "maxSelectMargin": self.max_select_margin
                }
            },
            "battleRules": {
                "maxItemUses": self.max_item_uses
            },
            "bag": self.bag,
            "team": [member.to_dict() for member in self.team]
        }
    
    def to_json(self, indent: int = 2) -> str:
        """Convertit en JSON formaté"""
        return json.dumps(self.to_dict(), indent=indent)


# ============================================================================
# GÉNÉRATEURS
# ============================================================================

def calculate_team_size_from_level(level_min: int, level_max: int) -> int:
    """
    Calcule la taille de l'équipe basée sur le niveau avec une composante aléatoire
    
    Args:
        level_min: Niveau minimum
        level_max: Niveau maximum
    
    Returns:
        Taille de l'équipe (1-6)
    """
    avg_level = (level_min + level_max) / 2
    
    # Probabilités de base selon le niveau
    if avg_level < 15:
        # Bas niveau: 1-3 Pokémon (avec petite chance d'avoir plus)
        weights = [30, 40, 20, 7, 2, 1]  # 1-6 Pokémon
    elif avg_level < 30:
        # Niveau faible: 2-4 Pokémon (avec petite chance d'avoir plus)
        weights = [10, 30, 35, 15, 7, 3]  # 1-6 Pokémon
    elif avg_level < 50:
        # Niveau moyen: 3-4 Pokémon principalement
        weights = [5, 15, 30, 30, 15, 5]  # 1-6 Pokémon
    elif avg_level < 70:
        # Niveau avancé: 4-5 Pokémon principalement
        weights = [2, 5, 15, 30, 35, 13]  # 1-6 Pokémon
    else:
        # Niveau expert: 5-6 Pokémon principalement
        weights = [1, 2, 5, 15, 35, 42]  # 1-6 Pokémon
    
    # Sélection aléatoire basée sur les poids
    team_size = random.choices([1, 2, 3, 4, 5, 6], weights=weights)[0]
    
    return team_size


def generate_random_trainer(
    difficulty: str = "intermediate",
    team_size: int = 3,
    trainer_class: Optional[str] = None,
    trainer_name: Optional[str] = None,
    level_min: Optional[int] = None,
    level_max: Optional[int] = None
) -> Trainer:
    """
    Génère un dresseur aléatoire
    
    Args:
        difficulty: Niveau de difficulté (starter, intermediate, advanced, expert, legendary)
        team_size: Nombre de Pokémon dans l'équipe (1-6)
        trainer_class: Classe du dresseur (optionnel)
        trainer_name: Nom du dresseur (optionnel)
        level_min: Niveau minimum (optionnel, override difficulty)
        level_max: Niveau maximum (optionnel, override difficulty)
    
    Returns:
        Objet Trainer
    """
    # Récupérer les données de difficulté
    if level_min is None or level_max is None:
        difficulty_data = POKEMON_DATABASE.get(difficulty, POKEMON_DATABASE["intermediate"])
        if level_min is None:
            level_min = difficulty_data["level_range"][0]
        if level_max is None:
            level_max = difficulty_data["level_range"][1]
        available_pokemon = difficulty_data["pokemon"]
    else:
        # Si des niveaux personnalisés sont fournis, utiliser tous les Pokémon
        all_pokemon = []
        for tier_data in POKEMON_DATABASE.values():
            all_pokemon.extend(tier_data["pokemon"])
        available_pokemon = list(set(all_pokemon))  # Enlever les doublons
    
    # Générer le nom complet du dresseur
    if not trainer_class:
        trainer_class = random.choice(list(TRAINER_CLASSES.values()))
    elif trainer_class in TRAINER_CLASSES:
        trainer_class = TRAINER_CLASSES[trainer_class]
    
    if not trainer_name:
        trainer_name = random.choice(TRAINER_NAMES)
    
    full_name = f"{trainer_class} {trainer_name}"
    
    # Générer l'équipe
    team = []
    selected_pokemon = random.sample(available_pokemon, min(team_size, len(available_pokemon)))
    
    for pokemon_species in selected_pokemon:
        level = random.randint(level_min, level_max)
        
        # Sélectionner 4 moves aléatoires
        physical_moves = random.sample(MOVES_DATABASE["physical"], 2)
        special_moves = random.sample(MOVES_DATABASE["special"], 1)
        status_moves = random.sample(MOVES_DATABASE["status"], 1)
        moveset = physical_moves + special_moves + status_moves
        random.shuffle(moveset)
        
        pokemon = PokemonTeamMember(
            species=pokemon_species,
            level=level,
            moveset=moveset
        )
        team.append(pokemon)
    
    # Créer le dresseur
    trainer = Trainer(
        name=full_name,
        team=team,
        max_select_margin=random.uniform(0.1, 0.2),
        max_item_uses=random.randint(2, 6)
    )
    
    return trainer


def generate_custom_trainer(
    name: str,
    team_data: List[Dict],
    ai_config: Optional[Dict] = None,
    bag: Optional[List[Dict]] = None
) -> Trainer:
    """
    Génère un dresseur personnalisé
    
    Args:
        name: Nom complet du dresseur
        team_data: Liste de dictionnaires avec les données des Pokémon
        ai_config: Configuration de l'IA (optionnel)
        bag: Sac d'items (optionnel)
    
    Returns:
        Objet Trainer
    """
    # Créer l'équipe
    team = []
    for pokemon_data in team_data:
        pokemon = PokemonTeamMember(
            species=pokemon_data["species"],
            level=pokemon_data["level"],
            gender=pokemon_data.get("gender"),
            nature=pokemon_data.get("nature"),
            ability=pokemon_data.get("ability"),
            moveset=pokemon_data.get("moveset"),
            ivs=pokemon_data.get("ivs", {}),
            evs=pokemon_data.get("evs", {})
        )
        team.append(pokemon)
    
    # Configuration de l'IA
    ai_config = ai_config or {}
    max_select_margin = ai_config.get("maxSelectMargin", 0.15)
    max_item_uses = ai_config.get("maxItemUses", 4)
    
    # Créer le dresseur
    trainer = Trainer(
        name=name,
        team=team,
        max_select_margin=max_select_margin,
        max_item_uses=max_item_uses,
        bag=bag
    )
    
    return trainer


def save_trainer_to_file(trainer: Trainer, output_path: str):
    """Sauvegarde un dresseur dans un fichier JSON"""
    # Créer le répertoire si nécessaire
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Écrire le fichier JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(trainer.to_json())
    
    print(f"✓ Dresseur sauvegardé: {output_path}")


def generate_trainer_batch(
    count: int,
    output_dir: str,
    difficulty: str = "intermediate",
    team_size: Optional[int] = None,
    trainer_class: Optional[str] = None,
    level_min: Optional[int] = None,
    level_max: Optional[int] = None
):
    """
    Génère un batch de dresseurs
    
    Args:
        count: Nombre de dresseurs à générer
        output_dir: Répertoire de sortie
        difficulty: Niveau de difficulté
        team_size: Taille de l'équipe (None = auto basé sur niveau)
        trainer_class: Classe du dresseur (optionnel)
        level_min: Niveau minimum (optionnel)
        level_max: Niveau maximum (optionnel)
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Créer une liste de noms uniques
    used_names = set()
    available_names = TRAINER_NAMES.copy()
    random.shuffle(available_names)
    
    for i in range(count):
        # Si on a épuisé les noms, régénérer la liste
        if not available_names:
            available_names = TRAINER_NAMES.copy()
            random.shuffle(available_names)
        
        # Prendre un nom unique
        trainer_name = available_names.pop(0)
        
        # Calculer la taille de l'équipe si non spécifiée
        if team_size is None:
            # Utiliser les niveaux pour calculer la taille
            if level_min is not None and level_max is not None:
                calculated_team_size = calculate_team_size_from_level(level_min, level_max)
            else:
                difficulty_data = POKEMON_DATABASE.get(difficulty, POKEMON_DATABASE["intermediate"])
                lvl_min, lvl_max = difficulty_data["level_range"]
                calculated_team_size = calculate_team_size_from_level(lvl_min, lvl_max)
        else:
            calculated_team_size = team_size
        
        trainer = generate_random_trainer(
            difficulty=difficulty,
            team_size=calculated_team_size,
            trainer_class=trainer_class,
            trainer_name=trainer_name,
            level_min=level_min,
            level_max=level_max
        )
        
        # Générer un nom de fichier unique sans numéro
        filename = trainer.name.lower().replace(" ", "_").replace("é", "e") + ".json"
        filepath = os.path.join(output_dir, filename)
        
        # Si le fichier existe déjà, ajouter un suffixe
        counter = 1
        while os.path.exists(filepath):
            base_filename = trainer.name.lower().replace(" ", "_").replace("é", "e")
            filename = f"{base_filename}_{counter}.json"
            filepath = os.path.join(output_dir, filename)
            counter += 1
        
        save_trainer_to_file(trainer, filepath)
    
    print(f"\n✓ {count} dresseurs générés dans {output_dir}")


# ============================================================================
# FONCTION GENERATE PRINCIPALE
# ============================================================================

def generate(
    trainer_class: str,
    level_min: int,
    level_max: int,
    count: int,
    team_size: Optional[int] = None,
    output_dir: str = "output/generated"
):
    """
    Fonction principale de génération de dresseurs
    
    Args:
        trainer_class: Type de dresseur (ex: "DRAGON_TAMER", "ACE_TRAINER", etc.)
        level_min: Niveau minimum des Pokémon
        level_max: Niveau maximum des Pokémon
        count: Quantité de dresseurs à générer
        team_size: Taille de l'équipe (None = auto basé sur niveau, sinon 1-6)
        output_dir: Répertoire de sortie (par défaut "output/generated")
    
    Exemple:
        generate("DRAGON_TAMER", 71, 80, 8)
        generate("YOUNGSTER", 10, 15, 5, team_size=2)  # Force 2 Pokémon
    """
    print("=" * 60)
    print(f"GÉNÉRATION DE {count} DRESSEURS")
    print("=" * 60)
    print(f"Type: {trainer_class}")
    print(f"Niveaux: {level_min}-{level_max}")
    if team_size is None:
        print(f"Taille d'équipe: Auto (basée sur le niveau)")
    else:
        print(f"Taille d'équipe: {team_size}")
    print(f"Répertoire: {output_dir}")
    print("=" * 60)
    
    # Vérifier que la classe existe
    if trainer_class not in TRAINER_CLASSES:
        print(f"\n⚠️  Attention: '{trainer_class}' n'est pas dans la liste des classes prédéfinies")
        print(f"Classes disponibles: {', '.join(TRAINER_CLASSES.keys())}")
        print(f"Utilisation du nom tel quel...\n")
    
    # Générer les dresseurs
    generate_trainer_batch(
        count=count,
        output_dir=output_dir,
        team_size=team_size,
        trainer_class=trainer_class,
        level_min=level_min,
        level_max=level_max
    )
    
    print("\n✅ Génération terminée!")


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Fonction principale"""
    
    # ========================================================================
    # NIVEAU DÉBUTANT (5-20)
    # ========================================================================
    print("\n🌱 GÉNÉRATION DES DRESSEURS DÉBUTANTS (5-20)")
    generate("YOUNGSTER", 5, 12, 20, output_dir="data/rct_trainers/trainers/starter/youngster")
    generate("LASS", 5, 12, 20, output_dir="data/rct_trainers/trainers/starter/lass")
    generate("BUG_CATCHER", 8, 15, 20, output_dir="data/rct_trainers/trainers/starter/bug_catcher")
    generate("SCHOOLBOY", 10, 18, 20, output_dir="data/rct_trainers/trainers/starter/schoolboy")
    
    # ========================================================================
    # NIVEAU INTERMÉDIAIRE (20-40)
    # ========================================================================
    print("\n⚡ GÉNÉRATION DES DRESSEURS INTERMÉDIAIRES (20-40)")
    generate("CAMPER", 20, 30, 20, output_dir="data/rct_trainers/trainers/intermediate/camper")
    generate("PICNICKER", 20, 30, 20, output_dir="data/rct_trainers/trainers/intermediate/picnicker")
    generate("HIKER", 22, 35, 20, output_dir="data/rct_trainers/trainers/intermediate/hiker")
    generate("FISHERMAN", 22, 35, 20, output_dir="data/rct_trainers/trainers/intermediate/fisherman")
    generate("BEAUTY", 25, 38, 20, output_dir="data/rct_trainers/trainers/intermediate/beauty")
    generate("SWIMMER", 25, 38, 20, output_dir="data/rct_trainers/trainers/intermediate/swimmer")
    
    # ========================================================================
    # NIVEAU AVANCÉ (40-60)
    # ========================================================================
    print("\n🔥 GÉNÉRATION DES DRESSEURS AVANCÉS (40-60)")
    generate("ACE_TRAINER", 40, 55, 20, output_dir="data/rct_trainers/trainers/advanced/ace_trainer")
    generate("COOLTRAINER", 42, 55, 20, output_dir="data/rct_trainers/trainers/advanced/cooltrainer")
    generate("BLACKBELT", 40, 58, 20, output_dir="data/rct_trainers/trainers/advanced/blackbelt")
    generate("BATTLE_GIRL", 40, 58, 20, output_dir="data/rct_trainers/trainers/advanced/battle_girl")
    generate("PSYCHIC", 42, 56, 20, output_dir="data/rct_trainers/trainers/advanced/psychic")
    generate("SCIENTIST", 38, 52, 20, output_dir="data/rct_trainers/trainers/advanced/scientist")
    generate("BIRD_KEEPER", 40, 55, 20, output_dir="data/rct_trainers/trainers/advanced/bird_keeper")
    
    # ========================================================================
    # NIVEAU EXPERT (60-80)
    # ========================================================================
    print("\n💪 GÉNÉRATION DES DRESSEURS EXPERTS (60-80)")
    generate("VETERAN", 60, 75, 20, output_dir="data/rct_trainers/trainers/expert/veteran")
    generate("DRAGON_TAMER", 65, 78, 20, output_dir="data/rct_trainers/trainers/expert/dragon_tamer")
    generate("POKEMON_RANGER", 62, 75, 20, output_dir="data/rct_trainers/trainers/expert/pokemon_ranger")
    generate("POKEMON_BREEDER", 60, 72, 20, output_dir="data/rct_trainers/trainers/expert/pokemon_breeder")
    generate("NINJA", 64, 78, 20, output_dir="data/rct_trainers/trainers/expert/ninja")
    generate("RUIN_MANIAC", 62, 76, 20, output_dir="data/rct_trainers/trainers/expert/ruin_maniac")
    
    # ========================================================================
    # NIVEAU LÉGENDAIRE (80-100)
    # ========================================================================
    print("\n👑 GÉNÉRATION DES DRESSEURS LÉGENDAIRES (80-100)")
    generate("GYM_LEADER", 80, 90, 20, output_dir="data/rct_trainers/trainers/legendary/gym_leader")
    generate("ELITE_FOUR", 85, 95, 20, output_dir="data/rct_trainers/trainers/legendary/elite_four")
    generate("CHAMPION", 90, 100, 20, output_dir="data/rct_trainers/trainers/legendary/champion")
    
    print("\n" + "=" * 60)
    print("✅ GÉNÉRATION COMPLÈTE TERMINÉE!")
    print("=" * 60)
    print("\nRécapitulatif:")
    print("  • Débutants (5-20): 80 dresseurs")
    print("  • Intermédiaires (20-40): 120 dresseurs")
    print("  • Avancés (40-60): 140 dresseurs")
    print("  • Experts (60-80): 120 dresseurs")
    print("  • Légendaires (80-100): 60 dresseurs")
    print("  • TOTAL: 520 dresseurs générés")
    print("=" * 60)


if __name__ == "__main__":
    main()

