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
    if not p_list or all(coeff == 0 for coeff in p_list):  # If the list is empty or all elements are 0, return 0
        return '0'
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if coeff == 0:  # Don't print 0x^degree
            degree += 1
            continue
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
print(poly_to_string([-1, -2, 0, -3, -1]))
print(poly_to_string_improved([-1, -2, 0, -3, -1]))
print(poly_to_string([0, 0, 0, 0, 0]))
print(poly_to_string_improved([0, 0, 0, 0, 0]))


def drop_zeros(p_list):
    """
    Remove all trailing zeros from the list p_list.
    """
    while p_list and p_list[-1] == 0:
        p_list.pop()
    return p_list

p0 = [2,0,1,0]

print(drop_zeros(p0))

q0 = [0,0,0]
print(drop_zeros(q0))

print(drop_zeros([]))


def eq_poly(p1, p2):
    """
    Return True if the polynomials p1 and p2 are equal, otherwise return False.
    """
    p1 = drop_zeros(p1)
    p2 = drop_zeros(p2)
    if len(p1) != len(p2):
        return False
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            return False
    return True

print(eq_poly(p, p0))
print(eq_poly(q, q0))
print(eq_poly(q0, []))


def eval_poly(p_list, x):
    """
    Evaluate the polynomial given in p_list at the point x.
    """
    result = 0
    for i in range(len(p_list)):
        result += p_list[i] * x ** i
    return result

print(eval_poly(q, -2))
print(poly_to_string_improved(q))


def negate_poly(p_list):
    """
    Negate the polynomial given in p_list.
    """
    return [-coeff for coeff in p_list]

print(poly_to_string_improved(negate_poly(q)))