class MathService:
    """
    Service implementing requirements from Jira MDP-7: Addition of 2 numbers
    """
    def add(self, a, b):
        """
        Adds two numbers together.
        
        Args:
            a (int, float): First number
            b (int, float): Second number
            
        Returns:
            int, float: The sum of a and b
        """
        return a + b

# --- Example Usage ---
if __name__ == "__main__":
    service = MathService()
    
    num1 = 5
    num2 = 10
    result = service.add(num1, num2)
    
    print(f"Jira Ticket MDP-7: Addition of 2 numbers")
    print(f"Input: {num1}, {num2}")
    print(f"Result: {result}")