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


# Task 3a: Create a function that drop zeros
def drop_zeros(p_list):
    """
    Remove all zeros at the end the list p_list and return the result.
    """
    while p_list and p_list[-1] == 0:  # While p_list is not empty and the last element is 0, remove the last element
        p_list.pop()  # Remove the last element
    return p_list


# Task 3b: Create a function that checks if two polynomials are equal by ignoring zeros at the end of the list
def eq_poly(p_list, q_list):
    """
    Return True if the polynomials p_list and q_list are equal, otherwise return False.
    """
    p_list = drop_zeros(p_list)  # Remove zeros at the end of p_list
    q_list = drop_zeros(q_list)  # Remove zeros at the end of q_list
    if len(p_list) != len(q_list):  # If the length of p_list and q_list are not equal, they are not equal (False)
        return False
    for i in range(len(p_list)):  # Loop through the list
        if p_list[i] != q_list[i]:  # If the i elements of p_list and q_list are not equal, they are not equal (False)
            return False
    return True  # If the length of p_list and q_list are equal and the elements are equal, it is True


# Task 4: Create a function that evaluates a polynomial at a given point
def eval_poly(p_list, x):
    """
    Evaluate the polynomial given in p_list at the point x and return the result.
    """
    result = 0
    for i in range(len(p_list)):  # Loop through the list
        result += p_list[i] * x ** i  # Add the result of the polynomial at the point x to the result
    return result  # Return the result


# Task 5a: Create a function that convert a polynomial to its negative form
def negate_poly(p_list):
    """
    Negate the polynomial given in p_list.
    """
    return [-coeff for coeff in p_list]  # Return the list with all elements multiplied by -1


# Task 5b: Create a function that add two polynomials
def add_poly(p_list, q_list):
    """
    Add the polynomials p_list and q_list.
    """
    result = []
    for i in range(max(len(p_list), len(q_list))):  # Loop through the list with the highest length
        if i < len(p_list) and i < len(q_list):  # If i is less than the length of p_list and q_list (inside the range)
            result.append(p_list[i] + q_list[i])  # Add the elements of p_list and q_list and append to result list
        elif i < len(p_list):  # If i is less than the length of p_list, append the element of p_list
            result.append(p_list[i])
        else:  # If i is less than the length of q_list, append the element of q_list
            result.append(q_list[i])
    return drop_zeros(result)  # Return the result list without zeros at the end


# Task 5c: Create a function that subtract two polynomials
def sub_poly(p_list, q_list):
    """
    Subtract the polynomial p_list from the polynomial q_list.
    """
    return add_poly(p_list, negate_poly(q_list))  # Return the result of adding p_list and the negative of q_list

