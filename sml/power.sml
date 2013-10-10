fun pow(x, y) =
  if y = 0 then x else pow(x * x, y - 1)

