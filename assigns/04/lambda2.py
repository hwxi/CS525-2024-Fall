############################################################
# HX-2024-10-12:
# Type-checking for some
# extended lambda-calculus
# This part is worth 60 points
# Please see assign04.py for another 40 points
# The total number of points for Assign04 is 60+40=100
# Please see lambdas/XATS/lambda2.dats
# for a mostly completed implementation of a type-checker 
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
# datatype dexp =
# | DEvar of strn
# | DElam of (strn, dexp)
# | DEapp of (dexp, dexp)
# | DEint of (sint)
# | DEbtf of (bool)
# | DEopr of (strn, list(dexp))
# | DEif0 of (dexp, dexp, dexp)
# | DEfix of (strn, strn, dexp)
################################################
# | DEnil0 of ()//unit
# | DEcons of (dexp, dexp)//pair
# | DEpfst of (dexp) // 1st project
# | DEpsnd of (dexp) // 2nd project
################################################
# | DElam2 of (strn, styp, dexp)
# | DEfix2 of (strn, strn, styp, dexp, styp)
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
DE0fix = 7
DE0if0 = 8
#
DE0nil0 = 9
DE0cons = 10
DE0pfst = 11
DE0psnd = 12
#
DE0cast = 13 # for type casting
#
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
def DE1fix(f00, x01, deb):
    return dexp_fix(f00, x01, deb)
#
def DE1if0(de1, de2, de3):
    return dexp_if0(de1, de2, de3)
#
############################################################
############################################################
# end of [HWXI/CS525-2024-Fall/assigns/04/lambda2.py]
############################################################
