class MathService:
    """
    Service providing basic mathematical operations.
    """
    def add(self, a, b):
        """
        Returns the sum of two numbers.
        """
        return a + b

# --- Example Usage ---
if __name__ == "__main__":
    service = MathService()
    
    num1 = 10
    num2 = 5
    result = service.add(num1, num2)
    
    print(f"The sum of {num1} and {num2} is: {result}")