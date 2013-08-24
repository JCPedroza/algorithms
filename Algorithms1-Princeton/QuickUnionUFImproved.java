/**
* Improved implementation of QuickUnionUF. This one IS quick enough. The improvements implemented
* are: Weighting and Path Compression.
*
* Improvement 1: Weighting. Implemented in the union method. Achieves balance by linking root of 
* smaller tree to root of larger tree. This avoids tall trees. Keeps track of size of each 
* tree (number of objects). this way we have some guarantee that no item will be too far away 
* from the root
*
* Improvement 2: Path Compression. Implemented in the root method. Just after computing 
* the root of p, set the id of each examined node to point to that root. Added a second loop
* to root() to set the id[] of each examined node to the root. Only one extra line of code.
*
* Analysis:
* Example: 10^9 unions and finds (roots) with 10^9 objets
* Weighted Quick-union with path compression reduces time from 30 years to 6 seconds
*/

public class QuickUnionUFImproved{
    
    /**
    * Index represents object, value represents root.
    * If two objects share root (directly or indirectly, they don't need to have 
    * the same value), they are connected. id[i] = parent of i
    */
    private int[] id; 

    /**
    * Size of a tree. sz[i] = number of objects in subtree rooted at i
    */
    private int[] sz;  

    /**
    * Number of components
    */ 
    private int   count;
    
    /**
    * Create an empty union find data structure with N isolated sets.
    * @param N Number isolated sets. 
    */
    public QuickUnionUFImproved(int N){
        count = N;
        id    = new int[N];
        sz    = new int[N];
        for (int i = 0; i < N; i++){
            id[i] = i;
            sz[i] = i;
        }
    }
    
    /**
    * Chase parent pointers until reach root (depth of i array accesses).
    * Implements Path Compression.
    * @param i Object that will be searched for its root.
    */
    private int root(int i){
        while (i != id[i]){
            id[i] = id[id[i]]; // Path Compression implementation.
            i     = id[i];
        }
        return i;
    }
    
    /**
    * Are objects p and q in the same set, are they connected?
    */
    public boolean connected(int p, int q){
        return find(p) == find(q);
    }

    public int getCount(){
        return count;
    }
    
    /**
    * Replace sets containing p and q with their union.
    * Implements weighted quick-union. 
    */
    public void union(int p, int q) {
        int i = root(p);
        int j = root(q);
        if (i == j) return;

        // Weighting. Make smaller root point to larger one
        if   (sz[i] < sz[j]) { id[i] = j; sz[j] += sz[i]; }
        else                 { id[j] = i; sz[i] += sz[j]; }
        count--;
    }

}