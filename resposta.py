def resolucao():
    A = {1,2,3,4,5}
    B = {4,5,6,7}
    C={1,3,5}
    a= A.intersection(B)
    print('Resposta da a:',a)
    b=A.union(B)
    print ('Resposta da b:',b)
    c=A.difference(B)
    print ('Resposta da c:',c)
    d=B.difference(A)
    print ('Resposta da d:',d)
    e=C.difference(a)
    print ('Resposta da e:',e)
    f=C.difference(b)
    print ('Resposta da f:',f)
    g=b.difference(A)
    print ('Resposta da g:',g)
    h=b.difference(B)
    print ('Resposta da h:',h)
    conjunto_vazio = set()
    i=A.difference(conjunto_vazio)
    return 'Resposta da i:',i