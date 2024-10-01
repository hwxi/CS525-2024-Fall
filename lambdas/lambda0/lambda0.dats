(* ****** ****** *)
(* ****** ****** *)
#include
"share\
/atspre_staload.hats"
(* ****** ****** *)
#include "./mylib00.dats"
(* ****** ****** *)
typedef sint = int
typedef bool = bool
typedef char = char
typedef strn = string
(* ****** ****** *)
implement main0 = lam () => ()
(* ****** ****** *)
(* ****** ****** *)
datatype term =
| TMvar of strn
| TMlam of (strn, term)
| TMapp of (term, term)
(* ****** ****** *)
//
val I = TMlam("x", TMvar("x"))
//
val K = TMlam("x", TMlam("y", TMvar("x")))
val K' = TMlam("x", TMlam("y", TMvar("y")))
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
extern
fun
print_term(tm0:term): void
extern
fun
fprint_term
(out:FILEref, tm0:term): void
//
implement
fprint_val<term> = fprint_term
//
overload print with print_term
overload fprint with fprint_term
//
(* ****** ****** *)
//
implement
print_term(tm0) =
fprint_term(stdout_ref, tm0)
//
implement
fprint_term
(out, tm0) =
(
case+ tm0 of
|
TMvar(x00) =>
fprint!(out, "TMvar(", x00, ")")
|
TMlam(x00, tm1) =>
fprint!(out, "TMlam(", x00, ",", tm1, ")")
|
TMapp(tm1, tm2) =>
fprint!(out, "TMapp(", tm1, ",", tm2, ")")
)
//
(* ****** ****** *)
(* ****** ****** *)
//
val () =
println!("Hello from [lambda0]!")
//
val () = println!("I = ", I)
val () = println!("K = ", K)
val () = println!("K' = ", K')
val () = println!("S = ", S)
//
(* ****** ****** *)
(* ****** ****** *)
//
(* ****** ****** *)(* ****** ****** *)
(* ****** ****** *)(* ****** ****** *)

(* end of [CS525-2024-Fall/lambdas/lambda0/lambda0.dats] *)
