"""
Parking Lot Management System - Main Demo
==========================================
A complete Low-Level Design (LLD) implementation of a parking lot system
with multiple floors, different vehicle types, and smart slot assignment.

Features:
- Multiple floors support
- Multiple vehicle types (Motorcycle, Car, Truck)
- Automatic slot assignment strategies
- Ticket and payment management
- Real-time availability tracking
"""

from models.models import (
    ParkingLot, Floor, ParkingSlot, Vehicle, ParkingTicket, Payment,
    VehicleType, PaymentMethod, NearestSlotStrategy, OptimizedSlotStrategy
)

def setup_parking_lot():
    """Initialize and setup a complete parking lot with floors and slots"""
    
    # Create parking lot with strategy
    parking_lot = ParkingLot(
        name="Sky High Parking",
        address="123 Main Street, Tech City",
        slot_assignment_strategy=NearestSlotStrategy()
    )
    
    # Add 3 floors
    for floor_num in range(1, 4):
        floor = Floor(floor_number=floor_num, parking_lot=parking_lot)
        
        # Add motorcycle slots (2 per floor)
        for slot_num in range(1, 3):
            slot = ParkingSlot(
                slot_number=slot_num,
                vehicle_type=VehicleType.MOTORCYCLE,
                floor=floor
            )
            floor.add_parking_slot(slot)
        
        # Add car slots (4 per floor)
        for slot_num in range(3, 7):
            slot = ParkingSlot(
                slot_number=slot_num,
                vehicle_type=VehicleType.CAR,
                floor=floor
            )
            floor.add_parking_slot(slot)
        
        # Add truck slots (2 per floor)
        for slot_num in range(7, 9):
            slot = ParkingSlot(
                slot_number=slot_num,
                vehicle_type=VehicleType.TRUCK,
                floor=floor
            )
            floor.add_parking_slot(slot)
        
        parking_lot.add_floor(floor)
    
    return parking_lot

def demo_basic_operations(parking_lot):
    """Demonstrate basic parking lot operations"""
    print("\n" + "="*60)
    print("DEMO 1: Basic Parking Operations")
    print("="*60)
    
    # Create vehicles
    vehicles = [
        Vehicle("DL01AB1234", VehicleType.CAR),
        Vehicle("DL02CD5678", VehicleType.MOTORCYCLE),
        Vehicle("DL03EF9012", VehicleType.CAR),
        Vehicle("DL04GH3456", VehicleType.TRUCK),
        Vehicle("DL05IJ7890", VehicleType.MOTORCYCLE),
        Vehicle("DL06KL2345", VehicleType.CAR),
    ]
    
    # Park vehicles
    print("\n--- Parking Vehicles ---")
    tickets = []
    for vehicle in vehicles:
        ticket = parking_lot.park_vehicle(vehicle, floor_number=1)
        if ticket:
            tickets.append(ticket)
    
    # Display lot status
    parking_lot.display_lot_status()
    
    return tickets

def demo_unpark_vehicles(parking_lot, tickets):
    """Demonstrate unparking and fee collection"""
    print("\n" + "="*60)
    print("DEMO 2: Unparking Vehicles & Fee Collection")
    print("="*60)
    
    if not tickets:
        print("No tickets to process")
        return
    
    print("\n--- Unparking Vehicles ---")
    
    # Unpark first 3 vehicles
    for i, ticket in enumerate(tickets[:3]):
        vehicle_reg = ticket.vehicle.registration_number
        
        # Simulate time passage (in real system)
        fee = parking_lot.unpark_vehicle(vehicle_reg)
        
        if fee:
            # Process payment
            payment = Payment(amount=fee, method=PaymentMethod.CREDIT_CARD)
            payment.process_payment()
            print(f"  Payment processed: {payment}")
    
    # Display updated lot status
    parking_lot.display_lot_status()

