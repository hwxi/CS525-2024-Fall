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
#typedef snam = strn
#typedef dvar = strn
#typedef dopr = strn
(* ****** ****** *)
//
datatype styp =
//
| STbas of snam
| STtup of (styp, styp)
| STfun of (styp, styp)
//
(*
HX-2024-10-01:
these are for error handling:
*)
| STpfst of (styp) // nontup
| STpsnd of (styp) // nontup
| STfarg of (styp) // nonfun
| STfres of (styp) // nonfun
//
(* ****** ****** *)
(* ****** ****** *)
//
val STint0 = STbas"int0"
val STbool = STbas"bool"
val STchar = STbas"char"
val STstrn = STbas"strn"
val STunit = STbas"unit"
//
(* ****** ****** *)
(* ****** ****** *)
//
datatype dexp =
//
|DEint of sint
|DEbtf of bool
//
|DEvar of dvar
|DElam of
(dvar, styp, dexp)
|DEapp of (dexp, dexp)
//
|DEopr of (dopr, list(dexp))
|DEif0 of (dexp, dexp, dexp)
//
|DEfix of
(dvar(*f*)
,dvar(*x*), styp, dexp, styp)
//
|DEnil0 of ()//unit
|DEcons of (dexp, dexp)//pair
//
|DEpfst of (dexp) // 1st project
|DEpsnd of (dexp) // 2nd project
//
// HX: information-node
|DEinfo of (dexp, styp(*computed*))
// HX: type-checking-node
|DEcast of (dexp, styp(*expected*))
//
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
STbas(snam) =>
prints("STbas(", snam, ")")
|
STtup(st1, st2) =>
prints("STtup(", st1, ",", st2, ")")
|
STfun(st1, st2) =>
prints("STfun(", st1, ",", st2, ")")
//
|
STpfst(sta) => prints("STpfst(",sta,")")
|
STpsnd(sta) => prints("STpsnd(",sta,")")
|
STfarg(sta) => prints("STfarg(",sta,")")
|
STfres(sta) => prints("STfres(",sta,")")
//
end//let
//
}(*where*) // end-of-[ styp_print<>(st0) ]
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
prints
("DEapp(", de1, ",", de2, ")")
//
|
DEopr(opr, des) =>
prints
("DEopr(", opr, ",", des, ")")
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
|DEpfst(dea) =>
prints("DEpfst(", dea, ")")
|DEpsnd(dea) =>
prints("DEpsnd(", dea, ")")
//
|DEinfo(dea, tpa) =>
(
  prints("DEinfo(", dea, ",", tpa, ")"))
|DEcast(dea, tpa) =>
(
  prints("DEcast(", dea, ",", tpa, ")"))
//
end//let
}(*where*) // end-of-[ dexp_print<>(de0) ]
//
(* ****** ****** *)
//
local
val styp_print__ = styp_print<>(*void*)
val dexp_print__ = dexp_print<>(*void*)
in//local
#impltmp g_print<styp> = styp_print__(*void*)
#impltmp g_print<dexp> = dexp_print__(*void*)
end//local
//
(* ****** ****** *)
(* ****** ****** *)
//
#typedef senv = list@(dvar, styp)
//
(* ****** ****** *)
(* ****** ****** *)
//
#extern
fun
dexp_tpcheck
(de0: dexp): dexp
#extern
fun
dexp_tpcheck_env
(de0: dexp, env: senv): dexp
//
(* ****** ****** *)
(* ****** ****** *)
//
#impltmp
dexp_tpcheck(de0) =
let
val env = list_nil() in
dexp_tpcheck_env(de0, env) end
//
(* ****** ****** *)
//
#impltmp
dexp_tpcheck_env
  (de0, env) =
(
case+ de0 of
//
|DEint _ =>
let
val st0 = STint0 in DEinfo(de0, st0)
end//let
|DEbtf _ =>
let
val st0 = STbool in DEinfo(de0, st0)
end//let
//
|DEnil0() =>
(
DEinfo(de0, STunit(*0*)))
//
|DEcons
(de1, de2) =>
let
//
val de1 =
dexp_tpcheck_env(de1, env)
val de2 =
dexp_tpcheck_env(de2, env)
//
in//let
(
DEinfo(DEcons(de1, de2), st0)
) where
{
val st0 =
(
  STtup(styp(de1), styp(de2))) }
end//let
//
|DEpfst(dea) =>
let
val dea =
dexp_tpcheck_env(dea, env)
in//let
(
DEinfo(DEpfst(dea), st1)) where
{
val sta = styp(dea)
val st1 =
(
case+ sta of
| STtup(st1, st2) => st1
| _(*non-STtup*) => STpfst(sta)) }
end//let
//
|DEpsnd(dea) =>
let
val dea =
dexp_tpcheck_env(dea, env)
in//let
(
DEinfo(DEpsnd(dea), st2)) where
{
val sta = styp(dea)
val st2 =
(
case+ sta of
| STtup(st1, st2) => st2
| _(*non-STtup*) => STpsnd(sta)) }
end//let
//
) where // end-of-[case+]
{
//
fun
styp(de0: dexp): styp =
(case+ de0 of DEinfo(de1, st0) => st0)
//
}(*where*)//end-of-[dexp_tpcheck_env(de0,env)]
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
