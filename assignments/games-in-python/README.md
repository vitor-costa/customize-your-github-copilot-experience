# 📘 Assignment: Hangman Game Challenge

## 🎯 Objetivo

Construa o clássico jogo da Forca (Hangman) usando Python. Os estudantes devem praticar manipulação de strings, estruturas de repetição, condicionais e entrada do usuário enquanto implementam a lógica do jogo.

## 📝 Tarefas

### 🛠️	Hangman — Jogo da Forca

#### Description
Implemente um programa em Python que permita ao jogador adivinhar letras de uma palavra escolhida aleatoriamente. O programa deve mostrar o progresso (por exemplo: _ a _ _ o), aceitar palpites do usuário, e terminar quando a palavra for completamente adivinhada ou quando as tentativas acabarem.

#### Requirements
Completed program should:

- Selecionar aleatoriamente uma palavra a partir de uma lista predefinida (mínimo 10 palavras)
- Aceitar palpites de letra do jogador (uma letra por vez) e atualizar a exibição do progresso com underscores e letras reveladas
- Rastrear letras já adivinhadas e impedir palpites repetidos sem penalidade ou informando o jogador
- Contabilizar e mostrar o número de tentativas incorretas restantes (por exemplo, 6 tentativas iniciais)
- Encerrar o jogo quando a palavra for completamente adivinhada (mensagem de vitória) ou quando as tentativas forem esgotadas (mensagem de derrota mostrando a palavra correta)
- Ser tolerante a maiúsculas/minúsculas (palpites podem ser em qualquer case)

#### Example
Exemplo de fluxo (exibição simplificada):

```
Palavra: _ a _ _ o
Tentativas restantes: 4
Letras já tentadas: a, e, i

Digite uma letra: n
Palavra: _ a n _ o
Tentativas restantes: 4

...
```
