import unittest
import os
from main import Ticket, FileManager

class TestTicketSystem(unittest.TestCase):
    def setUp(self):
        # Setup temporary file for testing
        self.test_file = "test_tickets.csv"
        self.manager = FileManager()
        self.manager.csv_file = self.test_file
        
        # Create some test tickets
        self.tickets = [
            Ticket("1001", "Test Ticket 1", "Hoch", "Text 1"),
            Ticket("1002", "Test Ticket 2", "Mittel", "Text 2"),
            Ticket("1003", "Test Ticket 3", "Mittel", "Text 3")
        ]
        self.manager.save_tickets(self.tickets)

    def tearDown(self):
        # Clean up temporary file
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_calculate_priority_stats(self):
        # Execute the method to test
        stats = self.manager.calculate_priority_stats()
        
        # Verify the expected behavior
        self.assertEqual(stats.get("Hoch", 0), 1)
        self.assertEqual(stats.get("Mittel", 0), 2)
        self.assertEqual(stats.get("Niedrig", 0), 0)

    def test_search_tickets(self):
        # Test searching for a ticket
        result = self.manager.search_tickets("Ticket 2")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_ticket_id(), "1002")

if __name__ == "__main__":
    unittest.main()
