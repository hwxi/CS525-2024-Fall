############################################################
#
# Assign02 for CS525, Fall, 2024
# It is due the 25th of September, 2024
# Note that the due time is always 11:59pm of
# the due date unless specified otherwise.
#
############################################################
# HX-2024-09-19:
# Compiling an extended lambda-calculus to
# Church's pure lambda-calculus
############################################################
# //
# datatype term =
# //
# |TMint of sint
# |TMbtf of bool
# //
# |TMvar of tvar
# |TMlam of (tvar, term)
# |TMapp of (term, term)
# //
# |TMopr of (topr, list(term))
# |TMif0 of (term, term, term)
# //
# #typedef termlst = list(term)
# //
############################################################
#
TM0var = 0
TM0lam = 1
TM0app = 2
#
TM0int = 3
TM0btf = 4
TM0opr = 5
TM0if0 = 5
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
def TM1var(x00):
    return term_var(x00)
def TM1lam(x00, tm1):
    return term_lam(x00, tm1)
def TM1app(tm1, tm2):
    return term_app(tm1, tm2)
#
############################################################
############################################################
#
# HX-2024-09-19:
# Points: 50
# This assignment asks you to translate
# a given lambda-term in the above extended lambda-calculus
# into Church's pure lambda-calculus.
# More specifically, given a term tm0 (which may contain
# extended constructs like TMint, TMbtf, TMopr, and TMif0),
# the following function assign02_transpile should return a
# term tm1 that contains only constructs TMvar, TMlam, and
# TMapp. In addition, if tm0 evaluates to an integer n, then
# tm1 should evaluate to a lambda-term beta-equivalent to the
# Church numeral representing n.
#
def assign02_transpile(tm0):
  raise NotImplementedError
############################################################
############################################################
# end of [HWXI/CS525-2024-Fall/assigns/02/lambda0.py]
############################################################
