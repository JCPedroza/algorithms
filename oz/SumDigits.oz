declare
fun {SumDigitsR N}
   if N==0 then 0
   else
	  (N mod 10) +
	  {SumDigitsR (N div 10)}
   end
end
