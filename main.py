from package import COMPANIES
from package import setup_logging


def main():
    log = setup_logging()

    log.info("Iniciando o processamento do summarize-budget...")

    # Exemplo de uso do log com os dados que já temos
    log.info(f"Empresas carregadas: {list(COMPANIES.keys())}")

    # Acessando um valor específico (Ex: ID da Da Fonte)
    if "Da Fonte" in COMPANIES:
        print(f"\nO ID da empresa Da Fonte é: {COMPANIES['Da Fonte']}")


if __name__ == "__main__":
    main()
