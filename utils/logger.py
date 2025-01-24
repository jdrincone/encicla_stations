import logging
import os
from datetime import datetime


def setup_logger(log_dir="logs"):
    """
    Configura el logger para guardar logs en un archivo y mostrarlos en la consola.
    """
    # Crear el directorio de logs si no existe
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Nombre del archivo de log (usando la fecha actual)
    log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
    log_filepath = os.path.join(log_dir, log_filename)

    # Configurar el logger
    logger = logging.getLogger("encicla_stations")
    logger.setLevel(logging.DEBUG)  # Nivel base para todos los handlers

    # Formato de los mensajes de log
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # Handler para archivo (guarda todos los niveles)
    file_handler = logging.FileHandler(log_filepath)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Handler para consola (solo muestra niveles INFO y superiores)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # Añadir los handlers al logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger