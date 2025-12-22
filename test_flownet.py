"""
Unit tests for FlowNet Winnings Mode Activation System
"""

import unittest
from datetime import datetime
from flownet import WinningsTracker


class TestWinningsTracker(unittest.TestCase):
    """Test cases for WinningsTracker class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.tracker = WinningsTracker(threshold=1000)
        self.today = datetime.now().strftime("%Y-%m-%d")
    
    def test_initialization(self):
        """Test tracker initialization."""
        self.assertEqual(self.tracker.threshold, 1000)
        self.assertFalse(self.tracker.mode_active)
        self.assertEqual(len(self.tracker.winnings_data), 0)
    
    def test_add_winning_today(self):
        """Test adding winnings for today."""
        self.tracker.add_winning(500)
        self.assertIn(self.today, self.tracker.winnings_data)
        self.assertEqual(len(self.tracker.winnings_data[self.today]), 1)
        self.assertEqual(self.tracker.winnings_data[self.today][0], 500)
    
    def test_add_winning_specific_date(self):
        """Test adding winnings for a specific date."""
        test_date = "2025-01-01"
        self.tracker.add_winning(750, date=test_date)
        self.assertIn(test_date, self.tracker.winnings_data)
        self.assertEqual(self.tracker.winnings_data[test_date][0], 750)
    
    def test_get_total_winnings_empty(self):
        """Test getting total winnings when no data exists."""
        self.assertEqual(self.tracker.get_total_winnings(), 0)
    
    def test_get_total_winnings_single(self):
        """Test getting total winnings with single entry."""
        self.tracker.add_winning(500)
        self.assertEqual(self.tracker.get_total_winnings(), 500)
    
    def test_get_total_winnings_multiple(self):
        """Test getting total winnings with multiple entries."""
        self.tracker.add_winning(500)
        self.tracker.add_winning(300)
        self.tracker.add_winning(250)
        self.assertEqual(self.tracker.get_total_winnings(), 1050)
    
    def test_mode_not_activated_below_threshold(self):
        """Test that mode is not activated below threshold."""
        self.tracker.add_winning(500)
        self.tracker.add_winning(400)  # Total: 900
        result = self.tracker.check_and_activate_mode()
        self.assertFalse(result)
        self.assertFalse(self.tracker.is_mode_active())
    
    def test_mode_not_activated_at_threshold(self):
        """Test that mode is not activated exactly at threshold."""
        self.tracker.add_winning(1000)
        result = self.tracker.check_and_activate_mode()
        self.assertFalse(result)
        self.assertFalse(self.tracker.is_mode_active())
    
    def test_mode_activated_above_threshold(self):
        """Test that mode is activated above threshold (>1000)."""
        self.tracker.add_winning(500)
        self.tracker.add_winning(300)
        self.tracker.add_winning(250)  # Total: 1050
        result = self.tracker.check_and_activate_mode()
        self.assertTrue(result)
        self.assertTrue(self.tracker.is_mode_active())
    
    def test_mode_activated_exact_1001(self):
        """Test that mode is activated at exactly 1001."""
        self.tracker.add_winning(1001)
        result = self.tracker.check_and_activate_mode()
        self.assertTrue(result)
        self.assertTrue(self.tracker.is_mode_active())
    
    def test_activate_mode_with_sufficient_winnings(self):
        """Test activate_mode method with winnings > 1000."""
        self.tracker.add_winning(1500)
        status = self.tracker.activate_mode()
        self.assertIn("Mode ACTIVATED", status)
        self.assertIn("1500.00", status)
        self.assertTrue(self.tracker.is_mode_active())
    
    def test_activate_mode_with_insufficient_winnings(self):
        """Test activate_mode method with winnings <= 1000."""
        self.tracker.add_winning(800)
        status = self.tracker.activate_mode()
        self.assertIn("Mode NOT activated", status)
        self.assertIn("800.00", status)
        self.assertFalse(self.tracker.is_mode_active())
    
    def test_custom_threshold(self):
        """Test tracker with custom threshold."""
        custom_tracker = WinningsTracker(threshold=500)
        custom_tracker.add_winning(600)
        result = custom_tracker.check_and_activate_mode()
        self.assertTrue(result)
        self.assertTrue(custom_tracker.is_mode_active())
    
    def test_multiple_dates_independence(self):
        """Test that different dates are tracked independently."""
        date1 = "2025-01-01"
        date2 = "2025-01-02"
        
        self.tracker.add_winning(1500, date=date1)
        self.tracker.add_winning(500, date=date2)
        
        self.assertTrue(self.tracker.check_and_activate_mode(date=date1))
        self.assertFalse(self.tracker.check_and_activate_mode(date=date2))


if __name__ == "__main__":
    unittest.main()
