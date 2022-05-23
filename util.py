def lerp(x, x0, x1, y0, y1):
    """Calculate linear interpolation. Clamp x within x0 and x1 bounds."""
    if x > x1:
        x = x1
    if x < x0:
        x = x0
    return round(y0 + (y1 - y0) * ((x - x0) / (x1 - x0)))

def lerp3(x, x0, x1, y0, y1):
    """Calculate linear interpolation of all values of 3-tuple."""
    return lerp(x, x0, x1, y0[0], y1[0]), lerp(x, x0, x1, y0[1], y1[1]), lerp(x, x0, x1, y0[2], y1[2])
