// =================================
//          The Algorithms
// =================================

/**
* Calculates the nth fibonacci number, recusrively, without tail recursion.
* Performance: O(2^n).
*/
function fiboRecursive(n){
    if      (n === 0) return 0;
    else if (n === 1) return 1;
    else return fiboRecursive(n - 1) + fiboRecursive(n - 2);
}

/**
* Calculates the nth fibonacci number, using tail recursion. 
*/
function fiboTailRecursive(n){
    function recursion(n, a, b){
        if (n > 0) return recursion(n - 1, b, a + b);
        else       return a;
    }
    return recursion(n, 0, 1);
}

/**
* Calculates the nth fibonacci number, using iteration.
*/
function fiboIter(n){
    var a = 0;
    var b = 1;
    for (var i = 0; i < n; i++){
        var buffer = a;
        a = b;
        b = buffer + b;
    }
    return a;
}

/** 
* Calculates the nth fibonacci number, using Binet's formula
*/
function fiboBinet(n){
    return (Math.pow(1 + Math.sqrt(5), n) - (Math.pow(1-Math.sqrt(5), n))) /
           (Math.pow(2, n) * Math.sqrt(5));
}

/** 
* Calculates the nth fibonacci number, based on these formulas:
* F(2n-1) = F(n)^2 + F(n-1)^2
* F(2n) = (2F(n-1) + F(n))*F(n)
*/
function fib(n){
    function fibs(n){
        // console.log("fibs called with " + n);
        if (n === 1) return [1, 0];
        else{
            var ab = fibs(Math.floor(n/2));
            var p  = (2*ab[1]+ab[0])*ab[0];
            var q  = ab[0]*ab[0] + ab[1]*ab[1];
            if(n % 2 === 0) return [p,q];
            else            return [p+q,p];
        }
    }
    return fibs(n)[0];
}

// =================================
//               Tests
// =================================
