
import datetime

from models.models import Ticket, Vehicle, SlotStatus

from strgy import *

from strgy.getSlotFactory import SlotFactory


class TicketService:
    def __init__(self, GateRepo, VehicleRepo, slotRepo,
                 parkingLotRepo, ticketRepo):
        self.gateRepo = GateRepo
        self.vehicleRepo = VehicleRepo
        self.slotRepo = slotRepo
        self.parkingLotRepo = parkingLotRepo
        self.ticketRepo = ticketRepo

    def issueTicket(self, vehicle_number, owner_name, gate_id, vehicleType) -> Ticket:
        # create a ticket..
        ticket = Ticket(id=-1, number="", entry_time=datetime.datetime.now(), vehicle=None, parking_slot=None,
                        generated_gate=None)
        #  set info.. like gate no...
        gate = self.gateRepo.find_gate_by_id(gate_id)
        if gate == None:
            raise Exception("Gate not found")
        ticket.generated_gate = gate

        # Vehicle info..
        vehicle = self.vehicleRepo.find_vehicle_by_number(vehicle_number)
        if vehicle is None:
            vehicle = Vehicle(id=vehicle_number, owner_name=owner_name, vehicle_type=vehicleType)
            vehicle = self.vehicleRepo.save_vehicle(vehicle)
        ticket.vehicle = vehicle

        # find a slot..
        slotStgy = SlotFactory.get_slot_stgy_obj(gate.parking_lot.slot_assignment_strategy)

        if not slotStgy:
            raise Exception("Slot stgy not found")

        slot = slotStgy.get_slot(vehicle.vehicle_type, gate)
        if not slot:
            raise Exception("Slot not found")

        ticket.parking_slot = slot

        #  update slot..
        self.slotRepo.update_slot_status(slot, SlotStatus.FILLED)

        # update parking counters..
        self.parkingLotRepo.update_parking_lot_count(gate.parking_lot)

        # return ticket..
        return self.ticketRepo.save_ticket(ticket)
