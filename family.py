class FamilyArrangement:
    def __init__(self, family):
        # Inicializa a classe com uma representação da família.
        self.family = family

    def __str__(self):
        # Retorna a representação da família como uma string.
        return self.family

    def add_child(self, gender, age):
        # Adiciona um filho à família com um sexo e idade específicos.
        if gender not in "hmHM":
            raise ValueError("Gênero inválido")
        if age < 0 or age > len(self.family):
            raise ValueError("Idade inválida")

        self.family = self.family[:age] + gender + self.family[age:]

    def remove_child(self, age):
        # Remove um filho da família com base na idade.
        if age < 0 or age >= len(self.family):
            raise ValueError("Idade inválida")

        self.family = self.family[:age] + self.family[age + 1:]

    def meets_criterion1(self):
        # Verifica se a família atende ao critério 1: Casais heterossexuais mais velhos que os filhos
        # com pelo menos duas filhas mulheres, ou pelo menos um filho homem, ou ainda pelo menos
        # dois filhos homens e uma filha mulher.
        return self.family.count("m") >= 2 or "H" in self.family or (self.family.count("h") >= 2 and "M" in self.family)

    def meets_criterion2(self):
        # Verifica se a família atende ao critério 2: Casais heterossexuais mais velhos que os filhos
        # com a filha mais velha mulher e o filho mais novo homem.
        return "H" in self.family and "M" in self.family and self.family.index("H") < self.family.index("M")

    def meets_criterion3(self):
        # Verifica se a família atende ao critério 3: Casais heterossexuais mais velhos que os filhos
        # com a filha mais velha mulher e o filho mais novo homem.
        return "H" in self.family and "M" in self.family and self.family.index("H") < self.family.index("M")

    def meets_criterion4(self):
        # Verifica se a família atende ao critério 4: Casais heterossexuais mais velhos que os filhos
        # com a filha mais velha mulher e o filho mais novo homem.
        return self.family[-1] == "h" and "M" in self.family

    def meets_criterion5(self):
        # Verifica se a família atende ao critério 5: Casais homossexuais mais velhos que os filhos,
        # com pelo menos seis filhos, em que os dois primeiros filhos formam um casal e os últimos também.
        return "h" * 6 in self.family or "H" * 6 in self.family or "M" * 6 in self.family

    def meets_criterion6(self):
        # Verifica se a família atende ao critério 6: Casais homossexuais mais velhos que os filhos,
        # em que o sexo dos filhos é alternado conforme a ordem de nascimento.
        return all(self.family[i] != self.family[i + 1] for i in range(len(self.family) - 1))

    def meets_criterion7(self):
        # Verifica se a família atende ao critério 7: Casais homossexuais mais velhos que os filhos,
        # com qualquer quantidade de filhos homens e mulheres, mas que não tiveram dois filhos homens consecutivos.
        return "hh" not in self.family

    def meets_criterion8(self, x, y):
        # Verifica se a família atende ao critério 8: Arranjo de no mínimo x adultos mais velhos que os filhos,
        # com qualquer quantidade de filhos homens e mulheres, mas os três filhos mais novos não são homens.
        return self.family.count("H") + self.family.count("M") >= x and self.family.count("hh") <= 2


if __name__ == "__main__":
    family = FamilyArrangement("MHhmm")
    while True:
        choice = int(input("1. Casais heterossexuais mais velhos que os filhos\n"
                "2. Casais heterossexuais mais velhos que os filhos (critério 2)\n"
                "3. Casais heterossexuais mais velhos que os filhos (critério 3)\n"
                "4. Casais heterossexuais mais velhos que os filhos (critério 4)\n"
                "5. Casais homossexuais com pelo menos seis filhos\n"
                "6. Casais homossexuais com filhos de sexo alternado\n"
                "7. Casais homossexuais sem dois filhos homens consecutivos\n"
                "8. Arranjo de adultos mais velhos com 3 filhas mulheres\n"
                "9. Sair\n"
                "Escolha uma alternativa: "))

        if choice == 1:
            family = FamilyArrangement("MHhmm")
            result = family.meets_criterion1()
            print(f"Resultado para critério 1: {result}")
        elif choice == 2:
            family = FamilyArrangement("MHhmm")
            result = family.meets_criterion2()
            print(f"Resultado para critério 2: {result}")
        elif choice == 3:
            family = FamilyArrangement("MHhmm")
            result = family.meets_criterion3()
            print(f"Resultado para critério 3: {result}")
        elif choice == 4:
            family = FamilyArrangement("MHhmm")
            result = family.meets_criterion4()
            print(f"Resultado para critério 4: {result}")
        elif choice == 5:
            family = FamilyArrangement("hhhhhh")
            result = family.meets_criterion5()
            print(f"Resultado para critério 5: {result}")
        elif choice == 6:
            family = FamilyArrangement("hmhmhm")
            result = family.meets_criterion6()
            print(f"Resultado para critério 6: {result}")
        elif choice == 7:
            family = FamilyArrangement("hhhhhh")
            result = family.meets_criterion7()
            print(f"Resultado para critério 7: {result}")
        elif choice == 8:
            family = FamilyArrangement("HHMHHhhM")
            result = family.meets_criterion8(3, 10)
            print(f"Resultado para critério 8: {result}")
        elif choice == 9:
            break
        else:
            print("Opção inválida. Tente novamente.")