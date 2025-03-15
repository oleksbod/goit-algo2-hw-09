import random
import math

# Визначення функції Сфери
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Генерація випадкової точки в межах bounds
def random_point(bounds):
    return [random.uniform(bound[0], bound[1]) for bound in bounds]

# Генерація сусідньої точки з малим зсувом (локальний крок)
def neighbor_point(point, bounds, step_size=0.1):
    neighbor = []
    for i in range(len(point)):
        delta = random.uniform(-step_size, step_size)
        new_value = point[i] + delta        
        new_value = max(bounds[i][0], min(bounds[i][1], new_value))
        neighbor.append(new_value)
    return neighbor

# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current_point = random_point(bounds)
    current_value = func(current_point)

    for it in range(iterations):
        next_point = neighbor_point(current_point, bounds)
        next_value = func(next_point)
        
        if next_value < current_value:
            if abs(current_value - next_value) < epsilon:
                print(f"Hill Climbing завершено на ітерації {it}")
                break
            current_point, current_value = next_point, next_value

    return current_point, current_value

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    current_point = random_point(bounds)
    current_value = func(current_point)

    for it in range(iterations):
        next_point = random_point(bounds)
        next_value = func(next_point)

        if next_value < current_value:
            if abs(current_value - next_value) < epsilon:
                print(f"Random Local Search завершено на ітерації {it}")
                break
            current_point, current_value = next_point, next_value

    return current_point, current_value

# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current_point = random_point(bounds)
    current_value = func(current_point)
    best_point = list(current_point)
    best_value = current_value
    current_temp = temp

    for it in range(iterations):
        next_point = neighbor_point(current_point, bounds)
        next_value = func(next_point)
       
        delta = next_value - current_value

        if delta < 0 or random.random() < math.exp(-delta / current_temp):
            current_point, current_value = next_point, next_value

            if current_value < best_value:
                best_point, best_value = current_point, current_value

        current_temp *= cooling_rate

        if current_temp < epsilon:            
            break

        if abs(delta) < epsilon:            
            break

    return best_point, best_value

if __name__ == "__main__":
    # Межі для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритмів
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
