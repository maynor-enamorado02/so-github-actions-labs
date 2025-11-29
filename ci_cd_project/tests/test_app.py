
import unittest
import tempfile
import os
from utils import write_file, read_file


class TestFileOperations(unittest.TestCase):
    def test_write_and_read_file(self):
        with tempfile.TemporaryDirectory() as d:
            test_file = os.path.join(d, "test.txt")
            test_content = "Contenido de prueba"
            write_file(test_file, test_content)
            result = read_file(test_file)
            self.assertEqual(result, test_content)


if __name__ == '__main__':
    unittest.main()
