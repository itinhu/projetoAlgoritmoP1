# Guia de estudo — Sistema da clínica odontológica

Este guia explica como o programa de `main.py` funciona e destaca os conceitos
que você pode apresentar ao professor.

## 1. Visão geral

O programa é uma aplicação de terminal. Ele mostra um menu inicial e permite
escolher entre:

- **Paciente:** consultar dentistas, agendar e cancelar suas consultas.
- **Administração:** cadastrar e gerenciar dentistas, consultórios, pacientes
  e a agenda.

Os dados ficam guardados em listas enquanto o programa está aberto. Ao sair,
as listas são perdidas, porque o projeto ainda não usa arquivos ou banco de
dados.

## 2. Como os dados são organizados

Cada lista guarda registros em outra lista. Por exemplo, um dentista é
armazenado nesta ordem:

```python
[id, nome, cro, especialidade]
```

Os campos são acessados pela posição: `dentista[0]` é o ID,
`dentista[1]` é o nome, `dentista[2]` é o CRO e `dentista[3]` é a
especialidade.

Os outros registros seguem a mesma ideia:

| Lista | Conteúdo de cada registro |
| --- | --- |
| `dentistas` | ID, nome, CRO, especialidade |
| `consultorios` | ID, nome da sala, lista de IDs dos dentistas vinculados |
| `pacientes` | nome, CPF, senha, telefone, observações/alergias |
| `consultas` | ID, CPF do paciente, ID do dentista, data, horário, ID do consultório |

Os contadores `id_dentista`, `id_consultorio` e `id_consulta` geram IDs
sequenciais. Depois de cadastrar um item, o contador correspondente aumenta em
um.

## 3. Menus e controle do programa

O `while True` do início mantém o menu principal aberto até a opção de sair
executar `break`.

As escolhas são lidas com `input()` como textos. Por isso, o programa compara
opções com valores como `"1"` e `"2"`. Os blocos `if` e `elif` encaminham a
execução para a opção escolhida.

Há menus dentro de menus: por exemplo, o menu da administração abre as opções
de dentistas, consultórios, pacientes e agenda. Um `while True` mantém cada
menu aberto; `break` volta ao menu anterior e `continue` pula para a próxima
repetição do menu atual.

## 4. Acesso do paciente

O programa pede um CPF e percorre a lista `pacientes` para procurar esse
registro. Se encontrar, pede a senha. Se não encontrar, solicita nome, senha
e telefone e adiciona o novo paciente à lista.

O valor `False` é usado para indicar que uma busca ainda não encontrou um
registro. Quando encontra, a variável passa a guardar a própria lista do
registro. Por exemplo:

```python
paciente_atual = False
for paciente in pacientes:
    if paciente[1] == cpf:
        paciente_atual = paciente
        break
```

Assim, o programa não precisa usar `None`: `False` representa “não encontrado”
e uma lista representa “encontrado”.

## 5. Agendamento e conflito de horários

Para agendar, o paciente escolhe um dentista e um consultório vinculado a ele.
Depois informa a data e o horário.

O programa percorre `consultas` e compara a data e o horário com cada
agendamento existente. Se o horário for igual e o dentista **ou** o consultório
for o mesmo, marca `conflito = True` e não adiciona a consulta. Caso contrário,
cria um novo registro em `consultas`.

Em lógica simplificada, a regra é:

```text
mesma data e mesmo horário
E
(mesmo dentista OU mesmo consultório)
=> horário indisponível
```

O operador `and` exige que as duas condições sejam verdadeiras; o operador
`or` aceita que uma das duas condições seja verdadeira.

## 6. Consultas e cancelamentos

As consultas de um paciente são encontradas comparando o CPF guardado no
registro da consulta com o CPF informado no acesso. O paciente só pode cancelar
uma consulta que esteja nessa lista.

Na administração, a agenda percorre a mesma lista, mas pode mostrar todas as
consultas, filtrar por ID do dentista ou data, e cancelar uma consulta pelo ID.
Ao remover um paciente, as consultas associadas a esse CPF também são
removidas.

## 7. Administração

O módulo administrativo pede o login `admin` e a senha `admin123`. Para
encontrar registros por ID, o programa percorre a lista com um `for` e compara
o ID digitado com o primeiro campo do registro.

As opções para dentistas permitem cadastrar, listar, buscar, atualizar e
remover. Um dentista que tenha consultas não pode ser removido; primeiro é
necessário cancelar essas consultas. Os consultórios guardam os IDs dos
dentistas que atendem em cada sala. Na gestão de pacientes, a secretaria pode
listar, buscar, atualizar dados, registrar observações/alergias e remover um
paciente.

## 8. Por que não há funções ou `datetime`

O código foi mantido em um único arquivo e sem declarações `def`, conforme a
restrição do projeto. Cada fluxo está escrito diretamente dentro dos menus.

O programa também não usa `datetime`. Data e horário são tratados como textos,
por exemplo `"15/10/2026"` e `"14:30"`. Isso permite verificar se o mesmo texto
de data e horário já foi usado para aquele dentista ou consultório, mas não
permite validar automaticamente se a data existe ou se já passou. Por isso,
deve-se digitar a data no formato `DD/MM/AAAA` e o horário em `HH:MM`.

## 9. Limitações atuais

- Os dados não são preservados depois que o programa é encerrado.
- O login administrativo está fixo no código e é apenas para demonstração.
- O formato da data e do horário é informado ao usuário, mas não validado.
- Para a comparação de conflitos, data e horário precisam ser digitados sempre
  com o mesmo formato, incluindo zeros à esquerda, como `05/03/2027` e `09:00`.
- As consultas exibidas ao paciente são as consultas associadas ao CPF; sem
  `datetime`, o sistema não consegue separar automaticamente consultas futuras
  de consultas passadas.

## 10. Roteiro curto para apresentar

> “O programa usa listas para guardar dentistas, consultórios, pacientes e
> consultas durante a execução. Os menus são feitos com `while`, e as opções
> são controladas com `if` e `elif`. Para localizar um cadastro, percorro a
> lista com `for`. No agendamento, comparo data, horário, dentista e
> consultório com as consultas existentes para evitar conflito. Uso `False`
> como marcador de que uma busca não encontrou o registro. Não uso funções nem
> `datetime`, então os dados são temporários e a data é comparada como texto.”

## Execução

No terminal, dentro da pasta do projeto:

```bash
python main.py
```
