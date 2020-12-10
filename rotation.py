def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in radians.
    """
    # Convert negative angles to positive
    angle = normalise_angle(angle)

    # Convert to radians
    angle = math.radians(angle)

    # Convert to radians
    ox, oy = origin
    px, py = point
    
    # Move point 'p' to origin (0,0)
    _px = px - ox
    _py = py - oy
    
    # Rotate the point 'p' 
    qx = (math.cos(angle) * _px) - (math.sin(angle) * _py)
    qy = (math.sin(angle) * _px) + (math.cos(angle) * _py)
    
    # Move point 'p' back to origin (ox, oy)
    qx = ox + qx
    qy = oy + qy
    
    return [qx, qy]


def normalise_angle(angle):
    """ If angle is negative then convert it to positive. """
    if (angle != 0) & (abs(angle) == (angle * -1)):
        angle = 360 + angle
    return angle
