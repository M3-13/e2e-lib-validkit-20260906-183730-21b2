# validkit

Eine kleine, eigenständige Python-Bibliothek mit reinen, einzeln nutzbaren
Prüf- und Normalisierungsfunktionen. Jede Funktion lebt in ihrem eigenen Modul
und kommt ohne Abhängigkeiten außerhalb der Standardbibliothek aus. Alle
Funktionen sind typannotiert und lassen sich direkt aus dem Paket importieren.

## Tech Stack

- **Sprache**: Python (>= 3.10)
- **Tests**: pytest
- **Abhängigkeiten**: nur Standardbibliothek (`re`, `unicodedata`, `string`, `math`)

## Installation

```bash
pip install -e .
```

## Tests ausführen

```bash
python -m pytest
```

## Funktionen und Beispiele

### is_valid_email

Prüft, ob ein Text eine gültige E-Mail-Adresse ist.

```python
from validkit import is_valid_email

is_valid_email("a@b.de")  # True
is_valid_email("a@b")  # False
```

### luhn_check

Prüft eine Ziffernfolge nach dem Luhn-Algorithmus.

```python
from validkit import luhn_check

luhn_check("79927398713")  # True
luhn_check("79927398712")  # False
```

### is_valid_iban

Prüft eine IBAN inklusive Prüfziffer.

```python
from validkit import is_valid_iban

is_valid_iban("DE89 3704 0044 0532 0130 00")  # True
```

### is_valid_isbn13

Prüft eine ISBN-13 inklusive Prüfziffer.

```python
from validkit import is_valid_isbn13

is_valid_isbn13("978-3-16-148410-0")  # True
```

### normalize_phone

Normalisiert eine Telefonnummer nach E.164.

```python
from validkit import normalize_phone

normalize_phone("030 1234567", "49")  # '+49301234567'
normalize_phone("+49 30 1234567", "49")  # '+49301234567'
```

### strip_accents

Entfernt diakritische Zeichen (Akzente, Umlaute).

```python
from validkit import strip_accents

strip_accents("Über Café")  # 'Uber Cafe'
```

### mask_secret

Maskiert einen Text und lässt die letzten `keep` Zeichen sichtbar.

```python
from validkit import mask_secret

mask_secret("geheim123456", keep=4)  # '********3456'
mask_secret("geheim", keep=0)  # '******'
```

### slugify

Erzeugt einen URL-tauglichen Slug aus einem Text.

```python
from validkit import slugify

slugify("Über Café!")  # 'uber-cafe'
```

### clamp

Begrenzt einen Wert auf ein Intervall `[low, high]`.

```python
from validkit import clamp

clamp(5, 0, 10)  # 5
clamp(-3, 0, 10)  # 0
clamp(15, 0, 10)  # 10
```

## Feature-Liste

- E-Mail-Validierung
- Luhn-Prüfsumme
- IBAN-Validierung
- ISBN-13-Validierung
- Telefonnummer-Normalisierung (E.164)
- Akzent-/Umlaut-Entfernung
- Secret-Maskierung
- Slugify
- Clamp (Wertbegrenzung)
