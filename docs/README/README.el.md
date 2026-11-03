# Haas Japanese Colab

Σημειωματάριο Google Colab για μεταγραφή ιαπωνικού ήχου και βίντεο με το Third Intelligence **Haas-ja-v1.0**.

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/piccoripico/haas-ja-colab/blob/main/notebooks/Haas_Japanese_Colab_el.ipynb)

## Δυνατότητες

- **Δωρεάν:** Εκτελείται στο δωρεάν περιβάλλον GPU του Google Colab.
- **Ιαπωνικό ASR:** Χρησιμοποιεί το [`third-intelligence/Haas-ja-v1.0`](https://huggingface.co/third-intelligence/Haas-ja-v1.0), ένα μοντέλο περίπου 0.6B παραμέτρων για αναγνώριση ιαπωνικής ομιλίας.
- **Γρήγορο:** Η μεταγραφή μπορεί να εκτελεστεί γρήγορα.
- **Στίξη:** Το μοντέλο παράγει εκτιμώμενη ιαπωνική στίξη.
- **Χρονικές σημάνσεις και υπότιτλοι:** `subtitle` generates SRT with approximate chunk-boundary timestamps; `none` disables timing. Native word/character timestamps are unavailable.
- **Επεξεργασία μεγάλων αρχείων:** Μπορούν να επεξεργαστούν και μεγάλα αρχεία ήχου και βίντεο.
- **Υποστήριξη Google Drive:** Ανεβάστε αρχεία απευθείας ή διαβάστε τα από το Google Drive· το ZIP εξόδου μπορεί προαιρετικά να αποθηκευτεί στο Drive.
- **Πολλαπλές έξοδοι:** TXT, Markdown, JSON, CSV, XLSX, SRT, manifest και ZIP.

## Χρήση

1. Επιλέξτε `INPUT_MODE` στο **1. Settings** και προσαρμόστε άλλες ρυθμίσεις αν χρειάζεται.
2. Επιλέξτε **Runtime → Run all**.
3. Με `INPUT_MODE = "upload"`, επιλέξτε αρχεία στο **2. File selection / Google Drive mount**.
4. Το ZIP εξόδου λαμβάνεται αυτόματα μετά την ολοκλήρωση της επεξεργασίας.

## Λειτουργίες χρονικών σημάνσεων

- `none`: χωρίς χρονικές πληροφορίες.
- `subtitle`: SRT with approximate audio-chunk start/end times (not word-level alignment).

## Αποκωδικοποιητής

Haas-ja-v1.0 uses TDT only; CTC is unavailable.

## Μεγάλα αρχεία

Το `CHUNK_SECONDS` ελέγχει τη διάρκεια των εσωτερικών τμημάτων για μεγάλα αρχεία. Μεγαλύτερες τιμές μειώνουν τα όρια και διατηρούν περισσότερο πλαίσιο, αλλά κάνουν κάθε inference βαρύτερο και μπορεί να αυξήσουν τη χρήση μνήμης GPU. Μικρότερες τιμές ελαφρύνουν κάθε inference αλλά δημιουργούν περισσότερα όρια, τα οποία μπορεί να επηρεάσουν την αναγνώριση γύρω από αυτά τα σημεία. Η προεπιλεγμένη τιμή συνιστάται στις περισσότερες περιπτώσεις.

## Τοπικοποιημένο περιβάλλον

Το ίδιο το μοντέλο ASR είναι **μόνο για ιαπωνικά**. Η τοπικοποίηση του README και του Colab UI καλύπτει και τις **183 ενεργές γλώσσες ISO 639 Set 1** (το παρωχημένο `sh` εξαιρείται).

Τα αγγλικά (`en`) είναι η κανονική πηγή μετάφρασης. Τα ιαπωνικά (`ja`) είναι ελεγμένη μετάφραση και αντιγράφονται στη ρίζα του repository ως προεπιλεγμένη παρουσίαση `README.md`. Το ιαπωνικό README της ρίζας **δεν** χρησιμοποιείται ως πηγή μετάφρασης. Τα υπόλοιπα 181 locales μεταφράζονται μηχανικά από τα αγγλικά.

## Σημειώσεις

- Το σημειωματάριο σταματά πριν από τη μεταγραφή αν δεν υπάρχει διαθέσιμη GPU.
- Ο χρόνος επεξεργασίας εξαρτάται από το μήκος εισόδου, τις ρυθμίσεις και την GPU που εκχωρεί το Colab. Η πρώτη εκτέλεση κατεβάζει επίσης το NeMo και το μοντέλο περίπου 1.23 GB.
- Ο μεγάλος ήχος επεξεργάζεται σε εσωτερικά τμήματα, οπότε η αναγνώριση μπορεί να επηρεαστεί κοντά στα όρια των τμημάτων.

## Κανονική πηγή και δημιουργία

Κανονικές μεταφράσιμες πηγές:

```text
source/README.en.md
notebooks/Haas_Japanese_Colab_en.ipynb
```

Το `locales/en.json` είναι το συγχρονισμένο κανονικό snapshot. Τα ιαπωνικά διατηρούνται ως ελεγμένη μετάφραση στο `locales/ja.json` και το snapshot README τους αντιγράφεται στη ρίζα ως `README.md`.

```bash
python scripts/sync_from_english.py
python scripts/build_languages.py
python scripts/build_notebooks.py
python scripts/build_readmes.py
python scripts/check_repository.py
```

Η συντήρηση μεταφράσεων είναι ξεχωριστή από το συνηθισμένο CI. Οι κανονικοί χρήστες και το CI δεν χρειάζονται διαπιστευτήρια μετάφρασης.

## Άδεια

Ο σκελετός του σημειωματαρίου και τα scripts build/check έχουν άδεια MIT. Το μοντέλο Third Intelligence δεν αναδιανέμεται εδώ και διέπεται από **Apache-2.0**. Οι εξαρτήσεις τρίτων διατηρούν τις δικές τους άδειες.
