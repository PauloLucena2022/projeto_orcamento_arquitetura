from time import sleep

print("Olá!!! Seja bem vindo(a) ao meu serviço de atendimento!")
print()
ref = ""
qua = ""
suite = ""
cor1 = ""
televisao = ""
guard_roup = ""
cabiceira = ""
cama = ""
a = ""
alt = ""
con = ""
cor = ""
while True:
    a = input("Você gostaria de fazer alguma mudança no seu quarto? [SIM/NAO]:").upper().strip()
    print("-=-" * 30)
    if a == "SIM": break
    elif a == "NAO": break
    else: continue
if a == "SIM":
    while a == "SIM":
        m = input("O que você gostaria de mudar no design?").upper().strip()
        print("-=-" * 30)
        idade = input("Esse quarto é específico para qual faixa etária? [Infantil,Adolescente,Adulto,Idoso]:").upper().strip()
        print("-=-" * 30)
        if idade == "INFANTIL":
            ref = input("Há algum desenho preferido,personagem ou até mesmo brinquedo? [SIM/NAO]:").upper().strip()
            if ref == "SIM":
              qua = input("Qual seria?:").upper().strip()
            print("-=-" * 30)
            cor = input("O(a) cliente possui uma cor favorita?[SIM/NAO]:").upper().strip()
            if cor == "SIM":
              cor1 = input("Qual seria?").upper().strip()
            print("-=-" * 30)
            print("Acerca dos móveis nesse compartimento:")
            televisao = input("Você gostaria de ter uma televisão?[SIM/NAO]:").upper().strip()
            guard_roup = input("Você gostaria de ter um guarda-roupa?[SIM/NAO]:").upper().strip()
            cama = input("Você gostaria de ter uma cama?[SIM/NAO]:").upper().strip()
            cabiceira = input("Você gostaria de ter uma cabeceira?[SIM/NAO]:").upper().strip()
            suite = input("O quarto será uma suíte?[SIM/NAO]:").upper().strip()
            if suite == "SIM":
              alt = input("Você gostaria de ter alguma alteração no seu banheiro também?[SIM/NAO]:").upper().strip()
        elif idade == "ADOLESCENTE":
            ref = input("Há alguma série preferida,personagem ou até mesmo filme? [SIM/NAO]:").upper().strip()
            if ref == "SIM":
              qua = input("Qual seria?:").upper().strip()
            print("-=-" * 30)
            cor = input("O(a) cliente possui uma cor favorita?[SIM/NAO]:").upper().strip()
            if cor == "SIM":
              cor1 = input("Qual seria?").upper().strip()
            print("-=-" * 30)
            print("Acerca dos móveis nesse compartimento:")
            televisao = input("Você gostaria de ter uma televisão?[SIM/NAO]:").upper().strip()
            guard_roup = input("Você gostaria de ter um guarda-roupa?[SIM/NAO]:").upper().strip()
            cama = input("Você gostaria de ter uma cama?[SIM/NAO]:").upper().strip()
            cabiceira = input("Você gostaria de ter uma cabeceira?[SIM/NAO]:").upper().strip()
            suite = input("O quarto será uma suíte?[SIM/NAO]:").upper().strip()
            if suite == "SIM":
              alt = input("Você gostaria de ter alguma alteração no seu banheiro também?[SIM/NAO]:").upper().strip()
        elif idade == "ADULTO":
            ref = input("Há alguma referência favorita? [SIM/NAO]:").upper().strip()
            if ref == "SIM":
              qua = input("Qual seria?:").upper().strip()
            print("-=-" * 30)
            cor = input("O(a) cliente possui uma cor favorita?[SIM/NAO]:").upper().strip()
            if cor == "SIM":
              cor1 = input("Qual seria?").upper().strip()
            print("-=-" * 30)
            print("Acerca dos móveis nesse compartimento:")
            televisao = input("Você gostaria de ter uma televisão?[SIM/NAO]:").upper().strip()
            guard_roup = input("Você gostaria de ter um guarda-roupa?[SIM/NAO]:").upper().strip()
            cama = input("Você gostaria de ter uma cama?[SIM/NAO]:").upper().strip()
            cabiceira = input("Você gostaria de ter uma cabeceira?[SIM/NAO]:").upper().strip()
            suite = input("O quarto será uma suíte?[SIM/NAO]:").upper().strip()
            if suite == "SIM":
              alt = input("Você gostaria de ter alguma alteração no seu banheiro também?[SIM/NAO]:").upper().strip()
        elif idade == "IDOSO":
            ref = input("Há alguma referência favorita? [SIM/NAO]:").upper().strip()
            if ref == "SIM":
              qua = input("Qual seria?:").upper().strip()
            print("-=-" * 30)
            cor = input("O(a) cliente possui uma cor favorita?[SIM/NAO]:").upper().strip()
            if cor == "SIM":
              cor1 = input("Qual seria?").upper().strip()
            print("-=-" * 30)
            print("Acerca dos móveis nesse compartimento:")
            televisao = input("Você gostaria de ter uma televisão?[SIM/NAO]:").upper().strip()
            guard_roup = input("Você gostaria de ter um guarda-roupa?[SIM/NAO]:").upper().strip()
            cama = input("Você gostaria de ter uma cama?[SIM/NAO]:").upper().strip()
            cabiceira = input("Você gostaria de ter uma cabeceira?[SIM/NAO]:").upper().strip()
            suite = input("O quarto será uma suíte?[SIM/NAO]:").upper().strip()
            if suite == "SIM":
              alt = input("Você gostaria de ter alguma alteração no seu banheiro também?[SIM/NAO]:").upper().strip()
        print("PROCESSANDO...")
        sleep(5)
        print("-=-" * 30)
        print("Certo,então seguem abaixo as especificações:")
        print(f"Mudança no quarto : {a}.")
        print(f"Qual a mudança ?: {m}.")
        print(f"Faixa etária: {idade}.")
        print(f"Preferência referencial ? {ref} - {qua}.")
        print(f"Cor favorita? {cor} - {cor1}.")
        print(f"Televisão: {televisao}.")
        print(f"Guarda-roupa: {guard_roup}")
        print(f"Cama: {cama}")
        print(f"Cabeceira: {cabiceira}")
        print(f"suíte: {suite}")
        if suite == "SIM":
            print(f"Mudança no banheiro: {alt}.")
            print("Verifique se está tudo certo, por favor!")
        a = input("Você gostaria de descartar esse e fazer um novo orçamento? [SIM/NAO]:").upper().strip()
        if a == "NAO":
            con = input("Você poderia deixar seu número de telefone ou e-mail para eu entrar em contato? [SIM/NAO]").upper().strip()
        if con == "SIM":
            opcao = input("Você prefere deixar telefone ou e-mail? [TELEFONE / EMAIL]:").upper().strip()
            if opcao == "TELEFONE":
              contato = input("Coloque seu número de telefone para entrar em contato:").strip()
              cont = input(f"{contato} - correto? [SIM/NAO]:").upper().strip()
              while cont == "NAO":
                contato = input("Coloque seu número de telefone para entrar em contato:").strip()
                cont = input(f"{contato} - correto? [SIM/NAO]:").upper().strip()
            elif opcao == "EMAIL":
              email = input("Coloque seu e-mail para contato:").strip()
              em = input(f"{email} - correto? [SIM/NAO]:").upper().strip()
              while em == "NAO":
                email = input("Coloque seu e-mail para contato:").strip()
                em = input(f"{email} - correto? [SIM/NAO]:").upper().strip()
            print("Tudo pronto, mais tarde entrarei em contato com você!")
            print("Muito Obrigada!!!")
        if con == "NAO":
            print("Tudo bem! Muito obrigado por ter entrado em contato!")
            print("Qualquer coisa, meu escritório fica no *ENDEREÇO*")
