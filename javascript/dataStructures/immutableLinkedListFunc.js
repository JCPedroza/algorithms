var Nil = null

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
	console.log(arg_array.length); 
	return Nil;}
    else {
	console.log(arg_array.length); 
	console.log(arg_array); 
	return cons(arg_array[0], lst.apply(this, arg_array.slice(1)));}

}

var a = cons(1, cons(2, cons(3, Nil)));
var b = cons(1, cons(2, cons(3, Nil)));

console.log(a);
console.log(b);
console.log("");
console.log(lst(1, 2, 3));


