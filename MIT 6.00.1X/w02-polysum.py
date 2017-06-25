import math


def polysum(n, s):
    """
    param n: number of sides
    param s: side length

    return: positive float rounded to 4 decimals, area + perimeter^2 of a polygon
    """
    # separate the top section and bottom section of area equation for added clarity
    top = (0.25 * n * s**2)
    bottom = math.tan(math.pi/n)
    area = top / bottom

    perim = n * s

    ans = area + perim**2
    ans = round(ans, 4)
    return ans


polysum(52, 66)
# 12714796.4405
polysum(28, 44)
# 1638101.3267
polysum(100, 57)
# 35074621.4083