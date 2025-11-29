import unittest
import os
import tempfile
import shutil
from src.app import SimpleApp

class TestSimpleApp(unittest.TestCase):
    def setUp(self):
        # Directorio temporal para pruebas
        self.test_dir = tempfile.mkdtemp()
        self.app = SimpleApp()
        # Cambiar directorio de datos para pruebas
        self.app.file_manager.data_dir = os.path.join(self.test_dir, "test_data")
    
    def tearDown(self):
        # Limpiar directorio temporal
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_process_data(self):
        """Test del procesamiento de datos"""
        test_data = "test data"
        result = self.app.process_data(test_data)
        
        self.assertIn("PROCESADO: TEST DATA", result)
        self.assertIn("PROCESADO:", result)
    
    def test_get_statistics(self):
        """Test de obtención de estadísticas"""
        # Procesar algunos datos primero
        self.app.process_data("test1")
        self.app.process_data("test2")
        
        stats = self.app.get_statistics()
        
        self.assertEqual(stats["file_count"], 2)
        self.assertGreater(stats["total_size_bytes"], 0)
    
    def test_empty_statistics(self):
        """Test de estadísticas con directorio vacío"""
        stats = self.app.get_statistics()
        self.assertEqual(stats["file_count"], 0)

if __name__ == '__main__':
    unittest.main()
