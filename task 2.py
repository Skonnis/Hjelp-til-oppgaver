
class QuizGift:
    def compute_result(capacity, weight, values, n):
        grid = [[0 for x in range(capacity + 1)]
            for x in range(n + 1)]
    
        for item in range(n + 1):
            for cap in range(capacity + 1):
                if item == 0 or cap == 0:
                    grid[item][cap] = 0
                elif weight[item - 1] <= cap:
                    grid[item][cap] = max(values[item - 1] +
                                        grid[item - 1][cap - weight[item - 1]],
                                        grid[item - 1][cap])
                else:
                    grid[item][cap] = grid[item - 1][cap]
        return grid[n][capacity]

    def print_result(points):
        if points >= 200 and points <= 250:
            print("You get a watch!")
        elif points >= 250 and points < 750:
            print("You get a smarthphone!")
        elif points >= 750:
            print("You get a laptop!")
        else:
            print("You didnt get any points!")
            
    


points = [120, 200, 150, 350, 100, 90]
minutes = [15 ,20, 40, 50, 20, 10]
total_minutes = 100
n_points = len(points)

compute = QuizGift.compute_result(total_minutes, minutes, points, n_points)
print = QuizGift.print_result(compute)