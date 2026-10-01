# Online Home Appliance Booking System

This project is a command-line Python application that simulates an Online Home Appliance Repair Booking System using a state machine. It manages the lifecycle of an appliance repair booking from creation to service completion, including various edge cases such as payment failures, service rejections, and cancellations.

## Features
- **State Machine Architecture**: Robust state management using Enum (`BookingState`), preventing invalid transitions.
- **Complete Booking Lifecycle**: Simulates creation, payment, center approval, technician assignment, dispatch, service progress, and completion.
- **Smart Cancellation Policy**: Handles partial (50%) and full (100%) refunds depending on the current state of the booking.
- **Interactive CLI**: Easy-to-use menu to step through the state transitions manually.
- **Automated Test Cases**: Includes built-in test scenarios (TC01 to TC07) validating normal flows, error states (e.g., payment failures), and boundary conditions (cancellation when technician is en-route).

## Project Structure
- `src/booking.py`: Contains the `Booking` state machine logic and `BookingState` enumerations.
- `src/main.py`: Interactive CLI application and automated test suite runner.
- `ID_Lab8_RunInstructions.txt`, `ID_Lab8_UML.md`: Documentation and instructions.
- `Requirment Analysis & Design.pdf`, `UML State Diagram.pdf`: System design and UML documentation.
- `Test Case Result.png`: Execution output of the test cases.

## How to Run

1. Make sure you have Python installed.
2. Navigate to the `src` folder (or run from the root directory).
3. Execute the `main.py` file:

```bash
python src/main.py
```

4. You will be presented with a menu. Select `11` to run all automated test cases, or use options `1` through `10` to manually simulate a booking flow.
