############################################################
############################################################
# HX-2024-10-12:
# Type-checking for some
# extended lambda-calculus
############################################################
############################################################
# datatype styp =
# | STbas of (snam)
# | STtup of (styp, styp)
# | STfun of (styp, styp)
# | STnone of (   ) // none
# | STpfst of (styp) // nontup
# | STpsnd of (styp) // nontup
# | STfarg of (styp) // nonfun
# | STfres of (styp) // nonfun
############################################################
############################################################
#
ST0bas = 0
ST0tup = 1
ST0fun = 2
#
ST0none = 3
#
ST0pfst = 4
ST0pfst = 5
ST0farg = 6
ST0fres = 7
#
############################################################
############################################################
# datatype dexp =
# | DEvar of strn
# | DElam of (strn, dexp)
# | DEapp of (dexp, dexp)
# | DEint of (sint)
# | DEbtf of (bool)
# | DEopr of (strn, list(dexp))
# | DEif0 of (dexp, dexp, dexp)
# | DEfix of (strn, strn, dexp)
############################################################
# | DEnil0 of ()//unit
# | DEcons of (dexp, dexp)//pair
# | DEpfst of (dexp) // 1st project
# | DEpsnd of (dexp) // 2nd project
############################################################
# | DElet0 of (strn, dexp, dexp)
############################################################
# | DElam2 of (strn, styp, dexp)
# | DEfix2 of (strn, strn, styp, dexp, styp)
############################################################
# | DEcast of (dexp, styp) // type-casting
############################################################
#
DE0cst = 0
#
DE0var = 1
DE0lam = 2
DE0app = 3
#
DE0int = 4
DE0btf = 5
#
DE0opr = 6
#
DE0if0 = 7
DE0fix = 8
#
DE0nil0 = 9
DE0cons = 10
DE0pfst = 11
DE0psnd = 12
#
DE0let0 = 13
#
DE0lam2 = 14
DE0fix2 = 15
#
DE0cast = 16 # for type casting
#
############################################################
############################################################
class dexp:
    ctag = -1
    styp = None
# end-of-class(dexp)
############################################################
class dexp_cst(dexp):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DE0cst
    def __str__(self):
        return ("DEcst(" + self.arg1 + ")")
# end-of-class(dexp_var(dexp))
############################################################
class dexp_var(dexp):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DE0var
    def __str__(self):
        return ("DEvar(" + self.arg1 + ")")
# end-of-class(dexp_var(dexp))
############################################################
class dexp_lam(dexp):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DE0lam
    def __str__(self):
        return ("DElam(" + self.arg1 + "," + str(self.arg2) + ")")
