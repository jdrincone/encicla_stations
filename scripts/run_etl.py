from encicla_stations.client import APIClient
from database.manager import DatabaseManager
from utils.logger import setup_logger

# Configurar el logger
logger = setup_logger()


def main():
    logger.info("Iniciando el proceso ETL...")
    url = "https://api.citybik.es/v2/networks/encicla"
    db_path = "encicla_stations.db"

    try:
        # Obtener datos de la API
        logger.info("Obteniendo datos de la API...")
        client = APIClient(url)
        stations = client.fetch_data()

        # Guardar datos en la base de datos
        logger.info("Guardando datos en la base de datos...")
        db_manager = DatabaseManager(db_path)
        db_manager.connect()
        db_manager.insert_stations(stations)
        db_manager.close()

        logger.info("Proceso ETL completado con éxito.")
    except Exception as e:
        logger.error(f"Error durante el proceso ETL: {e}", exc_info=True)


if __name__ == "__main__":
    main()
