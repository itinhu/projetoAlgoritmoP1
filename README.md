# Projeto de Algoritmos – Primeira Etapa

## Descrição do projeto

A avaliação da segunda unidade da disciplina será realizada por meio do
desenvolvimento, em **Python**, de um sistema para gerenciar uma clínica
odontológica. Renê comprou uma clínica que será utilizada por diversos
dentistas, e o sistema deverá apoiar tanto a administração da clínica quanto o
atendimento aos pacientes.

O sistema será executado em terminal/linha de comando, com menus numéricos
interativos, e utilizará listas para armazenar os dados em memória.

## Objetivo

O sistema deve apresentar um menu inicial para que a pessoa escolha entre
acessar o módulo de paciente ou o módulo de administração/secretaria. A
navegação entre os módulos deve ser clara, e as regras de agendamento devem
impedir conflitos de horários para um mesmo dentista.

## Requisitos gerais

- **Linguagem:** Python.
- **Interface:** somente terminal/linha de comando, com menus numéricos
  interativos.
- **Estrutura de dados:** listas para armazenamento em memória.
- **Módulos:** paciente e administração/secretaria, acessíveis pelo menu inicial.

## Módulo do paciente

O acesso é feito por meio da inserção do CPF. Caso o CPF não esteja cadastrado,
o sistema deve permitir o autocadastro com nome, CPF, senha e telefone.

Após entrar no sistema, o paciente poderá:

- **Ver o corpo clínico:** listar todos os dentistas disponíveis e suas
  especialidades, como Ortodontia, Facetas em resina composta e Endodontia.
- **Agendar consulta:** escolher um dentista, um dia e um horário desejado.
- **Consultar minhas consultas:** listar somente os agendamentos futuros
  associados ao CPF do paciente autenticado.
- **Cancelar consulta:** desmarcar um de seus próprios agendamentos.

### Regra de agendamento

O sistema deve bloquear o agendamento quando o dentista escolhido já tiver uma
consulta no dia e horário selecionados. Assim, não pode haver conflito de
horários para um mesmo dentista.

## Módulo da secretaria/administração

O acesso à administração é protegido por login e senha. A secretaria poderá
gerenciar os dados e a agenda da clínica.

### Gestão de dentistas (CRUD)

Permitir cadastrar, listar, buscar, atualizar e remover dentistas. Cada
dentista deve possuir:

- ID;
- nome;
- CRO;
- especialidade.

### Gestão de consultórios

Permitir cadastrar salas, como Sala 1 e Sala 2, e vincular os dentistas que
atendem em cada uma delas.

### Gestão de pacientes (CRUD completo)

A secretaria poderá listar todos os pacientes, buscar pacientes por nome ou
CPF, atualizar seus dados cadastrais e adicionar observações ou alergias. Essa
gestão é mais ampla que as opções disponíveis ao paciente, que acessa apenas
seus próprios dados.

### Gestão da agenda geral

Permitir:

- visualizar todas as consultas da clínica;
- filtrar os agendamentos por dentista;
- filtrar os agendamentos por data;
- cancelar consultas de qualquer paciente, quando necessário.

## Resumo dos módulos

| Módulo | Acesso | Funcionalidades principais |
| --- | --- | --- |
| Paciente | CPF e senha; autocadastro quando não houver cadastro | Consultar corpo clínico, agendar, ver consultas futuras e cancelar consultas próprias |
| Administração/secretaria | Login e senha | Gerenciar dentistas, consultórios e pacientes; visualizar, filtrar e cancelar consultas |
