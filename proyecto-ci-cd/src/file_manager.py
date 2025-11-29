import os
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class FileManager:
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self._ensure_data_dir()
    
    def _ensure_data_dir(self):
        """Asegura que el directorio de datos exista"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            logger.info(f"Directorio creado: {self.data_dir}")
    
    def save_data(self, data):
        """Guarda datos en un archivo con timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data_{timestamp}.txt"
        filepath = os.path.join(self.data_dir, filename)
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(data)
            
            logger.info(f"Archivo guardado: {filepath}")
            return filepath
            
        except Exception as e:
            logger.error(f"Error guardando archivo: {e}")
            raise
    
    def get_file_stats(self):
        """Obtiene estadísticas de los archivos en data_dir"""
        if not os.path.exists(self.data_dir):
            return {"file_count": 0, "total_size": 0}
        
        files = os.listdir(self.data_dir)
        total_size = 0
        
        for file in files:
            filepath = os.path.join(self.data_dir, file)
            if os.path.isfile(filepath):
                total_size += os.path.getsize(filepath)
        
        stats = {
            "file_count": len(files),
            "total_size_bytes": total_size,
            "data_directory": self.data_dir
        }
        
        return stats
    
    def cleanup_old_files(self, days_old=7):
        """Elimina archivos más antiguos que days_old días"""
        cutoff_time = datetime.now().timestamp() - (days_old * 24 * 60 * 60)
        deleted_count = 0
        
        if not os.path.exists(self.data_dir):
            return deleted_count
        
        for file in os.listdir(self.data_dir):
            filepath = os.path.join(self.data_dir, file)
            if os.path.isfile(filepath):
                file_time = os.path.getctime(filepath)
                if file_time < cutoff_time:
                    os.remove(filepath)
                    deleted_count += 1
                    logger.info(f"Archivo eliminado: {filepath}")
        
        return deleted_count
