from booking import Booking, BookingState

def run_test_cases():
    print("\n--- RUNNING REQUIRED TEST CASES ---")
    
    print("\n[TC01] Successful booking flow")
    t1 = Booking("T01", "User", "AC", "Issue", 100, "Addr")
    t1.pay(True)
    t1.accept_booking()
    t1.assign_technician()
    t1.dispatch_technician()
    t1.start_service()
    t1.complete_service()
    print(f"Expected: SERVICE_COMPLETED. Actual: {t1.current_state.name}")
    print("RESULT: PASS" if t1.current_state == BookingState.SERVICE_COMPLETED else "RESULT: FAIL")

    print("\n[TC02] Payment failure + retry")
    t2 = Booking("T02", "User", "AC", "Issue", 100, "Addr")
    t2.pay(False)
    print(f"  After failure -> Expected: PAYMENT_FAILED_STATE. Actual: {t2.current_state.name}")
    print("  " + ("PASS" if t2.current_state == BookingState.PAYMENT_FAILED_STATE else "FAIL"))
    # Now retry payment successfully (customer retry path)
    t2.pay(True)
    print(f"  After retry   -> Expected: PAID_PENDING_APPROVAL. Actual: {t2.current_state.name}")
    print("RESULT: " + ("PASS" if t2.current_state == BookingState.PAID_PENDING_APPROVAL else "FAIL"))

    print("\n[TC03] Service center rejection")
    t3 = Booking("T03", "User", "AC", "Issue", 100, "Addr")
    t3.pay(True)
    t3.reject_booking()
    print(f"Expected: BOOKING_REJECTED. Actual: {t3.current_state.name}")
    print("RESULT: PASS" if t3.current_state == BookingState.BOOKING_REJECTED else "RESULT: FAIL")

    print("\n[TC04] Invalid transition")
    t4 = Booking("T04", "User", "AC", "Issue", 100, "Addr")
    t4.start_service() # Invalid
    print(f"Expected: PENDING_PAYMENT. Actual: {t4.current_state.name}")
    print("RESULT: PASS" if t4.current_state == BookingState.PENDING_PAYMENT else "RESULT: FAIL")

    print("\n[TC05] Cancellation before technician assignment")
    t5 = Booking("T05", "User", "AC", "Issue", 100, "Addr")
    t5.pay(True)
    t5.accept_booking()
    t5.cancel() # 100% refund
    print(f"Expected: CANCELLED. Actual: {t5.current_state.name}")
    print("RESULT: PASS" if t5.current_state == BookingState.CANCELLED else "RESULT: FAIL")

    print("\n[TC06] Cancellation after service start (Invalid)")
    t6 = Booking("T06", "User", "AC", "Issue", 100, "Addr")
    t6.pay(True)
    t6.accept_booking()
    t6.assign_technician()
    t6.dispatch_technician()
    t6.start_service()
    t6.cancel() # should fail
    print(f"Expected: SERVICE_IN_PROGRESS. Actual: {t6.current_state.name}")
    print("RESULT: PASS" if t6.current_state == BookingState.SERVICE_IN_PROGRESS else "RESULT: FAIL")

    print("\n[TC07] Boundary Condition: Cancellation when Technician En-Route")
    t7 = Booking("T07", "User", "AC", "Issue", 100, "Addr")
    t7.pay(True)
    t7.accept_booking()
    t7.assign_technician()
    t7.dispatch_technician()
    t7.cancel() # Should allow with 50% refund
    print(f"Expected: CANCELLED. Actual: {t7.current_state.name}")
    print("RESULT: PASS" if t7.current_state == BookingState.CANCELLED else "RESULT: FAIL")
    print("EXPLANATION: This is a boundary condition because it is the very last state where cancellation is still allowed. Once the state moves to SERVICE_IN_PROGRESS, cancellation is fully rejected. The result is correct because it successfully processed the cancellation and applied the 50% penalty as defined in our policy design.")
    
    print("\n--- TEST CASES COMPLETED ---")

def main():
    booking = None
    while True:
        print("\n--- Repair Booking System ---")
        print("1.  Create / View Booking")
        print("2.  Show Current Status")
        print("3.  Pay Booking")
        print("4.  Accept Booking (Center)")
        print("5.  Reject Booking (Center)")
        print("6.  Assign Technician")
        print("7.  Dispatch Technician")
        print("8.  Start Service")
        print("9.  Complete Service")
        print("10. Cancel Booking")
        print("11. Run Required Test Cases")
        print("12. Exit")
        
        try:
            choice = input("Select an option: ").strip()
        except EOFError:
            break

        if choice == '1':
            if booking is not None:
                print(f"Booking already exists! Status: {booking.current_state.name}")
                ans = input("Overwrite with new booking? (y/n): ")
                if ans.lower() != 'y':
                    continue
            booking = Booking("B001", "John Doe", "Washing Machine", "Does not spin", 150.0, "123 Main St")
        elif choice == '2':
            if booking:
                print(f"Current Status: {booking.current_state.name}")
            else:
                print("No booking exists.")
        elif choice == '3':
            if booking:
                ans = input("Simulate success? (y/n): ")
                booking.pay(ans.lower() == 'y')
            else:
                print("No booking exists.")
        elif choice == '4':
            if booking: booking.accept_booking()
            else: print("No booking exists.")
        elif choice == '5':
            if booking: booking.reject_booking()
            else: print("No booking exists.")
        elif choice == '6':
            if booking: booking.assign_technician()
            else: print("No booking exists.")
        elif choice == '7':
            if booking: booking.dispatch_technician()
            else: print("No booking exists.")
        elif choice == '8':
            if booking: booking.start_service()
            else: print("No booking exists.")
        elif choice == '9':
            if booking: booking.complete_service()
            else: print("No booking exists.")
        elif choice == '10':
            if booking: booking.cancel()
            else: print("No booking exists.")
        elif choice == '11':
            run_test_cases()
        elif choice == '12':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
