# Haas Japanese Colab

Notebook Google Colab per trascrivere audio e video in giapponese con Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_it.ipynb)

## Funzionalità

- **Gratuito:** Funziona nell'ambiente GPU gratuito di Google Colab.
- **ASR giapponese:** Usa [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), un modello da circa 0.6B parametri per il riconoscimento vocale giapponese.
- **Veloce:** La trascrizione può essere elaborata rapidamente.
- **Punteggiatura:** Il modello produce una punteggiatura giapponese stimata.
- **Timestamp e sottotitoli:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Elaborazione di file lunghi:** È possibile elaborare anche file audio e video lunghi.
- **Supporto Google Drive:** Carica direttamente i file o leggili da Google Drive; il ZIP di output può essere salvato facoltativamente su Drive.
- **Output multipli:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest e ZIP.

## Utilizzo

1. Scegli `INPUT_MODE` in **1. Settings** e regola le altre impostazioni se necessario.
2. Seleziona **Runtime → Run all**.
3. Con `INPUT_MODE = "upload"`, scegli i file in **2. File selection / Google Drive mount**.
4. Il ZIP di output viene scaricato automaticamente al termine dell'elaborazione.

## Modalità timestamp

- `none`: nessuna informazione temporale.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## File lunghi

`CHUNK_SECONDS` controlla la durata interna dei chunk usati per i file lunghi. Valori maggiori riducono i confini e preservano più contesto, ma rendono ogni inferenza più pesante e possono aumentare l'uso della memoria GPU. Valori minori rendono ogni inferenza più leggera ma creano più confini, che possono influire sul riconoscimento in quei punti. Nella maggior parte dei casi è consigliato il valore predefinito.

## Interfaccia localizzata

Il modello ASR stesso è **solo giapponese**. La localizzazione del README e dell'interfaccia Colab copre tutte le **183 lingue attive ISO 639 Set 1** (l'obsoleto `sh` è escluso).

L'inglese (`en`) è la fonte canonica di traduzione. Il giapponese (`ja`) è una traduzione revisionata e viene copiato nella radice del repository come presentazione `README.md` predefinita. Il README giapponese nella radice **non** viene usato come fonte di traduzione. Gli altri 181 locale sono tradotti automaticamente dall'inglese.

## Note

- Il notebook si arresta prima della trascrizione se non è disponibile una GPU.
- Il tempo di elaborazione dipende dalla lunghezza dell'input, dalle impostazioni e dalla GPU assegnata da Colab. La prima esecuzione scarica anche NeMo e il modello da circa 1.23 GB.
- L'audio lungo viene elaborato in chunk interni, quindi il riconoscimento può essere influenzato vicino ai confini dei chunk.

## Fonte canonica e generazione

Fonti traducibili canoniche:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` è lo snapshot canonico sincronizzato. Il giapponese è mantenuto come traduzione revisionata in `locales/ja.json` e il relativo snapshot README viene copiato nella radice come `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

La manutenzione delle traduzioni è separata dalla CI ordinaria. Gli utenti normali e la CI non richiedono credenziali di traduzione.

## Licenza

La struttura del notebook e gli script di build/verifica sono distribuiti con licenza MIT. Il modello Third Intelligence non viene ridistribuito qui ed è regolato da **Apache-2.0**. Le dipendenze di terze parti mantengono le proprie licenze.
