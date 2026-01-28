# Guide d'Installation - RCT Override

## ⚠️ ATTENTION - Installation Critique

Ce datapack **REMPLACE** le système de Radical Cobblemon Trainers. L'installation doit être faite correctement pour fonctionner.

## 📋 Checklist Avant Installation

Vérifiez que vous avez :
- ✅ Minecraft 1.21.1 ou supérieur
- ✅ Forge ou Fabric (selon votre modpack)
- ✅ Cobblemon (dernière version)
- ✅ **Radical Cobblemon Trainers 0.13+** installé
- ✅ Un monde sauvegardé (au cas où)

## 🔧 Installation Étape par Étape

### Étape 1 : Préparation

1. **Sauvegardez votre monde** avant toute modification
   ```
   Copiez le dossier : saves/[NomMonde]/ vers un endroit sûr
   ```

2. **Vérifiez que RCT fonctionne**
   - Lancez le jeu
   - Les dresseurs RCT doivent spawner normalement
   - Si ce n'est pas le cas, installez d'abord RCT

### Étape 2 : Installation du Datapack

1. **Localisez votre dossier datapacks**
   ```
   Windows: %appdata%/.minecraft/saves/[NomMonde]/datapacks/
   Mac: ~/Library/Application Support/minecraft/saves/[NomMonde]/datapacks/
   Linux: ~/.minecraft/saves/[NomMonde]/datapacks/
   ```

2. **Copiez le dossier** `rct_override_extension` dans ce répertoire

3. **Structure finale attendue**
   ```
   datapacks/
   ├── rct_override_extension/
   │   ├── pack.mcmeta
   │   ├── data/
   │   └── README.md
   └── (autres datapacks éventuels)
   ```

### Étape 3 : Configuration de la Priorité

**CRUCIAL** : Ce datapack doit se charger APRÈS RCT !

1. **Lancez le jeu** et chargez votre monde

2. **Vérifiez l'ordre des datapacks**
   ```
   /datapack list
   ```
   
   Vous devriez voir quelque chose comme :
   ```
   [vanilla]
   [mod:cobblemon]
   [mod:rct] ou [file/radical_cobblemon_trainers]
   [file/rct_override_extension] ← Doit être EN DERNIER
   ```

3. **Si `rct_override_extension` n'est PAS en dernier**, corrigez avec :
   ```
   /datapack disable "file/rct_override_extension"
   /datapack enable "file/rct_override_extension" last
   ```

### Étape 4 : Activation

1. **Rechargez les datapacks**
   ```
   /reload
   ```

2. **Vérifiez dans les logs** (appuyez sur F3 + L pour ouvrir le dossier logs)
   - Ouvrez `latest.log`
   - Cherchez "rct_override"
   - Aucune erreur ne doit apparaître

3. **Test in-game**
   ```
   /datapack list enabled
   ```
   → `rct_override_extension` doit être listé

## ✅ Vérification du Fonctionnement

### Test 1 : Les anciens dresseurs ne spawent plus

1. Allez dans une zone où RCT faisait spawner des dresseurs de série
2. Ces dresseurs ne doivent **PLUS** apparaître
3. Si vous voyez encore des dresseurs de série RCT → Le datapack n'a pas priorité

### Test 2 : Les nouveaux dresseurs spawent aléatoirement

1. Explorez de nouveaux chunks
2. Attendez quelques minutes
3. Des dresseurs doivent spawner aléatoirement (2% de chance)
4. Vérifiez que leur niveau correspond à votre distance au spawn

### Test 3 : Calcul du niveau

```
1. Appuyez sur F3
2. Notez X et Z (exemple : X=10000, Z=5000)
3. Distance = |10000| + |5000| = 15000
4. Niveau attendu = 5 + (15000 ÷ 500) = 35
5. Les dresseurs doivent être niveau ~35 ± 5
```

## 🐛 Dépannage

### Problème : Les anciens dresseurs RCT spawent encore

**Causes possibles :**
- Le datapack n'a pas la bonne priorité
- Le datapack n'est pas chargé

**Solutions :**
```
1. /datapack list
2. Vérifiez que rct_override_extension est EN DERNIER
3. Si ce n'est pas le cas :
   /datapack disable "file/rct_override_extension"
   /datapack enable "file/rct_override_extension" last
   /reload
```

### Problème : Aucun dresseur ne spawne du tout

**Causes possibles :**
- RCT n'est pas installé
- Conflit avec un autre datapack
- Le spawn aléatoire prend du temps (2% de chance)

**Solutions :**
1. Vérifiez que RCT est installé : `/datapack list`
2. Attendez 10-15 minutes en explorant
3. Augmentez le taux de spawn (voir section Personnalisation)
4. Vérifiez les logs pour des erreurs

### Problème : Erreurs dans les logs

**Messages d'erreur typiques :**

```
"Failed to load datapack rct_override_extension"
→ Vérifiez que pack.mcmeta existe et est valide

"Could not parse JSON"
→ Un fichier JSON est corrompu, réinstallez le datapack

"Duplicate trainer pool"
→ Conflit avec un autre datapack, désactivez l'autre
```

