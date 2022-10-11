import math
# from shapely.geometry import Polygon, Point
from sympy import Polygon, Point, Ellipse
import numpy as np


def gen_line(p1, p2):
    """
    Line ax + by + c = 0
    :return: {"a": a, "b": b, "c": c}
    """
    a = - p1[1] + p2[1]
    b = p1[0] - p2[0]
    c = - b * p1[1] - a * p1[0]
    return {"a": a, "b": b, "c": c}


def calc_dist(p1, p2):
    """
    Calculates distance B/W P1, P2
    :return: distance: int
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def calc_poly_dist(poly, p):
    """
    :param p: 0-->p1, 1-->p2
    :param poly: Polygon represented by the list of tuple(x, y) of vertices.
    :return: Returns distance b/w the point and the give polygon.
    """
    v = map(Point, poly)
    poly = Polygon(*v)
    pnt = p

    return poly.distance(Point(pnt[0], pnt[1])) * (int(poly.encloses_point(Point(pnt[0], pnt[1]))) * (-2) + 1)


def calc_poly_tang(poly, p):
    """
    :param p: 0-->p1, 1-->p2
    :param poly: Polygon represented by the list of tuples(x, y) of vertices.
    :return: Returns numpy vector pointing the polygon from the point.
    """
    v = map(Point, poly)
    poly = Polygon(*v)
    pnt = p

    rad = poly.distance(Point(pnt))
    circ = Ellipse(Point(pnt), rad, rad)
    cls_pnt = poly.intersection(circ)
    x_tang = cls_pnt[0][0] - pnt[0]
    y_tang = cls_pnt[0][1] - pnt[1]
    return math.atan2(y_tang, x_tang)


def poly_intersection(poly1, poly2):
    """
    Finds intersections b/w two pol
    :param poly1: Polygon represented by the list of tuples(x, y) of vertices.
    :param poly2: Polygon represented by the list of tuples(x, y) of vertices.
    :return: List of points of intersections b/w poly1 and poly2
    """
    v11, v12, v13, v14 = map(Point, poly1)
    v21, v22, v23, v24 = map(Point, poly2)

    poly1 = Polygon(v11, v12, v13, v14)
    poly2 = Polygon(v21, v22, v23, v24)

    ret = list(map(list, poly1.intersection(poly2)))
    return ret
