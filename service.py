class CalculatorService:
    """
    Service implementation for Jira Ticket MDP-7: Addition of 2 numbers
    """
    
    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers together.
        
        Args:
            a (float): The first number.
            b (float): The second number.
            
        Returns:
            float: The sum of a and b.
        """
        return a + b

# --- Example Usage ---
if __name__ == "__main__":
    service = CalculatorService()
    
    # Test case 1: Positive integers
    result1 = service.add(5, 10)
    print(f"Addition of 5 + 10 = {result1}") # Expected: 15
    
    # Test case 2: Floating point numbers
    result2 = service.add(2.5, 4.1)
    print(f"Addition of 2.5 + 4.1 = {result2}") # Expected: 6.6