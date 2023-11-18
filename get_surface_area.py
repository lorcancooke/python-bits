from math import tan, sqrt, pi

def get_surface_area (f, n, s):
    #f = number of faces
    #n = no of faces per side
    #s = side length


    surface_area = (f * n * (s**2))/(4*tan(pi/n))

    return (surface_area)

print(f"{get_surface_area(8, 8, 5):.2f}")
