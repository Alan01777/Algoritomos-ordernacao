"""
Informações educacionais sobre os algoritmos de ordenação
"""

ALGORITHM_INFO = {
    "Bubble Sort": {
        "estrategia": "Comparação Direta e Trocas Adjacentes",
        "emoji": "🎈",
        "analogia_principal": "Propagação de elementos maiores através de comparações sucessivas",
        "analogias": [
            {
                "titulo": "Processo de Flutuação",
                "descricao": """
                O algoritmo realiza comparações sucessivas entre elementos adjacentes:
                - Elementos de maior valor são propagados em direção ao final do arranjo
                - A cada iteração, compara-se pares de elementos adjacentes
                - Quando um elemento maior precede um menor, realiza-se a troca
                - Após cada passagem completa, o maior elemento não ordenado alcança sua posição final
                - O processo se repete até que nenhuma troca seja necessária
                """
            },
            {
                "titulo": "Ordenação por Passagens Sucessivas",
                "descricao": """
                Mecanismo de ordenação por iterações:
                - Percorre-se o arranjo da esquerda para direita
                - Elementos adjacentes fora de ordem são permutados
                - O processo é repetido múltiplas vezes
                - Elementos maiores migram progressivamente para o final
                - A convergência ocorre quando nenhuma permutação é necessária
                """
            }
        ],
        "exemplo_visual": """
        **Arranjo inicial:** [5, 2, 8, 1, 9]

        **Passagem 1:** (propagação do maior elemento)
        - [5, 2, 8, 1, 9] → compara 5 e 2 → [2, 5, 8, 1, 9]
        - [2, 5, 8, 1, 9] → compara 5 e 8 → sem troca
        - [2, 5, 8, 1, 9] → compara 8 e 1 → [2, 5, 1, 8, 9]
        - [2, 5, 1, 8, 9] → compara 8 e 9 → sem troca
        - Maior elemento (9) na posição final

        **Passagem 2:** (propagação do segundo maior)
        - Processo continua até ordenação completa
        """,
        "complexidade": "O(n²) - duas iterações aninhadas",
        "quando_usar": "Finalidades didáticas ou conjuntos muito pequenos",
        "curiosidade": "Denominação derivada da analogia com bolhas que ascendem em um líquido"
    },
    "Insertion Sort": {
        "estrategia": "Inserção em Posição Ordenada",
        "emoji": "🃏",
        "analogia_principal": "Manutenção de sequência ordenada através de inserções sucessivas",
        "analogias": [
            {
                "titulo": "Ordenação Incremental",
                "descricao": """
                O algoritmo mantém uma porção ordenada que cresce progressivamente:
                - Inicia-se com o primeiro elemento considerado ordenado
                - Cada novo elemento é comparado com a sequência ordenada
                - O elemento é inserido na posição apropriada
                - A porção ordenada se expande a cada iteração
                - O processo preserva a ordenação em todos os estágios
                - Corresponde ao método intuitivo de ordenação manual
                """
            },
            {
                "titulo": "Inserção com Deslocamento",
                "descricao": """
                Processo de inserção com reorganização:
                - Região ordenada e região não ordenada são mantidas
                - Primeiro elemento da região não ordenada é selecionado
                - Compara-se com elementos da região ordenada
                - Elementos maiores são deslocados para criar espaço
                - Inserção ocorre na posição correta mantendo a ordem
                """
            },
            {
                "titulo": "Ordenação Adaptativa",
                "descricao": """
                Característica adaptativa do algoritmo:
                - Elemento é comparado sequencialmente com elementos ordenados
                - Inserção ocorre quando a posição correta é identificada
                - Número de comparações reduz significativamente em dados parcialmente ordenados
                - Eficiência aumenta proporcionalmente ao grau de pré-ordenação
                - Mantém invariante de ordenação durante toda execução
                """
            }
        ],
        "exemplo_visual": """
        **Arranjo inicial:** [5, 2, 8, 1, 9]

        **Início:** [5 | 2, 8, 1, 9]  ← primeiro elemento considerado ordenado

        **Passo 1:** Inserir 2
        - [5 | 2, 8, 1, 9] → 2 < 5
        - Desloca 5 para direita → [_, 5 | 8, 1, 9]
        - Insere 2 → [2, 5 | 8, 1, 9]

        **Passo 2:** Inserir 8
        - [2, 5 | 8, 1, 9] → 8 > 5
        - Posição correta → [2, 5, 8 | 1, 9]

        **Passo 3:** Inserir 1
        - [2, 5, 8 | 1, 9] → 1 menor que todos
        - Desloca 8, 5, 2 → [_, _, _, 8 | 9]
        - Insere 1 → [1, 2, 5, 8 | 9]
        """,
        "complexidade": "O(n) melhor caso (ordenado), O(n²) pior caso (reverso)",
        "quando_usar": "Conjuntos pequenos (n < 50), dados parcialmente ordenados, sub-rotina em algoritmos híbridos",
        "curiosidade": "Apresenta speedup de 5.945x em dados ordenados comparado a dados reversos"
    },
    "Selection Sort": {
        "estrategia": "Seleção do Mínimo",
        "emoji": "🏆",
        "analogia_principal": "Seleção sequencial do elemento mínimo para cada posição",
        "analogias": [
            {
                "titulo": "Seleção Iterativa do Mínimo",
                "descricao": """
                O algoritmo opera através de seleções sucessivas:
                - Para cada posição, percorre-se toda a porção não ordenada
                - Identifica-se o elemento de menor valor
                - O elemento mínimo é colocado em sua posição final
                - Cada seleção é definitiva e não requer ajustes posteriores
                - Processo se repete para as posições subsequentes
                - Busca exaustiva em cada iteração
                """
            },
            {
                "titulo": "Particionamento Progressivo",
                "descricao": """
                Organização por particionamento ordenado/não ordenado:
                - Examina-se integralmente a porção não ordenada
                - Elemento de menor valor é identificado
                - Troca é realizada para posicionar o elemento corretamente
                - Fronteira entre ordenado e não ordenado avança
                - Cada elemento é posicionado diretamente em seu local final
                - Redução progressiva do espaço de busca
                """
            },
            {
                "titulo": "Minimização de Operações de Escrita",
                "descricao": """
                Característica de otimização de escritas:
                - Múltiplas comparações precedem cada operação de troca
                - Elemento correto é identificado antes da escrita
                - Apenas uma troca por iteração (no máximo n trocas totais)
                - Minimização de operações de I/O
                - Ideal para memórias com custo elevado de escrita
                """
            }
        ],
        "exemplo_visual": """
        **Arranjo inicial:** [5, 2, 8, 1, 9]

        **Passagem 1:** Identificar mínimo global
        - [5, 2, 8, 1, 9] → mínimo é 1
        - Troca 5 ↔ 1 → [1 | 2, 8, 5, 9]

        **Passagem 2:** Identificar mínimo da porção restante
        - [1 | 2, 8, 5, 9] → mínimo é 2 (posição correta)
        - Sem troca necessária → [1, 2 | 8, 5, 9]

        **Passagem 3:** Identificar mínimo da porção restante
        - [1, 2 | 8, 5, 9] → mínimo é 5
        - Troca 8 ↔ 5 → [1, 2, 5 | 8, 9]

        Processo continua até ordenação completa
        """,
        "complexidade": "O(n²) invariante - independente da configuração inicial",
        "quando_usar": "Memórias flash/SSD (minimização de escritas), sistemas embarcados com restrições",
        "curiosidade": "Realiza exatamente n trocas, enquanto Bubble Sort pode realizar até n²/2 trocas"
    },
    "Merge Sort": {
        "estrategia": "Divisão e Conquista",
        "emoji": "🔀",
        "analogia_principal": "Paradigma de divisão e conquista com mesclagem",
        "analogias": [
            {
                "titulo": "Divisão Recursiva e Mesclagem",
                "descricao": """
                **Estrutura do algoritmo:**
                1. **Divisão:** Particionamento recursivo do arranjo em subconjuntos menores
                2. **Conquista:** Ordenação recursiva de cada partição
                3. **Combinação:** Mesclagem ordenada das partições
                4. **Caso base:** Subconjunto unitário é considerado ordenado

                **Propriedades garantidas:**
                - Complexidade O(n log n) invariante para todos os casos
                - Estabilidade: preservação da ordem relativa de elementos equivalentes
                - Previsibilidade de desempenho
                - Determinismo no comportamento temporal
                """
            }
        ],
        "exemplo_visual": "",
        "complexidade": "O(n log n) garantido, com requisito de O(n) memória adicional",
        "quando_usar": "Quando se requer garantia de O(n log n) ou estabilidade é requisito crítico",
        "curiosidade": "Constitui a base do algoritmo Timsort utilizado em Python"
    },
    "Quick Sort": {
        "estrategia": "Particionamento por Pivô",
        "emoji": "⚡",
        "analogia_principal": "Particionamento recursivo baseado em elemento pivô",
        "analogias": [
            {
                "titulo": "Particionamento e Recursão",
                "descricao": """
                **Mecanismo do algoritmo:**
                1. Seleção de elemento pivô (estratégia: mediana de três)
                2. Particionamento: elementos menores à esquerda, maiores à direita
                3. Aplicação recursiva em cada partição
                4. Caso base: partição unitária

                **Otimizações implementadas:**
                - **Mediana de três:** mitigação do pior caso para dados ordenados
                - **Insertion Sort híbrido:** transição para partições pequenas (n < 10)
                - **Tail call optimization:** limitação da profundidade de recursão
                - Redução do overhead para subconjuntos pequenos
                """
            }
        ],
        "exemplo_visual": "",
        "complexidade": "O(n log n) caso médio, O(n²) pior caso (raro com otimizações)",
        "quando_usar": "Uso geral - melhor desempenho prático para dados aleatórios",
        "curiosidade": "Algoritmo predominante em bibliotecas padrão de diversas linguagens"
    },
    "Shell Sort": {
        "estrategia": "Insertion Sort com Gaps Decrescentes",
        "emoji": "🐚",
        "analogia_principal": "Generalização do Insertion Sort com intervalos variáveis",
        "analogias": [
            {
                "titulo": "Ordenação por Intervalos Decrescentes",
                "descricao": """
                **Estrutura do algoritmo:**
                1. Generalização do Insertion Sort
                2. Comparações entre elementos separados por intervalo (gap)
                3. Redução progressiva do gap (sequência de Knuth: 1, 4, 13, 40, ...)
                4. Convergência para gap=1 (equivalente ao Insertion Sort padrão)

                **Vantagem de desempenho:**
                - Movimentação de elementos através de longas distâncias
                - Arranjo progressivamente pré-ordenado
                - Eficiência do Insertion Sort final (gap=1) em dados quase ordenados
                - Redução substancial de inversões antes da passagem final
                """
            }
        ],
        "exemplo_visual": "",
        "complexidade": "O(n^1.5) utilizando sequência de Knuth",
        "quando_usar": "Alternativa in-place eficiente sob restrições de memória",
        "curiosidade": "Desenvolvido em 1959, permanece relevante como alternativa eficiente"
    }
}
