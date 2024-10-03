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
typedef tvar = strn
(* ****** ****** *)
datatype term =
| TMcst of strn
| TMvar of tvar
| TMlam of (tvar, term)
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
TMcst(c01) =>
fprint!(out, "TMcst(", c01, ")")
|
TMvar(x01) =>
fprint!(out, "TMvar(", x01, ")")
|
TMlam(x01, tm1) =>
fprint!(out, "TMlam(", x01, ",", tm1, ")")
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
val () = println!("S = ", S)
val () = println!("K' = ", K')
//
(* ****** ****** *)
(* ****** ****** *)
//
//
fun
term_subst
(tm0: term
,x00: tvar, sub: term): term =
(
case+ tm0 of
|TMcst(c01) => tm0
|TMvar(x01) =>
if (x00=x01) then sub else tm0
//
|
TMlam(x01, tm1) =>
( if
  (x00=x01)
  then (tm0)
  else TMlam(x01, subst(tm1)))
//
|
TMapp(tm1, tm2) =>
(
  TMapp(subst(tm1), subst(tm2)))
//
) where
{
fun subst(tmx) = term_subst(tmx, x00, sub)
}
//
(* ****** ****** *)
(* ****** ****** *)
//
fun
term_evaluate
(tm0: term): term =
(
case+ tm0 of
//
|TMcst _ => tm0
//
|TMvar _ => tm0
//
|TMlam _ => tm0
//
|TMapp(tm1, tm2) =>
let
val tm1 =
term_evaluate(tm1)
in//let
case+ tm1 of
|
TMlam(x01, tma) =>
(
  term_evaluate(term_subst(tma, x01, tm2)))
|
_(* non-TMlam *) => TMapp(tm1, term_evaluate(tm2))
end
)
//
(* ****** ****** *)
(* ****** ****** *)
//
fun
Church$numeral_evaluate
  (num0: term): term =
term_evaluate
(TMapp(TMapp(num0, f), x)) where
{
  val x = TMcst"x" and f = TMcst"f"
}
//
(* ****** ****** *)
(* ****** ****** *)
//
val f = "f"
val x = "x"
val y = "y"
val m = "m"
val n = "n"
val p = "p"
//
val TMfact4 =
TMapp(TMapp(TMlam(f,TMapp(TMlam(x,TMapp(TMvar(f),TMapp(TMvar(x),TMvar(x)))),TMlam(x,TMapp(TMvar(f),TMapp(TMvar(x),TMvar(x)))))),TMlam(f,TMlam(n,TMapp(TMapp(TMapp(TMapp(TMapp(TMlam(n,TMapp(TMapp(TMvar(n),TMlam(x,TMlam(x,TMlam(y,TMvar(y))))),TMlam(x,TMlam(y,TMvar(x))))),TMapp(TMapp(TMlam(f,TMlam(x,TMvar(x))),TMlam(n,TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(x))))),TMapp(TMapp(TMvar(n),TMlam(p,TMapp(TMapp(TMlam(x,TMlam(y,TMlam(f,TMapp(TMapp(TMvar(f),TMvar(x)),TMvar(y))))),TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(y))))),TMvar(p))),TMapp(TMlam(n,TMlam(f,TMlam(x,TMapp(TMvar(f),TMapp(TMapp(TMvar(n),TMvar(f)),TMvar(x)))))),TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(y))))),TMvar(p)))))),TMapp(TMapp(TMlam(x,TMlam(y,TMlam(f,TMapp(TMapp(TMvar(f),TMvar(x)),TMvar(y))))),TMlam(f,TMlam(x,TMvar(x)))),TMlam(f,TMlam(x,TMvar(x)))))))),TMvar(n))),TMlam(x,TMlam(y,TMvar(y)))),TMlam(x,TMlam(y,TMvar(x)))),TMapp(TMapp(TMlam(m,TMlam(n,TMlam(f,TMlam(x,TMapp(TMapp(TMvar(m),TMapp(TMvar(n),TMvar(f))),TMvar(x)))))),TMvar(n)),TMapp(TMvar(f),TMapp(TMapp(TMlam(f,TMlam(x,TMapp(TMvar(f),TMvar(x)))),TMlam(n,TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(x))))),TMapp(TMapp(TMvar(n),TMlam(p,TMapp(TMapp(TMlam(x,TMlam(y,TMlam(f,TMapp(TMapp(TMvar(f),TMvar(x)),TMvar(y))))),TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(y))))),TMvar(p))),TMapp(TMlam(n,TMlam(f,TMlam(x,TMapp(TMvar(f),TMapp(TMapp(TMvar(n),TMvar(f)),TMvar(x)))))),TMapp(TMlam(p,TMapp(TMvar(p),TMlam(x,TMlam(y,TMvar(y))))),TMvar(p)))))),TMapp(TMapp(TMlam(x,TMlam(y,TMlam(f,TMapp(TMapp(TMvar(f),TMvar(x)),TMvar(y))))),TMlam(f,TMlam(x,TMvar(x)))),TMlam(f,TMlam(x,TMvar(x)))))))),TMvar(n))))),TMlam(f,TMlam(x,TMapp(TMvar(f),TMvar(x)))))))),TMlam(f,TMlam(x,TMapp(TMvar(f),TMapp(TMvar(f),TMapp(TMvar(f),TMapp(TMvar(f),TMvar(x))))))))
//
val () = println!("TMfact4 = ", Church$numeral_evaluate(term_evaluate(TMfact4)))
//
(* ****** ****** *)
(* ****** ****** *)
//
(* ****** ****** *)(* ****** ****** *)
(* ****** ****** *)(* ****** ****** *)

(* end of [CS525-2024-Fall/lambdas/lambda0/lambda0.dats] *)
