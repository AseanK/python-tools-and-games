from typing import List, Tuple

SUPPRORTED_OPS = ["+", "-", "*", "/"]

def begins_with_negative(equation:str) -> bool:
    """Checks if an equation begins with a negative (edge case for having string-initial negative #'s)"""
    return equation[0] == "-"

def is_operator(char:str) -> bool:
    """Checks of a given string character is an operator (aka, not a digit)"""
    return not char.isdigit()

def has_correct_equation_sides(equation:str) -> bool:
    """Checks if an equation has operators at the beginning or end of it, which is illicit (except for negative #'s at the beginning)"""
    try:
        beginning = equation[0]
        end = equation[-1]
    except IndexError:
        return False
    
    if beginning in SUPPRORTED_OPS or end in SUPPRORTED_OPS:
        if not begins_with_negative(equation):
            return False
    return True
        
def has_correct_neighbors(equation:str, operator_indices:List[int]) -> bool:
    """Each operator should have at least one digit on either side. """
    
    for operator_idx in operator_indices:
        left_neighbor = equation[operator_idx-1]
        right_neighbor = equation[operator_idx+1]
        #print(f"{left_neighbor = } AT {operator_idx-1}")
        #print(f"{right_neighbor = } AT {operator_idx+1}")
        
        if not left_neighbor.isdigit() or not right_neighbor.isdigit():
            return False
        
    return True

def contains_operators(equation:str) -> bool:
    """Check if there are any operators in the equation"""
    for char in equation:
        if is_operator(char) and char in SUPPRORTED_OPS:
            return True
    return False

def valid_equation_format(equation:str, equation_ops:List[int]) -> bool:
    """Applies all input validation functions to the user's equation"""
    
    if not has_correct_equation_sides(equation):
        print("Equation has trailing operators")
        return False
    
    if not has_correct_neighbors(equation, equation_ops):
        print("Equation has incorrect neighbors")
        return False
    
    if not contains_operators(equation):
        print("Equation does not contain operators")
        return False
    
    return True


def calculate(op:str, i:int, j:int) -> int:
    """Given an operator and two numbers, performs that operation on the nums"""    
    result = i+j if op == "+" else \
             i-j if op == "-" else \
             i*j if op == "*" else \
             i/j if op == "/" else None
    return result


def get_initial_op_left_num(equation:str, op_index:int) -> int:
    """Retrieves the numbers on an operators left side. This func is only called for the first operator in an equation"""
    digits = []
    
    for char in equation[op_index-1::-1]:
        if not is_operator(char):
            digits.append(char)
        else:
            break

    num = int("".join(digits))
    return -(num) if begins_with_negative(equation) else num

def get_op_right_num(equation:str, op_index:int) -> int:
    """Retrieves the numbers on an operators right side"""
    digits = []
    for char in equation[op_index+1:]:
        if not is_operator(char):
            digits.append(char)
        else:
            break
    return int("".join(digits))

def parse_equation(equation:str, equation_ops:List[int]):
    """Function is a bit messy"""
    result = None
    
    for i in equation_ops:
        current_op = equation[i]
        left_num = get_initial_op_left_num(equation, i) if result is None else result
        right_num = get_op_right_num(equation, i)
        result = calculate(current_op, left_num, right_num)
    
    return result
        
def locate_operators(equation:str) -> List[int]:
    """Given an equation, locates the string indices of each operator"""
    op_indices = []
    for i, char in enumerate(equation):
        if char in SUPPRORTED_OPS:
            if i == 0 and begins_with_negative(equation):
                continue
            op_indices.append(i)
            
    return op_indices

def main():
    
    print("Enter your equation here. Example: 4+3-55/2**2")
    print(f"Currently supported operations:{SUPPRORTED_OPS}\n")
    print("NOTE: Equations are strictly evaluated left-to-right (parenthesis NOT supported)")
    print("Type '\end' to exit the application")
    equation = ""
    while equation != "\end":
        equation = input(">>> ").strip()
        
        if equation != "\end":
            equation_ops = locate_operators(equation)
            if not valid_equation_format(equation, equation_ops):
                print(f"Invalid equation: '{equation}'. Please try again or type \end to quit")
            else:
                try:
                    print(parse_equation(equation, equation_ops))
                except ZeroDivisionError:
                    print("Your equation resulted in a ZeroDivisonError. Try again.")
    
    
    

    
    
if __name__ == "__main__":
    main()