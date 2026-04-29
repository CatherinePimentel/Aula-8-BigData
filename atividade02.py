def calcula_multa (e):
    multa = e * multa_valor
    return multa


limite = 100
multa_valor = 4.0
peso_pescado = float(input('Informe o peso:'))

if peso_pescado > 100:
    excedente = peso_pescado - limite 
    vl_multa = calcula_multa(excedente)
    print(f'Valor da multa R$ {vl_multa}')

else :
    print(f'Peso {peso_pescado}, sem multa!')

    
    
