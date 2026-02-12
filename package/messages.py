"""
Módulo de mensagens centralizadas para o sistema summarize-budget.
Suporta múltiplos idiomas e utiliza códigos identificadores (IDs).
Autor: Ubiratan Rocha da Silva
Data: 12/02/2026
"""

from typing import Final
from typing import Any

# Configuração padrão de idioma (pode ser movida para config futuramente)
DEFAULT_LANG: Final[str] = "pt_br"
# DEFAULT_LANG: Final[str] = "en"

# Dicionário de mensagens: [Código][Idioma]
MESSAGES: Final[dict[str, dict[str, str]]] = {
    "ERR_COMP_NOT_FOUND": {
        "pt_br": "Empresa não mapeada: {add_info}.",
        "en": "Company not mapped: {add_info}."
    },
    "ERR_CC_NOT_FOUND": {
        "pt_br": "Centro de Custo {cost_center} não mapeado para a empresa {company}.",
        "en": "Cost Center {cost_center} not mapped for company {company}."
    },
    "ERR_DEPT_NOT_CONFIGURED": {
        "pt_br": "Departamento '{dept_code}' não configurado para a empresa {company}.",
        "en": "Department '{dept_code}' not configured for company {company}."
    },
    "ERR_FILE_NOT_FOUND": {
        "pt_br": "Arquivo não encontrado: {add_info}.",
        "en": "File not found: {add_info}."
    },
    "ERR_PROCESSING": {
        "pt_br": "Ocorreu um erro durante o processamento: {add_info}.",
        "en": "An error occurred during processing: {add_info}."
    },
    "ERR_SHEET_NOT_FOUND": {
        "pt_br": "Guia não encontrada no arquivo: {add_info}.",
        "en": "Sheet not found in file: {add_info}."
    },
    "INFO_FILE_GENERATED": {
        "pt_br": "Arquivo gerado em: {add_info}.",
        "en": "File generated at: {add_info}."
    },
    "INFO_PROCESS_SUCCESS": {
        "pt_br": "Processamento concluído com sucesso!",
        "en": "Processing completed successfully!"
    },
    "INFO_START_FILE": {
        "pt_br": "Iniciando processamento do arquivo: {add_info}.",
        "en": "Starting file processing: {add_info}."
    },
    "INFO_SUCCESS_GEN": {
        "pt_br": "Sucesso! Arquivo gerado em: {add_info}.",
        "en": "Success! File generated at: {add_info}."
    },
}


def get_msg(msg_code: str, lang: str = DEFAULT_LANG, **kwargs: Any) -> str:
    """
    Recupera uma mensagem traduzida e formata com argumentos dinâmicos se necessário.

    Args:
        msg_code: O código identificador da mensagem.
        lang: O idioma desejado (padrão: 'pt_br').
        **kwargs: Variáveis para preencher placeholders na string (ex: path="C:/...").

    Returns:
        A mensagem formatada ou o código entre colchetes em caso de erro.
    """
    msg_dict: dict[str, str] = MESSAGES.get(msg_code, {})
    template: str = msg_dict.get(lang, f"[{msg_code}]")

    try:
        return template.format(**kwargs)
    except (KeyError, ValueError):
        # Se faltar algum argumento esperado, retorna o template bruto
        # Preferi esta abordagem para ver erros no get_msg
        return template
