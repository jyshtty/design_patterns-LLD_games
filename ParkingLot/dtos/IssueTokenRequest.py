class IssueTokenRequest:
    def __init__(self, vehicle_number, owner_name, gate_id, vehicle_type):
        self.vehicle_number = vehicle_number
        self.owner_name = owner_name
        self.gate_id = gate_id
        self.vehicle_type = vehicle_type    