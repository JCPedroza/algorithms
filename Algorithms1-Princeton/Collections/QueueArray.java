import java.util.Iterator;
import java.util.NoSuchElementException;

/**
* A generic queue, implemented using a resizeable array.
*
* The Queue class represents a first-in-first-out (FIFO)
* queue of generic items.
* It supports the usual enqueue and dequeue
* operations, along with methods like
* testing if the queue is empty, and iterating through
* the items in FIFO order.
*
* Tradeoffs between linked-list and resizing-array implementations:
* Linked-list: 
* 1) Every operation takes constant time in the worst case.
* 2) Uses extra time and space to deal with the links.
* Resizing-array:
* 1) Every operation takes constant amortized time.
* 2) Less wasted space.
* 3) It's faster, in general, than linked-list implementation, but you need to be 
* careful on when the array will be resized, since the operation can be very expensive.
*
* With this in mind, if you want the security that each operation will take the same time 
* use linked-list. If you want faster operations, and you can deal with the cost of 
* sometimes resizing the array, use resizing-array.
*
* Linked-list implementation is slower, but it gives us the guarantee of constant 
* operation time. Resizing-array implementation is faster in general, but at the cost
* of being slow at the moment of the array resize (which can happen infrequently).
*/
public class QueueArray<Item> implements Iterable<Item> {
    private Item[] q;            // queue elements
    private int N = 0;           // number of elements on queue
    private int first = 0;       // index of first element of queue
    private int last  = 0;       // index of next available slot
    
    /**
    * Create an empty stack.
    */
    @SuppressWarnings("unchecked")  // to prevent unchecked cast warning
    public QueueArray() {
        // note that this dynamic is used becaue Java doesn't allow generic array creation, -
        // so we create an array of type Object and cast it to the generic type Item, achieving
        // something similar to q = new Item[2] if it was possible in Java
        q = (Item[]) new Object[2]; // creates a new Item array with capacity 2 -
    }                               

    /**
    * Is the stack empty?
    */
    public boolean isEmpty() {return N == 0;}

    /**
    * Return number of items in the stack.
    */
    public int size() {return N;}

    /**
    * Resize the underlying array holding the elements.
    */
    @SuppressWarnings("unchecked") // to prevent unchecked cast warning
    private void resize(int max) {
        assert max >= N;
        // note that this dynamic is used becaue Java doesn't allow generic array creation, -
        // so we create an array of type Object and cast it to the generic type Item, achieving
        // something similar to Item[] temp = new Item[max] if it was possible in Java
        Item[] temp = (Item[]) new Object[max];  // create a new array with of size max
        for (int i = 0; i < N; i++) {            // copy elements from array q to array -
            temp[i] = q[(first + i) % q.length]; // temp
        }
        q = temp;  // q is now the resized array    
        first = 0; // index of the first element of queue
        last  = N; // index of the next available slot
    }

    /**
    * * Add the item to the end of the queue.
    */ 
    public void enqueue(Item item) {
        // doubles the capacty of array if stack is at maximum capacity, doubling dynamic -
        // is used to avoid frequent resizing of array, which is expensive (~N^2/2):
        if (N == q.length) resize(2*q.length);   // double size of array if necessary
        q[last++] = item;                        // add item, it is now the last item
        // tricky part: once you get past the capacity you need to reset back to 0, -
        // something similar to modulo operator; a circular dynamic, this way the space -
        // left by the dequeues can be used (see end of class for details):
        if (last == q.length) last = 0;          
        N++;                                     // queue size increases by 1
    }
    
    /**
    * Remove the least recently added item.
    * @throws NoSuchElementException if the queue is empty.
    */
    public Item dequeue() {
        if (isEmpty()) throw new NoSuchElementException("Queue underflow");
        Item item = q[first];                       // the first item in the queue
        q[first] = null;                            // to avoid loitering
        N--;                                        // queue size decreases by 1
        first++;                                    // index of the first item increases by 1
        // tricky part: once you get past the capacity you need to reset back to 0, -
        // something similar to modulo operator; a circular dynamic, this way the space -
        // left by the dequeues can be used (see end of class for details):
        if (first == q.length) first = 0;          
        // halves capacity of the array if stack size is at 1/4th of its capacity, 
        // halving dynamic is used to avoid frequent resizing of array, which is
        // expensive (~N^2/2), array is not shrinked when it is 1/2 capacity to avoid
        // thrashing, doing it when it is 1/4 capacity is much more efficient:
        if (N > 0 && N == q.length/4) resize(q.length/2); 
        return item;
    }

    public Iterator<Item> iterator() { return new ArrayIterator(); }

    /**
    * An iterator, doesn't implement remove() since it's optional
    */
    private class ArrayIterator implements Iterator<Item> {
        // support iteration over collection items by client, without -
        // revealing the internal representaion, we make data structures iterable -
        // to support elegant, compac, java client code: the for each loop
        private int i = 0;
        public boolean hasNext()  { return i < N;                               }
        public void remove()      { throw new UnsupportedOperationException();  }

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = q[(i + first) % q.length];
            i++;
            return item;
        }
    }
}

/**
* Explanation of if (last == q.length) last = 0; and if (first == q.length) first = 0; in
* enqueue() and dequeue() by Punnet Singh of the Coursera course forums: 
*
* Actually, it explains the concept of circular queue. For example when you enqueue, item gets added its 
* appended to end, for example an integer array of size 5 after enqueue of 4 items (9,5,6,10), will be like 
* this
* index: 0  1  2  3  4
* no.    9  5  6 10
* last = 4
*
* Now if you dequeue twice, 9 and 5 will be dequeued
* index: 0  1  2  3  4
* no:          6 10
* last = 4  
*
* Now as you can see there is space left at end, plus at beginning of the array due to dequeue operation.
* Now when you enqueue 11
* index: 0  1  2  3  4
* no:          6 10 11
* last = 5 (array length)
* last is made 0
*
* So in order to waste the space left at beginning of the array, last is then assigned to index = 0,
* this is called circular queue, where last is moved back to beginning of the array in circular fashion.
* So next enqueue will happen at index 0.
*
* Note that last points to next free space index, and its updated using last++, that means the no. will 
* be assigned first to the last index, after that last will be updated
*/