variable_global=1
#ambito local x
def number():
    x=42
    print(x)
    print(variable_global)
# por ello no existe en el ambito global
#print(x) # sale error porque no esta definido en el global solo local de la funcion number

print("paso por valor")
x=10
def demo(a:int):
    a=20
    print(a)

demo(x)
print(x)
print("paso por referencia")

def foo(x : list):
    x[0] = x[0] * 99

# lista original
my_list = [1, 2, 3] 

foo(my_list)
print(my_list)