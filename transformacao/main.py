import transformations
import maior_intencidade
opt = 1;
while opt!=0:
    print('-------ESCOLHA A OPERAÇÃO:')
    print('1 - Logaritmica')
    print('2 - Exponencial')
    print('3 - Inverso')
    print('0 - Sair')
    opt = int(input())
    if opt==1:
        transformations.log_proces()
    if opt == 2:
        transformations.exponential()
    if opt == 3:
        transformations.inversa()