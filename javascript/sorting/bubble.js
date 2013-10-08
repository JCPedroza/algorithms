// ========================================
//             Algorithm Area
// ========================================

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
                isSorted           = false;               // flag that there was a swap in the scan
                var toSwap         = returnArray[i];      // buffer to use in swap
                returnArray[i]     = returnArray[i + 1];  // swap items
                returnArray[i + 1] = toSwap;              // swap items
            }
        }
    }
    return returnArray;
}

// ========================================
//                Test Area
// ========================================

// Produces an array with random integers between min and max
function makeRandomArray(size, max, min){
    var returnArray = [];
    for (var i = 0; i < size; i++){
        returnArray[i] = Math.floor(Math.random() * (max - min + 1)) + min;
    }
    return returnArray;
}

// Array declarations to use in tests
var testArray1 = [3, 2, 1];
var testArray2 = [10, 7, 6, 99, 120, 20, 59, 48, 13];
var testArray3 = makeRandomArray(10, 0, 10);

// Tests
var testArray1Sorted = bubbleSort(testArray1);
var testArray2Sorted = bubbleSort(testArray2);
var testArray3Sorted = bubbleSort(testArray3);

// Prints
console.log(testArray1Sorted);
console.log(testArray2Sorted);
console.log(testArray3Sorted);