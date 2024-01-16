""" 
Las Tuplas son inmutables

()

"""
tupla=("uno", "dos", "tres")
print(tupla)
print(type(tupla))

tuplasVariablesDatos=(12, True, 23.56, "Mario", 122+4j)
print(tuplasVariablesDatos)

tuplasConTuplas= (1,2,3,(4,3,2,1))
print(tuplasConTuplas)

print(tuplasVariablesDatos[3])
print(tuplasVariablesDatos[-2])
print(tuplasVariablesDatos[0:2])

a,b,c=tupla
print(a)
print(b)
print(c)

