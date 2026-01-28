# RCT Override - Spawn Aléatoire

## ⚠️ ATTENTION - Ce datapack REMPLACE le système de RCT

Ce datapack **désactive complètement** le système de progression par série de Radical Cobblemon Trainers et le remplace par un système de spawn aléatoire basé sur la distance au spawn.

## 🎯 Ce qui change

### ❌ DÉSACTIVÉ (RCT de base)
- ✖️ Progression par série (Série 1, 2, 3, etc.)
- ✖️ Spawn fixe des dresseurs
- ✖️ Ordre prédéfini des combats
- ✖️ Limitation par badges

### ✅ NOUVEAU SYSTÈME
- ✔️ **Spawn 100% aléatoire** - Taux variable selon les zones (0.8% à 2.5%)
- ✔️ **Niveau basé sur la distance** - Plus vous êtes loin du spawn (0,0), plus c'est dur
- ✔️ **Aucune progression linéaire** - Vous pouvez rencontrer n'importe quel dresseur n'importe où
- ✔️ **Scaling par paliers** - 5 zones de difficulté selon la distance au spawn

## 📊 Système de Distance

```
Distance au spawn (0,0) = |X| + |Z|

Exemples:
• 0-1000 blocs → Dresseurs niveau 5-20 (Starter)
• 1000-2500 blocs → Dresseurs niveau 21-40 (Intermediate)
• 2500-4000 blocs → Dresseurs niveau 41-60 (Advanced)
• 4000-6000 blocs → Dresseurs niveau 61-80 (Expert)
• 6000+ blocs → Dresseurs niveau 81-100 (Legendary)
```

## 🎲 Spawn Aléatoire

**Taux variables selon la distance :**
- **Starter** (0-1km) : 2.5% de spawn
- **Intermediate** (1-2.5km) : 2.0% de spawn
- **Advanced** (2.5-4km) : 1.5% de spawn
- **Expert** (4-6km) : 1.2% de spawn
- **Legendary** (6km+) : 0.8% de spawn

Le niveau du dresseur dépend uniquement de votre distance au spawn, pas de votre progression.

### Conséquences

- Vous pouvez tomber sur un dresseur niveau 80+ si vous allez trop loin
- Plus vous vous éloignez, moins les dresseurs spawent (mais ils sont plus forts !)
- Pas de "série complétée" ou de progression forcée
- Explorez à vos risques et périls !
- Les récompenses sont proportionnelles au risque

## �️ Catégories de Dresseurs (157 trainers)

Le datapack utilise **5 pools de dresseurs** organisés par niveau de difficulté :

| Catégorie | Niveaux | Trainers | Spawn % | Zone Distance | Difficulté |
|-----------|---------|----------|---------|---------------|------------|
| **Starter** | 5-20 | 35 | 2.5% | 0 - 1,000 | 🟢 Facile |
| **Intermediate** | 21-40 | 32 | 2.0% | 1,000 - 2,500 | 🔵 Moyen |
| **Advanced** | 41-60 | 30 | 1.5% | 2,500 - 4,000 | 🟠 Difficile |
| **Expert** | 61-80 | 35 | 1.2% | 4,000 - 6,000 | 🟡 Expert |
| **Legendary** | 81-100 | 26 | 0.8% | 6,000+ | 🔴 Légendaire |

### Types de Dresseurs par Catégorie

**Starter :** Youngster, Lass, Camper, Picnicker, Bug Catcher, Fisherman, Sailor, Twins, Schoolboy  
**Intermediate :** Ace Trainer, Cooltrainer, Swimmer, Hiker, Beauty  
**Advanced :** Veteran, Dragon Tamer, Blackbelt, Elite Four (niveau moyen)  
**Expert :** Veteran (expert), Dragon Tamer (expert), Blackbelt (expert), Elite Four (expert)  
**Legendary :** Champion, Frontier Brain, Legendary Master

**Note importante** : Le niveau exact des dresseurs dépend de votre distance au spawn selon les paliers définis dans `level_scaling.json`.

## 📦 Prérequis

