# Präsentation: OOP-Verwaltung in Python (Ticket-System)

*(Hinweis: Diese Struktur ist für PowerPoint gedacht. Einfach die Texte in die jeweiligen Folien kopieren.)*

---

## Folie 1: Titelfolie
**Titel:** OOP-Verwaltung in Python: Ticket-System  
**Untertitel:** Abschluss-Projekt (Klausurersatz)  
**Team:** Bennet, Timothy, Jason (Klasse 10its2)  
**Datum:** 15.04.2026  

---

## Folie 2: Projektziel
**Titel:** 1. Projektziel
- Entwicklung eines voll funktionsfähigen Ticket-Management-Systems
- Strikte Anwendung der Objektorientierten Programmierung (OOP)
- Sichere und strukturierte Speicherung von Daten (persistente Datenhaltung)
- Vorbereitung auf reale IT-Support-Szenarien (professioneller Standard)

---

## Folie 3: Architektur & Datenhaltung
**Titel:** 2. Die Architektur (3-Schichten-Modell)
- **Schicht 1 (GUI):** `TicketSystem` - Benutzerinteraktion über Tkinter
- **Schicht 2 (Logik/Daten):** `FileManager` - Verarbeitet die Daten und führt Statistiken
- **Schicht 3 (Fachklasse):** `Ticket` - Repräsentiert ein einzelnes Support-Ticket
- **Datenhaltung:** CSV-basiert (ohne relationale Datenbank), um das System leichtgewichtig zu halten

---

## Folie 4: Kern-Funktionalitäten (CRUD)
**Titel:** 3. Funktionalitäten im Überblick
- **Create:** Neue Tickets (Incident, Request) mit Titel, Priorität und Text anlegen
- **Read:** Alle Tickets übersichtlich anzeigen (oder per CLI auflisten)
- **Update:** Vorhandene Tickets aktualisieren
- **Delete:** Tickets löschen
- **Extra Logik:** Statistische Auswertung nach Prioritäten und Suchfunktion nach Stichworten

---

## Folie 5: OOP in der Praxis (Leitfragen)
**Titel:** 4. Kapselung und Klassen
- **Kapselung (Encapsulation):** Attribute (z.B. `__ticket_id`) sind nach außen unsichtbar (private).
- **Sicherheit:** Der Zugriff auf die Daten erfolgt ausschließlich über kontrollierte Methoden (Getter).
- **Warum?** Verhindert unbeabsichtigte Überschreibung von kritischen Daten durch andere Programmteile.

---

## Folie 6: Code-Snippet: Die Ticket-Klasse
**Titel:** 5. Ein Blick in den Code

```python
class Ticket:
    def __init__(self, ticket_id, title, priority, text):
        self.__ticket_id = ticket_id # private
        self.__title = title
        self.__priority = priority
        self.__text = text

    def get_title(self):
        return self.__title # kontrollierter Zugriff
```

---

## Folie 7: UML Klassendiagramm
**Titel:** 6. Struktur unserer Anwendung
*(Hier das Bild des UML Klassendiagramms einfügen)*
- **TicketSystem** (1) ----> (1) **FileManager**
- **FileManager** (1) ----> (*) **Ticket**
- Klares Zusammenspiel durch Assoziationen.

---

## Folie 8: Reflexion & Fazit
**Titel:** 7. Fazit des Projekts
- **Was lief gut?** Die 3-Schichten-Architektur hat den Code übersichtlich gehalten.
- **Herausforderungen:** Die exakte Einhaltung der strikten Vorgaben (z.B. Variablen-Namen) erforderte einiges Refactoring.
- **Learnings:** Interfaces und Spezifikationen sind in der Teamentwicklung das A und O. Der Code ist jetzt sauber, professionell (ohne Emojis/Slang) und einsatzbereit.
- **Ausblick:** Einfache Erweiterbarkeit um weitere Klassen (z.B. `User`).

---

## Folie 9: Q&A
**Titel:** Fragen?
- Vielen Dank für die Aufmerksamkeit!
- Wir zeigen nun eine kurze Live-Demo.
