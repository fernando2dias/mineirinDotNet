# :bug: Linguagem: Mineirin.Net :beetle:

## Facens - Engenharia da Computação

### Disciplina de Compiladores

- Prof. André Carneiro Breda

- Fernando Dias Motta - RA 180016
- Kennedy Corrêa - RA 160080

## Função principal

- Funcao principal para iniciar um sistema escrito em Mineirin.Net.

```
Trem(
    //Prosa// Impletar funcao principal
)
```

## Operadores aritméticos, relacionais e lógicos

- Operador aritimetico de soma

```
"+.+"

//Prosa// Exemplo
40+.+50

```

- Operador aritimetico de subtracao

```
"-.-"

//Prosa// Exemplo
10-.-5

```

- Operdador aritimetico de divisao

```
"/./"

//Prosa// Exemplo
10/./2

```

- Operador aritimetico de multiplicacao

```
"*.*"

//Prosa// Exemplo
5*.*5

```

- Operador aritimetico de potencia

```
"**.**"

//Prosa// Exemplo
5**.**2

```

- Operador aritimetico de modulo

```
"%.%"

//Prosa// Exemplo
5%.%2

```

- Operador relacional de Equal

```
"=.="
//Prosa// Exemplo
a =.= b
```

- Operador relacional de Diferent

```
"\./"
//Prosa// Exemplo
a \./ b
```

- Operador relacional de Minor

```
"<.<"
//Prosa// Exemplo
a <.< b
```

- Operador relacional de Major

```
">.>"
//Prosa// Exemplo
a <.< b
```

- Operador relacional de Major Equal

```
">.="
//Prosa// Exemplo
a >.= b
```

- Operador relacional de Minor Equal

```
"<.="
//Prosa// Exemplo
a <.= b
```

- Operador lógico de And

```
"=.="
//Prosa// Exemplo
a =.= b
```

- Operador lógico de Or

```
"ˆ.ˆ"
//Prosa// Exemplo
a \./ b
```

- Operador lógico de Not

```
"!.!"
//Prosa// Exemplo
!.!(a == b)
```

## Declaração de variável

- atribuição de valor à variável

```
#intero numero1 .= 56

#quebradin numero2 .= 5,2

#trenzinDeChar .= "frase bem legal"

#charzin .= 'a'
```

## Estrutura(s) de repetição

```
">.>"
//Prosa// Exemplo
a <.< b
```

- Operador relacional de Major Equal

```
 if = "TemBase(<condição>)"

 else = "TemGaioNao"
```

- Operador relacional de Minor Equal

```
"<.="
//Prosa// Exemplo
a <.= b
```

## Exercícios

**1)** Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

**Entrada**

O arquivo de entrada contém 2 valores com uma casa decimal cada um.

**Saída**

Imprima a mensagem "MEDIA" e a média do aluno conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade. Utilize variáveis de dupla precisão (double) e como todos os problemas, não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

| Exemplos de entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 5.0                 | MEDIA = 6.43182   |
| 7.1                 |

**2)** Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

**Entrada**
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

**Saída**
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.

| Exemplos de entrada | Exemplos de Saída  |
| ------------------- | ------------------ |
| 25                  | NUMBER = 25        |
| 100                 | SALARY = U$ 550.00 |
| 5.50                |

**3)** Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.

**Entrada**
A primeira linha da entrada contém um valor inteiro N(N < 10000) que indica o número de casos de teste. Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).

**Saída**
Para cada caso, imprima uma mensagem correspondente, de acordo com o exemplo abaixo. Todas as letras deverão ser maiúsculas e sempre deverá haver um espaço entre duas palavras impressas na mesma linha.

| Exemplos de entrada | Exemplos de Saída |
| ------------------- | ----------------- |
| 4                   | ODD NEGATIVE      |
| -5                  | NULL              |
| 0                   | ODD POSITIVE      |
| 3                   | EVEN NEGATIVE     |
| -4                  |
