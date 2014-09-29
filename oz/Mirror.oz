declare
% Reverses the order of the digits of an integer using tail recursion
fun {MirrorTR Int}
   local Loop in
	  fun {Loop Int Acc}
		 if Int<1 then Acc
		 else {Loop (Int div 10) ((Acc * 10) + (Int mod 10))}
		 end
      end
	  {Loop Int 0}
   end
end
