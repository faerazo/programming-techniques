# Part 1: Polynomial representation, function provided by the professor.

def poly_to_string(p_list):
    """
    Return a string with a nice readable version of the polynomial given in p_list.
    """
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if degree == 0:
            terms.append(str(coeff))
        elif degree == 1:
            terms.append(str(coeff) + 'x')
        else:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)
        degree += 1

    final_string = ' + '.join(terms)  # The string ' + ' is used as "glue" between the elements in the string
    return final_string


# Part 2: Polynomial evaluation

p = [2, 0, 1]  # the evaluation of this list on poly_to_string should be equal to 2 + 0x + 1x^2
q = [-2, 1, 0, 0, 1]  # the evaluation of this list on poly_to_string should be equal to -2 + 1x + 0x^2 + 0x^3 + 1x^4


# Part 3: Edit the function poly_to_string with some new features

def poly_to_string_improved(p_list):
    """
    Return a string with a nice readable version of the polynomial given in p_list.
    """
    if not p_list:  # If the list is empty, return 0
        return '0'
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if coeff == 1 and degree > 0:  # Don't print 1x, print x instead
            if degree == 1:
                terms.append('x')
            else:
                term = 'x^' + str(degree)
                terms.append(term)
        elif coeff == -1:
            if degree == 0:
                terms.append('-1')
            elif degree == 1:
                terms.append('-x')
            else:
                term = '-x^' + str(degree)
                terms.append(term)

        else:
            if degree == 0:
                terms.append(str(coeff))
            elif degree == 1:
                terms.append(str(coeff) + 'x')
            else:
                term = str(coeff) + 'x^' + str(degree)
                terms.append(term)
        degree += 1

    final_string = ' + '.join(terms)  # The string ' + ' is used as "glue" between the elements in the string
    return final_string


print(poly_to_string(p))
print(poly_to_string_improved(p))
print(poly_to_string(q))
print(poly_to_string_improved(q))
print(poly_to_string([-1, -2, 0, -3]))
print(poly_to_string_improved([-1, -2, 0, -3]))

