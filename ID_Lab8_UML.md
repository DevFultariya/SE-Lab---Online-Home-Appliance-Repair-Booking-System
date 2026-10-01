# Lab Assignment 8 - UML State Diagram

Below is the UML State Machine diagram for the appliance repair booking system. It follows standard UML notation where transitions are labeled as `Event [Guard] / Action`.

```mermaid
stateDiagram-v2
    direction TB
    
    %% Initial State
    [*] --> PENDING_PAYMENT : BOOK_SERVICE [Valid Data] / Save Booking

    %% Legend / Notation Note
    note right of PENDING_PAYMENT
        === UML NOTATION LEGEND ===
        [*] : Initial or Terminal State
        Solid Arrow : Valid State Transition
        Format : Event [Guard Condition] / Action
    end note

    %% Pending Payment Transitions
    PENDING_PAYMENT --> PAID_PENDING_APPROVAL : PAY [Success] / Log Payment
    PENDING_PAYMENT --> PAYMENT_FAILED_STATE : PAYMENT_FAILED [Failure] / Notify Retry
    PENDING_PAYMENT --> CANCELLED : CANCEL [User Request] / No Refund

    %% Payment Failed Transitions
    PAYMENT_FAILED_STATE --> PAID_PENDING_APPROVAL : PAY [Success] / Log Payment
    PAYMENT_FAILED_STATE --> CANCELLED : CANCEL [User Request] / No Refund

    %% Paid Pending Approval Transitions
    PAID_PENDING_APPROVAL --> BOOKING_CONFIRMED : ACCEPT_BOOKING / Notify Customer
    PAID_PENDING_APPROVAL --> BOOKING_REJECTED : REJECT_BOOKING / Issue 100% Refund
    PAID_PENDING_APPROVAL --> CANCELLED : CANCEL [User Request] / Issue 100% Refund

    %% Booking Confirmed Transitions
    BOOKING_CONFIRMED --> TECHNICIAN_ASSIGNED : ASSIGN_TECHNICIAN / Save Tech Details
    BOOKING_CONFIRMED --> CANCELLED : CANCEL [User Request] / Issue 100% Refund

    %% Technician Assigned Transitions
    TECHNICIAN_ASSIGNED --> TECHNICIAN_EN_ROUTE : DISPATCH_TECHNICIAN / Notify ETA
    TECHNICIAN_ASSIGNED --> CANCELLED : CANCEL [User Request] / Issue 50% Refund

    %% Technician En Route Transitions
    TECHNICIAN_EN_ROUTE --> SERVICE_IN_PROGRESS : START_SERVICE / Log Start Time
    TECHNICIAN_EN_ROUTE --> CANCELLED : CANCEL [User Request] / Issue 50% Refund

    %% Service In Progress Transitions
    SERVICE_IN_PROGRESS --> SERVICE_COMPLETED : COMPLETE_SERVICE / Generate Receipt
    
    %% Note on Invalid Transitions
    note right of SERVICE_IN_PROGRESS
        CANCEL event is guarded
        against in this state
        and is rejected.
    end note
    
    note right of SERVICE_COMPLETED
        CANCEL event is guarded
        against in this state
        and is rejected.
    end note

    %% Terminal States
    BOOKING_REJECTED --> [*]
    CANCELLED --> [*]
    SERVICE_COMPLETED --> [*]
```
