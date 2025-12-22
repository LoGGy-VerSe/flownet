# FlowNet - Winnings Mode Activation System

A Python-based system that tracks winnings and automatically activates a special mode when total winnings exceed 1000 for today's date.

## Features

- **Winnings Tracking**: Track winnings amounts for different dates
- **Automatic Mode Activation**: Mode automatically activates when daily winnings exceed 1000
- **Date-based Operations**: All operations are date-aware and default to today's date
- **Flexible Threshold**: Configurable threshold value (default: 1000)

## Installation

No external dependencies required. Uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/LoGGy-VerSe/flownet.git
cd flownet

# Run the main script
python flownet.py

# Run the example script to see different scenarios
python example.py
```

## Usage

### Basic Usage

```python
from flownet import WinningsTracker

# Create a tracker with default threshold (1000)
tracker = WinningsTracker()

# Add winnings for today
tracker.add_winning(500)
tracker.add_winning(300)
tracker.add_winning(250)  # Total: 1050

# Check and activate mode
status = tracker.activate_mode()
print(status)  # "Mode ACTIVATED! Total winnings for 2025-12-22: 1050.00 (threshold: 1000)"

# Check if mode is active
if tracker.is_mode_active():
    print("Special mode is now active!")
```

### Custom Threshold

```python
# Create a tracker with custom threshold
tracker = WinningsTracker(threshold=500)

tracker.add_winning(600)
if tracker.check_and_activate_mode():
    print("Mode activated with 600 winnings!")
```

### Date-specific Operations

```python
# Add winnings for a specific date
tracker.add_winning(1500, date="2025-12-22")

# Get total winnings for a specific date
total = tracker.get_total_winnings(date="2025-12-22")

# Check mode activation for a specific date
is_active = tracker.check_and_activate_mode(date="2025-12-22")
```

## API Reference

### WinningsTracker

The main class for tracking winnings and managing mode activation.

#### `__init__(threshold=1000)`
Initialize the tracker with an optional custom threshold.

#### `add_winning(amount, date=None)`
Add a winning amount for a specific date (defaults to today).

#### `get_total_winnings(date=None)`
Get the total winnings for a specific date (defaults to today).

#### `check_and_activate_mode(date=None)`
Check if winnings exceed the threshold and activate mode if needed. Returns True if mode is activated.

#### `is_mode_active()`
Check if the mode is currently active.

#### `activate_mode()`
Activate the mode and return a status message.

## Testing

Run the test suite:

```bash
python -m unittest test_flownet.py -v
```

For a comprehensive demonstration of all scenarios, run:

```bash
python example.py
```

Expected test output:
```
test_activate_mode_with_insufficient_winnings ... ok
test_activate_mode_with_sufficient_winnings ... ok
test_add_winning_specific_date ... ok
test_add_winning_today ... ok
test_custom_threshold ... ok
test_get_total_winnings_empty ... ok
test_get_total_winnings_multiple ... ok
test_get_total_winnings_single ... ok
test_initialization ... ok
test_mode_activated_above_threshold ... ok
test_mode_activated_exact_1001 ... ok
test_mode_not_activated_at_threshold ... ok
test_mode_not_activated_below_threshold ... ok
test_multiple_dates_independence ... ok

----------------------------------------------------------------------
Ran 14 tests in 0.001s

OK
```

## Requirements

The mode activates when total winnings for a given date are **more than** 1000 (i.e., > 1000, not >= 1000).

- Winnings of 1000 or less: Mode **NOT** activated
- Winnings greater than 1000: Mode **ACTIVATED**

## License

This project is part of the FlowNet repository.
