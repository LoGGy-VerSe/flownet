"""
FlowNet - Winnings Mode Activation System

This module handles the activation of special mode when winnings exceed 1000
for today's date.
"""

from datetime import datetime
from typing import Dict, List


class WinningsTracker:
    """Tracks winnings and activates mode when threshold is exceeded."""
    
    def __init__(self, threshold: int = 1000):
        """
        Initialize the WinningsTracker.
        
        Args:
            threshold: The winnings threshold for mode activation (default: 1000)
        """
        self.threshold = threshold
        self.winnings_data: Dict[str, List[float]] = {}
        self.mode_active = False
    
    def add_winning(self, amount: float, date: str = None) -> None:
        """
        Add a winning amount for a specific date.
        
        Args:
            amount: The winning amount to add
            date: The date in YYYY-MM-DD format (defaults to today)
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        if date not in self.winnings_data:
            self.winnings_data[date] = []
        
        self.winnings_data[date].append(amount)
    
    def get_total_winnings(self, date: str = None) -> float:
        """
        Get total winnings for a specific date.
        
        Args:
            date: The date in YYYY-MM-DD format (defaults to today)
            
        Returns:
            Total winnings amount for the date
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        return sum(self.winnings_data.get(date, []))
    
    def check_and_activate_mode(self, date: str = None) -> bool:
        """
        Check if winnings exceed threshold and activate mode if needed.
        
        Args:
            date: The date in YYYY-MM-DD format (defaults to today)
            
        Returns:
            True if mode is activated, False otherwise
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        total = self.get_total_winnings(date)
        
        if total > self.threshold:
            self.mode_active = True
            return True
        
        self.mode_active = False
        return False
    
    def is_mode_active(self) -> bool:
        """
        Check if mode is currently active.
        
        Returns:
            True if mode is active, False otherwise
        """
        return self.mode_active
    
    def activate_mode(self) -> str:
        """
        Activate the special mode and return status message.
        
        Returns:
            Status message indicating mode activation
        """
        today = datetime.now().strftime("%Y-%m-%d")
        total = self.get_total_winnings(today)
        
        if self.check_and_activate_mode(today):
            return f"Mode ACTIVATED! Total winnings for {today}: {total:.2f} (threshold: {self.threshold})"
        else:
            return f"Mode NOT activated. Total winnings for {today}: {total:.2f} (threshold: {self.threshold})"


def main():
    """Main function to demonstrate the winnings tracker."""
    tracker = WinningsTracker(threshold=1000)
    
    print("FlowNet Winnings Mode Activation System")
    print("=" * 50)
    print(f"Threshold: {tracker.threshold}")
    print()
    
    # Example usage
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Add some sample winnings
    tracker.add_winning(500)
    tracker.add_winning(300)
    tracker.add_winning(250)
    
    print(f"Total winnings for today ({today}): {tracker.get_total_winnings():.2f}")
    print()
    
    # Check and activate mode
    status = tracker.activate_mode()
    print(status)
    print(f"Mode active: {tracker.is_mode_active()}")


if __name__ == "__main__":
    main()
