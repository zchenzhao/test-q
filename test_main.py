import unittest
import time
from main import timestamp_to_epoch, epoch_to_timestamp


class TestTimestampConversion(unittest.TestCase):
    def test_timestamp_to_epoch_iso(self):
        # Test ISO format
        timestamp = "2023-01-01T12:00:00Z"
        expected = 1672574400.0
        self.assertEqual(timestamp_to_epoch(timestamp), expected)
        
    def test_timestamp_to_epoch_custom_format(self):
        # Test custom format
        timestamp = "01/01/2023 12:00:00"
        format_str = "%m/%d/%Y %H:%M:%S"
        expected = 1672574400.0
        self.assertEqual(timestamp_to_epoch(timestamp, format_str), expected)
    
    def test_timestamp_to_epoch_with_timezone(self):
        # Test with explicit timezone
        timestamp = "2023-01-01T07:00:00-05:00"  # EST timezone
        expected = 1672574400.0  # Should be the same as UTC noon
        self.assertEqual(timestamp_to_epoch(timestamp), expected)
    
    def test_epoch_to_timestamp_default_format(self):
        # Test default ISO format
        epoch = 1672574400.0
        expected = "2023-01-01T12:00:00Z"
        self.assertEqual(epoch_to_timestamp(epoch), expected)
    
    def test_epoch_to_timestamp_custom_format(self):
        # Test custom format
        epoch = 1672574400.0
        format_str = "%m/%d/%Y %H:%M:%S"
        expected = "01/01/2023 12:00:00"
        self.assertEqual(epoch_to_timestamp(epoch, format_str), expected)
    
    def test_current_time_conversion(self):
        # Test that converting current time works correctly
        current_epoch = time.time()
        timestamp = epoch_to_timestamp(current_epoch)
        converted_back = timestamp_to_epoch(timestamp)
        # Allow for small floating point differences
        self.assertAlmostEqual(current_epoch, converted_back, places=0)


if __name__ == "__main__":
    unittest.main()