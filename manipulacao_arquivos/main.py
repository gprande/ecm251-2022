# Código para escrever dados em um arquivo

from traceback import print_stack


try:
   arquivo = open("data/sistemas.txt", "a")
   continuar = True
   while continuar:
       os_name = input("Diga um OS (vazio para sair): ")
       if not os_name:
           continuar = False
           continue
       arquivo.write(os_name + '\n') 
   arquivo.close()

except FileNotFoundError:
    print("O caminho não existe, favor verificar")
except Exception:
    print("Algo não esperado ocorreu: ")
    print_stack()
finally:
    print("Chegamos ao final família")