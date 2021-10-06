import transformations
import maior_intencidade
opt = 1;
while opt!=0:
    print('-------ESCOLHA A OPERAÇÃO:')
    print('1 - Logaritmica')
    print('2 - Exponencial')
    print('3 - Inverso')
    print('0 - Sair')
    try:
        opt = int(input())
    except:
        print("")
    if opt==1:
        re = transformations.transformacao_logaritmica()
        if re == 0:
            print("Informe um valor válido.")
    elif opt == 2:
        re = transformations.transformacao_exponential()
        if re == 0:
            print("Informe um valor válido.")
    elif opt == 3:
        transformations.transformacao_inversa()
    elif opt == 0:
        break
    else:
        print("Informe um valor válido")