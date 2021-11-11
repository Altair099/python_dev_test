print("Please enter vertex A's X coordinate")
a_vertex_x = int(input())
print("Please enter vertex A's Y coordinate")
a_vertex_y = int(input())
print("Please enter vertex B's X coordinate")
b_vertex_x = int(input())
print("Please enter vertex B's Y coordinate")
b_vertex_y = int(input())
print("Please enter vertex C's X coordinate")
c_vertex_x = int(input())
print("Please enter vertex C's Y coordinate")
c_vertex_y = int(input())


AB = (a_vertex_x - b_vertex_x, a_vertex_y - b_vertex_y)
AC = (a_vertex_x - c_vertex_x, a_vertex_y - c_vertex_y)
BC = (b_vertex_x - c_vertex_x, b_vertex_y - c_vertex_y)

if AB[0] * AC[0] + AB[1] * AC[1] == 0 or AB[0] * BC[0] + AB[1] * BC[1] == 0 or AC[0] * BC[0] + AC[1] * BC[1] == 0:
    print("yes")
else:
    print("no")
