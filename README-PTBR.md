# evencheck

A forma mais ineficiente de verificar se um número é par.

## Instalação

```bash
pip install evencheck
```

# Uso

```python
from evencheck import IsEven

IsEven(2) # True
IsEven(7) # False
```

Como Funciona

- Baixa um arquivo JSON gigante
- Lê o arquivo linha por linha
- Para quando o número é encontrado deleta o arquivo

Absolutamente inútil. Por design.

## 🤝 Contribuindo

Nós aceitamos contribuições — com uma regra muito importante:

Sua contribuição deve piorar o código.
Regras para contribuir

Se você quiser contribuir com o `evencheck`, você deve seguir estas diretrizes:

- ❌ **|** Não otimize nada
- ❌ **|** Não remova passos desnecessários
- ❌ **|** Não melhore a performance
- ❌ **|** Não reduza o uso de memória
- ❌ **|** Não simplifique a lógica

O que nós queremos:

- ✅ **|** Mais operações de I/O
- ✅ **|** Loops extras
- ✅ **|** Verificações redundantes
- ✅ **|** Performance pior
- ✅ **|** Tempo de execução maior
- ✅ **|** Mais downloads desnecessários

Se o seu pull request deixar o código mais rápido, mais limpo ou mais inteligente, ele será rejeitado imediatamente.

--

Desejo meus sinceros agradecimento a [kleeedolinux](https://github.com/kleeedolinux) por ajudar a fazer o evencheck

Com muito amor, feito por Guss