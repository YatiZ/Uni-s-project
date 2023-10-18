num = 0
counter = 1
print("Enter num")
num = int(input())
# while counter <= num:
#     star = "*" * counter
#     print(star)
#     counter= counter+14

row = 0
col = 0
for row in range(num):
    col = 0
    for col in range(num):
        print("*",end=" ")  
    print()
    
    
