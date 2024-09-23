(* ****** ****** *)
(* ****** ****** *)
(*
HX-2024-09-10:
Tue 10 Sep 2024 01:39:29 PM EDT
*)
(* ****** ****** *)
(* ****** ****** *)
#staload UN =
"prelude/SATS/unsfx00.sats"
(* ****** ****** *)
(* ****** ****** *)
#staload _ =
"prelude/DATS/gdbg000.dats"
(* ****** ****** *)
(* ****** ****** *)
#include
"srcgen2\
/prelude/HATS/prelude_dats.hats"
#include
"xatslib\
/githwxi/HATS/githwxi_dats.hats"
(* ****** ****** *)
(* ****** ****** *)
#include
"srcgen2\
/prelude/HATS/prelude_JS_dats.hats"
#include
"xatslib/HATS/xatslib_JS_dats.hats"
(* ****** ****** *)
(* ****** ****** *)
//
#include
"srcgen2\
/prelude/HATS/prelude_NODE_dats.hats"
//
(* ****** ****** *)
(* ****** ****** *)
//
val () = prints
("Hello from [lambda1]!\n")
//
(* ****** ****** *)
(* ****** ****** *)
#typedef tvar = strn
#typedef topr = strn
(* ****** ****** *)
//
datatype term =
//
|TMint of sint
|TMbtf of bool
//
|TMvar of tvar
|TMlam of (tvar, term)
|TMapp of (term, term)
//
|TMopr of (topr, list(term))
|TMif0 of (term, term, term)
//
|TMfix of (tvar, tvar, term)
//
#typedef termlst = list(term)
//
(* ****** ****** *)
#symload app with TMapp of 1000
(* ****** ****** *)
(*
#symload nil with list_nil
#symload cons with list_cons
*)
(* ****** ****** *)
(* ****** ****** *)
//
#extern
fun<>
term_print
(tm0: term): void
//
#impltmp
<(*tmp*)>
term_print
(  tm0  ) =
(
  auxpr(tm0)) where
{
fun
auxpr(tm0) =
let
//
#impltmp
g_print<term> = auxpr
//
in//let
//
case+ tm0 of
|
TMint(int) =>
prints("TMint(", int, ")")
|
TMbtf(btf) =>
prints("TMbtf(", btf, ")")
|
TMvar(x01) =>
prints("TMvar(", x01, ")")
|
TMlam(x01, tm1) =>
prints("TMlam(", x01, ",", tm1, ")")
|
TMapp(tm1, tm2) =>
prints("TMapp(", tm1, ",", tm2, ")")
//
|
TMopr(opr, tms) =>
prints("TMopr(", opr, ",", tms, ")")
//
|
TMif0(tm1, tm2, tm3) =>
prints
("TMif0(", tm1, ",", tm2, ",", tm3, ")")
//
|
TMfix(f00, x01, tma) =>
prints
("TMfix(", f00, ",", x01, ",", tma, ")")
//
end//let
}(*where*)//end-of-[term_print<>( tm0 )]
//
local
val term_print__ = term_print<>
in//local
#impltmp g_print<term> = term_print__
end//local
//
(* ****** ****** *)
(* ****** ****** *)
//
datatype dval =
//
| DVint of sint
| DVbtf of bool
| DVlam of (term, denv)
| DVfix of (term, denv)
//
where
{
#typedef
denv = list@(tvar, dval)
}
//
#typedef dvalist = list(dval)
//
(* ****** ****** *)
(* ****** ****** *)
//
#extern
fun<>
dval_print
(dv0: dval): void
//
#impltmp
<(*tmp*)>
dval_print(dv0) =
(
//
case+ dv0 of
|DVint(i00) =>
prints("DVint(", i00, ")")
|DVbtf(b00) =>
prints("DVbtf(", b00, ")")
|DVlam(tma, env) =>
prints("DVlam(", "...", ")")
|DVfix(tma, env) =>
prints("DVfix(", "...", ")")
//
)
//
local
val dval_print__ = dval_print<>
in//local
#impltmp g_print<dval> = dval_print__
end//local
//
(* ****** ****** *)
//
#impltmp
g_print
<denv>(denv) =
let
val () =
(
 prints("DENV("))
