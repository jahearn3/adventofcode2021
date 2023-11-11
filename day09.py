# Day 9: Smoke Basin

import load_data as ld

def sum_risk_levels_of_local_minima(data):
    low_points = []
    for i, row in enumerate(data):
        for j, point in enumerate(row):
            if((0 < i < len(data) - 1) and (0 < j < len(row) - 1)): # Check all adjacent points
                if((int(point) < int(row[j-1])) and (int(point) < int(row[j+1])) and ((int(point)) < int(data[i-1][j])) and ((int(point)) < int(data[i+1][j]))):
                    low_points.append(int(point))
            else: # Boundary conditions
                # Treat corners
                if((i == 0) and (j == 0)): # No need to check above or left
                    if((int(point) < int(row[j+1])) and ((int(point)) < int(data[i+1][j]))):
                        low_points.append(int(point))
                elif((i == 0) and (j == len(row) - 1)): # No need to check above or right
                    if((int(point) < int(row[j-1])) and ((int(point)) < int(data[i+1][j]))):
                        low_points.append(int(point))
                elif((i == len(data) - 1) and (j == 0)): # No need to check below or left
                    if((int(point) < int(row[j+1])) and ((int(point)) < int(data[i-1][j]))):
                        low_points.append(int(point))
                elif((i == len(data) - 1) and (j == len(row) - 1)): # No need to check below or right
                    if((int(point) < int(row[j-1])) and ((int(point)) < int(data[i-1][j]))):
                        low_points.append(int(point))
                else: # Treat edges
                    if(i == 0): # No need to check above
                        if((int(point) < int(row[j-1])) and (int(point) < int(row[j+1])) and ((int(point)) < int(data[i+1][j]))):
                            low_points.append(int(point))
                    if(j == 0): # No need to check left
                        if((int(point) < int(row[j+1])) and ((int(point)) < int(data[i-1][j])) and ((int(point)) < int(data[i+1][j]))):
                            low_points.append(int(point))
                    if(i == len(data) - 1): # No need to check below
                        if((int(point) < int(row[j-1])) and (int(point) < int(row[j+1])) and ((int(point)) < int(data[i-1][j]))):
                            low_points.append(int(point))
                    if(j == len(row) - 1): # No need to check right
                        if((int(point) < int(row[j-1])) and ((int(point)) < int(data[i-1][j])) and ((int(point)) < int(data[i+1][j]))):
                            low_points.append(int(point))

    return sum(low_points) + len(low_points)

data = ld.load_data('example09.txt')
data = ld.load_data('input09.txt') 
print(f'{sum_risk_levels_of_local_minima(data)}') # 530