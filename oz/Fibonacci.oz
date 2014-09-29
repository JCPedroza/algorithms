declare
% Computes the nth fibonacci number using recursion
fun {FibR N}
   if N < 2 then N
   else {FibR N-1} + {FibR N-2}
   end
end

declare
% Computes the nth fibonacci number using tail recursion
fun {FibTR N}
   local Loop in
      fun {Loop N Acc Buff}
	     if N < 2 then Acc
         else {Loop N-1 Acc+Buff Acc}
   	     end
      end
	  {Loop N 1 0}
   end
end
