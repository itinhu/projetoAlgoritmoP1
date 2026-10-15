dentistas = []
consultorios = []
pacientes = []
consultas = []

id_dentista = id_consultorio = id_consulta = 1
while True:
    print("\n=== CLINICA ODONTOLOGICA ===")
    print("1 - Paciente")
    print("2 - Administracao")
    print("0 - Sair")

    opcao = input("Opcao: ")

    if opcao == "0":
        break

    elif opcao == "1":
        cpf = input("Digite seu CPF (11 numeros): ")

        while True:
            if len(cpf) == 11 and all("0" <= c <= "9" for c in cpf):
                break
            cpf = input("CPF invalido. Digite os 11 numeros: ")

        paciente_atual = next((p for p in pacientes if p[1] == cpf), False)
        if paciente_atual == False:
            print("\nPaciente nao encontrado. Faca seu cadastro.")
            paciente_atual = [
                input("Nome: "), cpf, input("Crie uma senha: "),
                input("Telefone: "), ""
            ]
            pacientes.append(paciente_atual)
            print("Cadastro realizado com sucesso!")
        else:
            if input("Senha: ") != paciente_atual[2]:
                print("Senha incorreta.")
                continue

        while True:
            print("\n=== MENU DO PACIENTE ===")
            print("1 - Ver dentistas")
            print("2 - Agendar consulta")
            print("3 - Minhas consultas")
            print("4 - Cancelar consulta")
            print("0 - Voltar")

            opcao_paciente = input("Opcao: ")

            if opcao_paciente == "0":
                break

            elif opcao_paciente == "1":
                if not dentistas:
                    print("Nenhum dentista cadastrado.")
                else:
                    print("\n=== DENTISTAS DISPONIVEIS ===")
                    for dentista in dentistas:
                        print(f"ID: {dentista[0]} | Nome: {dentista[1]} | Especialidade: {dentista[3]}")

            elif opcao_paciente == "2":
                if len(dentistas) == 0:
                    print("Nao existem dentistas cadastrados.")
                    continue

                print("\n=== DENTISTAS ===")
                for dentista in dentistas:
                    print(f"ID: {dentista[0]} | Nome: {dentista[1]} | Especialidade: {dentista[3]}")

                escolha = input("Digite o ID do dentista: ")
                dentista_escolhido = next(
                    (d for d in dentistas if str(d[0]) == escolha), False
                )
                if dentista_escolhido == False:
                    print("Dentista nao encontrado.")
                    continue

                salas_disponiveis = [
                    s for s in consultorios if dentista_escolhido[0] in s[2]
                ]
                if len(salas_disponiveis) == 0:
                    print("Esse dentista nao possui consultorio vinculado.")
                    continue

                print("\n=== CONSULTORIOS DO DENTISTA ===")
                for sala in salas_disponiveis:
                    print(f"ID: {sala[0]} | {sala[1]}")

                escolha_sala = input("ID do consultorio: ")
                sala_escolhida = next(
                    (s for s in salas_disponiveis if str(s[0]) == escolha_sala),
                    False
                )
                if sala_escolhida == False:
                    print("Consultorio invalido.")
                    continue

                while True:
                    data = input("Data (DD/MM/AAAA): ")
                    data_valida = (
                        len(data) == 10 and data[2] == "/" and data[5] == "/"
                        and all("0" <= data[i] <= "9" for i in (0, 1, 3, 4, 6, 7, 8, 9))
                    )
                    if data_valida:
                        dia, mes, ano = int(data[:2]), int(data[3:5]), int(data[6:])
                        data_valida = 1 <= dia <= 31 and 1 <= mes <= 12 and ano >= 2026
                    if data_valida:
                        break
                    print("Data invalida. Use DD/MM/AAAA.")

                while True:
                    horario = input("Horario (HH:MM): ")
                    horario_valido = (
                        len(horario) == 5 and horario[2] == ":"
                        and all("0" <= horario[i] <= "9" for i in (0, 1, 3, 4))
                    )
                    if horario_valido:
                        hora, minuto = int(horario[:2]), int(horario[3:])
                        horario_valido = 0 <= hora <= 23 and 0 <= minuto <= 59
                    if horario_valido:
                        break
                    print("Horario invalido. Use HH:MM.")

                conflito = any(
                    c[3] == data and c[4] == horario
                    and (c[2] == dentista_escolhido[0]
                         or c[5] == sala_escolhida[0] or c[1] == cpf)
                    for c in consultas
                )
                if conflito:
                    print(
                        "Horario indisponivel. "
                        "O dentista, consultorio ou paciente "
                        "ja possui uma consulta nesse horario."
                    )

                else:
                    consultas.append([
                        id_consulta, cpf, dentista_escolhido[0], data,
                        horario, sala_escolhida[0]
                    ])
                    print(f"Consulta agendada com sucesso! Numero: {id_consulta}")
                    id_consulta += 1

            elif opcao_paciente == "3":
                print("\n=== MINHAS CONSULTAS ===")
                minhas_consultas = [c for c in consultas if c[1] == cpf]
                for consulta in minhas_consultas:
                    dentista = next(
                        (d for d in dentistas if d[0] == consulta[2]), False
                    )
                    sala = next(
                        (s for s in consultorios if s[0] == consulta[5]), False
                    )
                    nome_dentista = dentista[1] if dentista else "Nao encontrado"
                    nome_sala = sala[1] if sala else "Nao encontrada"
                    print(
                        f"Consulta {consulta[0]} | Data: {consulta[3]} | "
                        f"Horario: {consulta[4]} | Dentista: {nome_dentista} | "
                        f"Consultorio: {nome_sala}"
                    )
                if not minhas_consultas:
                    print("Voce nao possui consultas agendadas.")

            elif opcao_paciente == "4":
                minhas_consultas = [c for c in consultas if c[1] == cpf]
                if not minhas_consultas:
                    print("Voce nao possui consultas para cancelar.")
                else:
                    print("\n=== MINHAS CONSULTAS ===")
                    for consulta in minhas_consultas:
                        print(f"Numero: {consulta[0]} | Data: {consulta[3]} | Horario: {consulta[4]}")
                    numero = input("Numero da consulta para cancelar: ")
                    consulta_escolhida = next(
                        (c for c in minhas_consultas if str(c[0]) == numero),
                        False
                    )
                    if consulta_escolhida == False:
                        print("Consulta nao encontrada.")

                    else:
                        consultas.remove(consulta_escolhida)
                        print("Consulta cancelada com sucesso.")

            else:
                print("Opcao invalida.")

    elif opcao == "2":

        login = input("Login administrativo: ")
        senha_admin = input("Senha administrativa: ")
        if login != "admin" or senha_admin != "admin123":
            print("Login ou senha incorretos.")
            continue

        while True:
            print("\n=== ADMINISTRACAO ===")
            print("1 - Gerenciar dentistas")
            print("2 - Gerenciar consultorios")
            print("3 - Gerenciar pacientes")
            print("4 - Agenda geral")
            print("0 - Voltar")

            opcao_admin = input("Opcao: ")

            if opcao_admin == "0":
                break

            elif opcao_admin == "1":
                print("\n=== DENTISTAS ===")
                print("1 - Cadastrar")
                print("2 - Listar")
                print("3 - Buscar")
                print("4 - Atualizar")
                print("5 - Remover")

                acao = input("Opcao: ")

                if acao == "1":
                    dentistas.append([
                        id_dentista, input("Nome: "), input("CRO: "),
                        input("Especialidade: ")
                    ])
                    print(f"Dentista cadastrado com ID {id_dentista}.")
                    id_dentista += 1

                elif acao == "2":
                    if not dentistas:
                        print("Nenhum dentista cadastrado.")
                    for dentista in dentistas:
                        print(f"ID: {dentista[0]} | Nome: {dentista[1]} | CRO: {dentista[2]} | Especialidade: {dentista[3]}")

                elif acao == "3":
                    numero = input("ID do dentista: ")
                    escolhido = next(
                        (d for d in dentistas if str(d[0]) == numero), False
                    )
                    if escolhido == False:
                        print("Dentista nao encontrado.")
                    else:
                        print(f"ID: {escolhido[0]}")
                        print(f"Nome: {escolhido[1]}")
                        print(f"CRO: {escolhido[2]}")
                        print(f"Especialidade: {escolhido[3]}")

                elif acao == "4":
                    numero = input("ID do dentista: ")
                    escolhido = next(
                        (d for d in dentistas if str(d[0]) == numero), False
                    )
                    if escolhido == False:
                        print("Dentista nao encontrado.")

                    else:
                        nome = input(
                            f"Nome atual [{escolhido[1]}]. "
                            "Novo nome (Enter mantem): "
                        )

                        cro = input(
                            f"CRO atual [{escolhido[2]}]. "
                            "Novo CRO (Enter mantem): "
                        )

                        especialidade = input(
                            f"Especialidade atual [{escolhido[3]}]. "
                            "Nova especialidade (Enter mantem): "
                        )

                        if nome != "":
                            escolhido[1] = nome

                        if cro != "":
                            escolhido[2] = cro

                        if especialidade != "":
                            escolhido[3] = especialidade

                        print("Dentista atualizado.")

                elif acao == "5":
                    numero = input("ID do dentista: ")
                    escolhido = next(
                        (d for d in dentistas if str(d[0]) == numero), False
                    )
                    if escolhido == False:
                        print("Dentista nao encontrado.")

                    else:
                        ocupado = any(c[2] == escolhido[0] for c in consultas)
                        if ocupado:
                            print(
                                "Nao e possivel remover esse dentista. "
                                "Existem consultas vinculadas a ele."
                            )

                        else:
                            for sala in consultorios:
                                while escolhido[0] in sala[2]:
                                    sala[2].remove(escolhido[0])
                            dentistas.remove(escolhido)
                            print("Dentista removido.")

                else:
                    print("Opcao invalida.")

            elif opcao_admin == "2":
                print("\n=== CONSULTORIOS ===")
                print("1 - Cadastrar consultorio")
                print("2 - Listar consultorios")
                print("3 - Vincular dentista")
                print("4 - Remover consultorio")

                acao = input("Opcao: ")

                if acao == "1":
                    consultorios.append(
                        [id_consultorio, input("Nome do consultorio: "), []]
                    )
                    print(f"Consultorio cadastrado com ID {id_consultorio}.")
                    id_consultorio += 1

                elif acao == "2":
                    if not consultorios:
                        print("Nenhum consultorio cadastrado.")
                    for sala in consultorios:
                        print(f"ID: {sala[0]} | Nome: {sala[1]} | Dentistas vinculados: {sala[2]}")

                elif acao == "3":
                    sala_id = input("ID do consultorio: ")
                    dentista_id = input("ID do dentista: ")

                    sala_escolhida = next(
                        (s for s in consultorios if str(s[0]) == sala_id), False
                    )
                    dentista_escolhido = next(
                        (d for d in dentistas if str(d[0]) == dentista_id), False
                    )
                    if (
                        sala_escolhida == False
                        or dentista_escolhido == False
                    ):
                        print("Consultorio ou dentista nao encontrado.")

                    elif dentista_escolhido[0] in sala_escolhida[2]:
                        print("Esse dentista ja esta vinculado.")

                    else:
                        sala_escolhida[2].append(dentista_escolhido[0])
                        print("Dentista vinculado ao consultorio.")

                elif acao == "4":
                    sala_id = input("ID do consultorio: ")
                    sala_escolhida = next(
                        (s for s in consultorios if str(s[0]) == sala_id), False
                    )
                    if sala_escolhida == False:
                        print("Consultorio nao encontrado.")

                    else:
                        sala_ocupada = any(
                            c[5] == sala_escolhida[0] for c in consultas
                        )
                        if sala_ocupada:
                            print(
                                "Nao e possivel remover o consultorio. "
                                "Existem consultas vinculadas a ele."
                            )

                        else:
                            consultorios.remove(sala_escolhida)
                            print("Consultorio removido.")

                else:
                    print("Opcao invalida.")

            elif opcao_admin == "3":
                print("\n=== PACIENTES ===")
                print("1 - Listar todos")
                print("2 - Buscar por nome ou CPF")
                print("3 - Atualizar paciente")
                print("4 - Remover paciente")

                acao = input("Opcao: ")

                if acao == "1":
                    if not pacientes:
                        print("Nenhum paciente cadastrado.")
                    for paciente in pacientes:
                        print(f"Nome: {paciente[0]} | CPF: {paciente[1]} | Telefone: {paciente[3]} | Observacoes: {paciente[4]}")

                elif acao == "2":
                    termo = input("Digite o nome ou CPF: ")
                    encontrados = [
                        p for p in pacientes
                        if p[1] == termo or termo.lower() in p[0].lower()
                    ]
                    for paciente in encontrados:
                        print(f"Nome: {paciente[0]} | CPF: {paciente[1]} | Telefone: {paciente[3]} | Observacoes: {paciente[4]}")
                    if not encontrados:
                        print("Nenhum paciente encontrado.")

                elif acao == "3":
                    cpf_busca = input("CPF do paciente: ")
                    escolhido = next(
                        (p for p in pacientes if p[1] == cpf_busca), False
                    )
                    if escolhido == False:
                        print("Paciente nao encontrado.")

                    else:
                        nome = input(
                            f"Nome atual [{escolhido[0]}]. "
                            "Novo nome (Enter mantem): "
                        )

                        telefone = input(
                            f"Telefone atual [{escolhido[3]}]. "
                            "Novo telefone (Enter mantem): "
                        )

                        senha_nova = input(
                            "Nova senha (Enter mantem a atual): "
                        )

                        observacoes = input(
                            "Observacoes/alergias (Enter mantem): "
                        )

                        if nome != "":
                            escolhido[0] = nome

                        if telefone != "":
                            escolhido[3] = telefone

                        if senha_nova != "":
                            escolhido[2] = senha_nova

                        if observacoes != "":
                            escolhido[4] = observacoes

                        print("Paciente atualizado.")

                elif acao == "4":
                    cpf_busca = input("CPF do paciente: ")
                    escolhido = next(
                        (p for p in pacientes if p[1] == cpf_busca), False
                    )
                    if escolhido == False:
                        print("Paciente nao encontrado.")

                    else:
                        consultas = [c for c in consultas if c[1] != escolhido[1]]
                        pacientes.remove(escolhido)
                        print("Paciente removido e suas consultas foram canceladas.")

                else:
                    print("Opcao invalida.")

            elif opcao_admin == "4":
                print("\n=== AGENDA GERAL ===")
                print("1 - Todas as consultas")
                print("2 - Filtrar por dentista")
                print("3 - Filtrar por data")
                print("4 - Cancelar consulta")

                acao = input("Opcao: ")

                if acao == "1":
                    filtro = ""
                elif acao == "2":
                    filtro = input("ID do dentista: ")
                elif acao == "3":
                    filtro = input("Data (DD/MM/AAAA): ")
                elif acao == "4":
                    filtro = ""
                else:
                    print("Opcao invalida.")
                    continue

                if acao != "4":
                    consultas_filtradas = [
                        c for c in consultas
                        if (acao != "2" or str(c[2]) == filtro)
                        and (acao != "3" or c[3] == filtro)
                    ]
                    for consulta in consultas_filtradas:
                        paciente = next(
                            (p for p in pacientes if p[1] == consulta[1]), False
                        )
                        dentista = next(
                            (d for d in dentistas if d[0] == consulta[2]), False
                        )
                        sala = next(
                            (s for s in consultorios if s[0] == consulta[5]), False
                        )
                        nome_paciente = paciente[0] if paciente else "Nao encontrado"
                        nome_dentista = dentista[1] if dentista else "Nao encontrado"
                        nome_sala = sala[1] if sala else "Nao encontrada"
                        print(f"Consulta: {consulta[0]} | Data: {consulta[3]} | Horario: {consulta[4]}")
                        print(f"Paciente: {nome_paciente} | CPF: {consulta[1]}")
                        print(f"Dentista: {nome_dentista} | Consultorio: {nome_sala}")
                        print("------------------------------")
                    if not consultas_filtradas:
                        print("Nenhuma consulta encontrada.")
                else:
                    numero = input("Numero da consulta para cancelar: ")
                    escolhida = next(
                        (c for c in consultas if str(c[0]) == numero), False
                    )
                    if escolhida == False:
                        print("Consulta nao encontrada.")

                    else:
                        consultas.remove(escolhida)
                        print("Consulta cancelada pelo administrador.")

            else:
                print("Opcao invalida.")

    else:
        print("Opcao invalida.")

print("\nSistema encerrado.")