# end-of-class(dexp_lam(dexp))
############################################################
class dexp_app(dexp):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DE0app
    def __str__(self):
        return ("DEapp(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(dexp_app(dexp))
############################################################
class dexp_int(dexp):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DE0int
    def __str__(self):
        return ("DEint(" + str(self.arg1) + ")")
# end-of-class(dexp_int(dexp))
############################################################
class dexp_btf(dexp):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DE0btf
    def __str__(self):
        return ("DEbtf(" + str(self.arg1) + ")")
# end-of-class(dexp_btf(dexp))
############################################################
class dexp_opr(dexp):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DE0opr
    def __str__(self):
        return ("DEopr(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(dexp_opr(dexp))
############################################################
class dexp_if0(dexp):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = DE0if0
    def __str__(self):
        return ("DEif0(" + str(self.arg1) + "," + str(self.arg2) + str(self.arg3) + ")")
# end-of-class(dexp_if0(dexp))
############################################################
class dexp_fix(dexp):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = DE0fix
    def __str__(self):
        return ("DEfix(" + str(self.arg1) + "," + str(self.arg2) + str(self.arg3) + ")")
# end-of-class(dexp_fix(dexp))
############################################################
class dexp_nil0(dexp):
    def __init__(self):
        self.ctag = DE0nil0
    def __str__(self):
        return ("DEnil0(" + ")")
class dexp_cons(dexp):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DE0cons
    def __str__(self):
        return ("DEcons(" + str(self.arg1) + "," + str(self.arg2) + ")")
############################################################
class dexp_pfst(dexp):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DE0pfst
    def __str__(self):
        return ("DEpfst(" + str(self.arg1) + ")")
class dexp_psnd(dexp):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = DE0psnd
    def __str__(self):
        return ("DEpsnd(" + str(self.arg1) + ")")
############################################################
class dexp_let0(dexp):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = DE0let0
    def __str__(self):
        return ("DElet0(" + str(self.arg1) + str(self.arg2) + str(self.arg3) + ")")
############################################################
class dexp_lam2(dexp):
    def __init__(self, arg1, arg2, arg3):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.ctag = DE0lam2
    def __str__(self):
        return ("DElam2(" + str(self.arg1) + str(self.arg2) + str(self.arg3) + ")")
class dexp_fix2(dexp):
    def __init__(self, arg1, arg2, arg3, arg4, arg5):
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.arg4 = arg4        
        self.arg5 = arg5
        self.ctag = DE0fix2
    def __str__(self):
        return ("DEfix2(" + str(self.arg1) + str(self.arg2) + str(self.arg3) + str(self.arg4) + str(self.arg5) + ")")
############################################################
class dexp_cast(dexp):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = DE0cast
    def __str__(self):
        return ("DEcast(" + str(self.arg1) + str(self.arg2) + ")")
############################################################
#
def DE1cst(c00):
    return dexp_cst(c00)
#
def DE1var(x00):
    return dexp_var(x00)
def DE1lam(x00, de1):
    return dexp_lam(x00, de1)
def DE1app(de1, de2):
    return dexp_app(de1, de2)
#
def DE1int(i00):
    return dexp_int(i00)
def DE1btf(b00):
    return dexp_btf(b00)
#
def DE1opr(opr, des):
    return dexp_opr(opr, des)
#
def DE1if0(de1, de2, de3):
    return dexp_if0(de1, de2, de3)
#
def DE1fix(f00, x01, deb):
    return dexp_fix(f00, x01, deb)
#
def DE1nil0():
    return dexp_nil0()
def DE1cons(de1, de2):
    return dexp_cons(de1, de2)
def DE1pfst(tup):
    return dexp_pfst(tup)
def DE1psnd(tup):
    return dexp_psnd(tup)
#
def DE1let0(x00, de1, de2):
    return dexp_let0(x00, de1, de2)
#
def DE1lam2(x01, st1, de2):
    return dexp_lam2(x01, st1, de2)
def DE1fix2(f00, x01, st1, de2, st2):
    return dexp_fix2(f00, x01, st1, de2, st2)
#
def DE1cast(de1, st2):
    return dexp_cast(de1, st2)
#
############################################################
############################################################
# datatype dval =
# | DVint of sint
# | DVbtf of bool
# | DVlam of (dexp, denv)
# | DVfix of (dexp, denv)
############################################################
DV0int = 0
DV0btf = 1
DV0lam = 2
DV0fix = 3
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
############################################################
def dexp_evaluate(de0):
    def auxeval(de0, env):
        # print("auxeval: de0 =", de0)
        # print("auxeval: env =", env)
        if de0.ctag == DE0int:
            return dval_int(de0.arg1)
        if de0.ctag == DE0btf:
            return dval_btf(de0.arg1)
        if de0.ctag == DE0var:
            return denv_search2opt(env, de0.arg1)
        if de0.ctag == DE0lam:
            return dval_lam(de0, env.copy())
        if de0.ctag == DE0fix:
            return dval_fix(de0, env.copy())
        if de0.ctag == DE0app:
            dv1 = auxeval(de0.arg1, env)
            dv2 = auxeval(de0.arg2, env)
            if dv1.ctag == DV0lam:
                dea = dv1.arg1
                x01 = dea.arg1
                deb = dea.arg2
                env = dv1.arg2
                return auxeval(deb, env+[(x01, dv2)])
            if dv1.ctag == DV0fix:
                dea = dv1.arg1
                f00 = dea.arg1
                x01 = dea.arg2
                deb = dea.arg3
                env = dv1.arg2
                return auxeval(deb, env+[(f00, dv1), (x01, dv2)])
            raise TypeError(de0) # HX: should be deadcode!
        if (de0.ctag == DE0opr):
            opr = de0.arg1
            des = de0.arg2
            if (opr == "<"):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_btf(dv0.arg1 < dv1.arg1)
            if (opr == ">"):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_btf(dv0.arg1 > dv1.arg1)
            if (opr == "="):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_btf(dv0.arg1 == dv1.arg1)
            if (opr == "<="):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_btf(dv0.arg1 <= dv1.arg1)
            if (opr == ">="):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_btf(dv0.arg1 >= dv1.arg1)
            if (opr == "!="):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_btf(dv0.arg1 != dv1.arg1)
            if (opr == "+"):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_int(dv0.arg1 + dv1.arg1)
            if (opr == "-"):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_int(dv0.arg1 - dv1.arg1)
            if (opr == "*"):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_int(dv0.arg1 * dv1.arg1)
            if (opr == "/"):
                dv0 = auxeval(des[0], env)
                dv1 = auxeval(des[1], env)
                return dval_int(dv0.arg1 // dv1.arg1)
            raise TypeError(de0) # HX: unrecognized operator
        if (de0.ctag == DE0if0):
            dv1 = auxeval(de0.arg1, env)
            return auxeval(de0.arg2, env) \
                if (dv1.arg1) else auxeval(de0.arg3, env)
        raise TypeError(de0) # HX: should be deadcode!
    return auxeval(de0, [])
############################################################
############################################################
print("evaluate(DEint(0)) =", dexp_evaluate(DE1int(0)))
print("evaluate(DEbtf(True)) =", dexp_evaluate(DE1btf(True)))
############################################################
############################################################
def DE1lt(x, y):
    return DE1opr("<", [x, y])
def DE1gt(x, y):
    return DE1opr(">", [x, y])
def DE1eq(x, y):
    return DE1opr("=", [x, y])
def DE1lte(x, y):
    return DE1opr("<=", [x, y])
def DE1gte(x, y):
    return DE1opr(">=", [x, y])
def DE1neq(x, y):
    return DE1opr("!=", [x, y])
############################################################
def DE1add(x, y):
    return DE1opr("+", [x, y])
def DE1sub(x, y):
    return DE1opr("-", [x, y])
def DE1mul(x, y):
    return DE1opr("*", [x, y])
def DE1div(x, y):
    return DE1opr("/", [x, y])
############################################################
def DE1dbl():
    x = DE1var("x")
    return DE1lam("x", DE1add(x, x))
print("evaluate(DE1dbl(5)) =", dexp_evaluate(DE1app(DE1dbl(), DE1int(5))))
############################################################
def DE1fact():
    i0 = DE1int(0)
    i1 = DE1int(1)
    xf = DE1var("f")
    xn = DE1var("n")
    return DE1fix("f", "n", DE1if0(DE1gt(xn, i0), DE1mul(xn, DE1app(xf, DE1sub(xn, i1))), i1))
print("evaluate(DE1fact(5)) =", dexp_evaluate(DE1app(DE1fact(), DE1int(5))))
############################################################
############################################################
# end of [HWXI/CS525-2024-Fall/lambdas_lambda2_PYT3_lambda2.py]
############################################################
############################################################
