/**
*
* Constructing Linked Lists
*
* Our linked list data structure consists of two fundamental building blocks: Nil and cons. Nil represents the 
* empty list and serves as a sentinel for more complex lists. The cons operation extends a list at the front by 
* inserting a new value.
*
* The lists we construct using this method consist internally of nested arrays of 2 items. For example, the list [1, 2, 3] 
* is represented by the expression cons(1, cons(2, cons(3, Nil))) which evaluates to the nested arrays [1, [2, [3, Nil]]].
*
*/

var Nil = "Nil";

/** Extends a list at the front by inserting a new value. */
function cons(head, tail) {
    tail = typeof tail === "undefined" ? Nil : tail;
    return [head, tail];
}

/**
* Define list instances using a more convenient syntax and without deeply nested cons calls.
* lst() === Nil                                                                                                                                                                
* lst(1, 2, 3) === [1, [2, [3, Nil]]]
*/
function lst() {
    var arg_array = Array.prototype.slice.call(arguments);  // arguments cast from object to array
    if (arg_array.length === 0) return Nil;
    else return cons(arg_array[0], lst.apply(this, arg_array.slice(1)));
}

/** Returns the first element of a list */
function head(xs) {
    return xs[0];
}

/** Returns a list containing all elements except the first. */
function tail(xs) {
    return xs[1];
}

/** Returns True if the list contains zero elements. */
function isEmpty(xs) {
    return xs === Nil;
}

/** Returns number of elements in a given list. */
function length(xs) {
    if (isEmpty(xs)) return 0;
    else return 1 + length(tail(xs));
}

/** Concatenates two lists. */
function concat(xs, ys) {
    if (isEmpty(xs)) return ys;
    else return cons(head(xs), concat(tail(xs), ys));
}

/** Returns the last element of a non-empty list. */
function last(xs) {
    if (isEmpty(tail(xs))) return head(xs);
    else return last(tail(xs));
}

/** Returns all elements except the last one. */
function init(xs) {
    if (isEmpty(tail(tail(xs)))) return cons(head(xs));
    else return cons(head(xs), init(tail(xs)));
}


/** Returns the input list, reversed. */
function reverse(xs) {
    if (isEmpty(xs)) return xs;
    else return concat(reverse(tail(xs)), cons(head(xs), Nil));
}

/** Returns the first n elements of the given list. */
function take(n, xs){
    if (n < 1) return Nil;
    else return cons(head(xs), take(n - 1, tail(xs)));
}

/** Returns a copy of input list, without the first n elements. */
function drop(n, xs){
    if (n < 1) return xs;
    else return drop(n - 1, tail(xs));
}

/**  Returns a subset of the input list that includes the items in the range from, to. */
function piece(from, to, xs){
    return take(to - from, drop(from, xs));
}

/** Removes the element of the list at given index */
function removeOne(index, xs){
    return concat(take(index - 1, xs), drop(index, xs));
}



var a = lst();
var zz = lst(1, 2, 3, 4, 5, 6, 7);
var b = cons(7, cons(8, cons(9)));
var g = cons(1, cons(2, cons(3, cons(4, cons(5, cons(6))))));
console.log(JSON.stringify(g));
console.log(JSON.stringify(a));
console.log(length(g));
console.log(length(a));
console.log(JSON.stringify(concat(b, g)));
console.log(last(g));
console.log(JSON.stringify(init(g)));
console.log(JSON.stringify(reverse(g)));
console.log(JSON.stringify(zz));
console.log(JSON.stringify(take(3, g)));
console.log(JSON.stringify(drop(2, g)));
console.log(JSON.stringify(piece(2, 4, g)));
console.log(JSON.stringify(removeOne(2, g)));
console.log(lst());





