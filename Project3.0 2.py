# Ticket-Management-System: Verwaltet Support-Tickets mit Tkinter-GUI und CSV-Speicher
# Nutzt Klassen mit Datenkapselung für sichere Daten und wartbaren Code

import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from tkcalendar import Calendar
import csv
import os
import random
from datetime import datetime


class Ticket:
    def __init__(self, ticket_id, title, text, priority, due_date, assigned_to, request_date, reporter, company, status,
                 escalation_level, ticket_type, comments, department, progress, support_history):
        self.__ticket_id = ticket_id
        self.__title = title
        self.__text = text
        self.__priority = priority
        self.__due_date = due_date
        self.__assigned_to = assigned_to
        self.__request_date = request_date
        self.__reporter = reporter
        self.__company = company
        self.__status = status
        self.__escalation_level = escalation_level
        self.__ticket_type = ticket_type
        self.__comments = comments
        self.__department = department
        self.__progress = progress
        self.__support_history = support_history

    def get_ticket_id(self): return self.__ticket_id
    def get_title(self): return self.__title
    def get_text(self): return self.__text
    def get_priority(self): return self.__priority
    def get_due_date(self): return self.__due_date
    def get_assigned_to(self): return self.__assigned_to
    def get_request_date(self): return self.__request_date
    def get_reporter(self): return self.__reporter
    def get_company(self): return self.__company
    def get_status(self): return self.__status
    def get_escalation_level(self): return self.__escalation_level
    def get_ticket_type(self): return self.__ticket_type
    def get_comments(self): return self.__comments
    def get_department(self): return self.__department
    def get_progress(self): return self.__progress
    def get_support_history(self): return self.__support_history

    def set_title(self, title): self.__title = title
    def set_text(self, text): self.__text = text
    def set_priority(self, priority): self.__priority = priority
    def set_due_date(self, due_date): self.__due_date = due_date
    def set_assigned_to(self, assigned_to): self.__assigned_to = assigned_to
    def set_request_date(self, request_date): self.__request_date = request_date
    def set_reporter(self, reporter): self.__reporter = reporter
    def set_company(self, company): self.__company = company
    def set_status(self, status): self.__status = status
    def set_escalation_level(self, escalation_level): self.__escalation_level = escalation_level
    def set_ticket_type(self, ticket_type): self.__ticket_type = ticket_type
    def set_comments(self, comments): self.__comments = comments
    def set_department(self, department): self.__department = department
    def set_progress(self, progress): self.__progress = progress
    def set_support_history(self, support_history): self.__support_history = support_history

    def to_list(self):
        return [self.__ticket_id, self.__title, self.__text, self.__priority, self.__due_date, self.__assigned_to,
                self.__request_date, self.__reporter, self.__company, self.__status, self.__escalation_level,
                self.__ticket_type, self.__comments, self.__department, self.__progress, self.__support_history]


