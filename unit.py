'''
Created on Feb 3, 2015

@author: liu.chunming033@163.com
'''
import unittest

class Widget:
    def __init__(self, size = (40, 40)):
        self._size = size
    
    def getSize(self):
        return self._size

    def resize(self, width, height):
        if width < 0 or height < 0:
            raise ValueError, "illegal size"
        self._size = (width, height)

    def dispose(self):
        pass
    
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
        
    def tearDown(self):
        self.widget = None
        
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

if __name__ == "__main__":
    unittest.main()