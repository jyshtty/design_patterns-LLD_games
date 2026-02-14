from datetime import datetime
from enum import Enum
from typing import List


# ============================================================
# Base Model
# ============================================================

class BaseModel:
    def __init__(self, id: int):
        self.id = id
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


# ============================================================
# Enums — Parking Infra
# ============================================================

class ParkingLotStatus(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    FULL = "FULL"
    UNDER_MAINTENANCE = "UNDER_MAINTENANCE"


class FloorStatus(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    FULL = "FULL"
    UNDER_MAINTENANCE = "UNDER_MAINTENANCE"


class GateStatus(Enum):
    OPEN = "OPEN"
    CLOSED = "CLOSED"
    UNDER_MAINTENANCE = "UNDER_MAINTENANCE"


class GateType(Enum):
    ENTRY = "ENTRY"
    EXIT = "EXIT"


# ============================================================
# Enums — Slot / Vehicle
# ============================================================

class VehicleType(Enum):
    CAR = "CAR"
    BIKE = "BIKE"
    BUS = "BUS"
    TRUCK = "TRUCK"


class SlotStatus(Enum):
    EMPTY = "EMPTY"
    FILLED = "FILLED"
    RESERVED = "RESERVED"
    BLOCKED = "BLOCKED"


# ============================================================
# Enums — Billing / Payment
# ============================================================

class BillStatus(Enum):
    PAID = "PAID"
    PENDING = "PENDING"
    PARTIALLY_PAID = "PARTIALLY_PAID"


class PaymentStatus(Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class PaymentMode(Enum):
    CASH = "CASH"
    ONLINE = "ONLINE"
    CARD = "CARD"
    UPI = "UPI"


# ============================================================
# Strategy Enum (can be converted to interface later)
# ============================================================

class SlotAssignmentStrategy(Enum):
    RANDOM = "RANDOM"


# ============================================================
# Core Infrastructure Models
# ============================================================

class ParkingLot(BaseModel):
    def __init__(
        self,
        id: int,
        name: str,
        address: str,
        floors: List["Floor"],
        gates: List["Gate"],
        allowed_vehicles: List[VehicleType],
        capacity: int,
        status: ParkingLotStatus,
        slot_assignment_strategy: SlotAssignmentStrategy,
    ):
        super().__init__(id)
        self.name = name
        self.address = address
        self.floors = floors
        self.gates = gates
        self.allowed_vehicles = allowed_vehicles
        self.capacity = capacity
        self.status = status
        self.slot_assignment_strategy = slot_assignment_strategy


class Floor(BaseModel):
    def __init__(
        self,
        id: int,
        floor_number: int,
        slots: List["Slot"],
        status: FloorStatus,
        allowed_vehicles: List[VehicleType],
    ):
        super().__init__(id)
        self.floor_number = floor_number
        self.slots = slots
        self.status = status
        self.allowed_vehicles = allowed_vehicles


class Slot(BaseModel):
    def __init__(
        self,
        id: int,
        slot_number: int,
        vehicle_type: VehicleType,
        status: SlotStatus,
        floor: "Floor",
    ):
        super().__init__(id)
        self.slot_number = slot_number
        self.vehicle_type = vehicle_type
        self.status = status
        self.floor = floor


class Gate(BaseModel):
    def __init__(
        self,
        id: int,
        gate_number: int,
        gate_type: GateType,
        parking_lot: ParkingLot,
        status: GateStatus,
    ):
        super().__init__(id)
        self.gate_number = gate_number
        self.gate_type = gate_type
        self.parking_lot = parking_lot
        self.status = status


# ============================================================
# Vehicle & Ticket Models
# ============================================================

class Vehicle(BaseModel):
    def __init__(
        self,
        id: int,
        owner_name: str,
        vehicle_type: VehicleType,
    ):
        super().__init__(id)
        self.owner_name = owner_name
        self.vehicle_type = vehicle_type


class Ticket(BaseModel):
    def __init__(
        self,
        id: int,
        number: str,
        entry_time: datetime,
        vehicle: Vehicle,
        slot: Slot,
        generated_gate: Gate,
    ):
        super().__init__(id)
        self.number = number
        self.entry_time = entry_time
        self.vehicle = vehicle
        self.slot = slot
        self.generated_gate = generated_gate


# ============================================================
# Billing & Payment Models
# ============================================================

class Bill(BaseModel):
    def __init__(
        self,
        id: int,
        exit_time: datetime,
        ticket: Ticket,
        total_amount: int,
        status: BillStatus,
        payments: List["Payment"],
    ):
        super().__init__(id)
        self.exit_time = exit_time
        self.ticket = ticket
        self.total_amount = total_amount
        self.status = status
        self.payments = payments


class Payment(BaseModel):
    def __init__(
        self,
        id: int,
        amount: int,
        mode: PaymentMode,
        ref_id: str,
        bill: Bill,
        status: PaymentStatus,
        paid_at: datetime,
    ):
        super().__init__(id)
        self.amount = amount
        self.mode = mode
        self.ref_id = ref_id
        self.bill = bill
        self.status = status
        self.paid_at = paid_at
