var factorial_recursive = {
    arg x;
    if  (x == 0)
        { 1 }
        { factorial_recursive.(x-1) * x }
};

factorial_recursive.value(10);