(* ****** ****** *)
(* ****** ****** *)
(*
HX-2024-09-30:
Mon Sep 30 11:37:04 PM EDT 2024
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
(*
#include
"srcgen2\
/prelude/HATS/prelude_NODE_dats.hats"
*)
//
(* ****** ****** *)
(* ****** ****** *)
//
val () = prints
("Hello from [lambda2]!\n")
//
(* ****** ****** *)
(* ****** ****** *)
#typedef tnam = strn
#typedef tvar = strn
#typedef topr = strn
(* ****** ****** *)
//
datatype styp =
| STbas of tnam
| STtup of (styp, styp)
| STfun of (styp, styp)
//
(* ****** ****** *)
//
datatype dexp =
//
|DEint of sint
|DEbtf of bool
//
|DEvar of tvar
|DElam of
(tvar, styp, dexp)
|DEapp of (dexp, dexp)
//
|DEopr of (topr, list(dexp))
|DEif0 of (dexp, dexp, dexp)
//
|DEfix of
(tvar(*f*)
,tvar(*x*), styp, dexp, styp)
//
|DEnil0 of ()
|DEcons of (dexp, dexp)
//
|DEpfst of (dexp) // 1st proj
|DEpsnd of (dexp) // 2nd proj
//
(* ****** ****** *)
#typedef dexplst = list(dexp)
(* ****** ****** *)
(* ****** ****** *)
//
#extern
fun<>
styp_print(st0: styp): void
#extern
fun<>
dexp_print(de0: dexp): void
//
(* ****** ****** *)
(* ****** ****** *)
//
#impltmp
<(*tmp*)>
styp_print
(  st0  ) =
(
  auxpr(st0)) where
{
//
fun
auxpr(st0) =
let
//
#impltmp
g_print<styp> = auxpr
//
in//let
//
case+ st0 of
|
STbas(tnam) =>
prints("STbas(", tnam, ")")
|
STtup(st1, st2) =>
prints("STtup(", st1, ",", st2, ")")
|
STfun(st1, st2) =>
prints("STfun(", st1, ",", st2, ")")
//
end//let
//
}(*where*)//end-of-[styp_print<>(st0)]
//
(* ****** ****** *)
(* ****** ****** *)
//
#impltmp
<(*tmp*)>
dexp_print
(  de0  ) =
(
  auxpr(de0)) where
{
//
fun
auxpr(de0) =
let
//
#impltmp
g_print<dexp> = auxpr
//
in//let
//
case+ de0 of
|
DEint(int) =>
prints("DEint(", int, ")")
|
DEbtf(btf) =>
prints("DEbtf(", btf, ")")
|
DEvar(x01) =>
prints("DEvar(", x01, ")")
|
DElam
(x01, st1, de1) =>
prints("DElam(",
x01, ",", st1, ",", de1, ")")
|
DEapp(de1, de2) =>
prints("DEapp(", de1, ",", de2, ")")
//
|
DEopr(opr, des) =>
prints("DEopr(", opr, ",", des, ")")
//
|
DEif0(de1, de2, de3) =>
prints(
"DEif0(", de1, ",", de2, ",", de3, ")")
//
|
DEfix
(f00
,x01, st1, dea, sta) =>
prints("DEfix(",
f00, ",",
x01, ",", st1, ",", dea, ",", sta, ")")
//
|
DEnil0() =>
prints("DEnil(", ")")
|
DEcons(de1, de2) =>
prints
("DEcons(", de1, ",", de2, ")")
//
|DEpfst
( tup ) => prints("DEpfst(", tup, ")")
|DEpsnd
( tup ) => prints("DEpsnd(", tup, ")")
//
end//let
}(*where*) // end-of-[ dexp_print<>(de0) ]
//
(* ****** ****** *)
//
local
val dexp_print__ = dexp_print<>(*void*)
in//local
#impltmp g_print<dexp> = dexp_print__(*void*)
end//local
//
(* ****** ****** *)
(* ****** ****** *)
//
val () = console_log(the_print_store_flush())
//
(* ****** ****** *)
(* ****** ****** *)
//
(* ****** ****** *)(* ****** ****** *)(* ****** ****** *)
(* ****** ****** *)(* ****** ****** *)(* ****** ****** *)

(* end of [HWXI/CS525-2024-Fall/lambdas_lambda2_XATS_lambda2.dats] *)
