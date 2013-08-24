// Returns the sorted version of the input array
function bubbleSort(theArray){
    var returnArray = theArray;
    var length      = returnArray.length - 1;
    var isSorted    = false;
    // Will continue iterating until no swap is made, in that case
    // isSorted = True and the sorted array is returned.
    while (isSorted !== true){
        isSorted = true;
        for (var i = 0; i < length; i++){
            if (returnArray[i] > returnArray[i + 1]){
                isSorted = false; // flag that there was a swap in the scan
                returnArray[i]     = returnArray[i + 1]; // swap items
                returnArray[i + 1] = returnArray[i];     // swap items
            }
        }
    }
    return returnArray;
}
