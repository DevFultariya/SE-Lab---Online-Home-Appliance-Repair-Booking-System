from enum import Enum

class BookingState(Enum):
    PENDING_PAYMENT = 1
    PAYMENT_FAILED_STATE = 2
    PAID_PENDING_APPROVAL = 3
    BOOKING_CONFIRMED = 4
    TECHNICIAN_ASSIGNED = 5
    TECHNICIAN_EN_ROUTE = 6
    SERVICE_IN_PROGRESS = 7
    SERVICE_COMPLETED = 8
    BOOKING_REJECTED = 9
    CANCELLED = 10

class Booking:
    def __init__(self, booking_id, customer, appliance, issue, charge, address):
        self.booking_id = booking_id
        self.customer = customer
        self.appliance = appliance
        self.issue = issue
        self.charge = charge
        self.address = address
        self.current_state = BookingState.PENDING_PAYMENT
        print(f"Booking created successfully. Status: {self.current_state.name}")

    def pay(self, success):
        if self.current_state in [BookingState.PENDING_PAYMENT, BookingState.PAYMENT_FAILED_STATE]:
            if success:
                self.current_state = BookingState.PAID_PENDING_APPROVAL
                print(f"Payment successful. Status: {self.current_state.name}")
            else:
                self.current_state = BookingState.PAYMENT_FAILED_STATE
                print(f"Payment failed. Status: {self.current_state.name}")
        else:
            self._invalid_transition("PAY")

    def accept_booking(self):
        if self.current_state == BookingState.PAID_PENDING_APPROVAL:
            self.current_state = BookingState.BOOKING_CONFIRMED
            print(f"Booking accepted by service center. Status: {self.current_state.name}")
        else:
            self._invalid_transition("ACCEPT_BOOKING")

    def reject_booking(self):
        if self.current_state == BookingState.PAID_PENDING_APPROVAL:
            self.current_state = BookingState.BOOKING_REJECTED
            print(f"Booking rejected by service center. Status: {self.current_state.name}. 100% Full Refund issued.")
        else:
            self._invalid_transition("REJECT_BOOKING")

    def assign_technician(self):
        if self.current_state == BookingState.BOOKING_CONFIRMED:
            self.current_state = BookingState.TECHNICIAN_ASSIGNED
            print(f"Technician assigned. Status: {self.current_state.name}")
        else:
            self._invalid_transition("ASSIGN_TECHNICIAN")

    def dispatch_technician(self):
        if self.current_state == BookingState.TECHNICIAN_ASSIGNED:
            self.current_state = BookingState.TECHNICIAN_EN_ROUTE
            print(f"Technician dispatched. Status: {self.current_state.name}")
        else:
            self._invalid_transition("DISPATCH_TECHNICIAN")

    def start_service(self):
        if self.current_state == BookingState.TECHNICIAN_EN_ROUTE:
            self.current_state = BookingState.SERVICE_IN_PROGRESS
            print(f"Service started. Status: {self.current_state.name}")
        else:
            self._invalid_transition("START_SERVICE")

    def complete_service(self):
        if self.current_state == BookingState.SERVICE_IN_PROGRESS:
            self.current_state = BookingState.SERVICE_COMPLETED
            print(f"Service completed. Status: {self.current_state.name}")
        else:
            self._invalid_transition("COMPLETE_SERVICE")

    def cancel(self):
        if self.current_state in [BookingState.SERVICE_IN_PROGRESS, BookingState.SERVICE_COMPLETED]:
            print(f"Invalid Transition! Cannot cancel an ongoing or completed service. Status remains: {self.current_state.name}")
            return

        if self.current_state in [BookingState.BOOKING_REJECTED, BookingState.CANCELLED]:
            print(f"Booking is already terminated. Status remains: {self.current_state.name}")
            return

        print("Booking cancelled. ", end="")
        if self.current_state in [BookingState.PENDING_PAYMENT, BookingState.PAYMENT_FAILED_STATE]:
            print("No refund necessary.")
        elif self.current_state in [BookingState.PAID_PENDING_APPROVAL, BookingState.BOOKING_CONFIRMED]:
            print("100% Full Refund issued.")
        elif self.current_state in [BookingState.TECHNICIAN_ASSIGNED, BookingState.TECHNICIAN_EN_ROUTE]:
            print("50% Partial Refund issued.")

        self.current_state = BookingState.CANCELLED
        print(f"New Status: {self.current_state.name}")

    def _invalid_transition(self, event):
        print(f"Invalid Transition! Event '{event}' is not allowed in current state: {self.current_state.name}")
