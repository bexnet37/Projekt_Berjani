# Projektdokumentation: OOP-Verwaltung in Python (Ticket System)

**Team:** Bennet, Timothy, Jason (Klasse 10its2)  
**Datum:** 15.04.2026  
**Fach:** LF05 / Abschluss-Projekt (Klausurersatz)  

---

## 1. Projektziel und Funktionalität

Unser Ziel war es, ein einfaches, aber robustes Ticket-Management-System zu entwickeln, welches die Prinzipien der objektorientierten Programmierung (OOP) strikt anwendet. Die Anwendung dient der Verwaltung von Support-Tickets in einem Unternehmen. 

Zu den Kernfunktionalitäten gehören:
- **CRUD-Operationen:** Wir können Tickets erstellen, lesen, aktualisieren und löschen.
- **Benutzeroberflächen:** Die Anwendung verfügt über eine grafische Benutzeroberfläche (GUI) mit Tkinter sowie eine Command-Line Interface (CLI) als Alternative.
- **Logik-Methoden:** Das System bietet eine Suchfunktion, mit der wir Tickets anhand von Schlüsselwörtern finden können, sowie eine Statistikfunktion, die die Anzahl der Tickets nach Priorität berechnet.
- **Persistenz:** Die Daten werden dauerhaft in CSV-Dateien gespeichert.

## 2. Bewertung des Projekterfolgs und Reflexion

Das Projekt war für uns ein voller Erfolg. Wir konnten die definierten Projektanforderungen an die OOP-Struktur erfolgreich umsetzen. Besonders die Aufteilung in das 3-Schichten-Modell (Fachklasse, Datenhaltung, UI) hat uns geholfen, den Code übersichtlich und wartbar zu halten.
Wir haben uns bewusst dazu entschieden, eigene, strikte Schnittstellendefinitionen und Namensvorgaben festzulegen und diese konsequent einzuhalten. So konnten wir simulieren, wie in echten Projekten verschiedene Entwickler an unterschiedlichen Modulen arbeiten, die nahtlos ineinandergreifen müssen. Durch das iterative Vorgehen konnten wir unseren Code am Ende stark optimieren und einen sauberen, professionellen Standard etablieren.

## 3. Beantwortung der OOP-Leitfragen

Im Rahmen unseres Projekts haben wir uns intensiv mit den Kernkonzepten der OOP beschäftigt:

- **Datenkapselung:** In unserer Klasse `Ticket` haben wir Attribute wie `__ticket_id` oder `__title` durch zwei Unterstriche als privat (private) deklariert. Dadurch wird verhindert, dass von außen unkontrolliert auf die Daten zugegriffen oder diese manipuliert werden können. Der Zugriff erfolgt ausschließlich über kontrollierte Getter-Methoden (z.B. `get_title()`). Dies schützt die Integrität unserer Ticket-Daten.
- **Klassen und Objekte:** Die Klasse ist der "Bauplan" (z.B. `Ticket`), während ein konkretes Support-Ticket (z.B. ein Druckerfehler) das instanziierte Objekt zur Laufzeit ist.
- **Polymorphie & Vererbung:** Obwohl in diesem Basis-Projekt nicht zwingend eine tiefe Vererbungshierarchie verlangt wurde, haben wir die Struktur so aufgebaut, dass eine Klasse `VipTicket` problemlos von `Ticket` erben könnte. Polymorphie nutzen wir implizit bei der Übergabe von Ticket-Objekten an Methoden, die beliebige Subklassen von Tickets verarbeiten könnten.

## 4. Persistente Datenspeicherung (Datenformat)

Wir nutzen für die Datenspeicherung das CSV-Format (Comma-Separated Values). 
Die Datei `tickets.csv` speichert die Tickets zeilenweise.
Das Datenmodell ist simpel und flach strukturiert:
- Spalte 1: `ticket_id` (Eindeutiger Integer/String)
- Spalte 2: `title` (String)
- Spalte 3: `priority` (String: Hoch, Mittel, Niedrig)
- Spalte 4: `text` (String)

Der `FileManager` liest diese CSV-Datei ein (`load_tickets()`), wandelt jede Zeile in ein `Ticket`-Objekt um und reicht die Liste an die UI weiter. Beim Speichern (`save_tickets()`) wird die Objektliste wieder in CSV-Zeilen serialisiert.

## 5. Testfall-Dokumentation (Unit Test)

Um sicherzustellen, dass die Logik-Methoden korrekt arbeiten, haben wir einen Modultest konzipiert, der die Methode `calculate_priority_stats()` prüft:

**Testfall 1: Berechnung der Prioritäten-Statistik**
- **Vorbedingung:** Die `tickets.csv` enthält 3 Tickets: 1x Hoch, 2x Mittel, 0x Niedrig.
- **Aktion:** Aufruf von `FileManager.calculate_priority_stats()`.
- **Erwartetes Ergebnis:** Ein Dictionary `{"Hoch": 1, "Mittel": 2, "Niedrig": 0}` wird zurückgegeben.
- **Tatsächliches Ergebnis:** Das Dictionary entspricht exakt den Erwartungen.
- **Status:** Bestanden.

*(Hinweis: Den ausführbaren Code zum Unit Test findet sich in der Datei `test_ticket_system.py`)*

## 6. UML Diagramme

*(Hinweis: Die grafischen Diagramme müssen als Bilddateien oder im PDF eingebunden werden. Hier ist die textuelle Beschreibung als Platzhalter für die Präsentation)*

**Klassendiagramm:**
- `Ticket`: -__ticket_id, -__title, -__priority, -__text | +get_ticket(), +get_title(), +get_text(), +get_priority()
- `FileManager`: +csv_file, +status_option, +ticket_types | +load_users(), +save_users(), +delete_users(), +load_tickets(), +save_tickets(), +search_tickets(), +calculate_priority_stats()
- `TicketSystem`: +data_manager, +root | +setup_gui(), +save_ticket(), +update_tickets(), +load_tickets(), +delete_tickets()

**Assoziationen:** `TicketSystem` 1 --> 1 `FileManager` | `FileManager` 1 --> * `Ticket`