def demo_slot_availability(parking_lot):
    """Demonstrate slot availability checking"""
    print("\n" + "="*60)
    print("DEMO 3: Slot Availability Tracking")
    print("="*60)
    
    print("\n--- Available Slots by Type ---")
    print(f"Motorcycles: {parking_lot.get_available_slots_count(VehicleType.MOTORCYCLE)} slots")
    print(f"Cars: {parking_lot.get_available_slots_count(VehicleType.CAR)} slots")
    print(f"Trucks: {parking_lot.get_available_slots_count(VehicleType.TRUCK)} slots")

def demo_strategy_switching(parking_lot):
    """Demonstrate changing slot assignment strategy"""
    print("\n" + "="*60)
    print("DEMO 4: Slot Assignment Strategy Switching")
    print("="*60)
    
    # Switch to optimized strategy
    parking_lot.slot_assignment_strategy = OptimizedSlotStrategy()
    print("\n✓ Switched to Optimized Strategy (prefers slots away from entrance)")
    
    # Park new vehicles with new strategy
    print("\n--- Parking with Optimized Strategy ---")
    new_vehicles = [
        Vehicle("DL07MN5678", VehicleType.CAR),
        Vehicle("DL08OP9012", VehicleType.MOTORCYCLE),
    ]
    
    for vehicle in new_vehicles:
        ticket = parking_lot.park_vehicle(vehicle, floor_number=2)
        if ticket:
            print(f"  {ticket.vehicle.registration_number} assigned to {ticket.parking_slot}")

def demo_statistics(parking_lot):
    """Display parking lot statistics"""
    print("\n" + "="*60)
    print("DEMO 5: Parking Lot Statistics")
    print("="*60)
    
    total_slots = sum(
        len(floor.parking_slots) for floor in parking_lot.floors.values()
    )
    
    print(f"\n--- Lot Statistics ---")
    print(f"Total Floors: {len(parking_lot.floors)}")
    print(f"Total Parking Slots: {total_slots}")
    print(f"  - Motorcycle Slots: {sum(1 for floor in parking_lot.floors.values() for slot in floor.parking_slots.values() if slot.vehicle_type == VehicleType.MOTORCYCLE)}")
    print(f"  - Car Slots: {sum(1 for floor in parking_lot.floors.values() for slot in floor.parking_slots.values() if slot.vehicle_type == VehicleType.CAR)}")
    print(f"  - Truck Slots: {sum(1 for floor in parking_lot.floors.values() for slot in floor.parking_slots.values() if slot.vehicle_type == VehicleType.TRUCK)}")
    
    print(f"\nCurrently Parked Vehicles: {len(parking_lot.parked_vehicles)}")
    print(f"Active Tickets: {len(parking_lot.active_tickets)}")
    print(f"Completed Transactions: {len(parking_lot.completed_tickets)}")
    
    if parking_lot.completed_tickets:
        total_vehicles = len(parking_lot.completed_tickets)
        print(f"Total Parking Duration Tracked: {total_vehicles} vehicles")

def main():
    """Main execution"""
    print("\n" + "="*60)
    print("PARKING LOT MANAGEMENT SYSTEM - COMPLETE DEMO")
    print("="*60)
    
    # Setup parking lot
    parking_lot = setup_parking_lot()
    print(f"\n✓ Parking lot initialized: {parking_lot}")
    print(f"✓ Address: {parking_lot.address}")
    print(f"✓ Floors: {len(parking_lot.floors)}")
    
    # Run all demos
    tickets = demo_basic_operations(parking_lot)
    demo_slot_availability(parking_lot)
    demo_unpark_vehicles(parking_lot, tickets)
    demo_strategy_switching(parking_lot)
    demo_statistics(parking_lot)
    
    # Final status
    print("\n" + "="*60)
    print("FINAL PARKING LOT STATUS")
    print("="*60)
    parking_lot.display_lot_status()
    
    print("\n" + "="*60)
    print("✓ DEMO COMPLETED SUCCESSFULLY")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
