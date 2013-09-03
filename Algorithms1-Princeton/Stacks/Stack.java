import java.util.Iterator; // used only in iterator reference and ListIterator 
                           // inner class
import java.util.NoSuchElementException;

/**
* A generic stack, implemented using a linked list. Each stack element is of
* type Item.
*
* The Stack class represents the last-in-first-out (LIFO) stack of generic items.
* It supports the usual push and pop operations, along with methods 
* for peeking at the top item, testing if the stack is empty, and iterating
* through the items in LIFO order.
*
* All stack operations except iteration are constant time.
*/
public class Stack<Item> implements Iterable<Item>{

    private int  N;      // size of the stack
    private Node first;  // top of the stack

    /**
    * Helper linked list class.
    */
    private class Node{
        private Item item;    // the item
        private Node next;    // points to the next item
    }
    
    /**
    * Create an empty stack.
    */
    public Stack(){
        first = null;    // empty stack, no null object
        N     = 0;       // empty stack so size is 0
        assert check();
    }

    /**
    * Is the stack empty?
    */
    public boolean isEmpty(){
        return first == null; // if there is no first Node object, stack is empty
    }
    
    /**
    * Return  the number of items in the stack
    */
    public int size(){
        return N;   // return N, which is the size of the stack
    }

    /**
    * Add the item to the stack.
    */
    public void push(Item item){
        Node oldfirst = first; // remembers oldfirst so the new first can link to it
        first         = new Node(); // creates a new first Node object
        first.item    = item; // puts the item in the variable/reference
        first.next    = oldfirst; // links to the next item
        N++;  // adds 1 to N, which is the size of the stack
        assert check();
    }
    
    /**
    * Return the item most recentrly added to the stack.
    * @throws java.util.NoSuchElementException if stack is empty.
    */
    public Item pop(){
        if (isEmpty()) throw new NoSuchElementException("Stack underflow");
        Item item = first.item; // save item to return
        first     = first.next; // delete first node
        N--;                    // -1 to N, chich is the size of the stack
        assert check();
        return item;            // return the saved item
    }
    
    /**
    * Return the item most recently added to the stack.
    * @throws java.util.NoSuchElementException if stack is empty.
    */
    public Item peek(){
        if (isEmpty()) throw new NoSuchElementException("Stack underflow");
        return first.item; // see the first item
    }
    
    /**
    * Return string representation.
    */
    public String toString(){
        StringBuilder s = new StringBuilder();
        for (Item item : this)
            s.append(item + " ");
        return s.toString();
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