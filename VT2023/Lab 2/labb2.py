# Task 1: Polynomial representation, function provided by the professor.
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


# Define two lists for evaluating the function poly_to_string
p = [2, 0, 1]  # The evaluation of this list on poly_to_string should be equal to 2 + 0x + 1x^2
q = [-2, 1, 0, 0, 1]  # The evaluation of this list on poly_to_string should be equal to -2 + 1x + 0x^2 + 0x^3 + 1x^4


# Task 2: Edit the function poly_to_string with some new features
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
        # If statement for coefficients that are 0
        if coeff == 0:  # If coefficient is 0, continue to next iteration and increase degree by 1 (not added to list)
            degree += 1
            continue
        # If statement for coefficients that are 1
        if coeff == 1 and degree > 0:  # If coefficient is 1 and degree is greater than 0, append x or x^degree
            if degree == 1:
                terms.append('x')
            else:
                term = 'x^' + str(degree)
                terms.append(term)
        # If statement for coefficients that are -1
        elif coeff == -1:
            if degree == 0:  # If coefficient is -1 and degree is 0, append -1
                terms.append('-1')
            elif degree == 1:  # If coefficient is -1 and degree is 1, append -x
                terms.append('-x')
            else:  # If coefficient is -1 and degree is other than 1, append -x^degree
                term = '-x^' + str(degree)
                terms.append(term)
        # If statement for coefficients that are not 0, 1, -1
        else:
            if degree == 0:  # If degree is 0, append coefficient
                terms.append(str(coeff))
            elif degree == 1:  # If degree is 1, append coefficient*x
                terms.append(str(coeff) + 'x')
            else:  # If degree is other than 1, append coefficient*x^degree
                term = str(coeff) + 'x^' + str(degree)
                terms.append(term)
        degree += 1  # Increase degree by 1

    final_string = ' + '.join(terms)  # The string ' + ' is used as "glue" between the elements in the string
    return final_string


# Part 4: Create a function that drop zeros
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

def add_poly(p1, p2):
    """
    Add the polynomials p1 and p2.
    """
    result = []
    for i in range(max(len(p1), len(p2))):
        if i < len(p1) and i < len(p2):
            result.append(p1[i] + p2[i])
        elif i < len(p1):
            result.append(p1[i])
        else:
            result.append(p2[i])
    return drop_zeros(result)


print(p)
print(q)
print(poly_to_string_improved(add_poly(p, q)))

print(eq_poly(add_poly(p, q), add_poly(q, p)))


def sub_poly(p1, p2):
    """
    Subtract the polynomial p2 from the polynomial p1.
    """
    return add_poly(p1, negate_poly(p2))

print(poly_to_string_improved(sub_poly(p, q)))



