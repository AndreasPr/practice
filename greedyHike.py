def calculate_elevation_change(current_elevation, next_elevation):
    return abs(current_elevation - next_elevation)

def find_best_next_position(current_x, current_y, elevations, X, Y):
    best_x = current_x
    best_elevation_change = calculate_elevation_change(elevations[current_x][current_y], elevations[current_x][current_y+1])

    for dx in [-1, 0, 1]:
        new_x = current_x + dx

        if 0 <= new_x < X:
            elevation_change = calculate_elevation_change(elevations[current_x][current_y], elevations[new_x][current_y+1])

            if elevation_change < best_elevation_change or (elevation_change == best_elevation_change and dx == 0):
                best_x = new_x
                best_elevation_change = elevation_change

    return best_x, best_elevation_change

X, Y = map(int, input().split())
xs, ys = map(int, input().split())

elevations = []
for _ in range(X):
    elevations.append(list(map(int, input().split())))


current_x = xs
total_elevation_change = 0

for current_y in range(ys, Y - 1):
    next_x, elevation_change = find_best_next_position(current_x, current_y, elevations, X, Y)
    current_x = next_x
    total_elevation_change += elevation_change

print(current_x, Y - 1, total_elevation_change)
