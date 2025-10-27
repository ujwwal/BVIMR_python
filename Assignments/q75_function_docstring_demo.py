def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Compute the Euclidean distance between two points (x1, y1) and (x2, y2).

    Parameters:
    - x1, y1: Coordinates of the first point.
    - x2, y2: Coordinates of the second point.

    Returns:
    - float: The distance between the two points.

    Example:
    >>> distance(0, 0, 3, 4)
    5.0
    """
    dx = x2 - x1
    dy = y2 - y1
    return (dx * dx + dy * dy) ** 0.5

if __name__ == "__main__":
    print(distance.__doc__)
    print("Distance (0,0) to (3,4):", distance(0, 0, 3, 4))