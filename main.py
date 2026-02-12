from package import setup_logging
from package import process_budget_data


def main():
    log = setup_logging()

    log.info("   Inicializando processamento do arquivo")
    process_budget_data("Contorno", "VN")


if __name__ == "__main__":
    main()