class DataManager:
    def __init__(self):
        self.__csv_file = "tickets.csv"
        self.__employees_file = "employees.csv"
        self.__reporters_file = "reporters.csv"
        self.__companies_file = "companies.csv"
        self.__status_options = ["Gesichtet", "In Bearbeitung", "Fertig", "Abgebrochen", "Wartend", "Überprüfung"]
        self.__ticket_types = ["Fehler", "Eskalation", "Wartung", "Support", "Verbesserung"]
        self.__departments = ["IT", "HR", "Finanzen", "Sales", "Support"]

    def load_employees(self):
        if os.path.exists(self.__employees_file):
            with open(self.__employees_file, "r", encoding="utf-8") as file:
                return [row[0] for row in csv.reader(file) if row]
        return ["Monitoring API"]

    def save_employee(self, employee):
        if not employee: return
        employees = self.load_employees()
        if employee not in employees:
            employees.append(employee)
            with open(self.__employees_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for emp in employees:
                    writer.writerow([emp])

    def delete_employee(self, employee):
        if not employee or employee == "Nicht zugewiesen": return
        employees = self.load_employees()
        if employee in employees:
            employees.remove(employee)
            with open(self.__employees_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for emp in employees:
                    writer.writerow([emp])

    def load_reporters(self):
        if os.path.exists(self.__reporters_file):
            with open(self.__reporters_file, "r", encoding="utf-8") as file:
                return {row[0]: row[1] for row in csv.reader(file) if len(row) >= 2}
        return {}

    def save_reporter(self, reporter, info=""):
        if not reporter: return
        reporters = self.load_reporters()
        reporters[reporter] = info
        with open(self.__reporters_file, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for name, inf in reporters.items():
                writer.writerow([name, inf])

    def delete_reporter(self, reporter):
        if not reporter: return
        reporters = self.load_reporters()
        if reporter in reporters:
            del reporters[reporter]
            with open(self.__reporters_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for name, inf in reporters.items():
                    writer.writerow([name, inf])

    def load_companies(self):
        if os.path.exists(self.__companies_file):
            with open(self.__companies_file, "r", encoding="utf-8") as file:
                return [row[0] for row in csv.reader(file) if row]
        return []

    def save_company(self, company):
        if not company: return
        companies = self.load_companies()
        if company not in companies:
            companies.append(company)
            with open(self.__companies_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for comp in companies:
                    writer.writerow([comp])

    def delete_company(self, company):
        if not company: return
        companies = self.load_companies()
        if company in companies:
            companies.remove(company)
            with open(self.__companies_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                for comp in companies:
                    writer.writerow([comp])

    def generate_ticket_id(self):
        return random.randint(1000, 9999)

    def load_tickets(self, file_path=None):
        file_path = file_path or self.__csv_file
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                return [Ticket(*row) for row in csv.reader(file) if len(row) >= 16]
        return []

    def save_tickets(self, tickets, file_path=None):
        file_path = file_path or self.__csv_file
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([ticket.to_list() for ticket in tickets])

    def get_status_options(self): return self.__status_options
    def get_ticket_types(self): return self.__ticket_types
    def get_departments(self): return self.__departments
    def set_csv_file(self, file_path): self.__csv_file = file_path


class TicketSystemGUI:
    def __init__(self, data_manager):
        self.data_manager = data_manager
        self.root = tk.Tk()
        self.root.title("Ticket System 🎫")
        self.root.geometry("1550x920")
        self.root.minsize(1200, 700)
        self.root.resizable(True, True)
        self.root.configure(bg="#1e1e2e")

        # Moderne Styles
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(".", background="#1e1e2e", foreground="#cdd6f4", font=("Segoe UI", 10))
        self.style.configure("TLabel", background="#1e1e2e", foreground="#cdd6f4")
        self.style.configure("TEntry", fieldbackground="#313244", foreground="#cdd6f4", insertcolor="#89b4fa")
        self.style.configure("TButton", background="#89b4fa", foreground="#1e1e2e", font=("Segoe UI", 10, "bold"), padding=8)
        self.style.map("TButton", background=[("active", "#74a8fc")])
        self.style.configure("Accent.TButton", background="#cba6f7", foreground="#1e1e2e")
        self.style.map("Accent.TButton", background=[("active", "#b4a0e0")])
        self.style.configure("Treeview", background="#313244", foreground="#cdd6f4", fieldbackground="#313244")
        self.style.configure("Treeview.Heading", background="#45475a", foreground="#cdd6f4")
        self.style.map("Treeview", background=[("selected", "#89b4fa")], foreground=[("selected", "#1e1e2e")])

        # Variablen
        self.priority_var = tk.StringVar(value="Mittel")
        self.assigned_var = tk.StringVar(value="Nicht zugewiesen")
        self.reporter_var = tk.StringVar(value="")
        self.company_var = tk.StringVar(value="")
        self.status_var = tk.StringVar(value=self.data_manager.get_status_options()[0])
        self.escalation_var = tk.StringVar(value="Level 1")
        self.ticket_type_var = tk.StringVar(value=self.data_manager.get_ticket_types()[0])
        self.department_var = tk.StringVar(value=self.data_manager.get_departments()[0])
        self.progress_var = tk.StringVar(value="0%")

        self.setup_modern_gui()

    def setup_modern_gui(self):
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header = ttk.Frame(main_frame)
        header.pack(fill=tk.X, pady=(0, 15))
        ttk.Label(header, text="🎫 Ticket Management System", font=("Segoe UI", 18, "bold")).pack(side=tk.LEFT)
        ttk.Button(header, text="📤 Exportieren", style="Accent.TButton", command=self.export_tickets).pack(side=tk.RIGHT, padx=5)
        ttk.Button(header, text="🔄 Laden", command=self.load_tickets).pack(side=tk.RIGHT, padx=5)

        # PanedWindow für dynamisch skalierbare Spalten (drag & drop möglich)
        self.paned = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True)

        # === Linke Spalte: Eingabefelder (vollständig scrollbar) ===
        left_pane = ttk.LabelFrame(self.paned, text=" Neues / Bearbeitetes Ticket ", padding=10)
        self.paned.add(left_pane, weight=35)

        left_canvas = tk.Canvas(left_pane, bg="#1e1e2e", highlightthickness=0)
        v_scroll = ttk.Scrollbar(left_pane, orient="vertical", command=left_canvas.yview)
        h_scroll = ttk.Scrollbar(left_pane, orient="horizontal", command=left_canvas.xview)

        self.left_frame = ttk.Frame(left_canvas, padding=10)

        left_canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        left_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas_window = left_canvas.create_window((0, 0), window=self.left_frame, anchor="nw")

        def configure_left(event):
            left_canvas.configure(scrollregion=left_canvas.bbox("all"))
        self.left_frame.bind("<Configure>", configure_left)

        def resize_left(event):
            left_canvas.itemconfig(self.canvas_window, width=event.width)
        left_canvas.bind("<Configure>", resize_left)

        # === Mittlere Spalte: Ticket-Liste (vollständig scrollbar) ===
        middle_pane = ttk.LabelFrame(self.paned, text=" Tickets ", padding=10)
        self.paned.add(middle_pane, weight=40)

        # === Rechte Spalte: Ticket-Details (vollständig scrollbar) ===
        right_pane = ttk.LabelFrame(self.paned, text=" Ticket-Details ", padding=10)
        self.paned.add(right_pane, weight=25)

        self.create_form(self.left_frame)
        self.create_ticket_list(middle_pane)
        self.create_detail_view(right_pane)

        self.update_ticket_list(self.data_manager.load_tickets())

    def create_form(self, parent):
        row = 0
        ttk.Label(parent, text="Ticket ID 🆔:").grid(row=row, column=0, sticky="w", pady=6)
        self.entry_ticket_id = ttk.Entry(parent, width=50)
        self.entry_ticket_id.grid(row=row, column=1, pady=6, sticky="ew")
        row += 1

        ttk.Label(parent, text="Titel 📝:").grid(row=row, column=0, sticky="w", pady=6)
        self.entry_title = ttk.Entry(parent, width=50)
        self.entry_title.grid(row=row, column=1, pady=6, sticky="ew")
        row += 1

        ttk.Label(parent, text="Beschreibung ✍️:").grid(row=row, column=0, sticky="nw", pady=6)
        self.entry_text = tk.Text(parent, width=50, height=6, bg="#313244", fg="#cdd6f4", insertbackground="#89b4fa", font=("Segoe UI", 10))
        self.entry_text.grid(row=row, column=1, pady=6, sticky="ew")
        row += 1

        ttk.Label(parent, text="Priorität ⚡:").grid(row=row, column=0, sticky="w", pady=6)
        ttk.OptionMenu(parent, self.priority_var, "Mittel", "Hoch", "Mittel", "Niedrig").grid(row=row, column=1, sticky="w", pady=6)
        row += 1

        ttk.Label(parent, text="Fällig bis 📅:").grid(row=row, column=0, sticky="w", pady=6)
        self.entry_due = ttk.Entry(parent, width=40)
        self.entry_due.grid(row=row, column=1, pady=6, sticky="w")
        ttk.Button(parent, text="🗓️", width=3, command=self.open_calendar).grid(row=row, column=1, sticky="e")
        row += 1

        ttk.Label(parent, text="Erstelldatum 🕒:").grid(row=row, column=0, sticky="w", pady=6)
        self.entry_request_date = ttk.Entry(parent, width=40)
        self.entry_request_date.grid(row=row, column=1, pady=6, sticky="w")
        ttk.Button(parent, text="🗓️", width=3, command=self.open_request_date_calendar).grid(row=row, column=1, sticky="e")
        row += 1

        ttk.Label(parent, text="Zugewiesen an 👤:").grid(row=row, column=0, sticky="w", pady=6)
        frame = ttk.Frame(parent)
        frame.grid(row=row, column=1, sticky="ew", pady=6)
        self.assigned_menu = ttk.OptionMenu(frame, self.assigned_var, "Nicht zugewiesen")
        self.assigned_menu.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry_new_employee = ttk.Entry(frame, width=18)
        self.entry_new_employee.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame, text="➕", width=3, command=self.add_employee).pack(side=tk.LEFT)
        ttk.Button(frame, text="🗑️", width=3, command=self.delete_employee).pack(side=tk.LEFT)
        row += 1

        ttk.Label(parent, text="Meldender 🗣️:").grid(row=row, column=0, sticky="w", pady=6)
        frame = ttk.Frame(parent)
        frame.grid(row=row, column=1, sticky="ew", pady=6)
        self.reporter_menu = ttk.OptionMenu(frame, self.reporter_var, "")
        self.reporter_menu.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry_new_reporter = ttk.Entry(frame, width=18)
        self.entry_new_reporter.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame, text="➕", width=3, command=self.add_reporter).pack(side=tk.LEFT)
        ttk.Button(frame, text="🗑️", width=3, command=self.delete_reporter).pack(side=tk.LEFT)
        row += 1

        ttk.Label(parent, text="Unternehmen 🏢:").grid(row=row, column=0, sticky="w", pady=6)
        frame = ttk.Frame(parent)
        frame.grid(row=row, column=1, sticky="ew", pady=6)
        self.company_menu = ttk.OptionMenu(frame, self.company_var, "")
        self.company_menu.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry_new_company = ttk.Entry(frame, width=18)
        self.entry_new_company.pack(side=tk.LEFT, padx=5)
        ttk.Button(frame, text="➕", width=3, command=self.add_company).pack(side=tk.LEFT)
        ttk.Button(frame, text="🗑️", width=3, command=self.delete_company).pack(side=tk.LEFT)
        row += 1

        ttk.Label(parent, text="Status 🌟:").grid(row=row, column=0, sticky="w", pady=6)
        ttk.OptionMenu(parent, self.status_var, self.data_manager.get_status_options()[0], *self.data_manager.get_status_options()).grid(row=row, column=1, sticky="w", pady=6)
        row += 1

        ttk.Label(parent, text="Eskalationsstufe 📈:").grid(row=row, column=0, sticky="w", pady=6)
        ttk.OptionMenu(parent, self.escalation_var, "Level 1", "Level 1", "Level 2", "Level 3").grid(row=row, column=1, sticky="w", pady=6)
        row += 1

        ttk.Label(parent, text="Ticket-Typ 🎟️:").grid(row=row, column=0, sticky="w", pady=6)
        ttk.OptionMenu(parent, self.ticket_type_var, self.data_manager.get_ticket_types()[0], *self.data_manager.get_ticket_types()).grid(row=row, column=1, sticky="w", pady=6)
        row += 1

        ttk.Label(parent, text="Abteilung 🏬:").grid(row=row, column=0, sticky="w", pady=6)
        ttk.OptionMenu(parent, self.department_var, self.data_manager.get_departments()[0], *self.data_manager.get_departments()).grid(row=row, column=1, sticky="w", pady=6)
        row += 1

        ttk.Label(parent, text="Fortschritt 📊:").grid(row=row, column=0, sticky="w", pady=6)
        ttk.OptionMenu(parent, self.progress_var, "0%", "0%", "25%", "50%", "75%", "100%").grid(row=row, column=1, sticky="w", pady=6)
        row += 1

        ttk.Label(parent, text="Support Historie 📜:").grid(row=row, column=0, sticky="nw", pady=6)
        self.entry_support_history = tk.Text(parent, width=50, height=5, bg="#313244", fg="#cdd6f4", insertbackground="#89b4fa")
        self.entry_support_history.grid(row=row, column=1, pady=6, sticky="ew")
        row += 1

        ttk.Label(parent, text="Kommentare 💬:").grid(row=row, column=0, sticky="nw", pady=6)
        self.entry_comments = tk.Text(parent, width=50, height=5, bg="#313244", fg="#cdd6f4", insertbackground="#89b4fa")
        self.entry_comments.grid(row=row, column=1, pady=6, sticky="ew")
        row += 1

        ttk.Label(parent, text="Kontaktdaten ℹ️:").grid(row=row, column=0, sticky="nw", pady=6)
        self.entry_reporter_info = tk.Text(parent, width=50, height=4, bg="#313244", fg="#cdd6f4", insertbackground="#89b4fa")
        self.entry_reporter_info.grid(row=row, column=1, pady=6, sticky="ew")
        row += 1

        btn_frame = ttk.Frame(parent)
        btn_frame.grid(row=row, column=0, columnspan=2, pady=15)
        ttk.Button(btn_frame, text="💾 Ticket speichern", style="Accent.TButton", command=self.save_ticket).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🧹 Leeren", command=self.clear_entries).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="🗑️ Löschen", command=self.delete_ticket).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="📑 Nach ID sortieren", command=lambda: self.sort_tickets("ID")).pack(side=tk.LEFT, padx=5)

        parent.columnconfigure(1, weight=1)

        self.update_assigned_menu()
        self.update_reporter_menu()
        self.update_company_menu()

    def create_ticket_list(self, parent):
        columns = ("ID", "Titel", "Priorität", "Fällig bis", "Status", "Abteilung", "Fortschritt")
        self.ticket_list = ttk.Treeview(parent, columns=columns, show="headings", height=25)

        for col in columns:
            self.ticket_list.heading(col, text=col, command=lambda c=col: self.sort_tickets(c))
            self.ticket_list.column(col, width=130 if col != "Titel" else 320, minwidth=80)

        v_scroll = ttk.Scrollbar(parent, orient="vertical", command=self.ticket_list.yview)
        h_scroll = ttk.Scrollbar(parent, orient="horizontal", command=self.ticket_list.xview)
        self.ticket_list.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        self.ticket_list.grid(row=0, column=0, sticky="nsew")
        v_scroll.grid(row=0, column=1, sticky="ns")
        h_scroll.grid(row=1, column=0, sticky="ew")

        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)

        self.ticket_list.bind("<<TreeviewSelect>>", self.display_ticket)

        self.ticket_list.tag_configure("overdue", background="#f38ba8", foreground="#1e1e2e")
        self.ticket_list.tag_configure("due_today", background="#f9e2af", foreground="#1e1e2e")
        self.ticket_list.tag_configure("on_time", background="#a6e3a1", foreground="#1e1e2e")

    def create_detail_view(self, parent):
        detail_canvas = tk.Canvas(parent, bg="#1e1e2e", highlightthickness=0)
        v_scroll = ttk.Scrollbar(parent, orient="vertical", command=detail_canvas.yview)
        h_scroll = ttk.Scrollbar(parent, orient="horizontal", command=detail_canvas.xview)

        detail_inner = ttk.Frame(detail_canvas)
        self.detail_text = tk.Text(detail_inner, bg="#313244", fg="#cdd6f4", font=("Segoe UI", 10), wrap="none", state="disabled")

        detail_canvas.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)

        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        detail_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        detail_canvas.create_window((0, 0), window=detail_inner, anchor="nw")

        self.detail_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        def configure_detail(event):
            detail_canvas.configure(scrollregion=detail_canvas.bbox("all"))
        detail_inner.bind("<Configure>", configure_detail)

    # ==================== Alle weiteren Methoden (unverändert) ====================

    def update_assigned_menu(self):
        menu = self.assigned_menu["menu"]
        menu.delete(0, "end")
        for emp in ["Nicht zugewiesen"] + self.data_manager.load_employees():
            menu.add_command(label=emp, command=lambda v=emp: self.assigned_var.set(v))

    def update_reporter_menu(self):
        menu = self.reporter_menu["menu"]
        menu.delete(0, "end")
        for rep in self.data_manager.load_reporters().keys():
            menu.add_command(label=rep, command=lambda v=rep: [self.reporter_var.set(v), self.update_reporter_info()])

    def update_company_menu(self):
        menu = self.company_menu["menu"]
        menu.delete(0, "end")
        for comp in [""] + self.data_manager.load_companies():
            menu.add_command(label=comp, command=lambda v=comp: self.company_var.set(v))

    def update_reporter_info(self):
        reporter = self.reporter_var.get()
        reporters = self.data_manager.load_reporters()
        self.entry_reporter_info.delete("1.0", tk.END)
        if reporter in reporters:
            self.entry_reporter_info.insert("1.0", reporters[reporter])

    def save_ticket(self):
        ticket_id = self.entry_ticket_id.get().strip()
        if not ticket_id:
            ticket_id = str(self.data_manager.generate_ticket_id())
            self.entry_ticket_id.delete(0, tk.END)
            self.entry_ticket_id.insert(0, ticket_id)

        title = self.entry_title.get().strip()
        text = self.entry_text.get("1.0", tk.END).strip()
        priority = self.priority_var.get()
        due_date = self.entry_due.get().strip()
        assigned_to = self.assigned_var.get() if self.assigned_var.get() != "Nicht zugewiesen" else ""
        request_date = self.entry_request_date.get().strip() or datetime.now().strftime("%Y-%m-%d")
        reporter = self.reporter_var.get().strip()
        company = self.company_var.get().strip()
        status = self.status_var.get()
        escalation_level = self.escalation_var.get()
        ticket_type = self.ticket_type_var.get()
        comments = self.entry_comments.get("1.0", tk.END).strip()
        department = self.department_var.get()
        progress = self.progress_var.get()
        support_history = self.entry_support_history.get("1.0", tk.END).strip()

        if not title or not text or not due_date or not reporter:
            messagebox.showwarning("Fehlende Daten", "Bitte die Pflichtfelder (Titel, Text, Fällig bis, Meldender) ausfüllen!")
            return

        tickets = self.data_manager.load_tickets()
        ticket = Ticket(ticket_id, title, text, priority, due_date, assigned_to, request_date, reporter, company,
                        status, escalation_level, ticket_type, comments, department, progress, support_history)

        for i, t in enumerate(tickets):
            if t.get_ticket_id() == ticket_id:
                tickets[i] = ticket
                break
        else:
            tickets.append(ticket)

        self.data_manager.save_tickets(tickets)
        self.update_ticket_list(tickets)
        self.clear_entries()
        messagebox.showinfo("Erfolg", "Ticket erfolgreich gespeichert!")

    def update_ticket_list(self, tickets):
        for item in self.ticket_list.get_children():
            self.ticket_list.delete(item)
        for ticket in tickets:
            status_display = "✅ " + ticket.get_status() if ticket.get_status() == "Fertig" else ticket.get_status()
            iid = self.ticket_list.insert("", "end", values=(
                ticket.get_ticket_id(), ticket.get_title(), ticket.get_priority(),
                ticket.get_due_date(), status_display, ticket.get_department(), ticket.get_progress()
            ))
            self.colorize_ticket(ticket.get_due_date(), iid)

    def colorize_ticket(self, due_date, item):
        try:
            due = datetime.strptime(due_date, "%Y-%m-%d")
            now = datetime.now()
            if due < now:
                self.ticket_list.item(item, tags=("overdue",))
            elif due.date() == now.date():
                self.ticket_list.item(item, tags=("due_today",))
            else:
                self.ticket_list.item(item, tags=("on_time",))
        except:
            pass

    def display_ticket(self, event):
        sel = self.ticket_list.selection()
        if not sel: return
        values = self.ticket_list.item(sel[0])['values']
        ticket_id = values[0]

        for ticket in self.data_manager.load_tickets():
            if ticket.get_ticket_id() == str(ticket_id):
                self.clear_entries()
                self.entry_ticket_id.insert(0, ticket.get_ticket_id())
                self.entry_title.insert(0, ticket.get_title())
                self.entry_text.delete("1.0", tk.END)
                self.entry_text.insert("1.0", ticket.get_text())
                self.priority_var.set(ticket.get_priority())
                self.entry_due.delete(0, tk.END)
                self.entry_due.insert(0, ticket.get_due_date())
                self.entry_request_date.delete(0, tk.END)
                self.entry_request_date.insert(0, ticket.get_request_date())
                self.assigned_var.set(ticket.get_assigned_to() or "Nicht zugewiesen")
                self.reporter_var.set(ticket.get_reporter())
                self.company_var.set(ticket.get_company())
                self.status_var.set(ticket.get_status())
                self.escalation_var.set(ticket.get_escalation_level())
                self.ticket_type_var.set(ticket.get_ticket_type())
                self.department_var.set(ticket.get_department())
                self.progress_var.set(ticket.get_progress())
                self.entry_comments.delete("1.0", tk.END)
                self.entry_comments.insert("1.0", ticket.get_comments())
                self.entry_support_history.delete("1.0", tk.END)
                self.entry_support_history.insert("1.0", ticket.get_support_history())
                self.update_reporter_info()

                self.detail_text.config(state="normal")
                self.detail_text.delete("1.0", tk.END)
                self.detail_text.insert("1.0", f"Ticket {ticket.get_ticket_id()}\n\n{ticket.get_text()}\n\nSupport-Historie:\n{ticket.get_support_history()}")
                self.detail_text.config(state="disabled")
                break

    def clear_entries(self):
        self.entry_ticket_id.delete(0, tk.END)
        self.entry_title.delete(0, tk.END)
        self.entry_text.delete("1.0", tk.END)
        self.entry_due.delete(0, tk.END)
        self.entry_request_date.delete(0, tk.END)
        self.assigned_var.set("Nicht zugewiesen")
        self.reporter_var.set("")
        self.company_var.set("")
        self.status_var.set(self.data_manager.get_status_options()[0])
        self.escalation_var.set("Level 1")
        self.ticket_type_var.set(self.data_manager.get_ticket_types()[0])
        self.department_var.set(self.data_manager.get_departments()[0])
        self.progress_var.set("0%")
        self.entry_comments.delete("1.0", tk.END)
        self.entry_support_history.delete("1.0", tk.END)
        self.entry_reporter_info.delete("1.0", tk.END)

    def delete_ticket(self):
        sel = self.ticket_list.selection()
        if not sel:
            messagebox.showwarning("Kein Ticket ausgewählt", "Bitte wählen Sie ein Ticket zum Löschen aus.")
            return
        ticket_id = self.ticket_list.item(sel[0])['values'][0]
        tickets = [t for t in self.data_manager.load_tickets() if t.get_ticket_id() != str(ticket_id)]
        self.data_manager.save_tickets(tickets)
        self.update_ticket_list(tickets)
        self.clear_entries()

    def sort_tickets(self, column):
        tickets = self.data_manager.load_tickets()
        if column == "ID":
            tickets.sort(key=lambda x: int(x.get_ticket_id()))
        elif column == "Titel":
            tickets.sort(key=lambda x: x.get_title().lower())
        elif column == "Priorität":
            tickets.sort(key=lambda x: x.get_priority())
        elif column == "Fällig bis":
            tickets.sort(key=lambda x: x.get_due_date())
        elif column == "Status":
            tickets.sort(key=lambda x: x.get_status())
        elif column == "Abteilung":
            tickets.sort(key=lambda x: x.get_department())
        elif column == "Fortschritt":
            tickets.sort(key=lambda x: x.get_progress())
        self.data_manager.save_tickets(tickets)
        self.update_ticket_list(tickets)

    def export_tickets(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not path: return
        tickets = self.data_manager.load_tickets()
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticket ID", "Titel", "Text", "Priorität", "Fällig bis", "Zugewiesen an", "Erstellungsdatum",
                             "Meldender", "Unternehmen", "Status", "Eskalationsstufe", "Ticket-Typ", "Kommentare",
                             "Abteilung", "Fortschritt", "Support Historie"])
            writer.writerows([t.to_list() for t in tickets])
        messagebox.showinfo("Export", "Tickets wurden erfolgreich exportiert!")

    def load_tickets(self):
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not path: return
        self.data_manager.set_csv_file(path)
        self.update_ticket_list(self.data_manager.load_tickets(path))

    def open_calendar(self):
        top = tk.Toplevel(self.root)
        cal = Calendar(top, selectmode="day", date_pattern="y-mm-dd")
        cal.pack(padx=10, pady=10)
        tk.Button(top, text="Auswählen", command=lambda: [self.entry_due.delete(0, tk.END), self.entry_due.insert(0, cal.get_date()), top.destroy()]).pack(pady=5)

    def open_request_date_calendar(self):
        top = tk.Toplevel(self.root)
        cal = Calendar(top, selectmode="day", date_pattern="y-mm-dd")
        cal.selection_set(datetime.now())
        cal.pack(padx=10, pady=10)
        tk.Button(top, text="Auswählen", command=lambda: [self.entry_request_date.delete(0, tk.END), self.entry_request_date.insert(0, cal.get_date()), top.destroy()]).pack(pady=5)

    def add_employee(self):
        emp = self.entry_new_employee.get().strip()
        if emp:
            self.data_manager.save_employee(emp)
            self.entry_new_employee.delete(0, tk.END)
            self.update_assigned_menu()

    def delete_employee(self):
        emp = self.assigned_var.get()
        self.data_manager.delete_employee(emp)
        self.assigned_var.set("Nicht zugewiesen")
        self.update_assigned_menu()

    def add_reporter(self):
        rep = self.entry_new_reporter.get().strip()
        info = self.entry_reporter_info.get("1.0", tk.END).strip()
        if rep:
            self.data_manager.save_reporter(rep, info)
            self.entry_new_reporter.delete(0, tk.END)
            self.update_reporter_menu()

    def delete_reporter(self):
        rep = self.reporter_var.get()
        self.data_manager.delete_reporter(rep)
        self.reporter_var.set("")
        self.update_reporter_menu()
        self.update_reporter_info()

    def add_company(self):
        comp = self.entry_new_company.get().strip()
        if comp:
            self.data_manager.save_company(comp)
            self.entry_new_company.delete(0, tk.END)
            self.update_company_menu()

    def delete_company(self):
        comp = self.company_var.get()
        self.data_manager.delete_company(comp)
        self.company_var.set("")
        self.update_company_menu()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    data_manager = DataManager()
    app = TicketSystemGUI(data_manager)
    app.run()