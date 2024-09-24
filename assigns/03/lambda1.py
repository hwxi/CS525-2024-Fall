############################################################
#
# Assign03 for CS525, Fall, 2024
# It is due the 2nd of October, 2024
# Note that the due time is always 11:59pm of
# the due date unless specified otherwise.
#
############################################################
#
# HX: This part is worth 50 points
#
# Please extend the closure based evaluator
# in the following file
# ./../../lambdas/lambda1/XATS/lambda1.dats
# More specifically, please also handle the additional
# language constructs in the following datatype definition
# Also, please introduce three operators: nilq, pfst, psnd:
#
# nilq: testing if a value is DVnil0()
# pfst: takes DVcons(dv1, dv2) and returns dv1
# psnd: takes DVcons(dv1, dv2) and returns dv2
#
############################################################
#
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
# |TMfix of (tvar, tvar, term)
#
# |TMnil0 of () // nil(): empty tuple
# |TMcons of (term, term) // cons(t1, t2): tuple of length 2 (pair)
# |TMlet0 of (tvar, term, term) // TMlet0(x, t1, t2): let x = t1 in t2 end
#
# datatype dval =
#
# | DVint of sint
# | DVbtf of bool
# | DVlam of (term, denv)
# | DVfix of (term, denv)
# | DVnil0 of () // for TMnil0()
# | DVcons of (dval, dval) // for TMcons0()
#
############################################################
# end of [HWXI/CS525-2024-Fall/assigns/03/lambda1.py]
############################################################
