from Q1 import gen_line, poly_intersection, calc_dist, calc_poly_dist, calc_poly_tang

p1 = (2, 2)
p2 = (2, 3)

print(gen_line(p1, p2))
print(calc_dist(p1, p2))
print(calc_poly_dist([(3, 4), (3, 1), (7, 1), (7, 4)], p1))
print(calc_poly_tang([(3, 4)], p1))
print(poly_intersection([(3, 4), (3, 1), (7, 1), (7, 4)], [(1, 4), (3, 5), (2, 1), (7, 3)]))
print(poly_intersection([(3, 4), (3, 1), (7, 1), (7, 4)], [(1, 4), (3, 5), (2, 1), (7, 3)])[0][1])
