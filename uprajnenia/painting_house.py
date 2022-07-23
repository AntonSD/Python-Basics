x = float(input())
y = float(input())
h = float(input())
side_wall = x * y
window = 1.5 * 1.5
total_side_walls = 2 * side_wall - 2 * window
back_wall = x * x
entrance = 1.2 * 2
back_front_walls = 2 * back_wall - entrance
total_green_area = total_side_walls + back_front_walls
green_paint = total_green_area / 3.4
roof_rectangle = 2 * (x * y)
roof_triangles = 2 * ((x * h) / 2)
roof = roof_rectangle + roof_triangles
red_paint = roof / 4.3
print(green_paint)
print(red_paint)