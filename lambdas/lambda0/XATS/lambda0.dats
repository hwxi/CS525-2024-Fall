(* ****** ****** *)
(* ****** ****** *)
(*
HX-2024-09-05:
Thu 05 Sep 2024 05:36:54 PM EDT
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
//
datatype term =
| TMvar of strn
| TMlam of (strn, term)
| TMapp of (term, term)
//
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

val () = prints("I = ", I, "\n")
val () = prints("K = ", K, "\n")
val () = prints("S = ", S, "\n")
val () = prints("K1 = ", K1, "\n")

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