- Minecraft 1.21.1+
- Cobblemon (dernière version)
- **Radical Cobblemon Trainers 0.13+** (le mod de base)
- Ce datapack **DOIT** être chargé **APRÈS** RCT (priorité haute)

## 🔧 Installation

1. **Placez ce datapack** dans `saves/[monde]/datapacks/`
2. **Chargez-le APRÈS RCT** (vérifiez avec `/datapack list`)
3. **Si nécessaire, changez la priorité** :
   ```
   /datapack disable "file/rct_override_extension"
   /datapack enable "file/rct_override_extension" last
   ```
4. **Rechargez** : `/reload`

## ⚙️ Configuration

### Modifier les taux de spawn

Éditez les fichiers dans `data/rct_override/trainer_pools/` :
- `starter_pool.json` : `spawn_chance: 0.025` (2.5%)
- `intermediate_pool.json` : `spawn_chance: 0.020` (2.0%)
- `advanced_pool.json` : `spawn_chance: 0.015` (1.5%)
- `expert_pool.json` : `spawn_chance: 0.012` (1.2%)
- `legendary_pool.json` : `spawn_chance: 0.008` (0.8%)

### Modifier la formule de niveau

Éditez `data/rct_override/config/level_scaling.json` pour ajuster la formule de calcul de niveau basée sur la distance.

## 🎮 Gameplay

### Stratégies conseillées

1. **Début** : Restez près du spawn (0-5km) pour monter en niveau
2. **Exploration prudente** : Avancez progressivement vers l'extérieur
3. **Vérifiez votre distance** : Appuyez sur F3 et calculez |X| + |Z|
4. **Fuyez si nécessaire** : Pas de honte à fuir un dresseur trop fort !

### Calculer le niveau des dresseurs à votre position

```
1. Appuyez sur F3
2. Notez X et Z
3. Calculez : Distance = |X| + |Z|
4. Vérifiez la catégorie selon les paliers :
   • 0-1000 blocs = Starter (niv. 5-20)
   • 1000-2500 blocs = Intermediate (niv. 21-40)
   • 2500-4000 blocs = Advanced (niv. 41-60)
   • 4000-6000 blocs = Expert (niv. 61-80)
   • 6000+ blocs = Legendary (niv. 81-100)

Exemple : X=3000, Z=500
→ Distance = 3000 + 500 = 3500 blocs
→ Catégorie Advanced (niv. 41-60)
```

## ⚠️ Avertissements

### Ce système est plus dangereux !

- ❌ **Pas de protection** - Vous pouvez rencontrer un dresseur trop fort
- ❌ **Pas de progression guidée** - À vous de gérer votre exploration
- ❌ **Récompenses variables** - Vous pouvez rater de bonnes récompenses si vous restez au spawn

### Ce système est plus libre !

- ✅ **Explorez comme vous voulez** - Pas de barrières artificielles
- ✅ **Récompenses immédiates** - Battez un fort → Grosse récompense
- ✅ **Rejouabilité** - Chaque monde est différent
- ✅ **Pas de grind forcé** - Avancez à votre rythme

## 🆚 Différences avec RCT de base

| Aspect | RCT Base | Ce Datapack |
|--------|----------|-------------|
| Progression | Par série (1→2→3) | Par distance au spawn |
| Spawn | Positions fixes | 100% aléatoire |
| Difficulté | Contrôlée par badges | Contrôlée par distance |
| Prévisibilité | Vous savez où aller | Surprises partout |
| Sécurité | Zones "safe" définies | Danger variable partout |

## 📝 Dresseurs Inclus

Le datapack inclut **158 dresseurs uniques** répartis en 5 catégories qui spawent aléatoirement selon le système de distance.

### Détails par Catégorie

**🟢 Starter (35 trainers, niv. 5-20) :**
- Équipes de 1-3 Pokémon communs
- EVs/IVs de base
- Intelligence AI : 0.3
- Récompenses : Pokéball, Potions

**🔵 Intermediate (32 trainers, niv. 21-40) :**
- Équipes de 3-4 Pokémon peu communs
- EVs partiels (100), IVs moyens (24)
- Intelligence AI : 0.6
- Récompenses : Super Potions, Great Balls

