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
- ✔️ **Spawn 100% aléatoire** - 2% de chance partout dans le monde
- ✔️ **Niveau basé sur la distance** - Plus vous êtes loin du spawn (0,0), plus c'est dur
- ✔️ **Aucune progression linéaire** - Vous pouvez rencontrer n'importe quel dresseur n'importe où
- ✔️ **Scaling automatique** - Formule : `Niveau = 5 + (Distance ÷ 500)`, max 100

## 📊 Système de Distance

```
Distance au spawn (0,0) = |X| + |Z|

Exemples:
• Spawn (0,0) → Dresseurs niveau 5
• 5,000 blocs → Dresseurs niveau 15
• 10,000 blocs → Dresseurs niveau 25
• 25,000 blocs → Dresseurs niveau 55
• 50,000 blocs → Dresseurs niveau 105 (plafonné à 100)
```

## 🎲 Spawn Aléatoire

**Taux de base : 2%**

Chaque chunk a 2% de chance de faire spawner un dresseur. Le niveau du dresseur dépend uniquement de votre distance au spawn, pas de votre progression.

### Conséquences

- Vous pouvez tomber sur un dresseur niveau 80 si vous allez trop loin
- Pas de "série complétée" ou de progression forcée
- Explorez à vos risques et périls !
- Les récompenses sont proportionnelles au risque

## 🗺️ Paliers Recommandés (mais pas obligatoires)

| Distance | Niveau Dresseurs | Pokémon Typiques | Danger |
|----------|------------------|------------------|---------|
| 0-10km | 5-25 | Communs | 🟢 Facile |
| 10-25km | 25-55 | Peu communs | 🔵 Moyen |
| 25-40km | 55-85 | Rares | 🟡 Difficile |
| 40km+ | 85-100 | Légendaires | 🔴 Expert |

**Note importante** : Ces paliers sont indicatifs. En réalité, le niveau augmente de façon continue, pas par paliers fixes.

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

### Modifier le taux de spawn

Éditez `data/rct/dimension_type/overworld.json` et changez :
```json
{
  "trainer_spawn_chance": 0.02  // 2% par défaut
}
```

### Modifier la formule de niveau

Éditez `data/rct/worldgen/density_function/trainer_level_scaling.json`

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
3. Calculez : (|X| + |Z|) ÷ 500 + 5 = Niveau
4. Maximum 100

Exemple : X=12000, Z=8000
→ (12000 + 8000) ÷ 500 + 5 = 45
→ Attendez-vous à des dresseurs niveau ~45
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

Le datapack désactive tous les dresseurs de série RCT et ajoute **20+ nouveaux dresseurs** qui spawent aléatoirement selon le système de distance.

Types de dresseurs :
- Campeurs, Randonneurs (Niv. 5-20)
- Dresseurs Élite, Nageurs (Niv. 20-40)
- Vétérans, Dompteurs (Niv. 40-60)
- Maîtres, Experts (Niv. 60-80)
- Champions, Légendes (Niv. 80-100)

## 🎁 Récompenses

Les récompenses sont calculées selon :
```
Qualité = Niveau du dresseur ÷ 10

Niveau 10 → Poké Balls, Potions
Niveau 50 → Ultra Balls, Hyper Potions, Rare Candy
Niveau 100 → Master Balls, Max Potions, Ability Patch, Or
```

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

---

**Version** : 2.0.0  
**Type** : Override complet  
**Date** : 28 Janvier 2026  

⚠️ **Utilisez ce datapack seulement si vous voulez REMPLACER le système RCT par défaut !**
