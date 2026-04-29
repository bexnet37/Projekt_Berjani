import os
import shutil

# Verzeichnisse definieren
abgabe_dir = "Lehrer_Abgabe"
dev_dir = "GitHub_Repository"

os.makedirs(abgabe_dir, exist_ok=True)
os.makedirs(dev_dir, exist_ok=True)

# A. Lehrer-Modus (Abgabe)
shutil.copy("main.py", os.path.join(abgabe_dir, "TicketSystem_Code.py"))
if os.path.exists("Dokumentation.md"):
    shutil.copy("Dokumentation.md", os.path.join(abgabe_dir, "Dokumentation.md"))
if os.path.exists("Praesentation.md"):
    shutil.copy("Praesentation.md", os.path.join(abgabe_dir, "Praesentation.md"))
if os.path.exists("test_ticket_system.py"):
    shutil.copy("test_ticket_system.py", os.path.join(abgabe_dir, "test_ticket_system.py"))

# B. Dev-Modus (GitHub)
shutil.copy("main.py", os.path.join(dev_dir, "main.py"))
if os.path.exists("cli.py"):
    shutil.copy("cli.py", os.path.join(dev_dir, "cli.py"))
if os.path.exists("test_ticket_system.py"):
    shutil.copy("test_ticket_system.py", os.path.join(dev_dir, "test_ticket_system.py"))

# Erstelle README.md für GitHub
readme_content = """# OOP-Verwaltung in Python: Ticket-System

Ein einfaches Ticket-System zur Verwaltung von Support-Anfragen.
Entwickelt von Bennet, Timothy und Jason (Klasse 10its2).

## Installation

1. Klonen Sie dieses Repository: `git clone <repo-url>`
2. Stellen Sie sicher, dass Python 3.x installiert ist.
3. (Optional) Richten Sie eine virtuelle Umgebung ein.
4. Führen Sie die Anwendung aus:
   - GUI: `python main.py`
   - CLI: `python cli.py`

## Architektur

Die App folgt einem 3-Schichten-Modell:
- **Fachklasse:** `Ticket`
- **Datenhaltung:** `FileManager` (CSV-basiert)
- **UI:** `TicketSystem` (Tkinter)
"""
with open(os.path.join(dev_dir, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

# Erstelle .gitignore für GitHub
gitignore_content = """__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/
tickets.csv
users.csv
test_tickets.csv
"""
with open(os.path.join(dev_dir, ".gitignore"), "w", encoding="utf-8") as f:
    f.write(gitignore_content)

# Erstelle Beispiel-CSVs für GitHub
with open(os.path.join(dev_dir, "tickets_example.csv"), "w", encoding="utf-8") as f:
    f.write("1001,Beispiel Ticket,Hoch,Das ist ein Test\n")
    
print("Abgabe-Ordner erfolgreich vorbereitet!")
