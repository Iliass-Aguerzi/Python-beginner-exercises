def greet(name, time_of_day):
    corrected_time = time_of_day.lower().capitalize()
    corrected_name = name.lower().capitalize()
    greeting = f"Good {corrected_time},{corrected_name}!"
    return greeting


print(greet("ILIASS", "morning"))

