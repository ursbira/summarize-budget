from pathlib import Path

# --- CAMINHOS DE PASTAS ---
# __file__ aponta para constants.py.
# .parent é a pasta 'package', .parent.parent é a raiz do projeto.
BASE_DIR = Path(__file__).parent.parent.resolve()
LOG_DIR = BASE_DIR / "logs"
BASES_DIR = BASE_DIR / "bases"
OUTPUT_DIR = BASE_DIR / "output"
FILE_NAME_LOG = "configproject.log"

# Garantir que as pastas existam assim que o módulo for importado
LOG_DIR.mkdir(exist_ok=True)
BASES_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

# Mapping for Cell [B2] - Company Name -> ID (emp)
COMPANIES = {
    "Da Fonte": 10,
    "Tropical Fiat": 20,
    "Renovel": 30,
    # Adicione novas empresas aqui conforme necessário
}

# Mapping for Cell [B1] - Department -> Cost Center Code (centro_custo_bal)
# Inclui as variações mencionadas no prompt.md
COST_CENTERS = {
    "Assistência Técnica": "01.01",
    "Oficina": "01.01",
    "Mecânica": "01.01",
    "Veículos Novos": "02.01",
    "Peças": "03.01",
    "Peças e Acessórios": "03.01",
    "Seminovos": "04.01",
    "Semi-Novos": "04.01",
    "Venda Direta": "05.01",
    "Administração": "00.01",
}

# Mapping for Account Descriptions in Column [B] -> (conta, des_conta)
# Conforme a "SUGESTÃO DE SOLUÇÃO PARA TRATAR AS LINHAS" do prompt.md
ACCOUNT_MAP = {
    "Volume de Vendas Orçado": {
        "conta": "V_VEN_ORC",
        "des_conta": "VOLUME DE VENDAS ORÇADO"
    },
    "Passagens  Orçadas": {
        "conta": "V_VEN_ORC",
        "des_conta": "VOLUME DE VENDAS ORÇADO"
    },
    "Receita Venda Bruta": {
        "conta": "R_VEN_BRU",
        "des_conta": "RECEITA VENDA BRUTA"
    },
    "Custo das Vendas": {
        "conta": "C_VEN_PRO",
        "des_conta": "CUSTO DAS VENDAS"
    },
    "Total Geral Despesas": {
        "conta": "T_GER_DES",
        "des_conta": "TOTAL GERAL DESPESAS"
    },
    "Resultado Líquido Departamental": {
        "conta": "R_LIQ_DEP",
        "des_conta": "RESULTADO LÍQUIDO DEPARTAMENTAL"
    },
}

# Standard Linkie Accounts - Detalhamento extra (Macro, Micro, etc.)
# Pode ser usado futuramente para enriquecer o arquivo de saída
STANDARD_LINKIE_ACCOUNTS = {
    "V_VEN_ORC": {
        "macro": "VENDAS",
        "micro": "VOLUME",
        "characteristic": "UNIDADE",
        "category": "RESULTADO",
        "class": "ESTATISTICA"
    },
    "R_VEN_BRU": {
        "macro": "RECEITA",
        "micro": "BRUTA",
        "characteristic": "VALOR",
        "category": "RESULTADO",
        "class": "CONTABIL"
    },
}

# Configuração fixa das colunas do arquivo Excel de saída
OUTPUT_COLUMNS = [
    'emp', 'mes', 'ano', 'origem', 'historico', 
    'centro_custo_bal', 'conta', 'des_conta', 'movimento', 'view'
]

# Conta padrão para as "Linhas Especiais" (Realizado no Ano Anterior)
SPECIAL_ACCOUNT_CODE = "9999.9999.9999.001"
