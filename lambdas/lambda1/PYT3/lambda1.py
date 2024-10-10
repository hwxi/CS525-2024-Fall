############################################################
# HX-2024-09-10:
# A substitution-based reference
# implementation of lambad-calculus
############################################################
# datatype term =
# | TMvar of strn
# | TMlam of (strn, term)
# | TMapp of (term, term)
# | TMint of (sint)
# | TMbtf of (bool)
# | TMopr of (strn, list(term))
# | TMif0 of (term, term, term)
############################################################
#
TM0cst = 0
#
TM0var = 1
TM0lam = 2
TM0app = 3
#
TM0int = 4
TM0btf = 5
#
TM0opr = 6
TM0if0 = 7
#
############################################################
class term:
    ctag = -1
# end-of-class(term)
############################################################
class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TM0var
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))
############################################################
class term_cst(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TM0cst
    def __str__(self):
        return ("TMcst(" + self.arg1 + ")")
# end-of-class(term_var(term))
############################################################
class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = TM0lam
    def __str__(self):
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")
# end-of-class(term_lam(term))
############################################################
class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = TM0app
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_app(term))
############################################################
class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TM0int
    def __str__(self):
        return ("TMint(" + str(self.arg1) + ")")
# end-of-class(term_int(term))
############################################################
class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TM0btf
    def __str__(self):
        return ("TMbtf(" + str(self.arg1) + ")")
# end-of-class(term_btf(term))
############################################################
class term_opr(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = TM0opr
    def __str__(self):
        return f"TMopr({self.arg1}, {self.arg2})"
        # return ("TMopr(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_opr(term))
############################################################
class term_if0(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = TM0if0
    def __str__(self):
        return f"TMif0({self.arg1}, {self.arg2}, {self.arg3})"
        # return ("TMif0(" + str(self.arg1) + "," + str(self.arg2) + str(self.arg3) + ")")
# end-of-class(term_if0(term))
############################################################
#
def TM1cst(c00):
    return term_cst(c00)
def TM1var(x00):
    return term_var(x00)
def TM1lam(x00, tm1):
    return term_lam(x00, tm1)
def TM1app(tm1, tm2):
    return term_app(tm1, tm2)
#
def TM1int(i00: int) -> term:
    return term_int(i00)
def TM1btf(b00: bool) -> term:
    return term_btf(b00)
#
def TM1opr(opr, tms):
    return term_opr(opr, tms)
def TM1if0(tm1: term, tm2: term, tm3: term) -> term:
    return term_if0(tm1, tm2, tm3)
#
############################################################
#
def I_():
    x = TM1var("x")
    return TM1lam("x", x)
def K_():
    x = TM1var("x")
    return TM1lam("x", TM1lam("y", x))
def S_():
    x = TM1var("x")
    y = TM1var("y")
    z = TM1var("z")
    return TM1lam("x", TM1lam("y", TM1lam("z", TM1app(TM1app(x, z), TM1app(y, z)))))
#
_ = print("I =", I_())
_ = print("K =", K_())
_ = print("S =", S_())
#
############################################################
############################################################
# datatype dval =
# | DVint of sint
# | DVbtf of bool
# | DVlam of (term, denv)
# | DVfix of (term, denv)
############################################################
DV0int = 1
DV0btf = 1
DV0lam = 2
DV0fix = 1
############################################################
class dval:
    ctag = -1
# end-of-class(dval)
############################################################
class dval_int:
    ctag = -1
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DV0int
    def __str__(self):
        return ("DVint(" + str(self.arg1) + ")")
# end-of-class(dval_int)
############################################################
class dval_btf:
    ctag = -1
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DV0btf
    def __str__(self):
        return ("DVbtf(" + str(self.arg1) + ")")
# end-of-class(dval_btf)
############################################################
class dval_lam:
    ctag = -1
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DV0lam
    def __str__(self):
        return f"DVlam({self.arg1}, ...)"
# end-of-class(dval_lam)
############################################################
class dval_fix:
    ctag = -1
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DV0fix
    def __str__(self):
        return f"DVfix({self.arg1}, ...)"
# end-of-class(dval_fix)
############################################################
def denv_search2opt(env, x00):
    for xtp in env:
        if x00 == xtp[0]:
            return xtp[1]
    return None # HX: x00 is not found
############################################################
def term_evaluate(tm0):
    def auxeval(tm0, env):
        if tm0.ctag == TM0int:
            return dval_int(tm0.arg1)
        if tm0.ctag == TM0btf:
            return dval_btf(tm0.arg1)
        raise TypeError(tm0) # HX: should be deadcode!
    return auxeval(tm0, [])
############################################################
############################################################
print("evaluate(TMint(0)) =", term_evaluate(TM1int(0)))
print("evaluate(TMbtf(True)) =", term_evaluate(TM1btf(True)))
############################################################
############################################################
# end of [HWXI/CS525-2024-Fall/lambdas_lambda1_PYT3_lambda1.py]
############################################################
