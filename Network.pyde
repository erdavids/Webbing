w, h = 1000, 1000

# Points
point_count = 6000

point_seperation = 4
connection_chance = .4
connection_distance = 30

use_noise = True
noise_scale = .02
noise_range = (.2, .5)

# Colors for the gradient 
colors = [(255, 20, 20), (0, 225, 225), (0, 0, 0)]

# Returns the color between two colors at a specific step in the gradient
def get_gradient_point(color_one, color_two, step, max_steps):
    s = (float(step)/max_steps)
    
    r = (color_two[0] - color_one[0]) * s + color_one[0]
    if (r < 0):
        r += 255.0
        
    g = (color_two[1] - color_one[1]) * s + color_one[1]
    if (g < 0):
        g += 255.0
        
    b = (color_two[2] - color_one[2]) * s + color_one[2]
    if (b < 0):
        b += 255.0
    
    return (r, g, b)

def setup():
    size(w, h)
    
    pixelDensity(2)
    
    background(30, 30, 30)
    
    
    points = []
    
    for i in range(point_count):
        
        # Give 50 attempts per point
        for a in range(20):
            new_point = (random(w), random(h))
            
            valid = True
            n = noise(new_point[0] * noise_scale, new_point[1] * noise_scale)
            if n < noise_range[0] or n > noise_range[1]:
                valid = False
            for e in points:
                if sqrt(pow(e[0] - new_point[0], 2) + pow(e[1] - new_point[1], 2)) < point_seperation:
                    valid = False
                    
            if (valid == True):
                points.append(new_point)
                break
            
    for i in points:
        for j in points:
            if sqrt(pow(i[0] - j[0], 2) + pow(i[1] - j[1], 2)) < connection_distance and random(1) < connection_chance:
                stroke(*get_gradient_point(colors[0], colors[1], j[1], h))
                line(i[0], i[1], j[0], j[1])
    print(points)
    
    save("Examples/web-2.png")
