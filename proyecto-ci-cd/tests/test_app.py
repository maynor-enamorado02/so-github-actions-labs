import unittest
import os
import tempfile
import shutil
import sys

# Agregar src al path
sys.path.append('src')

from app import SimpleApp

class TestSimpleApp(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.app = SimpleApp()
        self.app.data_dir = os.path.join(self.test_dir, "test_data")
    
    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_process_data(self):
        result = self.app.process_data("test data")
        self.assertIn("PROCESADO: TEST DATA", result)
    
    def test_get_statistics(self):
        self.app.process_data("test1")
        stats = self.app.get_statistics()
        self.assertEqual(stats["file_count"], 1)
        self.assertGreater(stats["total_size_bytes"], 0)
    
    def test_empty_statistics(self):
        stats = self.app.get_statistics()
        self.assertEqual(stats["file_count"], 0)

if __name__ == '__main__':
    unittest.main()
