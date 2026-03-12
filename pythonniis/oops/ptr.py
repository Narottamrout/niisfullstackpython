class Calculate:
    def __init__(self,pr,ti,ra):
        self.p=pr
        self.t=ti
        self.r=ra
    def si(self):
        si=(self.p*self.t*self.r)/100 
        print("simple intrest is=",si)   
   
c1=Calculate(1000,2,5)
c1.si()