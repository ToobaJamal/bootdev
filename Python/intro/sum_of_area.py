'''
Complete the area_sum() function. It accepts an array of rectangles, where each rectangle is a dictionary that has the following structure:

{
  "height": 5,
  "width": 6
}
The function will calculate the area of each rectangle, then sum them all up and return the result.
'''

def area_sum(rectangles):
    sum_of_area = 0
    area = 1
    for i in rectangles:
        area = i["height"] * i["width"]
        sum_of_area += area
    return sum_of_area    
