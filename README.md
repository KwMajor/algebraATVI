## Determinante de matriz 3x3 por triangularização (Álgebra – ATVI)

Este projeto calcula o determinante de uma matriz 3x3 a partir dos valores digitados pelo usuário, usando eliminação de Gauss (transformação em matriz triangular superior) e controle de trocas de linhas para ajustar o sinal do determinante.

Arquivo principal: `main.py`

---

## Visão geral

- Entrada: 9 números reais correspondentes aos elementos de uma matriz 3x3 (linha a linha).
- Processo: eliminações por linha para obter uma matriz triangular superior, registrando trocas de linha quando um pivô é zero.
- Saída: a matriz triangular superior resultante e o valor do determinante.

Observação: o determinante de uma matriz triangular é o produto de seus elementos na diagonal principal. Cada troca de linha muda o sinal do determinante.

$$\det(A) = (-1)^{\text{trocas}}\; \prod_{i=1}^{3} U_{ii}$$

---

## Pré-requisitos

- Python 3.8+ (recomendado 3.10 ou superior)
- NumPy

Instale as dependências com:

```powershell
pip install -r requirements.txt
```

---

## Como executar (Windows/PowerShell)

1) Clone/baixe o repositório e abra a pasta no terminal.

2) (Opcional, mas recomendado) Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) Instale as dependências:

```powershell
pip install -r requirements.txt
```

4) Execute o programa:

```powershell
python .\main.py
```

---

## Exemplo de uso

Entradas (matriz 3x3):

```
Digite os elementos da matriz 3x3:
Elemento [1,1]: 1
Elemento [1,2]: 2
Elemento [1,3]: 3
Elemento [2,1]: 0
Elemento [2,2]: 1
Elemento [2,3]: 4
Elemento [3,1]: 5
Elemento [3,2]: 6
Elemento [3,3]: 0
```

Saída (exemplo):

```
Matriz inserida:
[[1. 2. 3.]
 [0. 1. 4.]
 [5. 6. 0.]]

Matriz triangular superior:
[[ 1.  2.  3.]
 [ 0.  1.  4.]
 [ 0. -4. -15.]]

Determinante = 1.0
```

---

## Como o algoritmo funciona

1) Para cada coluna i, escolhe-se um pivô em `A[i, i]`. Se for 0, tenta-se trocar por uma linha abaixo que tenha elemento não nulo nessa coluna (contabilizando uma troca de linha).
2) Zera-se os elementos abaixo do pivô subtraindo um múltiplo da linha do pivô das linhas inferiores.
3) Ao final, a matriz está em forma triangular superior `U`.
4) O determinante é o produto dos elementos da diagonal principal de `U` ajustado por `(-1)^{trocas}`.

Notas importantes:
- Esta implementação não faz pivotamento parcial total (apenas troca quando o pivô é zero). Para maior estabilidade numérica, poderia-se escolher o maior pivô absoluto disponível na coluna.
- Como não há escalonamento de linhas (apenas somas/múltiplos), o produto da diagonal de `U` preserva o valor do determinante, exceto pelo sinal ajustado pelas trocas.

---

## Validação (opcional)

Você pode comparar com o resultado de `numpy.linalg.det` (atenção a pequenas diferenças numéricas):

```python
import numpy as np
A = np.array([[1,2,3],[0,1,4],[5,6,0]], dtype=float)
print(np.linalg.det(A))  # ~ 1.0
```

---

## Estrutura do projeto

- `main.py` — Script interativo que lê a matriz, triangulariza e calcula o determinante.
- `requirements.txt` — Dependências Python do projeto.
- `README.md` — Este guia.

---

## Licença

Uso acadêmico/educacional. Adapte conforme necessário para sua disciplina/curso.
