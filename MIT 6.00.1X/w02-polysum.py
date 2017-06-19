import math


def polysum(n, s):
    """
    n: number of sides
    s: side length

    returns: positive float rounded to 4 decimals, area + perimeter^2 of a polygon
    """
    # separate the top section and bottom section of area equation for added clarity
    top = (0.25 * n * s**2)
    bottom = math.tan(math.pi/n)
    area = top / bottom
    # perimeter of the polygon
    perim = n * s
    # the final answer needs to be rounded to 4 decimal places
    ans = area + perim**2
    ans = round(ans, 4)
    return ans


polysum(52, 66)
# 12714796.4405
polysum(28, 44)
# 1638101.3267
polysum(100, 57)
# 35074621.4083