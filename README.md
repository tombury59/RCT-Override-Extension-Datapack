# RCT Trainers Datapack

Datapack contenant 520 dresseurs générés automatiquement pour RCT (Random Challenger Trainers) avec le mod RCT Distance Scaler.

## 📦 Installation

1. Copiez le dossier `Datapack` dans `.minecraft/saves/[VotreMondeDeJeu]/datapacks/`
2. Rechargez les datapacks: `/reload`
3. Les dresseurs apparaîtront automatiquement!

## 🎮 Fonctionnement avec RCT Distance Scaler

Ce datapack est conçu pour fonctionner avec le mod **RCT Distance Scaler**. Le mod:
- **Écrase automatiquement les niveaux** des dresseurs en fonction de la distance au spawn
- Formule: `Niveau = 5 + floor(distance / 80)`
- Les niveaux dans les JSON servent uniquement de référence

### Exemples de niveaux par distance:
- **Spawn (0m)**: Niveau 5
- **800m**: Niveau 15
- **2000m**: Niveau 30
- **4000m**: Niveau 55
- **8000m**: Niveau 100

## 📊 Contenu

### 520 Dresseurs répartis en 5 catégories:

#### 🌱 Débutants (80 dresseurs)
- Youngster (20)
- Lass (20)
- Bug Catcher (20)
- Schoolboy (20)

#### ⚡ Intermédiaires (120 dresseurs)
- Camper (20)
- Picnicker (20)
- Hiker (20)
- Fisherman (20)
- Beauty (20)
- Swimmer (20)

#### 🔥 Avancés (140 dresseurs)
- Ace Trainer (20)
- Cooltrainer (20)
- Blackbelt (20)
- Battle Girl (20)
- Psychic (20)
- Scientist (20)
- Bird Keeper (20)

#### 💪 Experts (120 dresseurs)
- Veteran (20)
- Dragon Tamer (20)
- Pokémon Ranger (20)
- Pokémon Breeder (20)
- Ninja (20)
- Ruin Maniac (20)

#### 👑 Légendaires (60 dresseurs)
- Gym Leader (20)
- Elite Four (20)
- Champion (20)

## 🔧 Régénération

Pour régénérer les dresseurs:

```powershell
python generate_rct_trainers.py
```

Cela créera automatiquement la structure de datapack dans `data/rct_trainers/trainers/`.

## ⚙️ Configuration du mod

Fichier: `.minecraft/config/rct_distance_scaler.toml`

```toml
base_level = 5      # Niveau au spawn
scale_factor = 80   # Blocks par niveau (plus élevé = plus lent)
spawn_rate = 0.02   # Taux d'apparition (2%)
max_level = 100     # Niveau maximum
```

## 📝 Format JSON des dresseurs

Les fichiers JSON suivent le format RCT standard avec l'API RCT:

```json
{
  "name": "Ace Trainer Abel",
  "ai": {
    "type": "rct",
    "data": {
      "maxSelectMargin": 0.15
    }
  },
  "battleRules": {
    "maxItemUses": 4
  },
  "bag": [
    {
      "item": "cobblemon:superb_remedy",
      "quantity": 2
    }
  ],
  "team": [
    {
      "species": "aerodactyl",
      "gender": "MALE",
      "level": 59,
      "nature": "hardy",
      "ability": "rockhead",
      "moveset": ["stoneedge", "takedown", "crunch", "ironhead"],
      "ivs": {},
      "evs": {}
    }
  ]
}
```

## 🛠️ Prérequis

- Minecraft 1.21.1
- Fabric Loader
- Fabric API
- Cobblemon
- RCT (Radical Cobblemon Trainers)
- RCT Distance Scaler (mod)

## 📂 Structure

```
Datapack/
├── pack.mcmeta
├── generate_rct_trainers.py
├── README.md
└── data/
    └── rct_trainers/
        └── trainers/
            ├── starter/
            ├── intermediate/
            ├── advanced/
            ├── expert/
            └── legendary/
```
