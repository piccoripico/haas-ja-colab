# Haas Japanese Colab

Notebook Google Colab pour transcrire des fichiers audio et vidéo japonais avec Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_fr.ipynb)

## Fonctionnalités

- **Gratuit :** Fonctionne avec l'environnement GPU gratuit de Google Colab.
- **ASR japonais :** Utilise [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un modèle d'environ 0.6B paramètres pour la reconnaissance vocale japonaise.
- **Rapide :** La transcription peut être traitée rapidement.
- **Ponctuation :** Le modèle produit une ponctuation japonaise estimée.
- **Horodatages et sous-titres :** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Traitement des fichiers longs :** Les fichiers audio et vidéo longs peuvent également être traités.
- **Prise en charge de Google Drive :** Téléversez directement des fichiers ou lisez-les depuis Google Drive ; le ZIP de sortie peut aussi être enregistré dans Drive.
- **Sorties multiples :** TXT, Markdown, JSON, CSV, XLSX, SRT, manifeste et ZIP.

## Utilisation

1. Choisissez `INPUT_MODE` dans **1. Settings** et ajustez les autres paramètres si nécessaire.
2. Sélectionnez **Runtime → Run all**.
3. Avec `INPUT_MODE = "upload"`, choisissez les fichiers dans **2. File selection / Google Drive mount**.
4. Le ZIP de sortie est téléchargé automatiquement à la fin du traitement.

## Modes d'horodatage

- `none` : aucune information temporelle.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Décodeur

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Fichiers longs

`CHUNK_SECONDS` contrôle la durée interne des segments utilisés pour les fichiers longs. Des valeurs plus grandes réduisent le nombre de limites et préservent davantage de contexte, mais rendent chaque inférence plus lourde et peuvent augmenter l'utilisation de la mémoire GPU. Des valeurs plus petites allègent chaque inférence mais créent davantage de limites, ce qui peut affecter la reconnaissance à proximité de ces points. La valeur par défaut est recommandée dans la plupart des cas.

## Interface localisée

Le modèle ASR lui-même est **uniquement japonais**. La localisation du README et de l'interface Colab couvre les **183 langues actives ISO 639 Set 1** (`sh`, obsolète, est exclu).

L'anglais (`en`) est la source canonique de traduction. Le japonais (`ja`) est une traduction révisée et est copié à la racine du dépôt comme présentation `README.md` par défaut. Le README japonais racine **n'est pas** utilisé comme source de traduction. Les 181 autres locales sont traduites automatiquement depuis l'anglais.

## Remarques

- Le notebook s'arrête avant la transcription si aucun GPU n'est disponible.
- Le temps de traitement dépend de la longueur de l'entrée, des paramètres et du GPU attribué par Colab. La première exécution télécharge également NeMo et le modèle d'environ 1.23 GB.
- Les fichiers audio longs sont traités en segments internes ; la reconnaissance peut donc être affectée autour des limites de segments.

## Source canonique et génération

Sources canoniques traduisibles :

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` est l'instantané canonique synchronisé. Le japonais est maintenu comme traduction révisée dans `locales/ja.json`, et son instantané README est copié à la racine en tant que `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

La maintenance des traductions est séparée de la CI ordinaire. Les utilisateurs ordinaires et la CI n'ont pas besoin d'identifiants de traduction.

## Licence

La structure du notebook et les scripts de build/vérification sont sous licence MIT. Le modèle Third Intelligence n'est pas redistribué ici et est régi par **Apache-2.0**. Les dépendances tierces conservent leurs propres licences.
