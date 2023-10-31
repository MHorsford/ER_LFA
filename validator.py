class Validator:
    def __init__(self):
        pass

    # Validação de nome
    def validatorName(self, name):
        # Verifica se a entrada tem no mínimo 2 e no máximo 3 componentes do nome
        if len(name) < 2 or len(name) > 3:
            print("Você deve preencher no mínimo 2 e no máximo 3 componentes do seu nome!!")
            return False

        for n in name:
            # Verifica se a primeira letra de cada nome é maiúscula
            if not n[0].isupper():
                print(f"A primeira letra de {n} deve ser maiúscula")
                return False

            # Verifica se o restante dos caracteres é minúsculo
            if any(char.isupper() for char in n[1:]):
                print(f"O restante do nome {n} deve ser escrito em letras minúsculas.")
                return False

            # Verifica se contém apenas letras
            if not n.isalpha():
                print(f"{n} não contém apenas caracteres Σ e Γ.")
                return False
        return True
    ##################################################################
    # Validação de e-mails
    def validatorEmail(self, email):
        # Verifica se a sentença contém um, e apenas um, símbolo "@"
        if email.count('@') != 1:
            print("A sentença deve conter um, e apenas um, símbolo '@'")
            return False

        username, domain = email.split('@')

        # Verifica se a sentença não começa com o símbolo "@"
        if username == '':
            print("A sentença não deve começar com o símbolo '@'")
            return False

        # Verifica se a sentença termina com ".com.br" ou ".br"
        if not (domain.endswith(".com.br") or domain.endswith(".br")):
            print("A sentença deve terminar com '.com.br' ou '.br'")
            return False

        # Verifica se há pelo menos uma letra de Σ = {a, b, c, …, z} entre o "@" e a terminação
        domain_parts = domain.split('.')
        if len(domain_parts) > 1 and not any(char.isalpha() for char in domain_parts[0]):
            print("Deve haver, pelo menos, uma letra de Σ entre o '@' e a terminação")
            return False

        # Verifica se não há letras maiúsculas após o "@" até a terminação
        if any(char.isupper() for char in domain_parts[0]):
            print("Não podem haver letras maiúsculas após o '@'")
            return False

        # Verifica se não há símbolos inválidos entre o "@" e a terminação
        if any(char != '@' and char not in "abcdefghijklmnopqrstuvwxyz" for char in domain_parts[0]):
            print("A sentença deve conter apenas o símbolo '@' e caracteres de Σ, excluindo o '@'")
            return False

        return True
    #################################################################################
    # Validção de CPF
    def validatorPassword(self, password):
        psw_upper = False
        psw_digit = False
        if len(password) != 8:
            print("A sentença deve ser igual a 8!")
            return False
        for psw in password:
            if psw.isupper():
                psw_upper = True
            elif psw.isdigit():
                psw_digit = True
            # Verifica se contém digito Σ, N e Γ
            if not (psw.isalpha() or psw.isdigit()):
                print("A sentença deve conter apenas simbolose de Σ, N e Γ!")
                return False
        # Verifica se a sentença tem pelo menos um símbolo de Γ e outro de N
        if not (psw_upper and psw_digit):
            print("A sentença deve conter pelo menos um simbolo de Γ e outro de N!")
            return False
        return True

    # Validação de CPF
    def validatorCPF(self, cpf):

        if len(cpf) != 14:
            print("A sentença não possui o comprimento igual a 14(XXX.XXX.XXX-XX)!")
            return False

        for i in range(3):
            if (not cpf[i].isdigit() or cpf[3] != '.' or not cpf[4:7].isdigit() or cpf[7] != '.'
                    or not cpf[8:11].isdigit() or cpf[11] != '-' or not cpf[12:].isdigit()):
                print("O formato da sentença não corresponde a 'xxx.xxx.xxx-xx' onde x pertence a N!'")
                return False
        return True

    def validatorTelefone(self, telefone):
        # Remover espaços em branco e parênteses
        telefone = telefone.replace("(", "").replace(")", "").replace(" ", "")

        # Verificar se o número de telefone tem o comprimento correto
        if len(telefone) == 11:
            # Verificar se o primeiro dígito é 9
            if telefone[2] == '9':
                # Verificar se os dígitos restantes são numéricos
                if telefone[3:].isdigit():
                    return True
        return False

    # Validação de Data e Hora
    def validatorDataHora(self, data_hora):
        # Verifica o formato dd/mm/aaaa hh:mm:ss
        if len(data_hora) != 19:
            print("Formato de data e hora inválido. Deve ser 'dd/mm/aaaa hh:mm:ss'")
            return False

        if (
            data_hora[2] != "/"
            or data_hora[5] != "/"
            or data_hora[10] != " "
            or data_hora[13] != ":"
            or data_hora[16] != ":"
        ):
            print("Formato de data e hora inválido. Deve ser 'dd/mm/aaaa hh:mm:ss'")
            return False

        return True

