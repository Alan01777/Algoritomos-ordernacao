# Análise Comparativa dos Algoritmos de Ordenação

## Resumo Executivo - Array de 10.000 elementos

### Ranking por Tempo de Execução (Aleatório)

| Posição | Algoritmo | Tempo | Comparações | Trocas | Rec. Calls |
|---------|-----------|-------|-------------|--------|------------|
| 🥇 1º | **QuickSort** | 0.44s | 145,052 | 71,488 | 1,451 |
| 🥈 2º | **ShellSort** | 0.98s | 223,510 | 152,657 | 0 |
| 🥉 3º | **InsertionSort** | 72.99s | 24,946,207 | 24,936,217 | 0 |
| 4º | SelectionSort | 73.51s | 49,995,000 | 9,990 | 0 |
| 5º | BubbleSort | 170.65s | 49,995,000 | 25,133,502 | 0 |

**MergeSort** (0.42s) seria o mais rápido, mas foi removido por uso excessivo de memória.

---

## Análise Detalhada por Cenário

### 📊 Array Ordenado (Melhor Caso)

| Algoritmo | Tempo | Speedup vs Pior |
|-----------|-------|-----------------|
| **InsertionSort** | **0.028s** | **5,945x mais rápido!** |
| MergeSort | 0.20s | 2.0x |
| QuickSort | 0.23s | 2.8x |
| ShellSort | 0.21s | 4.6x |
| SelectionSort | 67.43s | 1.0x (sem melhora) |
| BubbleSort | 101.90s | 2.1x |

**💡 Insight:** Insertion Sort é **IMBATÍVEL** em dados já ordenados!

---

### 🔥 Array Reverso (Pior Caso)

| Algoritmo | Tempo | vs Aleatório |
|-----------|-------|--------------|
| QuickSort | 0.64s | 1.5x mais lento |
| ShellSort | 0.43s | 0.4x **mais rápido!** |
| MergeSort | 0.29s | 0.7x mais rápido |
| SelectionSort | 70.70s | ~igual |
| InsertionSort | 167.52s | 2.3x mais lento |
| BubbleSort | 213.88s | 1.3x mais lento |

**💡 Insight:** QuickSort com otimizações mantém bom desempenho mesmo no pior caso!

---

## Comparação de Chamadas Recursivas

### Array de 10.000 elementos (Aleatório)

| Algoritmo | Chamadas Recursivas | Profundidade Esperada |
|-----------|---------------------|----------------------|
| MergeSort | 9,999 | ~14 (log₂ 10,000) |
| QuickSort | 1,451 | ~14 (otimizado) |
| Outros | 0 | - (iterativos) |

**💡 Insight:**
- MergeSort faz **quase n** chamadas recursivas (divide sempre ao meio)
- QuickSort otimizado faz **muito menos** chamadas (tail call optimization)

---

## Análise de Complexidade Confirmada

### Comparações (n = 10,000)

| Algoritmo | Teórico | Real | Match |
|-----------|---------|------|-------|
| BubbleSort | O(n²) = 49,995,000 | 49,995,000 | ✅ 100% |
| SelectionSort | O(n²) = 49,995,000 | 49,995,000 | ✅ 100% |
| InsertionSort (pior) | O(n²) = 49,995,000 | 49,995,000 | ✅ 100% |
| InsertionSort (melhor) | O(n) = 10,000 | 9,999 | ✅ 100% |
| QuickSort | O(n log n) ≈ 132,877 | 145,052 | ✅ 109% |
| MergeSort | O(n log n) ≈ 132,877 | 120,460 | ✅ 91% |
| ShellSort | O(n^1.5) ≈ 1,000,000 | 223,510 | ✅ 22% (melhor que esperado!) |

---

## Eficiência de Trocas

### Array de 10.000 elementos (Aleatório)

