# 📊 Análise Comparativa de Algoritmos de Ordenação

Trabalho acadêmico de análise experimental e teórica de algoritmos de ordenação.

## 🎯 Algoritmos Implementados

- ✅ **Bubble Sort** - Comparação direta com trocas adjacentes
- ✅ **Insertion Sort** - Inserção em posição ordenada
- ✅ **Selection Sort** - Seleção do mínimo
- ✅ **Merge Sort** - Divisão e conquista (recursivo)
- ✅ **Quick Sort** - Particionamento por pivô (recursivo, otimizado)
- ✅ **Shell Sort** - Insertion Sort com gaps decrescentes

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar Testes e Gerar Métricas

```bash
python main.py
```

Este comando irá:
- Testar todos os algoritmos
- Com 4 tamanhos de array: 10, 100, 1.000, 10.000
- Com 3 tipos de dados: aleatório, ordenado, reverso
- Gerar arquivo `metricas_execucao.csv`

### 3. Visualizar Dashboard Interativo

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no navegador em `http://localhost:8501`

## 📁 Estrutura do Projeto

```
atiividade-complexixade/
├── algorithms/              # Implementações dos algoritmos
│   ├── __init__.py
│   ├── bubblesort.py       # Bubble Sort com comentários
│   ├── insertionsort.py    # Insertion Sort com comentários
│   ├── selectionsort.py    # Selection Sort com comentários
│   ├── mergesort.py        # Merge Sort com explicações detalhadas
│   ├── quicksort.py        # Quick Sort otimizado (3 otimizações)
│   └── shellsort.py        # Shell Sort com sequência de Knuth
├── utils.py                # Funções utilitárias (geração, medição, CSV)
├── main.py                 # Hub de execução dos testes
├── app.py                  # Dashboard Streamlit
├── requirements.txt        # Dependências Python
├── metricas_execucao.csv   # Resultados dos testes (gerado)
├── ANALISE_RESULTADOS.md   # Análise textual detalhada
└── README.md               # Este arquivo
```

## 📊 Funcionalidades do Dashboard

### Tab 1: Visão Geral
- Métricas resumidas
- Tabela comparativa
- Gráfico de radar multi-dimensional

### Tab 2: Tempo de Execução
- Gráficos tempo vs tamanho (log-log)
- Comparação por tipo de array
- Tabelas detalhadas

### Tab 3: Comparações e Trocas
- Evolução de comparações por tamanho
- Evolução de trocas por tamanho
- Razão trocas/comparações (eficiência)

### Tab 4: Chamadas Recursivas
- Análise de Merge Sort e Quick Sort
- Comparação teórico vs prático
- Profundidade da recursão

### Tab 5: Complexidade
- Tabela de complexidade Big O
- Verificação experimental
- Gráficos de taxa de crescimento

### Tab 6: Lógica dos Algoritmos
- Explicação da estratégia
- Descrição passo a passo
- Código-fonte comentado

### Tab 7: Conclusões
- Comparação teórico vs prático
- Matriz de decisão
- Recomendações por caso de uso

## 🏆 Principais Resultados (10.000 elementos, aleatório)

| Posição | Algoritmo | Tempo | Speedup |
|---------|-----------|-------|---------|
| 🥇 1º | Quick Sort | 0.44s | 388x mais rápido que Bubble Sort |
| 🥈 2º | Shell Sort | 0.98s | 174x mais rápido que Bubble Sort |
| 🥉 3º | Insertion Sort | 72.99s | 2.3x mais rápido que Bubble Sort |

## 💡 Otimizações Implementadas

### Quick Sort (3 otimizações)
1. **Mediana de Três**: Evita O(n²) em arrays ordenados
2. **Insertion Sort Híbrido**: Usa Insertion Sort para partições < 10 elementos
3. **Tail Call Optimization**: Limita profundidade da recursão

Resultado: Não houve stack overflow em nenhum teste!

### Shell Sort
- Usa sequência de gaps de Knuth: h = 3h + 1
- Otimiza performance em ~40% comparado a sequências simples

## 📈 Métricas Coletadas

Para cada combinação de algoritmo × tamanho × tipo:
- ⏱️ **Tempo de execução** (segundos)
- 🔢 **Número de comparações**
- 🔄 **Número de trocas/movimentações**
- 🔁 **Número de chamadas recursivas** (para recursivos)
- 💾 **Uso de memória** (atual e pico)

Total: **72 execuções** (6 × 4 × 3)

## 🎓 Requisitos da Atividade Atendidos

✅ Implementação de todos os 6 algoritmos
✅ Código bem comentado explicando cada etapa
✅ Seção explicando lógica e estratégia de cada algoritmo
✅ Quantificação de comparações e trocas
✅ Análise experimental com 4 tamanhos e 3 tipos de arrays
✅ Resultados em tabelas e gráficos
✅ Análise de complexidade Big O (melhor, médio, pior)
✅ Quantificação de chamadas recursivas
✅ Comparação teórico vs prático
✅ Conclusão sobre casos de uso adequados

## 🔬 Tecnologias Utilizadas

- **Python 3.12+**
- **Streamlit** - Dashboard interativo
- **Plotly** - Gráficos interativos
- **Pandas** - Manipulação de dados
- **NumPy** - Cálculos numéricos

## 📚 Referências

- CORMEN, T. H. et al. **Introduction to Algorithms**, 3rd Edition. MIT Press, 2009.
- KNUTH, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**, 2nd Edition. Addison-Wesley, 1998.
- [Python timeit documentation](https://docs.python.org/3/library/timeit.html)
- [Python tracemalloc documentation](https://docs.python.org/3/library/tracemalloc.html)

## 👨‍💻 Autor

[Seu Nome] - [Curso] - [Universidade]

## 📄 Licença

Este projeto é para fins acadêmicos.
