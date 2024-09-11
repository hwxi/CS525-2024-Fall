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
//
(* ****** ****** *)
(* ****** ****** *)
#include
"srcgen2\
/prelude/HATS/prelude_JS_dats.hats"
#include
"xatslib/HATS/xatslib_JS_dats.hats"
//
(* ****** ****** *)
(* ****** ****** *)
//
#include
"srcgen2\
/prelude/HATS/prelude_NODE_dats.hats"
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
//
|TMvar of tvar
|TMlam of (tvar, term)
|TMapp of (term, term)
//
|TMopr of (topr, list(term))
//
#typedef termlst = list(term)
//
(* ****** ****** *)
(* ****** ****** *)
(*
#symload nil with list_nil
#symload cons with list_cons
*)
(* ****** ****** *)
(* ****** ****** *)
//
#impltmp
g_print
<term>(tm0) =
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
TMint(i00) =>
prints("TMint(", i00, ")")
|
TMvar(x00) =>
prints("TMvar(", x00, ")")
|
TMlam(x00, tm1) =>
prints("TMlam(", x00, ", ", tm1, ")")
|
TMapp(tm1, tm2) =>
prints("TMapp(", tm1, ", ", tm2, ")")
//
|
TMopr(opr, tms) =>
prints("TMopr(", opr, ", ", tms, ")")
//
end//let
}(*where*)//end-of-[g_print<term>(tm0)]
//
(* ****** ****** *)
(* ****** ****** *)
//
(*
val () =
prints("Hello from [lambda0]!\n")
*)
//
(* ****** ****** *)
(* ****** ****** *)
//
val I = TMlam("x", TMvar("x"))
//
val K = TMlam("x", TMlam("y", TMvar("x")))
val K1 = TMlam("x", TMlam("y", TMvar("y")))
//
val S =
let
val x = TMvar"x" and y = TMvar"y" and z = TMvar"z"
in//let
TMlam("x", TMlam("y", TMlam("z", TMapp(TMapp(x, z), TMapp(y, z)))))
end//let
//
(* ****** ****** *)
//
val omega =
let
val x = TMvar"x" in
TMlam("x", TMapp(x, x)) end
val Omega = TMapp(omega, omega)
//
(* ****** ****** *)
//
fun
f_omega
(f: term): term =
let
val x = TMvar"x" in
TMlam
("x", TMapp(f, TMapp(x, x)))
end//let//end-of-[f_omega(f)]
//
fun
f_Omega
(f: term): term =
TMapp(fomega, fomega)
where { val fomega = f_omega(f) }
//
(*
HX: The famous Y-combinator:
*)
val Y = TMlam("f", f_Omega(TMvar"f"))
//
(* ****** ****** *)
(* ****** ****** *)
//
val () = prints("I = ", I, "\n")
val () = prints("K = ", K, "\n")
val () = prints("S = ", S, "\n")
val () = prints("K1 = ", K1, "\n")
val () = prints("omega = ", omega, "\n")
val () = prints("Omega = ", Omega, "\n")
val () = prints("Y = ", Y, "\n")
//
(* ****** ****** *)
(* ****** ****** *)
//
fun
term_subst
(tm0: term
,x00: tvar, sub: term): term =
(
case+ tm0 of
|
TMint _ => tm0
|
TMvar(x01) =>
if
(x00=x01)
then sub else tm0
|
TMlam(x01, tm1) =>
if
(x00=x01)
then (tm0)
else TMlam(x01, subst(tm1))
|
TMapp(tm1, tm2) =>
TMapp(subst(tm1), subst(tm2))
//
|
TMopr(opr, tms) =>
TMopr(opr, list_map(tms, subst))
) where
{
fun
subst(tmx) = term_subst(tmx, x00, sub)
}
//
(* ****** ****** *)
(* ****** ****** *)
//
fun
term_beta$red
( tm1: term
, tm2: term): term =
let
val-TMlam(x00, tma) = tm1
in//let
  term_subst(tma, x00, tm2)
end//end
//
(* ****** ****** *)
//
fun
term_evaluate
(tm0: term): term =
(
case+ tm0 of
//
|TMint _ => tm0
|TMvar _ => tm0
|TMlam _ => tm0
//
|
TMapp(tm1, tm2) =>
let
val
tm1 = term_evaluate(tm1)
in//let
case+ tm1 of
|
TMlam _ =>
term_evaluate
(term_beta$red(tm1, tm2))
|
_(*non-TMlam*) =>
TMapp(tm1, term_evaluate(tm2))
end//let
//
|
TMopr(opr, tms) =>
let
val tms =
list_map(tms, term_evaluate)
in//let
  term$opr_evaluate(opr, tms)
end//end
//
) where
{
(*
val () = prints
("term_evaluate: tm0 = ", tm0, "\n")
*)
}
//
and
term$opr_evaluate
(opr: topr, tms: termlst) =
(
case- opr of
//
| "+" =>
(
let
val-
list_cons
(TMint(i01), tms) = tms
val-
list_cons
(TMint(i02), tms) = tms in TMint(i01+i02)
end//let
)
//
| "-" =>
(
let
val-
list_cons
(TMint(i01), tms) = tms
val-
list_cons
(TMint(i02), tms) = tms in TMint(i01-i02)
end//let
)
//
| "*" =>
(
let
val-
list_cons
(TMint(i01), tms) = tms
val-
list_cons
(TMint(i02), tms) = tms in TMint(i01*i02)
end//let
)
//
| "/" =>
(
let
val-
list_cons
(TMint(i01), tms) = tms
val-
list_cons
(TMint(i02), tms) = tms in TMint(i01/i02)
end//let
)
//
)(*case+*)//end-of-[term$opr_evaluate(opr,tms)]
//
(* ****** ****** *)
//
#symload
evaluate with term_evaluate
//
(* ****** ****** *)
(* ****** ****** *)
//
val () =
let
val x = TMvar"x"
val SKKx =
TMapp(TMapp(TMapp(S, K), K), x)
in//let
prints("SKKx = ", evaluate(SKKx), "\n")
end//let
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
//
(* ****** ****** *)
#symload + with TMadd of 1000
#symload - with TMsub of 1000
#symload * with TMmul of 1000
#symload / with TMdiv of 1000
(* ****** ****** *)
//
val () = prints
("TMint(1)+TMint(2) = "
,evaluate(TMint(1)+TMint(2)), "\n")
//
val () = prints
("TMint(1)-TMint(2) = "
,evaluate(TMint(1)-TMint(2)), "\n")
//
val () = prints
("TMint(1)*TMint(2) = "
,evaluate(TMint(1)*TMint(2)), "\n")
//
val () = prints
("TMint(1)/TMint(2) = "
,evaluate(TMint(1)/TMint(2)), "\n")
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

(* end of [HWXI/CS525-2024-Fall/lambdas_lambda0_XATS_lambda0.dats] *)
