def longest_side(max_len):
    solutions = [[x,y,z]
        for x in range(5, mx_len)
        for y in range(4, max_len)
        for z in range(3, max_len):
        if (x*x==y*y+z*z)
        ]
    return max([max(solution) for solution in solutions]);
    for solution in solutions:
        if m < max(solution):
            m = max(solution)
    return m

max_len = input("What is the maximal length of the triangle side? Enter a number: ")

print("The longest side possible is " + str(longest_side(int(max_len))))

