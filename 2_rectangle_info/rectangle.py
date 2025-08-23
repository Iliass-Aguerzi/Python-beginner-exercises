def rectangle_info(length, width):
    area = length*width
    perimeter = 2*(length+width)
    return (area, perimeter)


print(rectangle_info(5, 3))
"""
Calculates and returns the area and perimeter of a rectangle.

Args:
    length (float): The length of the rectangle
    width (float): The width of the rectangle

Returns:
    tuple: A tuple containing (area, perimeter)

Example:
     rectangle_info(5, 3)
    (15, 16)
"""
