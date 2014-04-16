var factorial_while = {
    arg x;
    var acc = 1;
    while {x > 0}
          {acc = acc * x; x = x - 1};
    acc;
};

var factorial_for = {
    arg x;
    var acc = 1;
    for (1, x)
        {arg i; acc = acc * i};
    acc;
};

var factorial_recursive = {
    arg x;
    if (x == 0)
       {1}
       {factorial_recursive.value(x - 1) * x}
};

var factorial_tail_recursive = {
    arg x;
    var tail_helper = {
        arg x, acc;
        if (x < 1)
           {acc}
           {tail_helper.value(x - 1, acc * x)};
    };
    tail_helper.value(x, 1);
};
