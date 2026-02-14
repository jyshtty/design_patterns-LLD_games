# Parking Lot System — LLD Workflow Mapping (Q&A)

This document maps a **generic Low-Level Design (LLD) workflow** to the implementation in the repository:

**Repo:** https://github.com/kbhatia01/parkingLot-Py

It is structured in **Q&A format** for interview prep and revision.

---

# 1️⃣ What is the overall architecture of the repository?

The repository follows a layered LLD architecture:

```
application.py          → Runner / Main
models/                 → Domain entities
controllers/            → Entry points / APIs
dtos/                   → Request & Response objects
services/               → Business logic
daos/                   → Repositories / Persistence
strategies/             → Strategy pattern implementations
adapters/               → External payment integrations
exceptions/             → Custom errors
```

This separation ensures:

- Clean responsibility boundaries
- Testability
- Extensibility
- Interview-friendly design

---

# 2️⃣ Where are the domain models implemented?

📂 `models/`

This folder contains all core entities derived from the class diagram.

### Examples

- ParkingLot
- ParkingFloor
- ParkingSpot
- Gate
- Ticket
- Bill
- Payment
- Vehicle
- Operator

### Responsibilities

- Represent business objects
- Hold attributes & relationships
- No business logic

---

# 3️⃣ Where are controllers implemented?

📂 `controllers/`

Controllers act as **entry points** for use cases.

### Examples

- GenerateTicketController
- GenerateBillController
- MakePaymentController

### Responsibilities

- Accept requests
- Call services
- Return responses
- No business logic

---

# 4️⃣ Where are DTOs defined?

📂 `dtos/`

Each controller has corresponding Request & Response DTOs.

### Examples

**Ticket**
- GenerateTicketRequestDto
- GenerateTicketResponseDto

**Bill**
- GenerateBillRequestDto
- GenerateBillResponseDto

**Payment**
- MakePaymentRequestDto
- MakePaymentResponseDto

### Purpose

- Isolate API contracts
- Avoid exposing domain models
- Enable validation

---

# 5️⃣ How does controller handle requests?

Controller receives a request DTO:

```python
def generate_ticket(self, request_dto):
```

It extracts:

- Vehicle number
- Vehicle type
- Gate ID

Then delegates to service.

---

# 6️⃣ How is the service layer structured?

📂 `services/`

### Examples

- TicketService
- BillService
- PaymentService

### Responsibilities

- Business logic
- Validations
- Entity creation
- State transitions

---

# 7️⃣ What service methods exist?

Typical methods:

```python
generate_ticket()
generate_bill()
make_payment()
```

Each represents a business use case.

---

# 8️⃣ Is design planned before coding?

Yes — flow is logically sequenced (even if comments aren’t verbose).

Example design thinking for ticket generation:

1. Validate gate
2. Fetch parking lot
3. Find available slot
4. Assign vehicle
5. Create ticket
6. Persist ticket

This reflects pre-coding planning.

---

# 9️⃣ How is logic implemented in services?

Services perform:

- Strategy invocation
- Object creation
- State updates

Example:

```python
spot = strategy.assign_spot(vehicle_type)
spot.park_vehicle(vehicle)
ticket = Ticket(...)
```

---

# 🔟 How are repositories identified?

While writing service logic, required repositories emerge.

### Examples

- GateDao
- ParkingLotDao
- SpotDao
- TicketDao

These dependencies are injected into services.

---

# 1️⃣1️⃣ Where are repositories implemented?

📂 `daos/`

DAO = Data Access Object (Repository layer)

### Examples

- GateDao
- ParkingLotDao
- ParkingSpotDao
- TicketDao
- BillDao
- PaymentDao

### Responsibilities

- Store entities
- Retrieve entities
- Update states

Persistence is typically in-memory.

---

# 1️⃣2️⃣ How is data persisted?

Inside services:

```python
ticket_dao.save(ticket)
spot_dao.update(spot)
bill_dao.save(bill)
```

Operations include:

- Save new entities
- Update slot status
- Link relationships

---

# 1️⃣3️⃣ How does service return results?

Service returns domain objects:

```python
return ticket
return bill
return payment
```

---

# 1️⃣4️⃣ How is response DTO prepared?

Controller maps domain → response DTO:

```python
response_dto = GenerateTicketResponseDto(
    ticket_id=ticket.id,
    slot_number=ticket.spot.number
)
```

---

# 1️⃣5️⃣ What is the complete request flow?

```
Client Request
     ↓
Controller
     ↓
Request DTO
     ↓
Service Layer
     ↓
Repositories (DAOs)
     ↓
Persistence Store
     ↓
Service Result
     ↓
Response DTO
     ↓
Controller Response
```

---

# 1️⃣6️⃣ How does Ticket Generation flow work?

### Step-by-step

1. Controller receives request
2. DTO created
3. Service invoked
4. Gate validated
5. Parking lot fetched
6. Slot assignment strategy executed
7. Spot allocated
8. Ticket created
9. Ticket persisted
10. Response DTO returned

---

# 1️⃣7️⃣ What design patterns are used?

## Strategy Pattern

📂 `strategies/`

Used for:

- Spot assignment
- Fee calculation

Examples:

- RandomSpotAssignmentStrategy
- NearestSpotAssignmentStrategy

---

## Adapter Pattern

📂 `adapters/`

Used for payment gateways:

- RazorPay adapter
- PayU adapter

Allows plug-and-play integrations.

---

# 1️⃣8️⃣ How are exceptions handled?

📂 `exceptions/`

Examples:

- SpotNotAvailableException
- GateClosedException
- PaymentFailedException

Used for domain-specific error handling.

---

# 1️⃣9️⃣ Mapping Generic LLD Workflow → Repo

| Generic Step | Repo Mapping |
|-------------|--------------|
| Models | `models/` |
| Controllers | `controllers/` |
| DTOs | `dtos/` |
| Request handling | Controllers |
| Service delegation | Controller → Service |
| Business logic | `services/` |
| Service methods | Inside services |
| Repo identification | During service coding |
| Repositories | `daos/` |
| Persistence | DAO save/update |
| Return values | Service return |
| Response DTO | Controller mapping |

---

# 2️⃣0️⃣ How to narrate this in interviews?

You can say:

> “After finalizing the class diagram, I structured the system into layered architecture — models, controllers, DTOs, services, repositories, strategies, and adapters. Controllers handle requests, DTOs encapsulate contracts, services implement business logic, repositories manage persistence, and strategies allow pluggable algorithms like slot assignment and fee calculation.”

---

# ✅ Summary

This repository is a textbook example of:

- Clean LLD layering
- SOLID principles
- Strategy pattern usage
- Adapter integrations
- DTO separation
- Repository abstraction

