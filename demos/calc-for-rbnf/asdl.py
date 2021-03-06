from Redy.Magic.Classic import record
from Redy.Magic.Classic import template
from Redy.ADT.Core import data

class ASDL:...

@data
class Op:
    Add: ...
    Sub: ...

    Mul: ...
    Div: ...
    FloorDiv: ...
    Pow: ...
    Mod: ...

@record
class Numeric(ASDL):
    value: ...

@record
class Bin(ASDL):
    op: ...
    l: ...
    r: ...

@template
def bin_cons(l, r, op):
    return Bin(op, l, r)

@bin_cons(op=Op.Add)
def Add(l, r): ...


@bin_cons(op=Op.Sub)
def Sub(l, r): ...


@bin_cons(op=Op.Mul)
def Mul(l, r): ...


@bin_cons(op=Op.Div)
def Div(l, r): ...


@bin_cons(op=Op.FloorDiv)
def FloorDiv(): ...


@bin_cons(op=Op.Pow)
def Pow(): ...


@bin_cons(op=Op.Mod)
def Mod(): ...
