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
#
class term:
    ctag = -1
# end-of-class(term)
#
class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TM0var
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))
#
class term_cst(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TM0cst
    def __str__(self):
        return ("TMcst(" + self.arg1 + ")")
# end-of-class(term_var(term))
#
class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = TM0lam
    def __str__(self):
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")
# end-of-class(term_lam(term))
#
class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = TM0app
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_app(term))
#
############################################################
#
class term_int(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TM0int
    def __str__(self):
        return ("TMint(" + str(self.arg1) + ")")
# end-of-class(term_int(term))
#
############################################################
#
class term_btf(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TM0btf
    def __str__(self):
        return ("TMbtf(" + str(self.arg1) + ")")
# end-of-class(term_btf(term))
#
############################################################
#
class term_opr(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = TM0opr
    def __str__(self):
        return f"TMopr({self.arg1}, {self.arg2})"
        # return ("TMopr(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_opr(term))
#
############################################################
#
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
#
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
#
# HX: [sub] should be closed!
#
def term_subst(tm0, x00, sub):
    def subst(tm0):
        return term_subst(tm0, x00, sub)
    if (tm0.ctag == TM0cst):
        return tm0
    if (tm0.ctag == TM0var):
        x01 = tm0.arg1
        return sub if (x00 == x01) else tm0
    if (tm0.ctag == TM0lam):
        x01 = tm0.arg1
        return tm0 if (x00 == x01) else TM1lam(x01, subst(tm0.arg2))
    if (tm0.ctag == TM0app):
        return TM1app(subst(tm0.arg1), subst(tm0.arg2))
    if (tm0.ctag == TM0int):
        return tm0
    if (tm0.ctag == TM0btf):
        return tm0
    if (tm0.ctag == TM0opr):
        return TM1opr(tm0.arg1, list(map(subst, tm0.arg2)))
    if (tm0.ctag == TM0if0):
        return TM1if0(subst(tm0.arg1), subst(tm0.arg2), subst(tm0.arg3))
    raise TypeError(tm0) # HX: should be deadcode!
    
############################################################

def term_beta2red(tm1, tm2):
    assert tm1.ctag == TM0lam
    return term_subst(tm1.arg2, tm1.arg1, tm2)

def term_evaluate(tm0):
    # print("term_evaluate: tm0 = ", tm0)
    if (tm0.ctag == TM0cst):
        return tm0
    if (tm0.ctag == TM0var):
        return tm0
    if (tm0.ctag == TM0lam):
        return tm0
    if (tm0.ctag == TM0app):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        tm1 = term_evaluate(tm1)
        if (tm1.ctag == TM0lam):
            return term_evaluate(term_beta2red(tm1, tm2))
        else:
            return TM1app(tm1, term_evaluate(tm2))
    if (tm0.ctag == TM0int):
        return tm0
    if (tm0.ctag == TM0btf):
        return tm0
    if (tm0.ctag == TM0opr):
        opr = tm0.arg1
        tms = tm0.arg2
        if (opr == "<"):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_btf(i00.arg1 < i01.arg1)
        elif (opr == ">"):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_btf(i00.arg1 > i01.arg1)
        elif (opr == "="):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_btf(i00.arg1 == i01.arg1)
        elif (opr == "<="):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_btf(i00.arg1 <= i01.arg1)
        elif (opr == ">="):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_btf(i00.arg1 >= i01.arg1)
        elif (opr == "!="):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_btf(i00.arg1 != i01.arg1)
        elif (opr == "+"):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_int(i00.arg1 + i01.arg1)
        elif (opr == "-"):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_int(i00.arg1 - i01.arg1)
        elif (opr == "*"):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_int(i00.arg1 * i01.arg1)
        elif (opr == "/"):
            i00 = term_evaluate(tms[0])
            i01 = term_evaluate(tms[1])
            return term_int(i00.arg1 // i01.arg1)
        else:
            return tm0 # unrecognized operator
    if (tm0.ctag == TM0if0):
        tm1 = tm0.arg1
        tm2 = tm0.arg2
        tm3 = tm0.arg3
        tm1 = term_evaluate(tm1)
        if (tm1.ctag == TM0btf):
            return term_evaluate(tm2) \
                if (tm1.arg1) else term_evaluate(tm3)
        else:
            TMif0(tm1, tm2, tm2) 
    raise TypeError(tm0) # HX: should be deadcode!

############################################################
#
def SKKx():
    S = S_()
    K = K_()
    x = TM1var("x")
    return TM1app(TM1app(TM1app(S, K), K), x)
#
print("evaluate(SKKx) =", term_evaluate(SKKx()))
#
############################################################
def TM1dbl():
    x = TM1var("x")
    return TM1lam("x", TM1opr("+", [x, x]))
print("evaluate(TM1dbl(5)) =", term_evaluate(TM1app(TM1dbl(), TM1int(5))))
############################################################
def Y():
    f = TM1var("f")
    x = TM1var("x")
    fomega = TM1lam("x", TM1app(f, TM1app(x, x)))
    return TM1lam("f", TM1app(fomega, fomega))
def TM1fix(fnm, xnm, term):
    return TM1app(Y(), TM1lam(fnm, TM1lam(xnm, term)))
############################################################
def TM1gt(tm1, tm2):
    return TM1opr(">", [tm1, tm2])
def TM1sub(tm1, tm2):
    return TM1opr("-", [tm1, tm2])
def TM1mul(tm1, tm2):
    return TM1opr("*", [tm1, tm2])
def TM1fact():
    i0 = TM1int(0)
    i1 = TM1int(1)
    xf = TM1var("f")
    xn = TM1var("n")
    return TM1fix("f", "n", TM1if0(TM1gt(xn, i0), TM1mul(xn, TM1app(xf, TM1sub(xn, i1))), i1))
print("evaluate(TM1fact(5)) =", term_evaluate(TM1app(TM1fact(), TM1int(5))))
############################################################
############################################################
# end of [HWXI/CS525-2024-Fall/lambdas_lambda1_PYT3_lambda1.py]
############################################################
