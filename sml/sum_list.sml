(* Sums the elements of a list, recursively *)
(* Functions:
   null: true if the list is empty
   hd:   head, first element of the list
   tl:   tail, the list without the first element
*)
fun sum_list(xs : int list) =
  if null xs                   (* test for empty list *)
  then 0                       (* return 0 if the list is empty *)
  else hd xs + sum_list(tl xs) (* head + tail, recursively *)
