import logging
import os
from datetime import datetime
from .file_manager import FileManager

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class SimpleApp:
    def __init__(self):
        self.file_manager = FileManager()
        logger.info("Aplicación inicializada")
    
    def process_data(self, data):
        """Procesa datos y los guarda en archivo"""
        try:
            logger.info(f"Procesando datos: {data}")
            
            # Simular procesamiento
            processed_data = f"PROCESADO: {data.upper()} - {datetime.now()}"
            
            # Guardar en archivo
            filename = self.file_manager.save_data(processed_data)
            
            logger.info(f"Datos guardados en: {filename}")
            return processed_data
            
        except Exception as e:
            logger.error(f"Error procesando datos: {e}")
            raise
    
    def get_statistics(self):
        """Obtiene estadísticas de los archivos procesados"""
        try:
            stats = self.file_manager.get_file_stats()
            logger.info(f"Estadísticas obtenidas: {stats}")
            return stats
        except Exception as e:
            logger.error(f"Error obteniendo estadísticas: {e}")
            raise

def main():
    app = SimpleApp()
    
    # Ejemplo de uso
    sample_data = "Hola mundo desde CI/CD Pipeline"
    result = app.process_data(sample_data)
    print(f"Resultado: {result}")
    
    stats = app.get_statistics()
    print(f"Estadísticas: {stats}")

if __name__ == "__main__":
    main()
