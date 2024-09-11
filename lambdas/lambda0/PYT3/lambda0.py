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
TMvar0 = 0
TMlam0 = 1
TMapp0 = 2
#
class term:
    ctag = -1
    def get_ctag(self):
        return self.ctag
# end-of-class(term)
#
class term_var(term):
    def __init__(self, arg1):
        self.arg1 = arg1
        self.ctag = TMvar0
    def __str__(self):
        return ("TMvar(" + self.arg1 + ")")
# end-of-class(term_var(term))
#
class term_lam(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = TMlam0
    def __str__(self):
        return ("TMlam(" + self.arg1 + "," + str(self.arg2) + ")")
# end-of-class(term_lam(term))
#
class term_app(term):
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        self.ctag = TMapp0
    def __str__(self):
        return ("TMapp(" + str(self.arg1) + "," + str(self.arg2) + ")")
# end-of-class(term_app(term))
#
############################################################
#
def TMvar1(x00):
    return term_var(x00)
def TMlam1(x00, tm1):
    return term_lam(x00, tm1)
def TMapp1(tm1, tm2):
    return term_app(tm1, tm2)
#
############################################################
#
def I():
    x = TMvar1("x")
    return TMlam1("x", x)
def K():
    x = TMvar1("x")
    return TMlam1("x", TMlam1("y", x))
def S():
    x = TMvar1("x")
    y = TMvar1("y")
    z = TMvar1("z")
    return TMlam1("x", TMlam1("y", TMlam1("z", TMapp1(TMapp1(x, z), TMapp1(y, z)))))
#
_ = print("I =", I())
_ = print("K =", K())
_ = print("S =", S())
#
############################################################
############################################################

