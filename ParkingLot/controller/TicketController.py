from dtos import IssueTokenRequest
from dtos import TicketResponse

form service.TicketService import TicketService

class TicketController:
    def __init__(self, ticket_service: TicketService):
        self.ticket_service = ticket_service

    def issue_ticket(self, request: IssueTokenRequest) -> TicketResponse:
        ticket = self.ticket_service.issue_ticket(request.vehicle_number, request.owner_name, request.gate_id, request.vehicle_type)
        





        return self.ticket_service.create_ticket(vehicle)

    # def close_ticket(self, ticket_id):
    #     return self.ticket_service.close_ticket(ticket_id)

    # def get_ticket_info(self, ticket_id):
    #     return self.ticket_service.get_ticket_info(ticket_id)