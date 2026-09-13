# python architecture:
# code-Tokenization-ast(abstract syntax tree)


# python runtime environment:to create a file in that we write python code - tokenization- convert tokens into ast - ast convert to bytecode (bytecode evaru chestharu compiler) pvm reads bytecode interpreter (line by line).
#  interpreter:2 phase:1.memory phase or memory allocation
# 2.code execution

# memory allocation :
# 1.stack memory : stores variables,func names,references and call()
# 2.heap memory: stores values and objects.


a=10
a=20
print(a)


a=10
print(a)
print(id(a))
a=20
print(id(a))



a=10
b=a
print(id(a))
print(id(b))