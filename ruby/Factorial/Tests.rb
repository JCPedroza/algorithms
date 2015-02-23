require "benchmark"
require "Factorial"

n = 170
m = 5000

Benchmark.bm(25) do |b|
    b.report('while loop:') {m.times {factorial_w(n)}}
    b.report('for loop:') {m.times {factorial_f(n)}}
    b.report('recursion:') {m.times {factorial_r(n)}}
    b.report('tail recursion') {m.times {factorial_tr(n)}}
    b.report('iterative range.each') {m.times {factorial_re(n)}}
    b.report('iterative range.reduce:') {m.times {factorial_rr(n)}}
    b.report("stirling's approximation:") {m.times {factorial_sa(n)}}

end
puts ""