from typing import List
import re


SUPPRORTED_OPS = ["+", "-", "*", "/", "**"]

def user_input():
    return input(">>>").strip()

def begins_with_negative(equation:str) -> bool:
    """Checks if an equation begins with a negative (edge case for having string-initial negative #'s)"""
    return equation[0] == "-"

def has_correct_equation_sides(equation:str) -> bool:
    """Checks if an equation has operators at the beginning or end of it, which is illicit (except for negative #'s at the beginning)"""
    beginning = equation[0]
    end = equation[-1]
    if beginning in SUPPRORTED_OPS or end in SUPPRORTED_OPS:
        if not begins_with_negative(equation):
            return False
    return True
        
    
def has_correct_neighbors(equation:str, operator_indices:List[int]) -> bool:
    """Each operator should have at least one digit on either side. """
    
    if len(equation) < 3:
        return False
    
    for operator_idx in operator_indices:
        left_neighbor = equation[operator_idx-1]
        right_neighbor = equation[operator_idx+1]
        print(f"{left_neighbor = } AT {operator_idx-1}")
        print(f"{right_neighbor = } AT {operator_idx+1}")
        
        if not left_neighbor.isdigit() or not right_neighbor.isdigit():
            return False
        
    return True

    


def validate_equation_format(equation:str, equation_ops:List[int]) -> bool:
    """Applies all input validation functions to the user's equation"""
    
    if not has_correct_equation_sides(equation):
        print("Equation has trailing operators")
        return False
    
    if not has_correct_neighbors(equation, equation_ops):
        print("Equation has incorrect neighbors")
        return False
    return True
        
        
    
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
    print(f"Currently supported operations:{SUPPRORTED_OPS}")
    print("Equations are evaluated left-to-right. Parenthesis are currently not supported")
    print("Type '\end' to exit the application")
    equation = ""
    while equation != "\end":
        equation = user_input()
        equation_ops = locate_operators(equation)
        
        
        print(validate_equation_format(equation, equation_ops))
    
    
    

    
    
if __name__ == "__main__":
    main()