import random

class actor:
    def __init__(self,myid,strategy):
        self.strategy=strategy
        self.myid=myid
        self.name=strategy.name
        self.ntrans=0
        self.score=0
    def pay(self,income):
        self.score+=income
        self.ntrans+=1

class defect:
    def __init__(self,Nactors,myid):
        self.Nactors=Nactors
        self.myid=myid
        self.name="defect"
    def response(self, other):
        return "Defect"
    def inform(self, other, other_response):
        return

class cooperate:
    def __init__(self,Nactors,myid):
        self.Nactors=Nactors
        self.myid=myid
        self.name="cooperate"
    def response(self, other):
        return "Cooperate"
    def inform(self, other, other_response):
        return

class tit_for_tat:
    def __init__(self,Nactors,myid):
        self.Nactors=Nactors
        self.myid=myid
        self.name="tit_for_tat"
        self.responses=["Cooperate"]*Nactors
    def response(self, other):
        return self.responses[other]
    def inform(self, other, other_response):
        self.responses[other]=other_response
        return

