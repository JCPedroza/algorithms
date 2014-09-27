declare
% Recursive factorial function
fun {FactorialR N}
   if N<1 then 1
   else
	  N * {FactorialR N-1}
   end
end

declare
% Tail recursive factorial function
fun {FactorialTR N}
   fun {Loop N Acc}
	  if N < 1 then Acc
	  else
		 {Loop N-1 N*Acc}
	  end
   end
in
   {Loop N 1}
end

declare
% Factorial function usng folding
fun {FactorialF N}
   {FoldL {List.number 1 N 1} Number.'*' 1}
end


