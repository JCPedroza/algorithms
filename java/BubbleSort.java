import java.util.Arrays;

public class BubbleSort{

    public static void main(String[] args){
        System.out.println("Bubble Sort algorith");
        int theArray[] = new int[] {2, 4, 9, 2, 3, 6, 5, 8, 7, 1, 0};
        descendingBubbleSort(theArray);
        System.out.println(Arrays.toString(theArray));
    }

    public static void descendingBubbleSort( int [ ] num ){
        int j;
        boolean flag = true;                 // set flag to true to begin first pass
        int temp;                            //holding variable
        while ( flag ){
            flag= false;                     //set flag to false awaiting a possible swap
            for( j=0;  j < num.length -1;  j++ ){
                if ( num[ j ] < num[j+1] ){  // change to > for ascending sort       
                    temp = num[ j ];         //swap elements
                    num[ j ] = num[ j+1 ];
                    num[ j+1 ] = temp;
                    flag = true;             //shows a swap occurred  
                } 
            } 
        } 
    } 
    
} 