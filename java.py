class Ticket:
    tickets_created = 0
    tickets_resolved = 0
    tickets_open = 0
    ticket_list = []

    def __init__(self, creator_name, staff_id, email, description):
        self.ticket_number = Ticket.tickets_created + 2001
        self.creator_name = creator_name
        self.staff_id = staff_id
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.tickets_created += 1
        Ticket.tickets_open += 1
        Ticket.ticket_list.append(self)

    def resolve_password_change(self):
        if "Password Change" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"New password generated: {new_password}"
            self.status = "Closed"
            Ticket.tickets_resolved += 1
            Ticket.tickets_open -= 1

    def resolve_ticket(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.tickets_resolved += 1
        Ticket.tickets_open -= 1

    def reopen_ticket(self):
        if self.status == "Closed":
            self.status = "Reopened"
            Ticket.tickets_resolved -= 1
            Ticket.tickets_open += 1

    def print_ticket(self):
        print("Ticket Number:", self.ticket_number)
        print("Ticket Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)
        print()

    @staticmethod
    def ticket_stats():
        print("Tickets Created:", Ticket.tickets_created)
        print("Tickets Resolved:", Ticket.tickets_resolved)
        print("Tickets To Solve:", Ticket.tickets_open)
        print()

    @staticmethod
    def print_all_tickets():
        for ticket in Ticket.ticket_list:
            ticket.print_ticket()
