(* This is a comment :D *)

val x = 34; 
(* static environment: x : int *)
(* dynamic environment: x --> 34 *)

val y = 17;
(* static environment: x : int, y : int +*)
(* dynamic environment: x --> 34, y --> 17 *)

val z = (x + y) + (y + 2);
(* dynamic environment: x -- 34, y --> 17, z --> 70 *)

