def greet(name, time_of_day):
    """
    Generates a personalized greeting based on time of day.
    
    Args:
        name (str): The person's name
        time_of_day (str): Time of day ('morning', 'evening')
    
    Returns:
        str: Formatted greeting
    """
    corrected_time = time_of_day.lower().capitalize()
    corrected_name = name.lower().capitalize()
    greeting = f"Good {corrected_time}, {corrected_name}!"  # Added space after comma
    return greeting

# Example usage - only runs if this file is executed directly
if __name__ == "__main__":
    print(greet("ILIASS", "morning"))
