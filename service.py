class MathService:
    """
    Service implementing requirements from Jira ticket MDP-7: 
    Addition of 2 numbers.
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
    service = MathService()
    
    num1 = 5
    num2 = 10
    result = service.add(num1, num2)
    
    print(f"Jira MDP-7 Implementation Test")
    print(f"Input: {num1}, {num2}")
    print(f"Result: {result}") # Expected: 15