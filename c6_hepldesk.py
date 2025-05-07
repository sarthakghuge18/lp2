class HelpDesk:
    def __init__(self):
        self.tickets = []  # List to store all tickets
        self.technicians = ["Alice", "Bob", "Charlie"]  # List of technicians

    def create_ticket(self, issue_description, priority="Medium"):
        """Create a new ticket with a unique ticket ID, description, priority, and status."""
        ticket_id = len(self.tickets) + 1
        ticket = {
            "ticket_id": ticket_id,
            "issue_description": issue_description,
            "priority": priority,
            "status": "Open",
            "assigned_to": None
        }
        self.tickets.append(ticket)
        print(f"\nTicket #{ticket_id} created: '{issue_description}' with Priority: {priority}")

    def assign_ticket(self, ticket_id):
        """Assign an open ticket to a technician."""
        for ticket in self.tickets:
            if ticket["ticket_id"] == ticket_id and ticket["status"] == "Open":
                # Assign technician using round-robin based on ticket ID
                assigned_tech = self.technicians[ticket_id % len(self.technicians)]
                ticket["assigned_to"] = assigned_tech
                print(f" Ticket #{ticket_id} assigned to {assigned_tech}.")
                return
        print(" Ticket not found or already resolved.")

    def resolve_ticket(self, ticket_id):
        """Mark an open ticket as resolved."""
        for ticket in self.tickets:
            if ticket["ticket_id"] == ticket_id and ticket["status"] == "Open":
                ticket["status"] = "Resolved"
                print(f" Ticket #{ticket_id} marked as resolved.")
                return
        print(" Ticket not found or already resolved.")

    def view_tickets(self):
        """View all tickets with their details."""
        print("\nCurrent Help Desk Tickets:")
        if not self.tickets:
            print("No tickets available.")
        for ticket in self.tickets:
            print(f"- Ticket #{ticket['ticket_id']}: {ticket['issue_description']} | "
                  f"Priority: {ticket['priority']} | Status: {ticket['status']} | "
                  f"Assigned to: {ticket['assigned_to']}")

def run_helpdesk_system():
    """Function to run the Help Desk system."""
    system = HelpDesk()
    print(" Welcome to the Help Desk Expert System ")

    while True:
        print("\nChoose an option:")
        print("1. Create a new ticket")
        print("2. View all tickets")
        print("3. Assign a ticket")
        print("4. Resolve a ticket")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            issue = input(" Enter issue description: ")
            priority = input("Enter priority (Low/Medium/High): ").capitalize()
            if priority not in ["Low", "Medium", "High"]:
                priority = "Medium"  # Default to Medium if an invalid priority is entered
            system.create_ticket(issue, priority)

        elif choice == "2":
            system.view_tickets()

        elif choice == "3":
            try:
                ticket_id = int(input("Enter ticket ID to assign: "))
                system.assign_ticket(ticket_id)
            except ValueError:
                print("Invalid ID")

        elif choice == "4":
            try:
                ticket_id = int(input("Enter ticket ID to resolve: "))
                system.resolve_ticket(ticket_id)
            except ValueError:
                print(" Invalid ID")

        elif choice == "5":
            print("Exiting Help Desk Expert System. Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

# Run the system
run_helpdesk_system()
