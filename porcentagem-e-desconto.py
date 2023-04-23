import os
from time import sleep
print("Irei calcular sua porcentagem...")
while(True):
    try:
        num = float(input("Selecione seu número para retirar a %\n"))
        os.system("clear")
        prcnt = float(input("Agora quantos porcentos deseja calcular?\n"))
        cento = num / 100
        resu = prcnt * cento
        desconto = num - resu
        break
    except:
        os.system("clear")
        print("Digite algo valido")
        sleep(1)
        continue
print(f"{prcnt}% de {num} equivale á {resu:.2f}\nDescontando, você tem {desconto}")
