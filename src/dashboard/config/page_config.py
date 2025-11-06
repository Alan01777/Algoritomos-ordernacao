"""
Configurações da página e constantes do dashboard
"""

PAGE_CONFIG = {
    "page_title": "Análise de Algoritmos de Ordenação",
    "page_icon": "📊",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

SIDEBAR_INFO = """
### Informações do Estudo

**Algoritmos analisados:**
- Bubble Sort
- Insertion Sort
- Selection Sort
- Merge Sort
- Quick Sort
- Shell Sort

**Tamanhos de entrada:**
- 10 elementos
- 100 elementos
- 1.000 elementos
- 10.000 elementos

**Tipos de arranjo:**
- Aleatório
- Ordenado
- Reverso
"""

COMPLEXITY_DATA = {
    'Algoritmo': [
        'Bubble Sort',
        'Insertion Sort',
        'Selection Sort',
        'Merge Sort',
        'Quick Sort',
        'Shell Sort'
    ],
    'Melhor Caso': [
        'O(n)',
        'O(n)',
        'O(n²)',
        'O(n log n)',
        'O(n log n)',
        'O(n log n)'
    ],
    'Caso Médio': [
        'O(n²)',
        'O(n²)',
        'O(n²)',
        'O(n log n)',
        'O(n log n)',
        'O(n^1.5)'
    ],
    'Pior Caso': [
        'O(n²)',
        'O(n²)',
        'O(n²)',
        'O(n log n)',
        'O(n²)',
        'O(n²)'
    ],
    'Espaço': [
        'O(1)',
        'O(1)',
        'O(1)',
        'O(n)',
        'O(log n)',
        'O(1)'
    ],
    'Estável?': [
        '✅ Sim',
        '✅ Sim',
        '❌ Não',
        '✅ Sim',
        '❌ Não',
        '❌ Não'
    ],
    'In-Place?': [
        '✅ Sim',
        '✅ Sim',
        '✅ Sim',
        '❌ Não',
        '✅ Sim',
        '✅ Sim'
    ]
}

ALGORITHM_ADVANTAGES = {
    "Bubble Sort": ["Implementação simples", "Algoritmo estável", "Ordenação in-place"],
    "Insertion Sort": ["Eficiente para conjuntos pequenos", "Eficiente para dados parcialmente ordenados", "Algoritmo estável", "Ordenação in-place", "Comportamento adaptativo"],
    "Selection Sort": ["Número mínimo de trocas (n)", "Implementação simples", "Ordenação in-place"],
    "Merge Sort": ["Complexidade garantida O(n log n)", "Algoritmo estável", "Desempenho previsível"],
    "Quick Sort": ["Melhor desempenho médio na prática", "Ordenação in-place", "Otimização de cache"],
    "Shell Sort": ["Complexidade melhor que O(n²)", "Ordenação in-place", "Não requer recursão"]
}

ALGORITHM_DISADVANTAGES = {
    "Bubble Sort": ["Complexidade O(n²) em todos os casos", "Impraticável para conjuntos grandes"],
    "Insertion Sort": ["Complexidade O(n²) para dados aleatórios", "Ineficiente para conjuntos grandes"],
    "Selection Sort": ["Complexidade O(n²) invariante", "Não se adapta a dados pré-ordenados"],
    "Merge Sort": ["Requer O(n) de memória adicional", "Constantes maiores que Quick Sort"],
    "Quick Sort": ["Pior caso O(n²) possível", "Não é estável", "Implementação recursiva"],
    "Shell Sort": ["Complexidade depende da sequência de gaps", "Não é estável"]
}

DECISION_MATRIX = {
    'Cenário': [
        'Conjuntos pequenos (n < 100)',
        'Dados parcialmente ordenados',
        'Dados aleatórios de grande volume',
        'Restrição de memória',
        'Requisito de estabilidade',
        'Minimização de operações de escrita',
        'Garantia de pior caso',
        'Desempenho médio ótimo'
    ],
    'Algoritmo Recomendado': [
        'Insertion Sort',
        'Insertion Sort',
        'Quick Sort (otimizado)',
        'Shell Sort',
        'Merge Sort',
        'Selection Sort',
        'Merge Sort',
        'Quick Sort'
    ],
    'Justificativa': [
        'Overhead reduzido e implementação simples',
        'Complexidade O(n) confirmada experimentalmente',
        'Tempo de 0.44s comparado a 0.98s do Shell Sort',
        'Ordenação in-place com overhead de memória de 2x',
        'Único algoritmo O(n log n) estável',
        'Número de trocas limitado a n',
        'Complexidade O(n log n) garantida',
        'Melhor desempenho prático confirmado'
    ]
}
