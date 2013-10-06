/**
* Different implementations of a simple factorial algorithm.
* To run this code: node factorial.py
*/

// ===============================
//        The Algorithms
// ===============================

/** Computes factorial of n using recursion. */
function factorialRecursive(n){
    if (n < 1) return 1;
    else       return n * factorialRecursive(n - 1);
}

/** Computes factorial of n using tail recursion. */
function factorialTailRecursive(n){
    function recursion(n, acc){
        if (n < 1) return acc;
        else       return recursion(n - 1, acc *= n);
    }
    return recursion(n, 1);
}

/** Computes factorial of n using iteration and while loop. */
function factorialIterW(n){
    var acc = 1;
    while (n > 1){
        acc *= n;
        n--;
    }
    return acc;
}

/** Computes factorial of n using iteration and for loop. */
function factorialIterF(n){
    var acc = 1;
    for (var i = 1; i < n + 1; i++) acc *= i;
    return acc;
}

// ===============================
//    Timing the Algorithms
// ===============================

var num     = 150;
var repeats = 5000;

/** Measures running time of a function */
function performance(f, name){
    console.time(name);
    for (var i = 0; i < repeats; i++)
        f(num);
    console.timeEnd(name);
}

console.log("");
console.log("===================================================================");
console.log("");
console.log("Running time of different factorial algorithm implementations,");
console.log("in wall clock seconds, not CPU time.");
console.log("");
console.log("Compute " + num + " factorial " + repeats + " times:");

console.log("");
performance(factorialRecursive, "factorialRecursive()");
console.log("");
performance(factorialTailRecursive, "factorialTailRecursive()");
console.log("");
performance(factorialIterW, "factorialIterW()");
console.log("");
performance(factorialIterF, "factorialIterF()");
console.log("");

console.log("===================================================================");
console.log("");

