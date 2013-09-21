import java.util.Arrays;

public class UnionFindTests{
    
    public static void main(String[] args){
        
        // Create instances of the 3 different implementations, with n isolated items/objects.
        int                  n          = 10; // Number of isolated items
        QuickFindUF          QF10       = new QuickFindUF(n);
        QuickUnionUF         QUUF10     = new QuickUnionUF(n);
        QuickUnionWeightedUF QUWUF10    = new QuickUnionWeightedUF(n);
        QuickUnionUFImproved QUUFI10    = new QuickUnionUFImproved(n);
        // To use as a string in the prints that represent objects in the array
        int[]                objects    = new int[n];
        for (int i = 0; i < n; i++){
            objects[i] = i;
        }
        String               objectsStr = Arrays.toString(objects);
        
        // Actions
        QF10.union(7, 5);
        QF10.union(8, 7);
        QF10.union(3, 7);
        QF10.union(9, 2);
        QF10.union(8, 0);
        QF10.union(4, 3);

        QUWUF10.union(6, 9);
        QUWUF10.union(2, 4);
        QUWUF10.union(8, 0);
        QUWUF10.union(5, 9);
        QUWUF10.union(0, 9);
        QUWUF10.union(3, 1);
        QUWUF10.union(2, 3);
        QUWUF10.union(5, 2);
        QUWUF10.union(9, 7);

        // Prints
        System.out.println(Arrays.toString(QF10.getId()));
        System.out.println(Arrays.toString(QUWUF10.getId()));
        


    }

}