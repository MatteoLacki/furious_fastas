def covered_area(sorted_intervals):
    """Calculate the area covered by the submitted intervals.

    Args:
        sorted_intervals (list): Tuples of two floats: the beginning and the end of an interval, increasing with the beginnings.

    Results:
        integer: The area covered by the intervals.
    """
    s0 = e0 = -float('Inf')
    N = 0
    for s1,e1 in sorted_intervals:
        if s1 >= e0:
            N += e1-s1
            s0,e0 = s1,e1
        else:
            if e1 > e0:
                N += e1-e0
                e0 = e1
    return N
