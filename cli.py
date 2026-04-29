import random
import os
from main import Ticket, FileManager

def print_menu():
    print("\n" + "="*30)
    print("Ticket Management System - CLI")
    print("="*30)
    print("1. Alle Tickets anzeigen")
    print("2. Ticket suchen")
    print("3. Neues Ticket einfuegen")
    print("4. Ticket aendern")
    print("5. Ticket loeschen")
    print("6. Statistik anzeigen")
    print("0. Programm beenden")
    print("="*30)

def main_cli():
    data_manager = FileManager()
    
    while True:
        print_menu()
        choice = input("Bitte waehlen Sie eine Option: ")
        
        if choice == "0":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
            
        elif choice == "1":
            tickets = data_manager.load_tickets()
            if not tickets:
                print("Keine Tickets gefunden.")
            else:
                for t in tickets:
                    print(f"ID: {t.get_ticket_id()} | Titel: {t.get_title()} | Prio: {t.get_priority()}")
                    
        elif choice == "2":
            keyword = input("Suchbegriff eingeben: ")
            result = data_manager.search_tickets(keyword)
            if not result:
                print("Keine passenden Tickets gefunden.")
            else:
                for t in result:
                    print(f"ID: {t.get_ticket_id()} | Titel: {t.get_title()} | Prio: {t.get_priority()}")
                    
        elif choice == "3":
            title = input("Titel des Tickets: ")
            text = input("Beschreibung: ")
            priority = input("Prioritaet (Hoch, Mittel, Niedrig): ")
            if not priority: priority = "Mittel"
            
            ticket_id = str(random.randint(1000, 9999))
            new_ticket = Ticket(ticket_id, title, priority, text)
            
            tickets = data_manager.load_tickets()
            tickets.append(new_ticket)
            data_manager.save_tickets(tickets)
            print(f"Ticket {ticket_id} erfolgreich angelegt.")
            
        elif choice == "4":
            ticket_id = input("ID des zu aendernden Tickets: ")
            tickets = data_manager.load_tickets()
            updated = False
            for i, t in enumerate(tickets):
                if t.get_ticket_id() == ticket_id:
                    print(f"Aktueller Titel: {t.get_title()}")
                    new_title = input("Neuer Titel (leer lassen fuer keine Aenderung): ") or t.get_title()
                    
                    print(f"Aktuelle Beschreibung: {t.get_text()}")
                    new_text = input("Neue Beschreibung (leer lassen fuer keine Aenderung): ") or t.get_text()
                    
                    print(f"Aktuelle Prioritaet: {t.get_priority()}")
                    new_prio = input("Neue Prioritaet (leer lassen fuer keine Aenderung): ") or t.get_priority()
                    
                    tickets[i] = Ticket(ticket_id, new_title, new_prio, new_text)
                    updated = True
                    break
                    
            if updated:
                data_manager.save_tickets(tickets)
                print("Ticket erfolgreich aktualisiert.")
            else:
                print("Ticket-ID nicht gefunden.")
                
        elif choice == "5":
            ticket_id = input("ID des zu loeschenden Tickets: ")
            tickets = data_manager.load_tickets()
            initial_count = len(tickets)
            tickets = [t for t in tickets if t.get_ticket_id() != ticket_id]
            
            if len(tickets) < initial_count:
                data_manager.save_tickets(tickets)
                print("Ticket erfolgreich geloescht.")
            else:
                print("Ticket-ID nicht gefunden.")
                
        elif choice == "6":
            stats = data_manager.calculate_priority_stats()
            print("Prioritaets-Statistik:")
            for k, v in stats.items():
                print(f"{k}: {v}")
                
        else:
            print("Ungueltige Eingabe. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main_cli()
