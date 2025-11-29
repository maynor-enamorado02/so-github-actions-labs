import logging
import os
from datetime import datetime

# Configuración simple de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimpleApp:
    def __init__(self):
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)
        logger.info("Aplicación inicializada")
    
    def process_data(self, data):
        """Procesa datos y los guarda en archivo"""
        try:
            logger.info(f"Procesando datos: {data}")
            processed_data = f"PROCESADO: {data.upper()} - {datetime.now()}"
            
            # Guardar en archivo
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"data_{timestamp}.txt"
            filepath = os.path.join(self.data_dir, filename)
            
            with open(filepath, 'w') as f:
                f.write(processed_data)
            
            logger.info(f"Datos guardados en: {filename}")
            return processed_data
            
        except Exception as e:
            logger.error(f"Error procesando datos: {e}")
            return f"ERROR: {e}"
    
    def get_statistics(self):
        """Obtiene estadísticas de los archivos procesados"""
        try:
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
                "total_size_bytes": total_size
            }
            
            logger.info(f"Estadísticas obtenidas: {stats}")
            return stats
        except Exception as e:
            logger.error(f"Error obteniendo estadísticas: {e}")
            return {"error": str(e)}

def main():
    app = SimpleApp()
    result = app.process_data("Hola mundo CI/CD")
    print(f"Resultado: {result}")
    stats = app.get_statistics()
    print(f"Estadísticas: {stats}")

if __name__ == "__main__":
    main()
