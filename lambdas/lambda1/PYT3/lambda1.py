############################################################
# HX-2024-10-10:
# A closured-based reference
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
# | TMfix of (strn, strn, term)
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
TM0fix = 7
TM0if0 = 8
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
class term_fix(term):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = TM0fix
    def __str__(self):
        return f"TMfix({self.arg1}, {self.arg2}, {self.arg3})"
        # return ("TMfix(" + str(self.arg1) + "," + str(self.arg2) + str(self.arg3) + ")")
# end-of-class(term_fix(term))
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
#
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
def TM1opr(opr, tms: list[term]) -> term:
    return term_opr(opr, tms)
#
def TM1fix(f00: str, x01: str, tm1: term) -> term:
    return term_fix(f00, x01, tm1)
#
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
DV0btf = 2
DV0lam = 3
DV0fix = 4
############################################################
class dval:
    ctag = -1
# end-of-class(dval)
############################################################
class dval_int:
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DV0int
    def __str__(self):
        return ("DVint(" + str(self.arg1) + ")")
# end-of-class(dval_int)
############################################################
class dval_btf:
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DV0btf
    def __str__(self):
        return ("DVbtf(" + str(self.arg1) + ")")
# end-of-class(dval_btf)
############################################################
class dval_lam:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DV0lam
    def __str__(self):
        return ("DVlam(" + str(self.arg1) + "..." + ")")
# end-of-class(dval_lam)
############################################################
class dval_fix:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DV0fix
    def __str__(self):
        return ("DVfix(" + str(self.arg1) + "..." + ")")
# end-of-class(dval_fix)
############################################################
def denv_search2opt(env, x00):
    # print("denv_search2opt: env =", env)
    for xdv in reversed(env):
        if x00 == xdv[0]:
            return xdv[1]
    return None # HX: x00 is not found
############################################################
def term_evaluate(tm0):
    def auxeval(tm0, env):
        # print("auxeval: tm0 =", tm0)
        # print("auxeval: env =", env)
        if tm0.ctag == TM0int:
            return dval_int(tm0.arg1)
        if tm0.ctag == TM0btf:
            return dval_btf(tm0.arg1)
        if tm0.ctag == TM0var:
            return denv_search2opt(env, tm0.arg1)
        if tm0.ctag == TM0lam:
            return dval_lam(tm0, env.copy())
        if tm0.ctag == TM0fix:
            return dval_fix(tm0, env.copy())
        if tm0.ctag == TM0app:
            dv1 = auxeval(tm0.arg1, env)
            dv2 = auxeval(tm0.arg2, env)
            if dv1.ctag == DV0lam:
                tma = dv1.arg1
                x01 = tma.arg1
                tmb = tma.arg2
                env = dv1.arg2
                return auxeval(tmb, env+[(x01, dv2)])
            if dv1.ctag == DV0fix:
                tma = dv1.arg1
                f00 = tma.arg1
                x01 = tma.arg2
                tmb = tma.arg3
                env = dv1.arg2
                return auxeval(tmb, env+[(f00, dv1), (x01, dv2)])
            raise TypeError(tm0) # HX: should be deadcode!
        if (tm0.ctag == TM0opr):
            opr = tm0.arg1
            tms = tm0.arg2
            if (opr == "<"):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_btf(dv0.arg1 < dv1.arg1)
            if (opr == ">"):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_btf(dv0.arg1 > dv1.arg1)
            if (opr == "="):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_btf(dv0.arg1 == dv1.arg1)
            if (opr == "<="):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_btf(dv0.arg1 <= dv1.arg1)
            if (opr == ">="):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_btf(dv0.arg1 >= dv1.arg1)
            if (opr == "!="):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_btf(dv0.arg1 != dv1.arg1)
            if (opr == "+"):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_int(dv0.arg1 + dv1.arg1)
            if (opr == "-"):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_int(dv0.arg1 - dv1.arg1)
            if (opr == "*"):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_int(dv0.arg1 * dv1.arg1)
            if (opr == "/"):
                dv0 = auxeval(tms[0], env)
                dv1 = auxeval(tms[1], env)
                return dval_int(dv0.arg1 // dv1.arg1)
            raise TypeError(tm0) # HX: unrecognized operator
        if (tm0.ctag == TM0if0):
            dv1 = auxeval(tm0.arg1, env)
            return auxeval(tm0.arg2, env) \
                if (dv1.arg1) else auxeval(tm0.arg3, env)
        raise TypeError(tm0) # HX: should be deadcode!
    return auxeval(tm0, [])
############################################################
############################################################
print("evaluate(TMint(0)) =", term_evaluate(TM1int(0)))
print("evaluate(TMbtf(True)) =", term_evaluate(TM1btf(True)))
############################################################
def TM1lt(x, y):
    return TM1opr("<", [x, y])
def TM1gt(x, y):
    return TM1opr(">", [x, y])
def TM1eq(x, y):
    return TM1opr("=", [x, y])
def TM1lte(x, y):
    return TM1opr("<=", [x, y])
def TM1gte(x, y):
    return TM1opr(">=", [x, y])
def TM1neq(x, y):
    return TM1opr("!=", [x, y])
############################################################
def TM1add(x, y):
    return TM1opr("+", [x, y])
def TM1sub(x, y):
    return TM1opr("-", [x, y])
def TM1mul(x, y):
    return TM1opr("*", [x, y])
def TM1div(x, y):
    return TM1opr("/", [x, y])
############################################################
def TM1dbl():
    x = TM1var("x")
    return TM1lam("x", TM1add(x, x))
print("evaluate(TM1dbl(5)) =", term_evaluate(TM1app(TM1dbl(), TM1int(5))))
############################################################
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
