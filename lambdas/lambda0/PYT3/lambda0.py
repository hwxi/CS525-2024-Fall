############################################################
# HX-2024-09-10:
# A substitution-based reference
# implementation of lambad-calculus
############################################################
# datatype term =
# | TMvar of strn
# | TMlam of (strn, term)
# | TMapp of (term, term)
############################################################
#
TM0cst = 0
TM0var = 1
TM0lam = 2
TM0app = 3
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
def TM1cst(c00):
    return term_cst(c00)
def TM1var(x00):
    return term_var(x00)
def TM1lam(x00, tm1):
    return term_lam(x00, tm1)
def TM1app(tm1, tm2):
    return term_app(tm1, tm2)
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
############################################################
#
def TMfact4():
    x = "x"
    y = "y"
    f = "f"
    m = "m"
    n = "n"
    p = "p"
    TMvar = TM1var
    TMlam = TM1lam
    TMapp = TM1app
    return TMapp(TMapp(TMlam(f,TMapp(TMlam(x,TMapp(TMvar(f),TMapp(TMvar(x),TMvar(x)))),TMlam(x,TMapp(TMvar(f),TMapp(TMvar(x),TMvar(x)))))),TMlam(f,TMlam(n,TMapp(TMapp(TMapp(TMapp(TMapp(TMlam(n,TMapp(TMapp(TMvar(n),TMlam(x,TMlam(x,TMlam(y,TMvar(y))))),TMlam(x,TMlam(y,TMvar(x))))),TMapp(TMapp(TMlam(f,TMlam(x,TMvar(x))),TMlam(n,TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(x))))),TMapp(TMapp(TMvar(n),TMlam(p,TMapp(TMapp(TMlam(x,TMlam(y,TMlam(f,TMapp(TMapp(TMvar(f),TMvar(x)),TMvar(y))))),TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(y))))),TMvar(p))),TMapp(TMlam(n,TMlam(f,TMlam(x,TMapp(TMvar(f),TMapp(TMapp(TMvar(n),TMvar(f)),TMvar(x)))))),TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(y))))),TMvar(p)))))),TMapp(TMapp(TMlam(x,TMlam(y,TMlam(f,TMapp(TMapp(TMvar(f),TMvar(x)),TMvar(y))))),TMlam(f,TMlam(x,TMvar(x)))),TMlam(f,TMlam(x,TMvar(x)))))))),TMvar(n))),TMlam(x,TMlam(y,TMvar(y)))),TMlam(x,TMlam(y,TMvar(x)))),TMapp(TMapp(TMlam(m,TMlam(n,TMlam(f,TMlam(x,TMapp(TMapp(TMvar(m),TMapp(TMvar(n),TMvar(f))),TMvar(x)))))),TMvar(n)),TMapp(TMvar(f),TMapp(TMapp(TMlam(f,TMlam(x,TMapp(TMvar(f),TMvar(x)))),TMlam(n,TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(x))))),TMapp(TMapp(TMvar(n),TMlam(p,TMapp(TMapp(TMlam(x,TMlam(y,TMlam(f,TMapp(TMapp(TMvar(f),TMvar(x)),TMvar(y))))),TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(y))))),TMvar(p))),TMapp(TMlam(n,TMlam(f,TMlam(x,TMapp(TMvar(f),TMapp(TMapp(TMvar(n),TMvar(f)),TMvar(x)))))),TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(y))))),TMvar(p)))))),TMapp(TMapp(TMlam(x,TMlam(y,TMlam(f,TMapp(TMapp(TMvar(f),TMvar(x)),TMvar(y))))),TMlam(f,TMlam(x,TMvar(x)))),TMlam(f,TMlam(x,TMvar(x)))))))),TMvar(n))))),TMlam(f,TMlam(x,TMapp(TMvar(f),TMvar(x)))))))),TMlam(f,TMlam(x,TMapp(TMvar(f),TMapp(TMvar(f),TMapp(TMvar(f),TMapp(TMvar(f),TMvar(x))))))))
#
print("evaluate(TMfact4) =", term_evaluate(TM1app(TM1app(TMfact4(), TM1cst("f")), TM1cst("x"))))
#
# evaluate(TMfact4) =
# TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMapp(TMcst(f),TMcst(x)))))))))))))))))))))))))
#
############################################################
############################################################
# end of [HWXI/CS525-2024-Fall/lambdas_lambda0_PYT3_lambda0.py]
############################################################
