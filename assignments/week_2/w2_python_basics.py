
def example(a): 
	a = a + '2' 
#	a = a*2 
	return a 

print(example("hello"))

set1={2,5,3}
set2={3,1}
set3={}
set3=set1&set2
print(set3)



class demo(dict):
    def __test__(self, key):
        return []

a = demo()
a.__test__('test')
a['test'] = 7
print(a)

str1 = "my isname isisis jameis isis bond";
sub = "is";
print(str1.count(sub, 4))