#    def validatorNumeroReal(self, numero):

if __name__ == "__main__":
    val = Validator()

    names = ["Ada Lovelace", "Alan Turing", "Stephen Cole Kleene", "Alan TURING", "Alan",
             "A1an", "A1an Turing", "Alan turing"]

    emails = ["a@a.br", "divulga@ufpa.br", "a@a.com.br", "a@@a.br", "a@.br", "@", "@a.br",
              "T@teste.br", "a@A.com.br", "ufpa@ufpa.ufpa"]

    password = ["518R2r5e", "F123456A", "1234567T", "ropsSoq0", "F1234567A",
                "abcdefgH", "1234567HI"]

    cpfs = ["123.456.789-09", "000.000.000-00", "123.456.789-0", "111.111.11-11",
            "999.999.999-99", "999.999.999-9a", "999.999.999*99"]

    telefones = ["(91) 99999-9999", "(91) 999999999", "91 999999999",
                 "(91) 59999-9999", "99 99999-9999", "(94)95555-5555"]

    datas = exemplos = ["31/08/2019 20:14:55", "99/99/9999 23:59:59", "99/99/9999 3:9:9",
                        "9/9/99 99:99:99", "99/99/999903:09:09", "00/00/0000 00:00:00"]

    numeroReal = ["-25.467", "1", "-1", "+1", "64.2", "1.", ".2", "+64,2"]

    while True:
        menu = int(input("Verificar lista de:\n"
                         "1 -> Names\n"
                         "2 -> E-mails\n"
                         "3 -> Password\n"
                         "4 -> CPF\n"
                         "5 -> Phone\n"
                         "6 -> Data\n"
                         "7 -> Nº Real com/sem sinal\n"
                         "0 -> exit\n"
                         "Escolha um numero: "))
        if menu == 1:
            for name in names:
                name_ = name.split()
                if val.validatorName(name_):
                    print(f'Nome Válido: {name}\n')
                else:
                    print(f'Nome Invalido: {name}\n')
        # Teste de e-mails
        elif menu == 2:
            for email in emails:
                if val.validatorEmail(email):
                    print(f'E-mail válido: {email}\n')
                else:
                    print(f'E-mail inválido: {email}\n')
        elif menu == 3:
            for psw in password:
                if val.validatorPassword(psw):
                    print(f'E-mail válido: {psw}\n')
                else:
                    print(f'E-mail inválido: {psw}\n')
        elif menu == 4:
            for cpf in cpfs:
                if val.validatorCPF(cpf):
                    print(f'CPF válido: {cpf}\n')
                else:
                    print(f'CPF inválido: {cpf}\n')
        elif menu == 5:
            for telefone in telefones:
                if val.validatorTelefone(telefone):
                    print(f'Telefone válido: {telefone}\n')
                else:
                    print(f'Telefone inválido: {telefone}\n')
        elif menu == 6:
            for data in datas:
                if val.validatorDataHora(data):
                    print(f'Data e Hora válido: {data}\n')
                else:
                    print(f'Data e Hora inválido: {data}\n')
        elif menu == 7:
            pass

        elif menu == 0:
            break
