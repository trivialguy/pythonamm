import amm

obj=amm.AMM(50000,50000)

obj.balances[1]["kshitij"]=20000
obj.balances[2]["kshitij"]=20000
obj.totalSupply=20000

while True:
    addr=input("Enter your address: ")
    obj.balances[0][addr]=obj.balances[0].get(addr,0)
    obj.balances[1][addr]=obj.balances[1].get(addr,0)
    obj.balances[2][addr]=obj.balances[2].get(addr,0)
    command=int(input("Enter the following value to get the following results:\n\
        1. \'1\' to swap token_1 to token_2\n\
        2. \'2\' to swap token_2 to token_1\n\
        3. \'3\' to buy shares\n\
        4. \'4\' to remove shares\n\
        5. \'5\' to get your account balance\n\
        6. \'6\' to get your shares\n\
        "))
    if command==1:
        x=int(input("Enter the amount of token_1 to be swapped: "))
        obj.swap1to2(x,addr)
    elif command==2:
        x=int(input("Enter the amount of token_2 to be swapped: "))
        obj.swap2to1(x,addr)
    elif command==3:
        print("( Warning! Excess tokens will be returned to your account")
        x=int(input("Enter the amount of token_1 to invest: "))
        y=int(input("Enter the amount of token_2 to invest: "))
        obj.addliquidity(x,y,addr)
    elif command==4:
        x=int(input("Enter the number of shares to withdraw: "))
        obj.removeliquidity(x,addr)
    elif command==5:
        x,y,z=obj.get_balance(addr)
        print("Number of token_1 in your account: "+str(x))
        print("Number of token_2 in your account: "+str(y))
    elif command==6:
        x,y,z=obj.get_balance(addr)
        print("Number of shares held: "+str(z))
    else:
        print("Kindly choose a number from the list!")
        