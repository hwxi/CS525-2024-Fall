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
TMint(int) =>
prints("TMint(", int, ")")
|
TMbtf(btf) =>
prints("TMbtf(", btf, ")")
|
TMvar(x00) =>
prints("TMvar(", x00, ")")
|
TMlam(x00, tm1) =>
prints("TMlam(", x00, ",", tm1, ")")
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
prints("TMif0(", tm1, ",", tm2, ",", tm3, ")")
//
|
TMfix(f00, x00, tm1) =>
prints("TMfix(", f00, ",", x00, ",", tm1, ")")
//
end//let
}(*where*)//end-of-[g_print<term>(tm0)]
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
