
(* is date1 older than date2? *)
fun is_older(date1 : int*int*int, date2 : int*int*int) =
    let
        (* converts a date to julian days *)
        (* https://en.wikipedia.org/wiki/Julian_date *)
        fun julian(date : int*int*int) = 
            let
            val y = real(#1 date)
            val m = real(#2 date)
            val d = real(#3 date)
        in
            (367.0 * y) - 7.0 * (y + 5001.0 + (m - 9.0) / 7.0) / 4.0 +
            275.0 * m / 9.0 + d + 1729776.5
        end
    in
        julian date1 < julian date2
    end 

(* returns number of dates that are in the given month *)
fun number_in_month(dates : (int*int*int) list, month: int) = 
    if   null dates
    then 0
    else if #2 (hd dates) = month
    then 1 + number_in_month(tl dates, month)
    else number_in_month(tl dates, month)

(* returns number of dates that are in any of the months *)
fun number_in_months(dates : (int*int*int) list, months : int list) =
    if   null months
    then 0
    else number_in_month(dates, hd months) + number_in_months(dates, tl months)

(* returns a list of dates that are in the given month *)
fun dates_in_month(dates : (int*int*int) list, month : int) = 
    if null dates
    then []
    else if #2 (hd dates) = month
    then (hd dates)::dates_in_month(tl dates, month)
    else dates_in_month(tl dates, month)

(* returns a list of dates that are in any of the given months *)
fun dates_in_months(dates : (int*int*int) list, months : int list) = 
    if   null months
    then []
    else dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

(* get the nth string *)
fun get_nth(strings : string list, n : int) = 
    if   n <= 1
    then hd strings
    else get_nth(tl strings, n - 1)

(* date to string *)
fun date_to_string(date : int*int*int) = 
    let
        val month_names = ["January", "February", "March", "April", "May", "June", 
                           "July", "August", "September", "October", "November", "December"]
    in
        get_nth(month_names, #2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)
    end

(* number of elements before reaching sum*)
fun number_before_reaching_sum(sum : int, intlist : int list) =
    if   sum <= hd intlist 
    then 0
    else 1 + number_before_reaching_sum(sum - hd intlist, tl intlist)

(* returns the number of month that corresponds to a number of day in a year *)
fun what_month(day : int) = 
    let
        val intlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in
        1 + number_before_reaching_sum(day, intlist)
    end

(* returns the range of months between two days, as a list *)
fun month_range(day1 : int, day2 : int) = 
    if   day1 > day2
    then []
    else what_month day1 :: month_range(day1 + 1, day2) 

(* returns the oldest date in a list *)
fun oldest (dates : (int * int * int) list) =
    if null dates
    then NONE
    else 
        let fun f dates =
                if null (tl dates)
                then hd dates
                else 
                    let val ans = f (tl dates)
                    in if is_older(ans, hd dates)
                       then ans
                       else hd dates
                    end
        in SOME(f dates) end  


(* ========= Challenges ========= *)

(* removes duplicates from an int list *)
fun remove_duplicates(numbers: int list)=
    let
        fun aux(xs: int list, y: int)=
            if null xs
            then []
            else if hd xs = y
            then aux(tl xs, y)
            else hd xs :: aux(tl xs, y)
    in
        if null numbers orelse null(tl numbers)
        then numbers
        else hd numbers :: remove_duplicates(aux(tl numbers, hd numbers))
    end

(* returns number of dates that are in the given month *)
fun number_in_months_challenge(dates: (int*int*int) list, months: int list) =
    number_in_months(dates, remove_duplicates(months))

(* returns a list of dates that are in any of the given months *)
fun dates_in_months_challenge(dates: (int*int*int) list, months: int list) =
    dates_in_months(dates, remove_duplicates(months))

(* number of days on each month *)
fun days_in_month(month: int) =
    let 
        fun list_in(y: int, xs: int list) =
            not (null xs) andalso (y = hd xs orelse list_in(y, tl xs))
    in
        if list_in(month, [1, 3, 5, 7, 8, 10, 12])
        then 31
        else 
            if list_in(month, [4, 6, 9, 11])
            then 30
            else 28
    end

(* is the date reasonable? *)
fun reasonable_date(date: int*int*int) =
    let
        val year  = #1 date;
        val month = #2 date;
        val day   = #3 date;
        fun is_leap(year: int) =
            year mod 400 = 0 orelse (year mod 4 = 0 andalso year mod 100 <> 0)
        fun check_year() = 
            year > 0
        fun check_month() = 
            0 < month andalso month < 13
        fun check_day() =
            if month = 2 andalso day = 29
            then is_leap(year)
            else 0 < day andalso day <= days_in_month(day)
        fun is_date_in_month(date: (int*int*int), number: int) =
            number = #2 date andalso #3 date <= days_in_month(#2 date)
    in
      check_year() andalso check_month() andalso check_day()
    end;


