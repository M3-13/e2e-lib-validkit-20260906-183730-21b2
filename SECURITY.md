VERDICT: CHANGES_REQUESTED

## Sicherheitsbericht

### Zusammenfassung der Prüfung

- **Secrets:** In allen sichtbaren Quelldateien wurden keine hartkodierten Passwörter, Tokens, API-Schlüssel oder geheimen URLs gefunden.
- **Injection/Inputs:** Die verwendeten regulären Ausdrücke (`email`, `phone`, `slug`) sind linear und ohne verschachtelte Quantoren; katastrophales Backtracking ist nicht möglich. IBAN, ISBN, Luhn und E-Mail prüfen Typen und Längen bzw. Zeichenbereiche explizit. Es werden keine dynamischen Ausführungsmechanismen (`eval`, `exec`, `pickle`, `subprocess`) verwendet.
- **AuthN/AuthZ:** Nicht anwendbar – reine Bibliothek ohne Authentifizierungs- oder Autorisierungslogik.
- **Dependencies:** Das Projekt deklariert keine externen Abhängigkeiten. Die Scanner `bandit` und `semgrep` wurden nicht ausgeführt (`[skipped]`); die manuelle Analyse deckt den sichtbaren Code ab, ein automatisierter Befund aus diesen Tools liegt daher nicht vor.
- **Configuration/Transport:** Keine unsicheren Standardeinstellungen oder offenen Debug-/CORS-Konfigurationen erkennbar.

### Befund

#### 1. Unbegrenzte Integer-Konvertierung für `country_code` (potenzieller CPU-DoS)
- **Schweregrad:** medium
- **Betroffene Stelle:** `validkit/phone.py`, Funktion `_country_code_to_int` – Zeile mit `return int(digits)`
- **Beschreibung:**  
  `normalize_phone` akzeptiert `country_code` als `str` oder `int`. Bei einem sehr langen Übergabe-String wird in `_country_code_to_int` ohne Längenbegrenzung `int(digits)` aufgerufen. Ein Angreifer, der die Bibliothek mit ungeprüften Nutzereingaben aufruft (z. B. in einem Web-Backend), kann so eine extrem lange Ziffernfolge übergeben. In Python 3.10 (Projekt-Mindestversion) existiert kein Standardlimit für die Länge von int-Konvertierungen; bereits eine Million Zeichen können zu erheblicher CPU-Last und Speicherverbrauch führen. In Python 3.11+ greift zwar das Standardlimit `sys.set_int_max_str_digits`, aber die Unterstützung von 3.10 eröffnet den Vector.
- **Konkreter Fix:**  
  Nach der Prüfung `digits.isdigit()` eine maximale Länge erzwingen. Da alle realen Ländercodes maximal drei Ziffern haben (z. B. 998), genügt:

  ```python
  if len(digits) > 3:
      raise ValueError(f"country_code must be at most 3 digits, got {digits!r}")
  ```

  Dadurch bleibt die Funktion uneingeschränkt für alle gültigen Codes nutzbar; überlange Eingaben werden früh abgelehnt, bevor die teure Konvertierung stattfindet.

### Bewertung

Der einzige sicherheitsrelevante Befund ist das fehlende Längenlimit für `country_code`. Er erfordert keine Blockade, sollte aber vor einem Release behoben werden, um Denial-of-Service-Szenarien in Anwendungen zu vermeiden, die diese Bibliothek mit nicht vertrauenswürdigen Eingaben betreiben. Alle übrigen geprüften Funktionen verhalten sich gemäß ihrer Verträge und weisen keine ausnutzbaren Schwachstellen auf.