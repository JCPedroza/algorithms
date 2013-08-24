/**
* Quick-union (lazy approach) union find class for dealing with dynamic connectivity.
* 
* Array indexes represent objects. We can see that a difference between QuickFindUF and 
* QuickUnionUF is that QuickUnionUF doesn't implement a for loop, but it has a while
* loop that we have to worry about a little bit; it also has less code. 
* 
* Quick-union is faster thatn Quick-find, but it is also too slow! Not fast enough.
* Quick-union defect 1: Trees can get tall.
* Quick-union defect 2: Find too expensive (could be N array accesses).
*/

public class QuickUnionUF{
    
    /**
    * Index represents object, value represents root.
    * If two objects share root (directly or indirectly, they don't need to have 
    * the same value), they are connected. id[i] = parent of i
    */
    private int[] id;
    
    /**
    * Create an empty union find data structure with N isolated sets.
    * @param N Number isolated sets. 
    */
    public QuickUnionUF(int N){
        id = new int[N];
        for (int i = 0; i < N; i++){
            id[i] = i;
        }
    }
    
    /**
    * Chase parent pointers until reach root (depth of i array accesses).
    * @param i Object that will be searched for its root.
    */
    private int root(int i){
        while (i != id[i]){
            i = id[i];
        }
        return i;
    }
    
    /**
    * Are objects p and q in the same set, are they connected?
    */
    public boolean connected(int p, int q){
        return root(p) == root(q);
    }
    
    /**
    * Change root of p to the root of q (depth of p and q array accesses).
    * @param p The object that will change its root to q's root.
    * @param q The object that will share its root with p.
    */
    public void union(int p, int q){
        int i = root(p);
        int j = root(q);
        id[i] = j;
    }

    public int[] getId(){
        return id;
    }
}