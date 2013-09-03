import java.util.Iterator;
import java.util.NoSuchElementException;

/**
* A generic stack implemented using a resized array.
*
* The StackArray class represents the last-in-first-out (LIFO) stack of 
* generic items. It supports the usual push and pop operations along with methods 
* testing if the stack is empty, and iterating through the items in LIFO order.
*
* Tradeoffs between linked-list and resizing-array implementations:
* Linked-list: 
* 1) Every operation takes constant time in the worst case.
* 2) Uses extra time and space to deal with the links.
* Resizing-array:
* 1) Every operation takes constant amortized time.
* 2) Less wasted space.
*/
public class StackArray<Item> implements Iterable<Item>{

    private Item[] a;  // array of items
    private int    N;  // number of elements on a stack
    

    /**
    * Create an empty stack.
    */
    @SuppressWarnings("unchecked") // to prevent unchecked cast warning
    public StackArray(){
        a = (Item[]) new Object[2]; // creates a new Item object with capacity 2
    }
    
    /**
    * Is the stack empty?
    */
    public boolean isEmpty(){return N == 0;}  // stack is empty if N == 0
 
    /**
    * Return number of items in the stack.
    */
    public int size(){return N;} // N is the size of the array

    /**
    * Resize the underlying array holding the elements
    */
    @SuppressWarnings("unchecked") // to prevent unchecked cast warning
    private void resize(int capacity){
        assert capacity >= N;
        Item[] temp = (Item[]) new Object[capacity]; // new array with x capacity
        for(int i = 0; i < N; i++){  // copy everything to new rezised array
            temp[i] = a[i];
        }
        a = temp; // a is now resized
    }
    
    /**
    * Push a new item onto the stack.
    */
    public void push(Item item){
        // doubles the capacty of array if stack is at maximum capacity, doubling dynamic
        // is used to avoid frequent resizing of array, which is expensive (~N^2/2):
        if (N == a.length) resize(2*a.length); 
        a[N++] = item; // assigns -item- to that index, the 
    }                  // adds 1 to N
    
    /**
    * Delete and return the item most recently added.
    */
    public Item pop(){
        if (isEmpty()) throw new NoSuchElementException("Stack underflow");
        Item item = a[N-1]; // last item in the array
        a[N-1] = null;      // that index is now empty
        N--;                // size of stack decreased by 1
        // halves capacity of the array if stack size is at 1/4th of its capacity, 
        // halving dynamic is used to avoid frequent resizing of array, which is
        // expensive (~N^2/2), array is not shrinked when it is 1/2 capacity to avoid
        // thrashing, doing it when it is 1/4 capacity is much more efficient:
        if (N > 0 && N == a.length/4) resize(a.length/2); 
        return item;        // returns the last item in the array                                     
    }                                                     
    
    
    public Iterator<Item> iterator(){ return new ReverseArrayIterator();}
    
    /**
    * An iterator, doesn't implement remove() since it's optional
    */
    private class ReverseArrayIterator implements Iterator<Item>{
        private int i;
        public ReverseArrayIterator(){
            i = N;
        }
        public boolean hasNext(){
            return i > 0;
        }
        public void remove(){
            throw new UnsupportedOperationException();
        }
        public Item next(){
            if (!hasNext()) throw new NoSuchElementException();
            return a[--i];
        }
    }
}