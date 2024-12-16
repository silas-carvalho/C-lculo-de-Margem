# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 08:42:41 2024

@author: Silas Carvalho

This code is released under the MIT License.

Copyright (c) 2024 Silas Carvalho

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from colorama import Fore, Style, init
from decimal import Decimal, getcontext, ROUND_HALF_UP, InvalidOperation

init(autoreset=True)
getcontext().prec = 10

def round_decimal(value):
    return value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def input_decimal(mensagem):
    while True:
        try:
            valor_str = input(mensagem).replace(',', '.')
            valor = Decimal(valor_str)
            if valor < 0:
                print(f"{Fore.RED}O valor não pode ser negativo.{Style.RESET_ALL}")
                continue  # Volta para o início do loop
            return valor  # Saída do loop, entrada válida
        except (ValueError, InvalidOperation) as e:
            print(f"{Fore.RED}Por favor, insira um número válido. Erro: {e}{Style.RESET_ALL}")
            continue  # Volta para o início do loop

def input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                raise ValueError("O número não pode ser negativo.")
            return valor
        except ValueError as e:
            print(f"{Fore.RED}Por favor, insira um número inteiro válido. Erro: {e}")
            continue  # Volta para o início do loop

def input_s_n(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()
        if resposta in ['s', 'n']:
            return resposta
        else:
            print(f"{Fore.RED}Por favor, digite 's' para sim ou 'n'.")

def print_section(title):
    length = len(title) + 8
    line = f"{Fore.YELLOW}{'=' * length}{Style.RESET_ALL}"
    print(f"\n{line}")
    print(f"   {title}")
    print(line)

def calcular_precos():
    while True:
        print_section("CÁLCULO DE MARGEM")
        preco_compra = input_decimal("Digite o custo total dos produtos (em R$): ")

        adicionar_custos_extras = input_s_n("Deseja adicionar custos extras? (s/n): ")
        custos_extras = Decimal('0.00')
        if adicionar_custos_extras == 's':
            num_custos_extras = input_int("Quantos custos extras deseja adicionar? ")
            for i in range(num_custos_extras):
                nome_custo = input(f"Digite o nome do custo extra {i+1}: ")
                valor_custo = input_decimal(f"Digite o valor do {nome_custo}: R$ ")
                custos_extras += valor_custo

            total_com_extras = preco_compra + custos_extras
            print(f"\nTotal dos Custos Extras: R$ {custos_extras:.2f}")
            print(f"Total (Compra + Custos Extras): R$ {total_com_extras:.2f}")
        else:
            total_com_extras = preco_compra

        print_section("CONFIGURAÇÕES DE GANHO ESTIMADO")

        while True:
            margem_lucro = input_decimal("Digite a margem de lucro desejada (em %): ") / 100
            if margem_lucro >= 1:
                print(f"{Fore.RED}Erro: A margem de lucro deve ser menor que 100% (até 99,99%). A fórmula PV = custo / (1 - margem) resulta em divisão por zero quando a margem é 100% ou mais. Por favor, insira um valor menor.")
                continue  # Volta para o início do loop da margem de lucro
            break  # Saída do loop, entrada válida

        pv = round_decimal(total_com_extras / (1 - margem_lucro))

        lucro_bruto = round_decimal(pv - total_com_extras)
        margem_percentual = round_decimal((lucro_bruto / pv) * 100)

        print_section("RESULTADOS DO CÁLCULO")
        print(f"Custo: R${total_com_extras:,.2f}")
        print(f"Preço de Venda (PV): R${pv:,.2f}")
        print(f"Lucro Bruto: R${lucro_bruto:,.2f}")
        print(f"Margem Percentual: {margem_percentual:.2f}%")

        continuar = input_s_n("\nDeseja realizar outro cálculo? (s/n): ")
        if continuar != 's':
            print("Encerrando o programa. Obrigado!")
            break

if __name__ == "__main__":
    calcular_precos()







