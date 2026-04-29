import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import random

# Fachklasse
class Ticket:
    def __init__(self, ticket_id, title, priority, text):
        self.__ticket_id = ticket_id
        self.__title = title
        self.__priority = priority
        self.__text = text

    def get_ticket(self):
        return {
            "ticket_id": self.__ticket_id,
            "title": self.__title,
            "priority": self.__priority,
            "text": self.__text
        }

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_priority(self):
        return self.__priority
        
    def get_ticket_id(self):
        return self.__ticket_id

# Datenverwaltung
class FileManager:
    def __init__(self):
        self.csv_file = "tickets.csv"
        self.users_file = "users.csv"
        self.status_option = ["Offen", "In Bearbeitung", "Geschlossen"] 
        self.ticket_types = ["Incident", "Service Request", "Problem"] 

    def load_users(self):
        users = []
        if os.path.exists(self.users_file):
            with open(self.users_file, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        users.append(row[0])
        return users

    def save_users(self, user_name):
        users = self.load_users()
        if user_name not in users:
            users.append(user_name)
            with open(self.users_file, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                for u in users:
                    writer.writerow([u])

    def delete_users(self, user_name):
        users = self.load_users()
        if user_name in users:
            users.remove(user_name)
            with open(self.users_file, mode="w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file)
                for u in users:
                    writer.writerow([u])

    def load_tickets(self):
        tickets = []
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 4:
                        tickets.append(Ticket(row[0], row[1], row[2], row[3]))
        return tickets

    def save_tickets(self, tickets):
        with open(self.csv_file, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            for t in tickets:
                ticket_data = t.get_ticket()
                writer.writerow([
                    ticket_data["ticket_id"],
                    ticket_data["title"],
                    ticket_data["priority"],
                    ticket_data["text"]
                ])
                
    # Logik-Methoden mit Rückgabewert
    def search_tickets(self, keyword):
        tickets = self.load_tickets()
        result = []
        for t in tickets:
            if keyword.lower() in t.get_title().lower() or keyword.lower() in t.get_text().lower():
                result.append(t)
        return result

    def calculate_priority_stats(self):
        tickets = self.load_tickets()
        stats = {"Hoch": 0, "Mittel": 0, "Niedrig": 0}
        for t in tickets:
            prio = t.get_priority()
            if prio in stats:
                stats[prio] += 1
            else:
                stats[prio] = 1 
        return stats

# Hauptklasse/UI
class TicketSystem:
    def __init__(self, root):
        self.data_manager = FileManager()
        self.root = root
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Ticket Management System")
        self.root.geometry("900x600")
        
        # Style (Sachliches, professionelles Design)
        style = ttk.Style()
        style.theme_use("clam")
        
        # Main Frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Left Panel (Inputs)
        left_panel = ttk.LabelFrame(main_frame, text="Ticket Eingabe", padding="10")
        left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        
        ttk.Label(left_panel, text="Ticket ID:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_id = ttk.Entry(left_panel)
        self.entry_id.grid(row=0, column=1, pady=2)
        
        ttk.Label(left_panel, text="Titel:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.entry_title = ttk.Entry(left_panel)
        self.entry_title.grid(row=1, column=1, pady=2)
        
        ttk.Label(left_panel, text="Prioritaet:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.combo_priority = ttk.Combobox(left_panel, values=["Hoch", "Mittel", "Niedrig"])
        self.combo_priority.grid(row=2, column=1, pady=2)
        self.combo_priority.set("Mittel")
        
        ttk.Label(left_panel, text="Text/Beschreibung:").grid(row=3, column=0, sticky=tk.NW, pady=2)
        self.text_desc = tk.Text(left_panel, height=5, width=20)
        self.text_desc.grid(row=3, column=1, pady=2)
        
        btn_frame = ttk.Frame(left_panel)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
        
        ttk.Button(btn_frame, text="Speichern", command=self.save_ticket).grid(row=0, column=0, padx=2)
        ttk.Button(btn_frame, text="Leeren", command=self.clear_inputs).grid(row=0, column=1, padx=2)
        ttk.Button(btn_frame, text="Loeschen", command=self.delete_tickets).grid(row=1, column=0, padx=2, pady=5)
        ttk.Button(btn_frame, text="Statistik", command=self.show_stats).grid(row=1, column=1, padx=2, pady=5)
        
        # Right Panel (List)
        right_panel = ttk.LabelFrame(main_frame, text="Ticket Liste", padding="10")
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Search Frame
        search_frame = ttk.Frame(right_panel)
        search_frame.pack(fill=tk.X, pady=5)
        ttk.Label(search_frame, text="Suchen:").pack(side=tk.LEFT)
        self.entry_search = ttk.Entry(search_frame)
        self.entry_search.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        ttk.Button(search_frame, text="Suchen", command=self.search_ticket_ui).pack(side=tk.LEFT)
        ttk.Button(search_frame, text="Alle", command=self.update_tickets).pack(side=tk.LEFT, padx=2)
        
        # Treeview
        columns = ("ID", "Titel", "Prioritaet")
        self.tree = ttk.Treeview(right_panel, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(fill=tk.BOTH, expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        
        self.load_tickets()

    def clear_inputs(self):
        self.entry_id.delete(0, tk.END)
        self.entry_title.delete(0, tk.END)
        self.combo_priority.set("Mittel")
        self.text_desc.delete("1.0", tk.END)

    def save_ticket(self):
        ticket_id = self.entry_id.get().strip()
        title = self.entry_title.get().strip()
        priority = self.combo_priority.get().strip()
        text = self.text_desc.get("1.0", tk.END).strip()
        
        if not title or not text:
            messagebox.showwarning("Fehler", "Titel und Text duerfen nicht leer sein.")
            return
            
        if not ticket_id:
            ticket_id = str(random.randint(1000, 9999))
            
        new_ticket = Ticket(ticket_id, title, priority, text)
        tickets = self.data_manager.load_tickets()
        
        updated = False
        for i, t in enumerate(tickets):
            if t.get_ticket_id() == ticket_id:
                tickets[i] = new_ticket
                updated = True
                break
                
        if not updated:
            tickets.append(new_ticket)
            
        self.data_manager.save_tickets(tickets)
        self.update_tickets()
        self.clear_inputs()
        messagebox.showinfo("Erfolg", "Ticket gespeichert.")

    def update_tickets(self):
        self.load_tickets()

    def load_tickets(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        tickets = self.data_manager.load_tickets()
        for t in tickets:
            self.tree.insert("", tk.END, values=(t.get_ticket_id(), t.get_title(), t.get_priority()))

    def delete_tickets(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Fehler", "Bitte ein Ticket zum Loeschen auswaehlen.")
            return
            
        ticket_id = self.tree.item(selected[0])['values'][0]
        tickets = self.data_manager.load_tickets()
        
        tickets = [t for t in tickets if t.get_ticket_id() != str(ticket_id)]
        self.data_manager.save_tickets(tickets)
        self.update_tickets()
        self.clear_inputs()
        messagebox.showinfo("Erfolg", "Ticket geloescht.")

    def on_tree_select(self, event):
        selected = self.tree.selection()
        if not selected:
            return
            
        ticket_id = self.tree.item(selected[0])['values'][0]
        tickets = self.data_manager.load_tickets()
        
        for t in tickets:
            if t.get_ticket_id() == str(ticket_id):
                self.clear_inputs()
                self.entry_id.insert(0, t.get_ticket_id())
                self.entry_title.insert(0, t.get_title())
                self.combo_priority.set(t.get_priority())
                self.text_desc.insert("1.0", t.get_text())
                break
                
    def search_ticket_ui(self):
        keyword = self.entry_search.get().strip()
        if not keyword:
            self.update_tickets()
            return
            
        result = self.data_manager.search_tickets(keyword)
        for item in self.tree.get_children():
            self.tree.delete(item)
        for t in result:
            self.tree.insert("", tk.END, values=(t.get_ticket_id(), t.get_title(), t.get_priority()))
            
    def show_stats(self):
        stats = self.data_manager.calculate_priority_stats()
        stat_text = f"Statistik der Prioritaeten:\n\nHoch: {stats.get('Hoch', 0)}\nMittel: {stats.get('Mittel', 0)}\nNiedrig: {stats.get('Niedrig', 0)}"
        messagebox.showinfo("Statistik", stat_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicketSystem(root)
    root.mainloop()
