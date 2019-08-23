def check_difference(protrusion, filename):
    """Check whether the protrusion pixel was also nonzero in the previous plane

   """

    from read_plane import read_plane
    if len(protrusion) < 4:
        return False
    if protrusion[3] == 1:
        return False
    plane, z, c, t = read_plane(filename, protrusion[3]-1)
    if plane[int(round(protrusion[1]))][int(round(protrusion[0]))]:
        return True

    return False
