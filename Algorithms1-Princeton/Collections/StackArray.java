import java.util.Iterator;
import java.util.NoSuchElementException;

/**
* A generic stack implemented using a resized array.
*
* The StackArray class represents the last-in-first-out (LIFO) stack of 
* generic items. It supports the usual push and pop operations along with methods 
* testing if the stack is empty, and iterating through the items in LIFO order.
*/
public class StackArray<Item> implements Iterable<Item>{

    private Item[] a;  // array of items
    private int    N;  // number of elements on a stack
    

    /**
    * Create an empty stack.
    */
    @SuppressWarnings("unchecked") // to prevent unchecked cast warning
    public StackArray(){
        a = (Item[]) new Object[2];
    }
    
    /**
    * Is the stack empty?
    */
    public boolean isEmpty(){return N == 0;} 
 
    /**
    * Return number of items in the stack.
    */
    public int size(){return N;}

    /**
    * Resize the underlying array holding the elements
    */
    @SuppressWarnings("unchecked") // to prevent unchecked cast warning
    private void resize(int capacity){
        assert capacity >= N;
        Item[] temp = (Item[]) new Object[capacity];
        for(int i = 0; i < N; i++){
            temp[i] = a[i];
        }
        a = temp;
    }
    
    /**
    * Push a new item onto the stack.
    */
    public void push(Item item){
        if (N == a.length) resize(2*a.length);
        a[N++] = item;
    }
    
    /**
    * Delete and return the item most recently added.
    */
    public Item pop(){
        if (isEmpty()) throw new NoSuchElementException("Stack underflow");
        Item item = a[N-1];
        a[N-1] = null;
        N--;
        // shrink size of array if necessary
        if (N > 0 && N == a.length/4) resize(a.length/2);
        return item;
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