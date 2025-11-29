import unittest
import os
import tempfile
import shutil
from src.file_manager import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.file_manager = FileManager(self.test_dir)
    
    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_save_data(self):
        """Test de guardado de datos"""
        test_data = "Hello, World!"
        filepath = self.file_manager.save_data(test_data)
        
        self.assertTrue(os.path.exists(filepath))
        
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.assertEqual(content, test_data)
    
    def test_get_stats_empty(self):
        """Test de estadísticas con directorio vacío"""
        stats = self.file_manager.get_file_stats()
        self.assertEqual(stats["file_count"], 0)
        self.assertEqual(stats["total_size_bytes"], 0)
    
    def test_get_stats_with_files(self):
        """Test de estadísticas con archivos"""
        self.file_manager.save_data("test1")
        self.file_manager.save_data("test2")
        
        stats = self.file_manager.get_file_stats()
        self.assertEqual(stats["file_count"], 2)
        self.assertGreater(stats["total_size_bytes"], 0)
    
    def test_cleanup_old_files(self):
        """Test de limpieza de archivos antiguos"""
        # Este test sería más completo con mocking de timestamps
        self.file_manager.save_data("test")
        deleted = self.file_manager.cleanup_old_files(days_old=0)
        self.assertEqual(deleted, 0)  # No debería eliminar archivos nuevos

if __name__ == '__main__':
    unittest.main()
