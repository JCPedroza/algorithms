var Nil = "Nil"

function cons(head, tail){
    tail = typeof tail !== "undefined" ? tail : Nil;
    return [head, tail];
}

function head(xs){
    return xs[0];
}

function tail(xs){
    return xs[1];
}

function lst(){
    var arg_array = Array.prototype.slice.call(arguments);  // arguments cast from object to array
    if (arg_array.length === 0) {
	return Nil;
    }
    else {
	return cons(arg_array[0], lst.apply(this, arg_array.slice(1)));
    }
}

var a = cons(Nil);
var b = cons(1, Nil);
var c = cons(1, cons(2));
var d = cons(1, cons(2, cons(3)));
var e = cons(1, cons(2, cons(3, cons(4))));
var f = cons(1, cons(2, cons(3, cons(4, cons(5)))));
var g = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6))))));
console.log(a);
console.log(b);
console.log(c);
console.log(d);
console.log(e);
console.log(f);
console.log(g);
console.log(JSON.stringify(g))







