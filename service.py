class MathService:
    """
    Service implementation for MDP-7: Addition of 2 numbers.
    """
    
    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers together and returns the result.
        
        Args:
            a (float): The first number.
            b (float): The second number.
            
        Returns:
            float: The sum of a and b.
        """
        return a + b

# --- Example Usage ---
if __name__ == "__main__":
    service = MathService()
    
    num1 = 10
    num2 = 5
    result = service.add(num1, num2)
    
    print(f"Jira Ticket MDP-7: Adding {num1} + {num2}")
    print(f"Result: {result}")