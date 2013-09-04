import java.util.Iterator;
import java.util.NoSuchElementException;

/**
* A generic queue, implemented using a linked list.
*
* The Queue class represents a first-in-first-out (FIFO)
* queue of generic items.
* It supports the usual enqueue and dequeue
* operations, along with methods for peeking at the top item,
* testing if the queue is empty, and iterating through
* the items in FIFO order.
*  
* All queue operations except iteration are constant time.
*/
public class QueueLinkedList<Item> implements Iterable<Item>{
    
    private int  N;     // number of elements on queue
    private Node first; // beginning of queue
    private Node last;  // end of queue
    
    /**
    * Helper linked list class.
    */
    private class Node{
        private Item item; // the item
        private Node next; // links to next item, first links -
    }                      // to second, and so on
    
    /**
    * Create an empty queue.
    */
    public QueueLinkedList(){
        first = null;  // queue is empty, so no first node
        last  = null;  // queue is empty, so no last node
        N     = 0;     // queue is empty, so its size is 0
        assert check();
    }
    
    /**
    * Is the queue empty?
    */
    public boolean isEmpty(){
        return first == null; // queue is empty if there is no -
    }                        // first node
    
    /**
    * Return the number of items in the queue.
    */
    public int size(){
        return N;  
    }
    
    /**
    * Return the item least recently added to the queue.
    * @throws java.util.NoSuchElementException if queue is empty.
    */
    public Item peek(){
        if (isEmpty()) throw new NoSuchElementException("Queue underflow.");
        return first.item;  // return the first item in the queue
    }
    
    /**
    * Add the item to the queue.
    */
    public void enqueue(Item item){
        Node oldlast = last;   // remembers the former last node
        last = new Node();     // creates a new Node in last reference
        last.item = item;      // adds the item to that node
        last.next = null;      // last item doesn't link to a node
        // if the queue was empty, assign the added Item as the first node:
        if (isEmpty()) first = last;  
        // if it was not empty, assign it as the last node:
        else           oldlast.next = last;
        N++;                   // queue size increses by 1
        assert check();
    }

    /**
    * Remove and return the item on the queue least recently added.
    * @throws java.util.NoSuchElementException if queue is empty.
    */
    public Item dequeue(){
        if (isEmpty()) throw new NoSuchElementException("Queue underflow.");
        Item item = first.item;     // item in the first node to be returned
        first = first.next;         // first item in the queue is now first.next
        N--;                        // decrease queue size by 1
        if (isEmpty()) last = null; // to avoid loitering, references do not point -
        assert check();             // to an object if the queue is empty
        return item;                // return the item in the first node
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
    * Check interval invariants.
    */
    private boolean check() {
        if (N == 0) {                         // if the queue is empty:
            if (first != null) return false;  // first reference should be null
            if (last  != null) return false;  // last reference should be null
        }
        else if (N == 1) {                                    // if the queue has one item:
            if (first == null || last == null) return false;  // first and last should reference a Node
            if (first != last)                 return false;  // first and last should reference the same Node
            if (first.next != null)            return false;  // first.next should reference null
        }
        else {                                    // if the queue has more than one item
            if (first == last)      return false; // first and last should not reference the same Node
            if (first.next == null) return false; // first.next should reference the next Node 
            if (last.next  != null) return false; // last.next should reference null

            // check internal consistency of instance variable N
            int numberOfNodes = 0;
            for (Node x = first; x != null; x = x.next) {
               numberOfNodes++;                     // count the number of nodes
            }
            if (numberOfNodes != N) return false;  // the number of nodes should be equal to the -
                                                   // queue size
            // check internal consistency of instance variable last
            Node lastNode = first;                 
            while (lastNode.next != null) { // follows the links, until it reaches the last Node
               lastNode = lastNode.next;
            }
            if (last != lastNode) return false; // the link chain should point to the last Node
        }

        return true; // return true if everything is fine 
    } 

    /**
    * Return an iterator that iterates over the items on the queue in FIFO order.
    */
    public Iterator<Item> iterator()  {
        return new ListIterator();  
    }

    // an iterator, doesn't implement remove() since it's optional
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