def example_function1():
    local_var=5
    print(local_var)
    
local_var=6
example_function1()
print(local_var)

print("#================================practice 2==================================")

def outer_function():
    nonlocal_var=10
    def inner_function():
        nonlocal nonlocal_var
        nonlocal_var+=5
        
    inner_function()
    print(nonlocal_var)

outer_function()

print("#================================practice 2 mofified==================================")
def outer_function():
    nonlocal_var=10
    def inner_function():
       # nonlocal nonlocal_var
        nonlocal_var=5
        print(nonlocal_var)
        
    inner_function()
    print(nonlocal_var)

outer_function()

print("#================================practice global var==================================")
global_var=20
def example_function2():
    global global_var
    global_var+=5
    
print(global_var)
example_function2()
print(global_var)

print("#================================practice global var==================================")

global_var=20
def example_function3():
   # global global_var - unbound exception
    global_var+=5
    
print(global_var)
example_function3()
print(global_var)
 
