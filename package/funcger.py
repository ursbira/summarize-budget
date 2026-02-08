import logging
import sys
from .constants import LOG_DIR, FILE_NAME_LOG


def setup_logging():
    """
    Configura o sistema de logs para o projeto.
    As mensagens serão exibidas no console e salvas em um arquivo .log.
    """
    log_file = LOG_DIR / FILE_NAME_LOG
    log_format = "%(asctime)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # Criando o logger básico
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        datefmt=date_format,
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout)
        ]
    )

    logger = logging.getLogger("summarize-budget")
    logger.info("Sistema de Logs inicializado com sucesso.")
    return logger
