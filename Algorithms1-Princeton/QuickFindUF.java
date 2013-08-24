/**
* Quick-find (eager approach) union find class for dealing with dynamic connectivity. 
*
* Array indexes represent objects. 
*
* Quick-find is too slow for dynamic connectivity. It doesn't work very well for large arrays. 
*
* Quick-find defect 1: union is too expensive. Takes N^2 (quadratic) array accesses to process sequence
* of N unions commands on N objects.
*
* Quick-find defect 2: Trees are flat, but too expensive to keep them flat.
*/
public class QuickFindUF{
    
    /**
    * Index represents object, ID represents connectivity.
    * If two indexes share ID it means they are connected
    */
    private int[] id;
    
    /**
    * Creates the array, and sets the ID values for each element of the array.
    * The ID of each element of the array is equal to its index.
    * @param N Number of objects to be created.
    */
    public QuickFindUF(int N){
        id = new int[N];
        for (int i = 0; i < N; i++){
            id[i] = i;
        }
    }
    
    /**
    * Checks if two objects are connected.
    * @param p An object (array index).
    * @param q An object (array index).
    * @return True if objects are connected, false if they aren't.
    */
    public boolean connected(int p, int q){
        return id[p] == id[q];
    }
    
    /**
    * Connects two objects.
    * Changes the ID of the q object and all the objects that share ID with q to the
    * ID of the p object.
    * @param p The object that will be connected to the q object.
    * @param q The object that will be connected to the p object.
    */
    public void union(int p, int q){
        int pid = id[p];
        int qid = id[q];
        for (int i = 0; i < id.length; i++){
            if (id[i] == pid){
                id[i] = qid;
            }
        }
    }

    public int[] getId(){
        return id;
    }
}