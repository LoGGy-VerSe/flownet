#!/usr/bin/env python
"""
Example script demonstrating mode activation for winnings > 1000 on today's date
"""

from flownet import WinningsTracker
from datetime import datetime


def demonstrate_mode_activation():
    """Demonstrate the mode activation feature."""
    print("=" * 60)
    print("FlowNet: Activate Mode When Winnings > 1000 Today")
    print("=" * 60)
    print()
    
    # Create tracker
    tracker = WinningsTracker(threshold=1000)
    today = datetime.now().strftime("%Y-%m-%d")
    
    print(f"Date: {today}")
    print(f"Threshold: {tracker.threshold}")
    print()
    
    # Scenario 1: Winnings below threshold
    print("Scenario 1: Adding winnings totaling 900")
    print("-" * 60)
    tracker1 = WinningsTracker(threshold=1000)
    tracker1.add_winning(400)
    tracker1.add_winning(300)
    tracker1.add_winning(200)
    
    total1 = tracker1.get_total_winnings()
    print(f"Total winnings: {total1:.2f}")
    status1 = tracker1.activate_mode()
    print(f"Status: {status1}")
    print(f"Mode Active: {tracker1.is_mode_active()}")
    print()
    
    # Scenario 2: Winnings exactly at threshold
    print("Scenario 2: Adding winnings totaling exactly 1000")
    print("-" * 60)
    tracker2 = WinningsTracker(threshold=1000)
    tracker2.add_winning(1000)
    
    total2 = tracker2.get_total_winnings()
    print(f"Total winnings: {total2:.2f}")
    status2 = tracker2.activate_mode()
    print(f"Status: {status2}")
    print(f"Mode Active: {tracker2.is_mode_active()}")
    print()
    
    # Scenario 3: Winnings above threshold (ACTIVATED)
    print("Scenario 3: Adding winnings totaling 1050 (>1000)")
    print("-" * 60)
    tracker3 = WinningsTracker(threshold=1000)
    tracker3.add_winning(500)
    tracker3.add_winning(300)
    tracker3.add_winning(250)
    
    total3 = tracker3.get_total_winnings()
    print(f"Total winnings: {total3:.2f}")
    status3 = tracker3.activate_mode()
    print(f"Status: {status3}")
    print(f"Mode Active: {tracker3.is_mode_active()}")
    print()
    
    # Scenario 4: Multiple winnings exceeding 1000
    print("Scenario 4: Adding multiple winnings totaling 2500 (>1000)")
    print("-" * 60)
    tracker4 = WinningsTracker(threshold=1000)
    tracker4.add_winning(800)
    tracker4.add_winning(700)
    tracker4.add_winning(500)
    tracker4.add_winning(500)
    
    total4 = tracker4.get_total_winnings()
    print(f"Total winnings: {total4:.2f}")
    status4 = tracker4.activate_mode()
    print(f"Status: {status4}")
    print(f"Mode Active: {tracker4.is_mode_active()}")
    print()
    
    print("=" * 60)
    print("Summary: Mode activates when winnings > 1000 for today")
    print("=" * 60)


if __name__ == "__main__":
    demonstrate_mode_activation()
