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
#typedef dexplst = list(dexp)
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
