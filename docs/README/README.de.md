# Haas Japanese Colab

Google-Colab-Notebook zur Transkription japanischer Audio- und Videodateien mit Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_de.ipynb)

## Funktionen

- **Kostenlos:** Läuft in der kostenlosen GPU-Laufzeit von Google Colab.
- **Japanische Spracherkennung:** Verwendet [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), ein Modell mit ungefähr 0.6B Parametern für die Erkennung japanischer Sprache.
- **Schnell:** Die Transkription kann schnell verarbeitet werden.
- **Interpunktion:** Das Modell gibt geschätzte japanische Satzzeichen aus.
- **Zeitstempel und Untertitel:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Verarbeitung langer Dateien:** Auch lange Audio- und Videodateien können verarbeitet werden.
- **Google-Drive-Unterstützung:** Dateien können direkt hochgeladen oder aus Google Drive gelesen werden; die Ausgabe-ZIP kann optional in Drive gespeichert werden.
- **Mehrere Ausgabeformate:** TXT, Markdown, JSON, CSV, XLSX, SRT, Manifest und ZIP.

## Verwendung

1. Wähle `INPUT_MODE` unter **1. Settings** und passe bei Bedarf weitere Einstellungen an.
2. Wähle **Runtime → Run all**.
3. Bei `INPUT_MODE = "upload"` wähle die Dateien unter **2. File selection / Google Drive mount** aus.
4. Nach Abschluss der Verarbeitung wird die Ausgabe-ZIP automatisch heruntergeladen.

## Zeitstempelmodi

- `none`: keine Zeitinformationen.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Decoder

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Lange Dateien

`CHUNK_SECONDS` steuert die interne Chunk-Dauer für lange Dateien. Größere Werte verringern die Anzahl der Grenzen und erhalten mehr Kontext, machen jede Inferenz jedoch aufwendiger und können den GPU-Speicherbedarf erhöhen. Kleinere Werte erleichtern jede Inferenz, erzeugen aber mehr Grenzen, was die Erkennung an diesen Stellen beeinträchtigen kann. In den meisten Fällen wird der Standardwert empfohlen.

## Lokalisierte Benutzeroberfläche

Das ASR-Modell selbst ist **nur für Japanisch** ausgelegt. README und Colab-UI sind für alle **183 aktiven ISO 639 Set 1-Sprachen** lokalisiert (das veraltete `sh` ist ausgeschlossen).

Englisch (`en`) ist die kanonische Übersetzungsquelle. Japanisch (`ja`) ist eine geprüfte Übersetzung und wird als standardmäßige `README.md`-Darstellung in das Repository-Stammverzeichnis kopiert. Die japanische README im Stammverzeichnis wird **nicht** als Übersetzungsquelle verwendet. Die übrigen 181 Locales werden maschinell aus dem Englischen übersetzt.

## Hinweise

- Das Notebook stoppt vor der Transkription, wenn keine GPU verfügbar ist.
- Die Verarbeitungszeit hängt von Eingabelänge, Einstellungen und der von Colab zugewiesenen GPU ab. Beim ersten Lauf werden außerdem NeMo und das ungefähr 1.23 GB große Modell heruntergeladen.
- Lange Audiodateien werden in internen Chunks verarbeitet, daher kann die Erkennung an Chunk-Grenzen beeinträchtigt werden.

## Kanonische Quelle und Generierung

Kanonische übersetzbare Quellen:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

`locales/en.json` ist der synchronisierte kanonische Snapshot. Japanisch wird als geprüfte Übersetzung in `locales/ja.json` gepflegt, und dessen README-Snapshot wird als `README.md` in das Stammverzeichnis kopiert.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Die Übersetzungspflege ist von der normalen CI getrennt. Normale Benutzer und CI benötigen keine Übersetzungszugangsdaten.

## Lizenz

Notebook-Grundgerüst sowie Build-/Prüfskripte stehen unter der MIT-Lizenz. Das Third Intelligence-Modell wird hier nicht weitergegeben und unterliegt **Apache-2.0**. Drittanbieterabhängigkeiten behalten ihre jeweiligen Lizenzen.