**🟠 Advanced (30 trainers, niv. 41-60) :**
- Équipes de 4-6 Pokémon rares
- EVs/IVs maximisés (252/31)
- Intelligence AI : 0.8
- Récompenses : 2 Rare Candy, Max Potions

**🟡 Expert (35 trainers, niv. 61-80) :**
- Équipes de 5-6 Pokémon puissants avec held items
- EVs/IVs maximisés (252/31)
- Intelligence AI : 0.9
- Récompenses : 3 Rare Candy, 1 Master Ball

**🔴 Legendary (26 trainers, niv. 81-100) :**
- Équipes de 6 Pokémon légendaires/pseudo-légendaires
- EVs/IVs parfaits (252/31)
- Intelligence AI : 1.0
- Récompenses : 5 Rare Candy, 1 Ability Patch

## 🎁 Récompenses

Les récompenses augmentent progressivement avec la difficulté :

| Catégorie | Argent de base | Potions | Bonus Items |
|-----------|---------------|---------|-------------|
| **Starter** | 50 + niv×5 | Potion ×1 | - |
| **Intermediate** | 250 + niv×10 | Hyper Potion ×2 | - |
| **Advanced** | 500 + niv×15 | Max Potion ×2 | 2 Rare Candy |
| **Expert** | 1000 + niv×18 | Full Restore ×3 | 3 Rare Candy + 1 Master Ball |
| **Legendary** | 2000 + niv×20 | Full Restore ×5 | 5 Rare Candy + 1 Ability Patch |

**Note :** Tous les dresseurs donnent aussi de l'XP avec un multiplicateur de `1.0 + (niveau ÷ 100)`

## 🐛 Dépannage

**Les anciens dresseurs RCT spawent encore :**
→ Vérifiez que ce datapack a la priorité avec `/datapack list`
→ Déplacez-le en dernier : `/datapack enable "file/rct_override_extension" last`

**Les nouveaux dresseurs ne spawent pas :**
→ Faites `/reload`
→ Attendez quelques minutes
→ Explorez de nouveaux chunks

**Le niveau ne correspond pas à ma distance :**
→ Utilisez la distance Manhattan : |X| + |Z|, pas la distance euclidienne
→ Vérifiez dans les logs si le datapack est bien chargé

## 💡 Conseils

1. **Construisez une base au spawn** - C'est la zone la plus sûre
2. **Créez des avants-postes** - Installez des bases à différentes distances
3. **Utilisez les téléportations** - `/tp` ou points de spawn multiples
4. **Notez vos découvertes** - Cartographiez les zones dangereuses
5. **Voyagez en groupe** (multijoueur) - Plus sûr pour l'exploration lointaine

## 📜 Crédits

- Système de base : **Radical Cobblemon Trainers** par hd42
- Override créé pour : **Cobblemon Academy Legacy**
- Compatible avec : **Cobblemon** par l'équipe Cobblemon

## 🔄 Compatibilité

✅ Compatible avec :
- Autres datapacks Cobblemon (badges, quêtes, etc.)
- Mods de biomes
- Mods de structures

❌ Incompatible avec :
- Autres datapacks qui modifient le spawn RCT
- Datapacks qui forcent la progression par série
## 🔨 Génération de Nouveaux Trainers

Ce datapack inclut un **script Python** (`generate_trainers.py`) pour générer automatiquement de nouveaux trainers avec :
- Pokémon valides de Cobblemon (Gen 1-9)
- Moves réels et équilibrés
- EVs/IVs selon la catégorie
- Held items stratégiques
- Configuration AI adaptée

Pour ajouter des trainers, modifiez `generate_trainers.py` et relancez : `python generate_trainers.py`

---

**Version** : 2.1.0  
**Type** : Override complet  
**Trainers** : 158 (35+32+30+35+26)  
**Date** : 28 Janvier 2026  

⚠️ **Utilisez ce datapack seulement si vous voulez REMPLACER le système RCT par défaut !**
