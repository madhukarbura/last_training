first_num=int(input())
second_num=int(input())
print('''1.+
2.-
3. %
4.*''')
choice=int(input("enter the choice: "))
if choice==1:
    print(first_num+second_num)
elif choice==2:
    print(first_num-second_num)
elif choice==3:
    print(first_num%second_num)
elif choice==4:
    print(first_num*second_num)
else:
    print("no option selected")
    