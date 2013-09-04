import java.util.Iterator;
import java.util.NoSuchElementException;

/**
* A generic bag or multiset, implemented using a linked list.
* Its implementation is like a stack without pop, or queue
* without dequeue. This specific class is implemented like
* a stack without pop. Its main application is adding items to a 
* collection and iterating (when order doesn't matter).
*
* The Bag class represents a bag (or multiset) of 
* generic items. It supports insertion and iterating over the 
* items in arbitrary order.
* 
* The add, isEmpty, and size operation take constant time.
* Iteration takes time proportional to the number of items.
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
public class BagLinkedList<Item> implements Iterable<Item> {
    private int  N;        // number of elements in bag
    private Node first;    // beginning of bag
    
    /**
    *Helper linked list class
    */
    private class Node {
        private Item item; // the item in the collection
        private Node next; // links to the next item in the collection
    }

    /**
    * Create an empty stack.
    */
    public BagLinkedList() {
        first = null;   // the bag is empty, so first reference points to null
        N = 0;          // size of bag is 0
        assert check();
    }

    /**
    * Is the BAG empty?
    */
    public boolean isEmpty() {
        return first == null;
    }

   /**
     * Return the number of items in the bag.
     */
    public int size() {
        return N;
    }

   /**
     * Add the item to the bag.
     */
    public void add(Item item) {
        Node oldfirst = first;  // remembers oldfirst so the new first can link to it
        first = new Node();     // creates a new first Node object
        first.item = item;      // assigns the item to the first.item reference
        first.next = oldfirst;  // links to the next item
        N++;                    // adds 1 to N, which is the size of the stack
        assert check();
    }

    /**
    * Check internal invariants.
    */
    private boolean check() {
        if (N == 0) {
            if (first != null) return false; // first must be null if the size of 
        }                                    // the size of the stack is 0
        else if (N == 1) {
            if (first == null)      return false; // first must be a Node object if N < 0
            if (first.next != null) return false; // first must always link to null
        }
        else {
            if (first.next == null) return false; // if N < 1, first must always link to 
        }                                         // the second Node object.

        // check internal consistency of instance variable N
        int numberOfNodes = 0;
        for (Node x = first; x != null; x = x.next) {
            numberOfNodes++;
        }
        if (numberOfNodes != N) return false; // number of nodes must be equal to the size
                                              // stack
        return true;
    }  


    /**
    * Return an iterator to the stack that iterates through the items in LIFO order.
    */
    public Iterator<Item> iterator()  { return new ListIterator();  }
    
    /**
    * An iterator, doesn't implement remove() since it's optional
    */
    private class ListIterator implements Iterator<Item> {
        // support iteration over collection items by client, without -
        // revealing the internal representaion, we make data structures iterable -
        // to support elegant, compac, java client code: the for each loop
        private Node current = first;
        public boolean hasNext()  { return current != null;                     }
        public void remove()      { throw new UnsupportedOperationException();  }

        public Item next() {
            if (!hasNext()) throw new NoSuchElementException();
            Item item = current.item;
            current = current.next; 
            return item;
        }
    }
}
