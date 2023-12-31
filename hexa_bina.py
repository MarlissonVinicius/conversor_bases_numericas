'''Conversão de Hexadecimal para Binário
Esta função converte um número hexadecimal em um número binário. Ela mapeia cada dígito hexadecimal para seu equivalente binário usando um dicionário e, em seguida, concatena os resultados para obter o número binário correspondente.'''

def hexa_bina(hexa):
    hex_dic = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    entrada = hexa
    bina = ""

    for i in hexa:
        i = i.upper() if i.isalpha() else i  # i receberá o próprio conteúdo maiúsculo, caso ele seja uma letra 
        hexa = hex_dic[i] 
        bina += hexa     
    print(f"{entrada}₁₆ = {bina}₂")

