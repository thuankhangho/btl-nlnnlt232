from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class StaticChecker(BaseVisitor, Utils):
    def __init__ (self, ast):
        self.ast = ast
        
    def check(self):
        print(self.ast)
