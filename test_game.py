#!/usr/bin/env python3
"""
Simple test to check if Python is working correctly
"""

def test_basic_functionality():
    """Test basic Python features"""
    print("Testing Python functionality...")
    
    # Test match-case (Python 3.10+)
    test_value = "test"
    match test_value:
        case "test":
            print("✅ Match-case statement works!")
        case _:
            print("❌ Match-case statement failed!")
    
    # Test imports
    try:
        import sys
        print("✅ sys module imported successfully!")
    except ImportError as e:
        print(f"❌ sys import failed: {e}")
    
    try:
        import pygame
        print("✅ pygame module imported successfully!")
    except ImportError as e:
        print(f"❌ pygame import failed: {e}")
        print("You need to install pygame: pip install pygame")
    
    print("\nTest completed!")

if __name__ == "__main__":
    test_basic_functionality() 