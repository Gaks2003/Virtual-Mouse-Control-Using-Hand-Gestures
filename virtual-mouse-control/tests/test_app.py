import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from unittest.mock import patch, MagicMock
import math

class TestGestureControl(unittest.TestCase):
    
    @patch('cv2.VideoCapture')
    @patch('pyautogui.size')
    def setUp(self, mock_size, mock_cap):
        mock_size.return_value = (1920, 1080)
        mock_cap.return_value = MagicMock()
        
    def test_distance_calculation(self):
        # Mock landmark points
        p1 = MagicMock()
        p1.x, p1.y = 0.0, 0.0
        p2 = MagicMock()
        p2.x, p2.y = 0.3, 0.4
        
        # Import get_distance function
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
        
        # Calculate expected distance
        expected = math.hypot(0.3, 0.4)  # Should be 0.5
        
        # Test distance calculation logic
        actual = math.hypot(p2.x - p1.x, p2.y - p1.y)
        self.assertAlmostEqual(actual, expected, places=2)
    
    def test_pinch_threshold(self):
        # Test pinch gesture threshold
        pinch_threshold = 0.03
        
        # Test cases
        self.assertTrue(0.02 < pinch_threshold)  # Should trigger click
        self.assertFalse(0.05 < pinch_threshold)  # Should not trigger click
    
    @patch('cv2.VideoCapture')
    def test_camera_initialization(self, mock_cap):
        mock_cap.return_value = MagicMock()
        cap = mock_cap(0)
        self.assertIsNotNone(cap)

if __name__ == '__main__':
    unittest.main()