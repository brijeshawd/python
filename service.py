class CalculatorService:
    """
    Service implementing requirements for Jira MDP-7: Addition of 2 numbers.
    """
    
    def add(self, a, b):
        """
        Adds two numbers and returns the result.
        
        Args:
            a (int, float): The first number.
            b (int, float): The second number.
            
        Returns:
            int, float: The sum of a and b.
        """
        return a + b

# --- Example Usage/Test ---
if __name__ == "__main__":
    service = CalculatorService()
    
    num1 = 10
    num2 = 5
    result = service.add(num1, num2)
    
    print(f"Jira MDP-7 Test: {num1} + {num2} = {result}")