'''Conversão de Decimal para Hexadecimal
Esta função converte um número decimal em um número hexadecimal. Ela divide o número decimal sucessivamente por 16, obtendo os restos em cada etapa e mapeando os restos para seus equivalentes hexadecimais usando um dicionário. Os resultados são concatenados da direita para a esquerda para formar o número hexadecimal correspondente.'''

def deci_hexa(deci):   
    deci_dic = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }

    entrada = deci
    hexa = ""
    while deci >= 16:
        resto = deci % 16
        deci //= 16 
        hexa = deci_dic[resto] + hexa 
    hexa = deci_dic[deci] + hexa
    print(f"{entrada}₁₀ = {hexa}₁₆")

deci_hexa(42)