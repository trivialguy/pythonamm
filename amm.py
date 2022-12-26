class AMM:
    balances=[{},{},{}]
    totalSupply=0
    reserve_1=0
    reserve_2=0
    constant=0
    fee=0
    def __init__(self,_token1,_token2):
        self.reserve_1=_token1
        self.reserve_2=_token2
        self.constant=_token1*_token2
    def swap1to2(self,x,_address):
        if self.balances[0][_address]<x:
            print("Not enough funds in your account!")
            return 0
        self.balances[0][_address]-=x
        y=(1-self.fee)*x
        self.balances[1][_address]+=(self.reserve_2*y)/(y+self.reserve_1)
        reward=(self.reserve_2*y)/(y+self.reserve_1)
        self.reserve_2=self.constant/(y+self.reserve_1)
        print("Got "+str(reward)+" token_2")
        self.reserve_1+=x
        return reward
    def swap2to1(self,x,_address):
        if self.balances[1][_address]<x:
            print(self.balances[1][_address])
            print("Not enough funds in your account!")
            return 0
        self.balances[1][_address]-=x
        y=(1-self.fee)*x
        self.balances[0][_address]+=(self.reserve_1*y)/(y+self.reserve_2)
        reward=(self.reserve_1*y)/(y+self.reserve_2)
        self.reserve_1=self.constant/(y+self.reserve_2)
        print("Got "+str(reward)+" token_1")
        self.reserve_2+=x
        return reward
    def addliquidity(self,_amount1,_amount2,_address):
        if self.balances[0][_address]<_amount1 and self.balances[0][_address]<_amount2:
            print("Not enough funds in your account!")
            return 0
        temp1=0
        temp2=0
        shares=0
        if self.totalSupply==0:
            temp1=_amount1
            temp2=_amount2
            shares=(_amount1*_amount2)**(1/2)
        else:
            if self.reserve_1*_amount2<self.reserve_2*_amount1:
                temp1=self.reserve_1*_amount2/self.reserve_2
                temp2=_amount2
            else:
                temp1=_amount1
                temp2=self.reserve_2*_amount1/self.reserve_1
            shares=(temp2*self.totalSupply)/self.reserve_2
        self.balances[0][_address]-=temp1
        self.balances[1][_address]-=temp2
        self.balances[2][_address]+=shares
        self.totalSupply+=shares
        self.reserve_1+=temp1
        self.reserve_2+=temp2
        self.constant=self.reserve_1*self.reserve_2
        return shares
    def removeliquidity(self,x,_address):
        if self.balances[2][_address]<x:
            print("You don't hold enough shares for this transaction!")
            return
        _amount1=x*self.reserve_1/self.totalSupply
        _amount2=x*self.reserve_2/self.totalSupply
        self.balances[0][_address]+=_amount1
        self.balances[1][_address]+=_amount2
        self.reserve_1-=_amount1
        self.reserve_2-=_amount2
        self.balances[2][_address]-=x
        self.totalSupply-=x
        self.constant=self.reserve_1*self.reserve_2
    def get_reserves(self):
        return self.reserve_1,self.reserve_2
    def get_totalSupply(self):
        return self.totalSupply
    def get_balance(self,_address):
        return self.balances[0][_address],self.balances[1][_address],self.balances[2][_address]
    
        
        