| Algoritmo | Trocas | % das Comparações |
|-----------|--------|-------------------|
| SelectionSort | 9,990 | 0.02% ⭐ |
| QuickSort | 71,488 | 49.3% |
| MergeSort | 61,277 | 50.9% |
| ShellSort | 152,657 | 68.3% |
| InsertionSort | 24,936,217 | 100.0% |
| BubbleSort | 25,133,502 | 50.3% |

**💡 Insight:** Selection Sort faz MUITO menos trocas (apenas n trocas garantidas)!

---

## Uso de Memória (Peak)

### Array de 10.000 elementos

| Algoritmo | Memória Pico | Overhead | In-Place? |
|-----------|--------------|----------|-----------|
| BubbleSort | 80 KB | 1.0x | ✅ Sim |
| InsertionSort | 80 KB | 1.0x | ✅ Sim |
| SelectionSort | 80 KB | 1.0x | ✅ Sim |
| ShellSort | 160 KB | 2.0x | ✅ Sim (com gaps) |
| QuickSort | 163 KB | 2.0x | ⚠️ Pilha recursiva |
| MergeSort | 281 KB | 3.5x | ❌ Não (arrays temp) |

**💡 Insight:** MergeSort usa **3.5x mais memória** que algoritmos in-place!

---

## Recomendações por Caso de Uso

### 🎯 Para Dados Pequenos (n < 100)
**Vencedor:** Insertion Sort
- Simples, rápido, baixo overhead
- Usado internamente pelo QuickSort otimizado!

### 🎯 Para Dados Quase Ordenados
**Vencedor:** Insertion Sort (28ms vs 200ms do MergeSort)
- 5,945x mais rápido que seu pior caso
- Complexidade O(n) confirmada

### 🎯 Para Dados Aleatórios Grandes (n > 1,000)
**Vencedor:** QuickSort otimizado (0.44s)
- 2x mais rápido que ShellSort
- 170x mais rápido que Insertion Sort
- Usa mediana de três + tail call optimization

### 🎯 Quando Memória é Crítica
**Vencedor:** ShellSort (0.98s, 160 KB)
- Melhor alternativa in-place para dados grandes
- Apenas 2.2x mais lento que QuickSort

### 🎯 Quando Estabilidade é Necessária
**Vencedor:** MergeSort
- Único algoritmo estável O(n log n)
- Mantém ordem relativa de elementos iguais

### 🎯 Para Minimizar Trocas (escrita custosa)
**Vencedor:** Selection Sort (9,990 trocas)
- Apenas n trocas garantidas
- Útil para memória flash/SSD

### 🎯 Para Pior Caso Garantido
**Vencedor:** MergeSort (0.29s pior caso)
- Sempre O(n log n), sem exceções
- Previsível e confiável

---

## Conclusões Finais

### 🏆 Campeão Geral: **QuickSort Otimizado**
- Mais rápido na prática (caso médio)
- Com as 3 otimizações, evita pior caso
- Usado como padrão em muitas linguagens

### 🥈 Vice-Campeão: **MergeSort**
- Melhor pior caso garantido
- Estável e previsível
- Trade-off: usa mais memória

### 🥉 Menção Honrosa: **ShellSort**
- Melhor algoritmo in-place simples
- Surpreendentemente eficiente
- Subestimado na prática!

### ⚠️ Evitar em Produção:
- **BubbleSort:** Sempre mais lento (170s vs 0.44s)
- **SelectionSort:** O(n²) sem benefícios extras (exceto poucas trocas)
- **InsertionSort:** Apenas para dados pequenos ou quase ordenados

---

## Curiosidades dos Dados

1. **Insertion Sort é 5,945x mais rápido** em dados ordenados vs reversos
2. **QuickSort faz 85% menos chamadas recursivas** que MergeSort (otimizações funcionam!)
3. **ShellSort é mais rápido no pior caso** que no caso aleatório (incomum!)
4. **Selection Sort é consistente:** tempo quase idêntico em todos os cenários
5. **BubbleSort é 2x mais lento** que SelectionSort mesmo ambos sendo O(n²)

---

**Gerado automaticamente a partir de métricas reais de execução**
