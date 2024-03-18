class MyHashMap:

    def __init__(self):
        self.my_list=[]

    def put(self, key:int, value:int) -> None:

        for pair in self.my_list:
            if key == pair[0]:
                pair[1]=value
                return
        pair=[key,value]
        self.my_list.append(pair)
           
    
    def get(self, key:int) -> int:

        for pair in self.my_list:
            if key==pair[0]:
                return pair[1]
        return -1

    def remove(self, key:int) -> None:

        for pair in self.my_list:
            if key==pair[0]:
                self.my_list.remove(pair)
                return


print("=========Created object from my class -- my list is empty atthis point==============")
myHashMap= MyHashMap()
print(myHashMap.my_list)

print("=========added first key, value pair to my list==============")
myHashMap.put(1,1)
print(myHashMap.my_list)

print("=========added second key, value pair to my list==============")        
myHashMap.put(2,2)
print(myHashMap.my_list)   

print("=========checking first 3 key values from the list(there is no third pair available)==============")   
print(myHashMap.get(1))
print(myHashMap.get(2))
print(myHashMap.get(3))

print("=========updating second keys value==============")   
myHashMap.put(2,1)
print(myHashMap.my_list)   

print("=========checking second keys value==============")   
print(myHashMap.get(2))  

print("=========deleting second pair==============")   
myHashMap.remove(2)
print(myHashMap.my_list) 
