% n mod 10 gives the last digit of n
% n div 10 is n without the last digit

declare
% Sum of the digits of N, recursive
fun {SumDigitsR N}
   if N<1 then 0
   else
	  (N mod 10) +
	  {SumDigitsR (N div 10)}
   end
end

declare
%Sum of the digits of N, tail recursion
fun {SumDigitsTR N}
   local Loop in
	  fun {Loop N A}
		 if N<1 then A
		 else {Loop (N div 10) A+(N mod 10)}
		 end
      end
	  {Loop N 0}
   end
end
