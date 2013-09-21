// =================================================
//                   The Algorithm
// =================================================

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

var exch = function(a, i, j){
    swap = a[i];
    a[i] = a[j];
    a[j] = swap;
};

exports.sort = sort;