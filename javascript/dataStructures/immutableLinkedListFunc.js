// !!! head ant tail need to thrw an exception then called on an empty list! and your code needs to 
// change to reflect this change
// !!! implement tail recursive alternatives when possible

/**
*
* Constructing Linked Lists
*
* Our linked list data structure consists of two fundamental building blocks: Nil and cons. Nil represents the 
* empty list and serves as a sentinel for more complex lists. The cons operation extends a list at the front by 
* inserting a new value.
*
* The lists we construct using this method consist internally of nested arrays of 2 items. For example, the list [1, 2, 3] 
* is represented by the expression cons(1, cons(2, cons(3, Nil))) which evaluates to the nested arrays [1, [2, [3, []]]].
*
*/

var Nil = [];

/** Extends a list at the front by inserting a new value. */
function cons(head, tail) {
    tail = typeof tail === "undefined" ? Nil : tail;  // default argument is Nil
    return [head, tail];
}

/**
* Define list instances using a more convenient syntax and without deeply nested cons calls.
* lst() === Nil                                                                                                                                                                
* lst(1, 2, 3) === [1, [2, [3, []]]]
*/
function lst() {
    var arg_array = Array.prototype.slice.call(arguments);  // arguments cast from object to array
    if (arg_array.length === 0) return Nil;
    else return cons(arg_array[0], lst.apply(this, arg_array.slice(1)));
}

/** Returns the first element of a list */
function head(xs) {
    if (xs === Nil) return [];
    else return xs[0];
}

/** Returns a list containing all elements except the first. */
function tail(xs) {
    if (xs === Nil) return [];
    else return xs[1];
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

/** Returns the first n elements of the given list. Inclusive, one-based indexing. */
function take(n, xs){
    if (n < 1) return Nil;
    else return cons(head(xs), take(n - 1, tail(xs)));
}

/** Returns a copy of input list, without the first n elements. Inclusive, one-based indexing. */
function drop(n, xs) {
    if (n < 1) return xs;
    else return drop(n - 1, tail(xs));
}

/** 
* Returns a subset of the input list that includes the items in the range from, to. 
* Zero-based indexing, from is inclusive, to is exclusive.  
*/
function piece(from, to, xs) {
    return take((to - from), drop(from, xs));
}

/** Removes the element of the list at given index. One-based indexing. */
function removeOne(index, xs) {
    return concat(take(index - 1, xs), drop(index, xs));
}

/** Returns the value at n index. Zero-based indexing. */
function at(index, xs){
    if (index < 1) return head(xs);
    else return(at(index - 1, tail(xs)));
}

// Some examples:

var a = lst(1, 2, 3, 4, 5);
var b = cons(6, cons(7, cons(8, cons(9, cons(10)))));
var c = lst(12, 3, 16, 22, 89, 4, 1);
var empty = lst();

console.log("a:               ", JSON.stringify(a));
console.log("b:               ", JSON.stringify(b));
console.log("empty:           ", JSON.stringify(empty));
console.log("head(a):         ", JSON.stringify(head(a)));
console.log("tail(a):         ", JSON.stringify(tail(a)));
console.log("tail(empty):     ", JSON.stringify(tail(empty)));
console.log("concat(a, b):    ", JSON.stringify(concat(a, b)));
console.log("take(3, a):      ", JSON.stringify(take(3, a)));
console.log("drop(3, a):      ", JSON.stringify(drop(3, a)));
console.log("piece(0, 4):     ", JSON.stringify(piece(0, 4, a)));
console.log("removeOne(3, a): ", JSON.stringify(removeOne(3, a)));
console.log("at(2, a):        ", JSON.stringify(at(2, a)));

// !!! still needs to_string and isort functions








