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
(* ****** ****** *)
//
datatype term =
|
TMvar of tvar
|
TMlam of (tvar, term)
|
TMapp of (term, term)
//
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
TMvar(x00) =>
prints("TMvar(", x00, ")")
|
TMlam(x00, tm1) =>
prints("TMlam(", x00, ", ", tm1, ")")
|
TMapp(tm1, tm2) =>
prints("TMapp(", tm1, ", ", tm2, ")")
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
TMvar(x01) =>
if
(x00=x01)
then sub else tm0
|
TMlam(x01, tm1) =>
if
(x00=x01)
then tm0
else TMlam(x01, subst(tm1))
|
TMapp(tm1, tm2) =>
TMapp(subst(tm1), subst(tm2))
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
) where
{
(*
val () = prints
("term_evaluate: tm0 = ", tm0, "\n")
*)
}
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
prints
("SKKx = ", term_evaluate(SKKx), "\n")
end//let
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

(* end of [HWXI/Teaching/CS525-2024-Fall/lambdas_lambda0_XATS.dats] *)