//
val () =
list_iforitm_f2un
(
denv,
lam(i, x) => (
if
(i > 0)
then pstrn(","); print( x )))
//
val () = prints(     ")"     )
end(*let*)//end-of-[g_print<denv>(denv)]
//
(* ****** ****** *)
(* ****** ****** *)
//
fun
denv_search$opt
( env: denv
, x00: tvar)
: optn_vt(dval) =
(
let
val opt =
strm_vt_head$opt0<kx>
(
gseq_filter_lstrm(env))
in//let
case+ opt of
| ~
optn_vt_nil
  ((*0*)) => optn_vt_nil()
| ~
optn_vt_cons
  ( kx0 ) => optn_vt_cons(kx0.1)
end
) where
{
#typedef kx = @(tvar, dval)
#impltmp
filter$test<kx>(kx0) = (x00 = kx0.0)
}
//
(* ****** ****** *)
(* ****** ****** *)
//
fun
term_evaluate
(tm0: term): dval =
(
  auxeval(tm0, env))
where
{
val env = list_nil()
//
fun
auxeval
(tm0: term, env: denv): dval =
(
case+ tm0 of
//
|
TMint(i00) => DVint(i00)
|
TMbtf(b00) => DVbtf(b00)
//
|
TMvar(x00) =>
let
//
val opt =
denv_search$opt(env, x00)
//
val ( ) =
if
nilq1(opt)
then prints(
"term_evaluate: ",
"auxeval: tm0 = ", tm0, "\n")
//
in//let
//
case+
opt of ~optn_vt_cons(dv0) => dv0
//
end//let
//
(* ****** ****** *)
|
TMlam _ => DVlam(tm0, env)
|
TMfix _ => DVfix(tm0, env)
//
(* ****** ****** *)
//
|
TMapp(tm1, tm2) =>
let
val dv1 = auxeval(tm1, env)
val dv2 = auxeval(tm2, env)
in//let
//
case- dv1 of
|
DVlam(tma, env) =>
let
val-
TMlam
(x01, tmb) = tma
in//let
(
auxeval(tmb, env)) where
{
val
env =
list_cons((x01, dv2), env) }
//
end//let
|
DVfix(tma, env) =>
let
val-
TMfix
(f00, x01, tmb) = tma
in//let
(
auxeval(tmb, env)) where
{
val
env =
list_cons((f00, dv1), env)
val
env =
list_cons((x01, dv2), env) }
end//let
//
end//end//end-of-[TMapp(tm1,tm2)]
//
|
TMopr(opr, tms) =>
(
term$opr_evaluate(opr, dvs))
where
{
val dvs = list_map_f1un
(tms, lam(tmx) => auxeval(tmx, env))
}
//
|
TMif0(tm1, tm2, tm3) =>
let
val dv1 = auxeval(tm1, env)
in//let
case- dv1 of
|DVbtf(btf) =>
(
 auxeval(ifval(btf, tm2, tm3), env))
end//let
//
)(*case+*)//end-of-[auxeval(tm0,env)]
//
}(*where*)//end-of-[term_evaluate(tm0)]
//
and
term$opr_evaluate
(opr: topr, dvs: dvalist) =
(
case+ opr of
//
| "+" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), _) = dvs in DVint(i01+i02)
end//let
| "-" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
in//let
(
case+ dvs of
| list_nil() => DVint(-i01)
| list_cons
( DVint(i02), dvs ) => DVint(i01 - i02))
end//let
| "*" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVint(i01*i02)
end//let
| "/" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVint(i01/i02)
end//let
| "%" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVint(i01%i02)
end//let
//
| "~" =>
let
val-
list_cons
(DVbtf(b01), dvs) = dvs in DVbtf( ~ b01 )
end//let
//
| "<" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVbtf(i01<i02)
end//let
| ">" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVbtf(i01>i02)
end//let
| "=" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVbtf(i01=i02)
end//let
//
| "<=" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVbtf(i01<=i02)
end//let
| ">=" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVbtf(i01>=i02)
end//let
| "!=" =>
let
val-
list_cons
(DVint(i01), dvs) = dvs
val-
list_cons
(DVint(i02), dvs) = dvs in DVbtf(i01!=i02)
end//let
//
) where
{
(*
val () =
prints("term$opr_evaluate: opr = ", opr, "\n")
val () =
prints("term$opr_evaluate: dvs = ", dvs, "\n")
*)
}(*where+*)//end-of-[term$opr_evaluate(opr,dvs)]
//
(* ****** ****** *)
(* ****** ****** *)
//
fun
TMadd(tm1, tm2) =
TMopr("+", list@(tm1, tm2))
fun
TMsub(tm1, tm2) =
TMopr("-", list@(tm1, tm2))
fun
TMmul(tm1, tm2) =
TMopr("*", list@(tm1, tm2))
fun
TMdiv(tm1, tm2) =
TMopr("/", list@(tm1, tm2))
fun
TMmod(tm1, tm2) =
TMopr("%", list@(tm1, tm2))
//
(* ****** ****** *)
#symload + with TMadd of 1000
#symload - with TMsub of 1000
#symload * with TMmul of 1000
#symload / with TMdiv of 1000
#symload % with TMmod of 1000
(* ****** ****** *)
(* ****** ****** *)
//
val TMtt0 = TMbtf(true)
val TMff0 = TMbtf(false)
//
fun
TMneg(tm1) = TMopr("~", tm1)
fun
TMand(tm1, tm2) = TMif0(tm1, tm2, TMff0)
fun
TMor0(tm1, tm2) = TMif0(tm1, TMtt0, tm2)
//
(* ****** ****** *)
#symload && with TMand of 1000
#symload || with TMor0 of 1000
(* ****** ****** *)
(* ****** ****** *)
//
fun
TMilt(tm1, tm2) =
TMopr("<", list@(tm1, tm2))
fun
TMigt(tm1, tm2) =
TMopr(">", list@(tm1, tm2))
fun
TMieq(tm1, tm2) =
TMopr("=", list@(tm1, tm2))
//
fun
TMilte(tm1, tm2) =
TMopr("<=", list@(tm1, tm2))
fun
TMigte(tm1, tm2) =
TMopr(">=", list@(tm1, tm2))
fun
TMineq(tm1, tm2) =
TMopr("!=", list@(tm1, tm2))
//
(* ****** ****** *)
#symload < with TMilt of 1000
#symload > with TMigt of 1000
#symload = with TMieq of 1000
#symload <= with TMilte of 1000
#symload >= with TMigte of 1000
#symload != with TMineq of 1000
(* ****** ****** *)
(* ****** ****** *)
//
val TMsqr =
let
val x = TMvar"x" in TMlam("x", x*x)
end
//
val () = prints(
"TMsqr\\app(TMint(10)) = ",
term_evaluate(TMsqr\app(TMint(10))), "\n")
//
(* ****** ****** *)
(* ****** ****** *)
//
val TMfact =
let
val i1 = TMint 1
val xf = TMvar"f"
val xn = TMvar"n"
in//let
TMfix("f", "n", 
TMif0(xn > i1, xn * TMapp(xf, xn-i1), i1))
end//let//end-of-[TMfact]
//
val () = prints(
"TMfact\\app(TMint(10)) = ",
term_evaluate(TMfact\app(TMint(10))), "\n")
//
(* ****** ****** *)
(* ****** ****** *)
//
val TMfibo =
let
val i1 = TMint 1
val i2 = TMint 2
val xf = TMvar"f"
val xn = TMvar"n"
in//let
TMfix("f", "n", 
TMif0(xn >= i2,
TMapp(xf, xn-i2)+TMapp(xf, xn-i1), xn))
end//let//end-of-[TMfibo]
//
val () = prints(
"TMfibo\\app(TMint(10)) = ",
term_evaluate(TMfibo\app(TMint(10))), "\n")
//
(* ****** ****** *)
(* ****** ****** *)
//
(*
val () = console_log(the_print_store_flush())
*)
//
(* ****** ****** *)
(* ****** ****** *)
//
(* ****** ****** *)(* ****** ****** *)(* ****** ****** *)
(* ****** ****** *)(* ****** ****** *)(* ****** ****** *)

(* end of [HWXI/CS525-2024-Fall/lambdas_lambda1_XATS_lambda1.dats] *)