### Problème : Les niveaux ne correspondent pas

**Vérifiez :**
1. Utilisez la distance Manhattan : `|X| + |Z|`, pas `√(X² + Z²)`
2. La formule : `Niveau = 5 + floor(distance ÷ 500)`
3. Les niveaux peuvent varier ±5 niveaux selon le dresseur

## ⚙️ Personnalisation

### Modifier le Taux de Spawn

Éditez : `data/rct_override/dimension_type/overworld.json`

```json
{
  "trainer_spawning": {
    "base_chance": 0.02  ← Changez ici (0.02 = 2%)
  }
}
```

**Valeurs recommandées :**
- Très rare : 0.005 (0.5%)
- Rare : 0.01 (1%)
- Normal : 0.02 (2%)
- Fréquent : 0.03 (3%)
- Très fréquent : 0.05 (5%)

### Modifier la Formule de Niveau

Éditez : `data/rct_override/dimension_type/overworld.json`

```json
{
  "level_scaling": {
    "formula": "5 + floor(distance / 500)",  ← Changez ici
    "min_level": 5,
    "max_level": 100
  }
}
```

**Exemples de formules :**
- Plus facile : `"3 + floor(distance / 700)"`
- Normal : `"5 + floor(distance / 500)"`
- Plus difficile : `"10 + floor(distance / 300)"`
- Très difficile : `"15 + floor(distance / 200)"`

### Ajouter des Biome Modifiers

Éditez : `data/rct_override/dimension_type/overworld.json`

```json
{
  "biome_modifiers": {
    "plains": 1.0,      ← Taux normal
    "forest": 1.5,      ← 50% plus de spawns
    "mountain": 0.5,    ← 50% moins de spawns
    "desert": 0.3       ← 70% moins de spawns
  }
}
```

## 🔄 Désinstallation

Si vous voulez revenir au système RCT normal :

1. **Sauvegardez votre monde** (important !)
2. **Supprimez le dossier** `rct_override_extension`
3. **Rechargez** : `/reload`
4. Les dresseurs RCT de base devraient réapparaître

**Note** : Les dresseurs déjà spawnés par l'override resteront jusqu'à despawn.

## 🆘 Commandes Utiles

### Diagnostic
```
/datapack list                    # Liste tous les datapacks
/datapack list enabled           # Liste les datapacks actifs
/reload                          # Recharge tous les datapacks
```

### Debug
```
/execute store result score @s test run data get entity @s Pos[0]
# Affiche votre position X

/scoreboard objectives add test dummy
/scoreboard objectives setdisplay sidebar test
# Affiche un scoreboard pour debug
```

### Gestion des Datapacks
```
/datapack enable "file/rct_override_extension"
/datapack disable "file/rct_override_extension"
/datapack enable "file/rct_override_extension" last    # Charge en dernier
/datapack enable "file/rct_override_extension" first   # Charge en premier
```

## 📊 Compatibilité

### ✅ Compatible avec

- Cobblemon (toutes versions récentes)
- Cobblemon Academy Legacy
- Mods de biomes (Biomes O' Plenty, etc.)
- Mods de structures
- Datapacks de badges Cobblemon
- Datapacks de quêtes

### ❌ Incompatible avec

- Autres datapacks qui modifient le spawn RCT
- Datapacks forçant la progression par série
- Mods qui désactivent les datapacks

### ⚠️ Partiellement compatible

- Datapacks ajoutant des dresseurs RCT : Ils seront ignorés, seuls les dresseurs de l'override spawneront

## 💡 Conseils Serveur Multijoueur

### Performance

Pour un serveur avec beaucoup de joueurs, optimisez :

```json
{
  "spawn_rules": {
    "check_interval_ticks": 400,           # Au lieu de 200 (vérifie moins souvent)
    "max_trainers_per_chunk": 1,           # Maximum 1 par chunk
    "min_distance_between_trainers": 200   # Distance minimale augmentée
  }
}
```

### Équilibrage

- Réduisez `base_chance` à 0.01 (1%) pour moins de spawns
- Augmentez `min_distance_between_trainers` à 300+
- Ajustez la formule de niveau selon la difficulté souhaitée

## 📝 Checklist Post-Installation

- [ ] Le datapack apparaît dans `/datapack list`
- [ ] Il est listé EN DERNIER (après RCT)
- [ ] `/reload` ne génère aucune erreur
- [ ] Les anciens dresseurs RCT ne spawent plus
- [ ] De nouveaux dresseurs spawent aléatoirement
- [ ] Leur niveau correspond à la distance
- [ ] Les récompenses sont données après victoire

---

**Si tout fonctionne :** Félicitations ! Vous êtes prêt à explorer ! 🎉  
**Si problèmes persistent :** Consultez les logs et vérifiez la section Dépannage.

**Support** : Consultez README.md pour plus d'informations.

---

Version : 2.0.0  
Date : 28 Janvier 2026  
Pour Cobblemon Academy Legacy
