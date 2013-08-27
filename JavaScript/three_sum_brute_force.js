// ==================================================
//    The 3-Sum algorithm, brute force approach
// ==================================================

// 3-Sum algorithm, brute force approach. 
// Running time: 10^-10 * N^3 seconds, where N is the number of numbers in the array.
// It solves the problem: Given N distinct integers, how many triples sum exactly zero?

// Counts how many triples sum to exactly zero. 
// It has a triple for loop that checks if each triple i, j, k sum equals zero.
var threeSumCount = function(numberArray){

    var arrayLength = numberArray.length; // Length of the input array, used in the for loop
    var count       = 0;                  // Will keep track of the number of triples that sum 0

    for(var i = 0; i < arrayLength; i++){
        for(var j = i + 1; j < arrayLength; j++){
            for(var k = j + 1; k < arrayLength; k++){ // Check each triple.
                if(numberArray[i] + numberArray[j] + numberArray[k] === 0){ // For simplicity, ignore integer overflow.
                    count ++; // Add one to count if the triple sums zero.
                }
            }
        }
    }

    return count;
};

// Same as threeSumCount(), but this implementation counts and returns the number of array accesses.
var threeSumCount2 = function(numberArray){

    var arrayLength = numberArray.length;
    var count       = 0;
    var arrayAccess = 0;

    for(var i = 0; i < arrayLength; i++){
        for(var j = i + 1; j < arrayLength; j++){
            for(var k = j + 1; k < arrayLength; k++){
                arrayAccess += 3; // Add 3 to array access count.
                if(numberArray[i] + numberArray[j] + numberArray[k] === 0){
                    count ++;
                }
            }
        }
    }

    return arrayAccess; // !!!Note that it is returning the number of array accesses!!!
};

// Same as threeSumCount(), but this returns an array of the different states i, j, k had.
var threeSumCount3 = function(numberArray){

    var arrayLength = numberArray.length;
    var count       = 0;
    var ijkValues   = [];

    for(var i = 0; i < arrayLength; i++){
        for(var j = i + 1; j < arrayLength; j++){
            for(var k = j + 1; k < arrayLength; k++){
                ijkValues.push([i, j, k]);
                if(numberArray[i] + numberArray[j] + numberArray[k] === 0){
                    count ++;
                }
            }
        }
    }

    return ijkValues;
};

// ==================================================
//                     Test Area
// ==================================================

// =================
// Helper functions:   
// =================

// Produces an array with random integers between min and max
function makeRandomArray(size, max, min){
    var returnArray = [];
    for (var i = 0; i < size; i++){
        returnArray[i] = Math.floor(Math.random() * (max - min + 1)) + min;
    }
    return returnArray;
}

// Produces arrays of random numbers
function makeManyRandomArrays(howManyArrays, sizeOfArrays, maxValue, minValue){
    var returnArray = [];
    for (var i = 0; i < howManyArrays; i ++){
        returnArray[i] = makeRandomArray(sizeOfArrays, maxValue, minValue);
    }
    return returnArray;
}

// ===================
// Array declarations: 
// ===================

var array0 = [1, -1, 2, -2, 3];
var array1 = [1, -2, 1, 1];
var array2 = [3, 4, 5, 6];
var array3 = makeRandomArray(100, 100, -100);

// Arrays of arrays. 

// There are arrays that cointain arrays of random integers bewteen 100 and -100 of size 100.
// arrays10 contains 10 arrays, arrays20 contains 20 arrays and so on. This will be used to measure
// the run time of the Three-sum algorithm with different array sizes, an average run time is 
// calculated. 
var arrays10   = makeManyRandomArrays(100, 10, 100, -100);
var arrays20   = makeManyRandomArrays(100, 20, 100, -100);
var arrays40   = makeManyRandomArrays(100, 40, 100, -100);
var arrays80   = makeManyRandomArrays(100, 80, 100, -100);
var arrays160  = makeManyRandomArrays(100, 160, 100, -100);
var arrays320  = makeManyRandomArrays(100, 320, 100, -100);
var arrays640  = makeManyRandomArrays(100, 640, 100, -100);
var arrays1280 = makeManyRandomArrays(100, 1280, 100, -100);
var arrays2560 = makeManyRandomArrays(100, 2560, 100, -100);

// ===================
// Time Measurements: 
// ===================

// Function that measures average time execution
function timeMeasure(arrayOfArrays){
    var size         = arrayOfArrays.length; // For use in for loop and average time
    var arrayOfTimes = [];  // Write times into this array
    var sum          = 0;   // sum of all the times
    var average      = 0;   // time average
    for(var i = 0; i < size; i++){
        var timeStart = new Date().getTime();

        // Start of function to be time measured

        threeSumCount(arrayOfArrays[i]);

        // End of function to be time measured

        var timeEnd   = new Date().getTime();
        var totalTime = timeEnd - timeStart;
        arrayOfTimes[i] = totalTime;
    }

    // Calculate average times:
    for(var j = 0; j < size; j++){
        sum += arrayOfTimes[j];
    }
    average = sum / size;

    return average;
}

// Calculate average times, in milliseconds:
// average10 contains arrays of size 10, average20 contains arrays of size 20, and so on.
// var average10   = timeMeasure(arrays10);
// var average20   = timeMeasure(arrays20);
// var average40   = timeMeasure(arrays40);
// var average80   = timeMeasure(arrays80);
// var average160  = timeMeasure(arrays160);
// var average320  = timeMeasure(arrays320);
// // Caution, the ones below can take a while.
// var average640  = timeMeasure(arrays640);
// var average1280 = timeMeasure(arrays1280);
// var average2560 = timeMeasure(arrays2560);

// ===================
// Other Tests
// ===================

var ijkValuesS4 = threeSumCount3(array0);


// ===================
// Logs:
// ===================

// some simple testing, to make sure everything is ok
// console.log(new Date().getTime());
// console.log(threeSumCount(array1)); // 3
// console.log(threeSumCount(array2)); // 0
// console.log(threeSumCount(array3)); // array of random numbers 

// observation of ijk values' dynamics:
console.log(ijkValuesS4);

// Time results
// console.log("Average running time for arrays of size 10: " + average10);
// console.log("Average running time for arrays of size 20: " + average20);
// console.log("Average running time for arrays of size 40: " + average40);
// console.log("Average running time for arrays of size 80: " + average80);
// console.log("Average running time for arrays of size 160: " + average160);
// console.log("Average running time for arrays of size 320: " + average320);
// // Caution, the ones below can take a while.
// console.log("Average running time for arrays of size 640: " + average640);
// // console.log("Average running time for arrays of size 1280: " + average1280);
// // console.log("Average running time for arrays of size 2560: " + average2560);

