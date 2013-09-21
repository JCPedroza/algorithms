/**
* Sorts a sequence of items using insertion sort.
*
* Insertion sort iterates, consuming one input element each repetition, and growing a sorted output 
* list. Each iteration, insertion sort removes one element from the input data, finds the location 
* it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.
*
* Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item 
* at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, 
* heapsort, or merge sort. However, insertion sort provides several advantages:
* 1) Simple imlepentation. 2) Efficient for small data sets. 3) Adaptive, efficient, for data sets that
* are already substantially sorted. 4) Most efficient in practice than most other simple quadratic
* (i.e., O(n^2)) algorithms such as selection sort or bubble sort 5) Stable: does not change the 
* relative order of elements with equals keys 6) In-place: only requires a constant amount O(1) of 
* additional memory space. 7) Online: can sort a list as it recieves it. 
* 
* Performance:
* Uses ~ 1/4 N^2 compares and ~ 1/4 N^2 exchanges on average.
* Best case, if the array is in ascending order: N - 1 compares and 0 exchanges: 
* O(n) comparisons, O(1) swaps.
* Worst case, if the array is in descending order and no duplicates:
* makes ~ 1/2 N^2 compares and ~ 1/2 N^2 exchanges: О(n^2) comparisons and swaps
* Average: О(n2) comparisons and swaps.
* Special case: For partially-sorted arrays, insertion sort runs in linear time. Number of
* exchanges equals the number of inversions. An inversion is a pair of keys that are out of 
* order. In other words, insertion sort is particularly good at dealing with partially 
* sorted arrays.
*
* Performance compared with selection sort:
* In best case it is better than selection sort, linear instead of quadratic. Worst case, in 
* the other hand, is worse than selection sort. Selection sort is: ~ 1/2 N^2 compares and N exchanges. 
* They both do around the same compares, but Insertion sort does many more exchanges.
*
* Demo:
* You can see an animation of this sorting algorithm at www.sorting-algorithms.com/insertion-sort
*/

// =================================================
//                   The Algorithm
// =================================================

/**
* Insertion sort algorithm.
* @param a The array to be sorted.
*/
var sort = function(a){
    N = a.length;                       // length of the array
    for (i = 0; i < N; i++){            // loop through the array
        for (j = i; j > 0; j--){        // loop from index i to 1
            if (a[j] < a[j - 1]){       // if index j < index j - 1:
                exch(a, j, j - 1);      // swap those items in the array
            }
            else break;                 // break the loop if j > j -1
        }
    }
};

// =================================================
//                 Helper Functions
// =================================================

/**
* Swaps two items in an array.
* @param i Index of item to be swaped.
* @param j Index of item to be swaped.
* @param a Array where the items will be swaped.
*/
var exch = function(a, i, j){
    swap = a[i];
    a[i] = a[j];
    a[j] = swap;
};

exports.sort = sort;