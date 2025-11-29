import os
from datetime import datetime

class SimpleApp:
    def __init__(self):
        self.data_dir = "data"
        os.makedirs(self.data_dir, exist_ok=True)
    
    def process_data(self, data):
        """Procesa datos y los guarda en archivo"""
        processed_data = f"PROCESADO: {data} - {datetime.now()}"
        
        # Guardar en archivo
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"data_{timestamp}.txt"
        filepath = os.path.join(self.data_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(processed_data)
        
        return processed_data
    
    def get_statistics(self):
        """Obtiene estadísticas de los archivos"""
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
        
        return stats

if __name__ == "__main__":
    app = SimpleApp()
    result = app.process_data("Test")
    print("Resultado:", result)
    stats = app.get_statistics()
    print("Stats:", stats)
