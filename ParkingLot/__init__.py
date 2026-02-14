"""
Parking Lot Management System
=============================
A complete low-level design (LLD) implementation of a parking lot management system.

This system demonstrates:
- Creational patterns (Factory, Strategy pattern for slot assignment)
- Structural organization with clear separation of concerns
- Behavioral patterns (Observer-like notification system using tickets)

Main components:
- ParkingLot: Main system orchestrator
- Floor: Represents each floor of the parking structure
- ParkingSlot: Individual parking spaces
- Vehicle: Vehicles to be parked
- ParkingTicket: Entry/exit ticket management
- Payment: Payment processing
- SlotAssignmentStrategy: Pluggable strategies for slot allocation
"""

from models import (
    ParkingLot,
    Floor,
    ParkingSlot,
    Vehicle,
    ParkingTicket,
    Payment,
    VehicleType,
    ParkingSlotStatus,
    ParkingLotStatus,
    SlotAssignmentStrategy,
    NearestSlotStrategy,
    OptimizedSlotStrategy,
)

__version__ = "1.0.0"
__author__ = "Design Patterns - LLD Games"

__all__ = [
    'ParkingLot',
    'Floor',
    'ParkingSlot',
    'Vehicle',
    'ParkingTicket',
    'Payment',
    'VehicleType',
    'ParkingSlotStatus',
    'ParkingLotStatus',
    'SlotAssignmentStrategy',
    'NearestSlotStrategy',
    'OptimizedSlotStrategy',
]
