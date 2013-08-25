import java.util.Arrays;

public class QuickUnionTests{
    
    public static void main(String[] args){
        
        // Create instances of the 3 different implementations, with n isolated items/objects.
        int                  n          = 10; // Number of isolated items
        QuickFindUF          QF10       = new QuickFindUF(n);
        QuickUnionUF         QUUF10     = new QuickUnionUF(n);
        QuickUnionUFImproved QUUFI10    = new QuickUnionUFImproved(n);
        // To use as a string in the prints that represent objects in the array
        int[]                objects    = new int[n];
        for (int i = 0; i < n; i++){
            objects[i] = i;
        }
        String               objectsStr = Arrays.toString(objects);

        // Check arrays
        System.out.println("");
        System.out.println("============================================");
        System.out.println("Initial state of arrays: ");
        System.out.println("");
        System.out.println("Quick Find:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QF10.getId()));
        System.out.println("");
        System.out.println("Quick Union:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QUUF10.getId()));
        System.out.println("");
        System.out.println("Quick Union Improved:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QUUFI10.getId()));
        System.out.println("T Size: " + Arrays.toString(QUUFI10.getSz()));
        
        // Perform union(1, 2);
        QF10.union(1, 2);
        QUUF10.union(1, 2);
        QUUFI10.union(1, 2);
        // Print after union(1, 2):
        System.out.println("");
        System.out.println("============================================");
        System.out.println("After union(1, 2): ");
        System.out.println("");
        System.out.println("Quick Find:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QF10.getId()));
        System.out.println("");
        System.out.println("Quick Union:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QUUF10.getId()));
        System.out.println("");
        System.out.println("Quick Union Improved:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QUUFI10.getId()));
        System.out.println("T Size: " + Arrays.toString(QUUFI10.getSz()));

        // Perform union(9, 1);
        QF10.union(9, 1);
        QUUF10.union(9, 1);
        QUUFI10.union(9, 1);
        // Print after union(1, 2):
        System.out.println("");
        System.out.println("============================================");
        System.out.println("After union(9, 1): ");
        System.out.println("");
        System.out.println("Quick Find:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QF10.getId()));
        System.out.println("");
        System.out.println("Quick Union:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QUUF10.getId()));
        System.out.println("");
        System.out.println("Quick Union Improved:");
        System.out.println("Object: " + objectsStr);
        System.out.println("ID:     " + Arrays.toString(QUUFI10.getId()));
        System.out.println("T Size: " + Arrays.toString(QUUFI10.getSz()));


    }

}