"""
Módulo de constantes e configurações para o sistema summarize-budget.
Inclui registros de empresas, departamentos, contas contábeis
e caminhos de arquivos.
Autor: Ubiratan Rocha da Silva
Data: 12/02/2026
"""
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List

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

# Valores padrão para os fatores, que podem ser sobrescritos por empresa
factor_credit = 1
factor_debit = -1
factor_additional = 1


# Registro das empresas com seus respectivos fatores
@dataclass(frozen=True)
class InputConfig:
    """Configuração dos arquivos de entrada Excel por departamento."""
    company_name: str
    file_name: str
    sheet_name: str
    accounting_dept_name: str
    internal_dept_code: str


@dataclass(frozen=True)
class CompanyConfig:
    """Configuração mestre da empresa e seus respectivos inputs."""
    id: int
    factor_credit: int
    factor_debit: int
    factor_additional: int = 1
    # Lista para armazenar as configurações de arquivos/departamentos
    inputs: List[InputConfig] = field(default_factory=list)


COMPANIES_REGISTRY: Dict[str, CompanyConfig] = {
    "Tropical Fiat": CompanyConfig(
        id=65, factor_credit=1, factor_debit=-1,
        inputs=[]
    ),
    "Tropical Multimarcas": CompanyConfig(
        id=66, factor_credit=1, factor_debit=-1,
        inputs=[]
    ),
    "Amauto Kia": CompanyConfig(
        id=94, factor_credit=-1, factor_debit=1,
        inputs=[
            InputConfig('Amauto Kia', 'ORÇAMENTO VN AMAUTO KIA.xlsx', 'O_VN', 'Veiculos Novos"', 'VN'),
            InputConfig('Amauto Kia', 'ORÇAMENTO SN AMAUTO KIA.xlsx', 'O_SN', 'Veiculos Semi-Novos', 'SN'),
            InputConfig('Amauto Kia', 'ORÇAMENTO PÇ AMAUTO KIA.xlsx', 'O_PC', 'peças', 'PC2'),
            InputConfig('Amauto Kia', 'ORÇAMENTO AT AMAUTO KIA.xlsx', 'O_SG', 'Mecânica', 'SG'),
        ]
    ),
    "Amauto Mitsubishi": CompanyConfig(
        id=72, factor_credit=1, factor_debit=-1,
        inputs=[
            InputConfig('Amauto Mitsubishi', 'ORÇAMENTO VN AMAUTO MIT.xlsx', 'O_VN AMAUTO MIT', 'veiculos novos', 'VN'),
            InputConfig('Amauto Mitsubishi', 'ORÇAMENTO SN AMAUTO MIT.xlsx', 'O_SN', 'Veiculos Semi-Novos', 'SN'),
            InputConfig('Amauto Mitsubishi', 'ORÇAMENTO PÇ AMAUTO MIT.xlsx', 'O_PC', 'peças', 'PC2'),
            InputConfig('Amauto Mitsubishi', 'ORÇAMENTO AT AMAUTO MIT.xlsx', 'O_SG', 'Mecânica', 'SG'),
        ]
    ),
    "Dubai Nissan": CompanyConfig(
        id=73, factor_credit=1, factor_debit=-1,
        inputs=[
            InputConfig('Dubai Nissan', 'ORÇAMENTO VN DUBAI NISSAN.xlsx', 'O_VN', 'veiculos novos', 'VN'),
            InputConfig('Dubai Nissan', 'ORÇAMENTO SN DUBAI NISSAN.xlsx', 'O_SN', 'Veiculos Semi-Novos', 'SN'),
            InputConfig('Dubai Nissan', 'ORÇAMENTO PÇ DUBAI.xlsx', 'O_PC', 'peças', 'PC2'),
            InputConfig('Dubai Nissan', 'ORÇAMENTO AT DUBAI.xlsx', 'O_SG', 'Mecânica', 'SG'),
        ]
    ),
    "Grand Cite Renault": CompanyConfig(
        id=74, factor_credit=1, factor_debit=-1,
        inputs=[
            InputConfig('Grand Cite Renault', 'ORÇAMENTO VN GRAND CITE RENAULT.xlsx', 'O_VN', 'veiculos novos', 'VN'),
            InputConfig('Grand Cite Renault', 'ORÇAMENTO SN GRAND CITE RENAULT.xlsx', 'O_SN', 'Veiculos Semi-Novos', 'SN'),
            InputConfig('Grand Cite Renault', 'ORÇAMENTO PÇ GRAND CITE.xlsx', 'O_PC', 'peças', 'PC2'),
            InputConfig('Grand Cite Renault', 'ORÇAMENTO AT GRAND CITE.xlsx', 'O_SG', 'Mecânica', 'SG'),
        ]
    ),
    "Contorno": CompanyConfig(
        id=96, factor_credit=1, factor_debit=-1,
        inputs=[
            InputConfig('Contorno', 'ORÇAMENTO VN GRUPO CONTORNO -JARDINS 2026.xlsx', 'O_VN', 'VEICULOS NOVOS', 'VN'),
            InputConfig('Contorno', 'ORÇAMENTO SN GRUPO CONTORNO  2026.xlsx', 'O_SN', 'VEICULOS USADOS', 'SN'),
            InputConfig('Contorno', 'xxxxxxxxxxxx111b.xlsx', 'O_PC', 'PECAS/ACESSORIOS', 'PC2'),
            InputConfig('Contorno', 'ORÇAMENTO AT GRUPO CONTORNO 2026.xlsx', 'O_SG', 'OFICINA MECANICA', 'SG'),
        ]
    ),
    "Rio Mar": CompanyConfig(
        id=101, factor_credit=1, factor_debit=-1,
        inputs=[
            InputConfig('Rio Mar', 'ORÇAMENTO VN GRUPO CONTORNO -RIO MAR 2026..xlsx', 'O_VN', 'VEICULOS NOVOS', 'VN'),
        ]
    ),
    "Renovel": CompanyConfig(
        id=87, factor_credit=1, factor_debit=-1,
        inputs=[]
    ),
}


