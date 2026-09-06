VERDICT: CHANGES_REQUESTED

## Prüfbericht

### 1. DSGVO / GDPR

**Befund (mittel):** In `validkit/luhn.py` gibt die Funktion `luhn_check()` bei nichtnumerischen Eingaben die Originaleingabe in der Fehlermeldung aus:

```python
raise ValueError(
    "luhn_check() accepts only digits, optionally separated by spaces or hyphens, "
    f"got {digits!r}"
)
```

`luhn_check` wird typischerweise für Kreditkarten-, Kontonummern oder ähnliche sensible Zeichenfolgen verwendet. Wird diese Exception vom Integrator abgefangen und protokolliert, landet die vollständige Eingabe im Klartext in Logs. Das ist ein vermeidbarer PII-Leak im Fehlerpfad.

**Abhilfe:** In `validkit/luhn.py` die Fehlermeldung ändern zu:

```python
raise ValueError(
    "luhn_check() accepts only digits, optionally separated by spaces or hyphens"
)
```

Den Teil `, got {digits!r}` entfernen. Dadurch bleibt die Funktion uneingeschränkt funktionsfähig, gibt aber keine Eingabedaten mehr preis.

**Positiv:** Die Bibliothek speichert oder protokolliert selbst keine personenbezogenen Daten. Die Funktionen verarbeiten Eingaben ausschließlich im Arbeitsspeicher und geben normalisierte Ergebnisse zurück. Mit `mask_secret` existiert zudem ein datenschutzfreundliches Werkzeug.

### 2. EU Cyber Resilience Act (CRA)

**Positiv:** Der Code erfüllt wesentliche Sicherheitsanforderungen:
- Kein `eval`, `exec`, `pickle`, `subprocess` oder vergleichbare dynamische Ausführung.
- Keine Eingabevalidierung über `assert`; Fehler werden explizit mit `TypeError`/`ValueError` ausgelöst.
- Regex-Performance-Tests vorhanden (z. B. 10.000-Zeichen-Eingaben), keine Anzeichen für katastrophales Backtracking.
- Keine Laufzeitabhängigkeiten (`dependencies = []`), geringe Angriffsfläche.

**Befund (niedrig):** Es ist keine explizite Meldemöglichkeit für Sicherheitslücken sichtbar, etwa eine `SECURITY.md` oder ein Security-Abschnitt in der README. Da der Inhalt der vorhandenen `README.md` hier nicht vollständig einsehbar ist, wird dies als Empfehlung und nicht als Blocker gewertet.

**Abhilfe:** Legen Sie eine `SECURITY.md` im Repository-Root an oder ergänzen Sie `README.md` um einen kurzen Abschnitt „Sicherheit / Schwachstellen melden“ mit Kontaktweg und erwartetem Prozess.

### 3. EU AI Act

Nicht relevant: Das Produkt enthält keine KI-Funktion.

### 4. Pflichttexte & UI

Nicht relevant: Reine Python-Bibliothek ohne Endbenutzer-UI, daher keine Impressums-, Cookie- oder AGB-Pflichten.

### 5. Barrierefreiheit

Nicht relevant: Keine öffentliche Web-UI.

## Fazit

Ein behebbarer Datenschutzmangel (personenbezogene Eingabedaten in Fehlermeldung) führt zu `CHANGES_REQUESTED`. Alle übrigen geprüften Bereiche sind unauffällig.