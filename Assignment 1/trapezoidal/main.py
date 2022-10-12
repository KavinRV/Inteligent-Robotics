import math
from sympy import Polygon, Point, Segment
import numpy as np
from tkinter import *


def find_insect(s1, s2):
    sec1 = map(Point, s1)
    sec2 = map(Point, s2)

    sec1 = Segment(*sec1)
    sec2 = Segment(*sec2)

    return sec1.intersection(sec2)


vertices = [(-3, -3), (3, -3), (3, 3), (-3, 3), (-2, 1.1), (-2, 0.9), (2, 0.9), (2, 1.1), (-2, -2.5), (-2, -0.9), (0, -0.9), (0, -1.1), (-1.8, -1.1), (-1.8, -2.5)]

edges = {"e1": [(3, 3), (-3, 3)], "e2": [(-3, 3), (-3, -3)], "e3": [(-3, -3), (3, -3)], "e4": [(3, -3), (3, 3)],
         "e5": [(2, 1.1), (-2, 1.1)], "e6": [(-2, 1.1), (-2, 0.9)], "e7": [(-2, 0.9), (2, 0.9)], "e8": [(2, 0.9), (2, 1.1)],
         "e9": [(-2, -0.9), (0, -0.9)], "e10": [(-2, -2.5), (-2, -0.9)], "e11": [(-2, -2.5), (-1.8, -2.5)], "e12": [(-1.8, -1.1), (-1.8, -2.5)], "e13": [(0, -1.1), (-1.8, -1.1)], "e14": [(0, -0.9), (0, -1.1)]}

pgons = [Polygon((-2, 1.1), (-2, 0.9), (2, 0.9), (2, 1.1)), Polygon((-2, -2.5), (-2, -0.9), (0, -0.9), (0, -1.1), (-1.8, -1.1), (-1.8, -2.5))]

win = Tk()

win.geometry("800x800")

canvas = Canvas(win, width=800, height=800)
canvas.pack()

v_lst = []
e_dict = {}
v_dict = {}

for e in edges:
    x1 = edges[e][0][0] * 100 + 400
    x2 = edges[e][1][0] * 100 + 400
    y1 = abs(edges[e][0][1] - 4) * 100
    y2 = abs(edges[e][1][1] - 4) * 100
    canvas.create_line(x1, y1, x2, y2, fill="green", width=2)

    e_dict[e] = [(x1, y1), (x2, y2)]
    v_lst.append((x1, y1))
    v_lst.append((x2, y2))
    v_dict[(x1, y1)] = (edges[e][0][0], edges[e][0][1])
    v_dict[(x2, y2)] = (edges[e][1][0], edges[e][1][1])

v_lst = list(set(v_lst))
v_lst.sort()

for v in v_lst:
    y = v[1]
    x = v[0]
    y1 = 100
    y2 = 700
    x1 = 100
    x2 = 700
    canvas.create_line(x, y1, x, y2, fill="blue", width=1)
    # print(v)
    # lne = Segment(*map(Point, [((x1-400)/100, v_dict[v][1]), ((x2-400)/100, v_dict[v][1])]))
    gk = pgons[1].intersection(Segment(*map(Point, [(v_dict[v][0], -3), (v_dict[v][0], 3)])))
    # if len(gk) > 0:
    #     print(lne - gk[0])


tk = pgons[0].contains(Segment(*map(Point, [(-1, 0.95), (-1, 1.05)])))
print(tk)

win.mainloop()


