# 📊 Análise Comparativa de Algoritmos de Ordenação

Projeto acadêmico para análise de complexidade e performance de algoritmos de ordenação.

## 🎯 Sobre o Projeto

Este projeto implementa e analisa 6 algoritmos clássicos de ordenação:
- **Bubble Sort** - Comparação de elementos adjacentes
- **Insertion Sort** - Inserção em posição correta
- **Selection Sort** - Seleção do menor elemento
- **Merge Sort** - Divisão e conquista
- **Quick Sort** - Particionamento (com otimizações)
- **Shell Sort** - Insertion sort com gaps

## 📁 Estrutura do Projeto

```
atiividade-complexixade/
├── src/                          # Código fonte
│   ├── algorithms/               # Implementações dos algoritmos
│   │   ├── bubblesort.py
│   │   ├── insertionsort.py
│   │   ├── selectionsort.py
│   │   ├── mergesort.py
│   │   ├── quicksort.py
│   │   └── shellsort.py
│   ├── utils/                    # Utilitários
│   │   ├── array_generator.py   # Geração de arrays
│   │   ├── performance.py       # Medição de performance
│   │   └── csv_handler.py       # Manipulação de CSV
│   ├── dashboard/                # Interface Streamlit
│   │   └── app.py               # Dashboard interativo
│   └── main.py                   # Script principal de execução
├── data/                         # Dados gerados
│   └── metricas_execucao.csv    # Resultados dos testes
├── docs/                         # Documentação
│   ├── README.md                # Documentação detalhada
│   └── ANALISE_RESULTADOS.md    # Análise dos resultados
├── tests/                        # Testes (futuro)
├── .gitignore                    # Arquivos ignorados pelo git
├── requirements.txt              # Dependências Python
└── pyproject.toml               # Configuração do projeto
```

## 🚀 Como Usar

### 1. Instalação

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

### 2. Executar Análise

Gera métricas de todos os algoritmos e salva em CSV:

```bash
cd src
PYTHONPATH=. python main.py
```

Isso irá:
- Testar cada algoritmo com arrays de tamanhos 10, 100, 1.000 e 10.000
- Usar 3 tipos de arrays: aleatório, ordenado e reverso
- Gerar 72 testes no total (6 algoritmos × 4 tamanhos × 3 tipos)
- Salvar resultados em `data/metricas_execucao.csv`

### 3. Visualizar Dashboard

Abre interface interativa com gráficos e análises:

```bash
streamlit run src/dashboard/app.py
```

O dashboard inclui 7 abas:
1. **Visão Geral** - Métricas resumidas
2. **Tempo de Execução** - Gráficos de performance
3. **Comparações e Trocas** - Operações realizadas
4. **Chamadas Recursivas** - Análise de recursão
5. **Complexidade** - Verificação de Big O
6. **Lógica dos Algoritmos** - Explicações didáticas
7. **Conclusões** - Recomendações de uso

## 📊 Métricas Coletadas

Para cada teste, coletamos:
- **Comparações**: Número de comparações entre elementos
- **Trocas**: Número de movimentações de elementos
- **Chamadas Recursivas**: Profundidade da recursão (quando aplicável)
- **Tempo de Execução**: Tempo em segundos
- **Uso de Memória**: Memória atual e pico (em bytes)

## 🧪 Tipos de Teste

### Tamanhos de Array
- **10 elementos** - Testes básicos
- **100 elementos** - Dados pequenos
- **1.000 elementos** - Dados médios
- **10.000 elementos** - Dados grandes

### Distribuições
- **Random** - Array aleatório (pior caso para a maioria)
- **Ordered** - Array já ordenado (melhor caso para alguns)
- **Reverse** - Array em ordem reversa (pior caso para outros)

## 🎓 Objetivo Acadêmico

Este projeto foi desenvolvido para a disciplina de **Complexidade de Algoritmos**, demonstrando:
- Implementação correta de algoritmos clássicos
- Análise empírica de complexidade
- Comparação entre diferentes abordagens
- Visualização e interpretação de dados

## 📜 Licença

Projeto acadêmico - Livre para uso educacional

## 👥 Autores

Desenvolvido como atividade acadêmica