@dataclass
class AccountEntry:
    """Estrutura para mapear as contas contábeis do orçamento."""
    account_code: str
    description: str
    factor: int = 1


# Refatoração do departments_config para usar AccountEntry
# Agora cada entrada é um objeto AccountEntry com o multiplicador de sinal
DEPARTMENTS_CONFIG: Dict[str, Dict[int, AccountEntry]] = {
    "VN": {
        38: AccountEntry("3.1.1.999.000001", "Venda de Veículos Novos", factor_credit),
        69: AccountEntry("3.3.1.999.000001", "Custo de Veículos Novos", factor_debit),
        76: AccountEntry("3.2.1.999.000001", "Impostos Outros - Veículos Novos", factor_debit),
        40: AccountEntry("3.7.1.999.000016", "Bônus - Veículos Novos", factor_credit),
        44: AccountEntry("3.1.1.999.000026", "Comissão Emplacamento", factor_credit),
        49: AccountEntry("3.1.1.999.000025", "Comissão Financiamento", factor_credit),
        53: AccountEntry("3.1.1.999.000023", "Comissão Seguro", factor_credit),
        82: AccountEntry("3.4.2.999.000001", "Outras Despesas com Pessoal", factor_debit),
        88: AccountEntry("3.4.1.999.000001", "Outras Despesas com Vendas", factor_debit),
        94: AccountEntry("3.4.3.999.000002", "Outras Despesa com Ocupação", factor_debit),
        100: AccountEntry("3.4.3.999.000001", "Outras Despesa com Funcionamento", factor_debit),
        37: AccountEntry("9.9.9.99.01.001", "Volume de Vendas VN", factor_additional)
    },
    "SN": {
        42: AccountEntry("3.1.1.999.000002", "Venda de Veículos Seminovos", factor_credit),
        73: AccountEntry("3.3.1.999.000003", "Custo de Veículos Seminovos", factor_debit),
        80: AccountEntry("3.2.1.999.000002", "Impostos Outros - Veículos Seminovos", factor_debit),
        44: AccountEntry("3.7.1.999.000017", "Bônus - Veículos Seminovos", factor_credit),
        48: AccountEntry("3.1.1.999.000026", "Comissão Emplacamento", factor_credit),
        53: AccountEntry("3.1.1.999.000025", "Comissão Financiamento", factor_credit),
        57: AccountEntry("3.1.1.999.000023", "Comissão Seguro", factor_credit),
        86: AccountEntry("3.4.2.999.000001", "Outras Despesas com Pessoal", factor_debit),
        92: AccountEntry("3.4.1.999.000001", "Outras Despesas com Vendas", factor_debit),
        98: AccountEntry("3.4.3.999.000002", "Outras Despesa com Ocupação", factor_debit),
        104: AccountEntry("3.4.3.999.000001", "Outras Despesa com Funcionamento", factor_debit),
        41: AccountEntry("9.9.9.99.01.002", "Volume de Vendas Seminovos", factor_additional)
    },
    "PC2": {
        88: AccountEntry("3.1.1.999.000010", "Venda de Peças", factor_credit),
        100: AccountEntry("3.3.2.999.000001", "Custo de Peças", factor_debit),
        107: AccountEntry("3.2.3.999.000001", "Impostos Outros - Peças", factor_debit),
        113: AccountEntry("3.4.2.999.000001", "Outras Despesas com Pessoal", factor_debit),
        119: AccountEntry("3.4.1.999.000001", "Outras Despesas com Vendas", factor_debit),
        125: AccountEntry("3.4.3.999.000002", "Outras Despesa com Ocupação", factor_debit),
        131: AccountEntry("3.4.3.999.000001", "Outras Despesa com Funcionamento", factor_debit)
    },
    "SG": {
        43: AccountEntry("3.1.1.999.000011", "Venda de M.O. Mecânica", factor_credit),
        55: AccountEntry("3.3.2.999.000002", "Custo Mão de Obra Mecânica", factor_debit),
        62: AccountEntry("3.2.3.999.000002", "Impostos Outros - Mecânica", factor_debit),
        68: AccountEntry("3.4.2.999.000001", "Outras Despesas com Pessoal", factor_debit),
        74: AccountEntry("3.4.1.999.000001", "Outras Despesas com Vendas", factor_debit),
        80: AccountEntry("3.4.3.999.000002", "Outras Despesa com Ocupação", factor_debit),
        86: AccountEntry("3.4.3.999.000001", "Outras Despesa com Funcionamento", factor_debit),
        42: AccountEntry("9.9.9.99.01.010", "Passagem Oficina Mecânica", factor_additional)
    }
}

# Configuração fixa das colunas do arquivo Excel de saída
OUTPUT_COLUMNS = [
    'emp', 'mes', 'ano', 'origem', 'historico', 
    'centro_custo_bal', 'conta', 'des_conta', 'movimento', 'view'
]
