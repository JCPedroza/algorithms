object Main extends App {
  def merge[T](f: (T, T) => Boolean, xs: List[T], ys: List[T]): List[T] = (xs, ys) match {
    case (Nil, ys) => ys
    case (xs, Nil) => xs
    case (x :: xs, y :: ys) =>
      if (f(x, y))
        x :: merge(f, xs, y :: ys)
      else
        y :: merge(f, x :: xs, ys)
  }
  def mergesort[T](f: (T, T) => Boolean, xs: List[T]): List[T] = {
    if (xs.length < 2)
      xs
    else
      merge(f, mergesort(f, xs.take(xs.length / 2)), mergesort(f, xs.drop(xs.length / 2)))
  }
  println(mergesort((a: Int, b: Int) => a < b, List(3, 2, 10, 3, 5, 6, 7, 1, 1, 8, 9, 4)))
}