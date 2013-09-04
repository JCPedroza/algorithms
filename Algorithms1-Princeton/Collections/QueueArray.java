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

    // cast needed since no generic array creation in Java
    public QueueArray() {
        q = (Item[]) new Object[2];
    }

    public boolean isEmpty() { return N == 0;    }
    public int     size()    { return N;         }

    // resize the underlying array
    private void resize(int max) {
        assert max >= N;
        Item[] temp = (Item[]) new Object[max];
        for (int i = 0; i < N; i++) {
            temp[i] = q[(first + i) % q.length];
        }
        q = temp;
        first = 0;
        last  = N;
    }


    public void enqueue(Item item) {
        // double size of array if necessary and recopy to front of array
        if (N == q.length) resize(2*q.length);   // double size of array if necessary
        q[last++] = item;                        // add item
        if (last == q.length) last = 0;          // wrap-around
        N++;
    }

    // remove the least recently added item 
    public Item dequeue() {
        if (isEmpty()) throw new NoSuchElementException("Queue underflow");
        Item item = q[first];
        q[first] = null;                            // to avoid loitering
        N--;
        first++;
        if (first == q.length) first = 0;           // wrap-around
        // shrink size of array if necessary
        if (N > 0 && N == q.length/4) resize(q.length/2); 
        return item;
    }

    public Iterator<Item> iterator() { return new ArrayIterator(); }

    // an iterator, doesn't implement remove() since it's optional
    private class ArrayIterator implements Iterator<Item> {
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