elif a == "NAO":
  op = input("Qual outra mudança seria?").upper().strip()
  print("-=-" * 20)
  con = input("Você poderia deixar seu número de telefone ou e-mail para eu entrar em contato e poder discorrer mais sobre? [SIM/NAO]").upper().strip()
  if con == "SIM":
    opcao = input("Você prefere deixar telefone ou e-mail? [TELEFONE / EMAIL]:").upper().strip()
    if opcao == "TELEFONE":
      contato = input("Coloque seu número de telefone para entrar em contato:").strip()
      cont = input(f"{contato} - correto? [SIM/NAO]:").upper().strip()
      while cont == "NAO":
        contato = input("Coloque seu número de telefone para entrar em contato:").strip()
        cont = input(f"{contato} - correto? [SIM/NAO]:").upper().strip()
    elif opcao == "EMAIL":
      email = input("Coloque seu e-mail para contato:").strip()
      em = input(f"{email} - correto? [SIM/NAO]:").upper().strip()
      while em == "NAO":
        email = input("Coloque seu e-mail para contato:").strip()
        em = input(f"{email} - correto? [SIM/NAO]:").upper().strip()
    print("Entrarei em contato então!")
    print("Muito Obrigado por ter entrado em contato!!!")
  if con == "NAO":
    print("Tudo bem! Muito obrigado por ter entrado em contato!")
    print("Qualquer coisa, meu escritório fica no *ENDEREÇO*")