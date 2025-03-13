import random
import math


# Визначення функції Сфери
def sphere_function(x):
    return sum(xi**2 for xi in x)


# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    # Кількість параметрів
    n = len(bounds)

    # Випадкова початкова точка у межах bounds
    current_point = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(n)]
    current_value = func(current_point)

    step_size = 0.1

    for _ in range(iterations):
        # Генеруємо сусідів для кожної ітерації
        neighbors = []
        for i in range(n):
            for delta in [-step_size, step_size]:
                neighbor = current_point[:]
                neighbor[i] += delta

                # Перевіряємо, чи сусід в межах допустимих значень
                if bounds[i][0] <= neighbor[i] <= bounds[i][1]:
                    neighbors.append(neighbor)

        # Шукаємо найкращого сусіда
        next_point = current_point
        next_value = current_value
        for neighbor in neighbors:
            value = func(neighbor)
            if value < next_value:
                next_point = neighbor
                next_value = value

        # Перевіряємо зупинку за умовою точності
        if abs(current_value - next_value) < epsilon:
            break

        # Переходимо до кращого сусіда
        current_point, current_value = next_point, next_value

    return current_point, current_value


# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    # Кількість параметрів
    n = len(bounds)

    # Випадкова початкова точка у межах bounds
    current_point = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(n)]
    current_value = func(current_point)

    for _ in range(iterations):
        # Генеруємо випадкового сусіда в межах області
        neighbor = [current_point[i] + random.uniform(-0.1, 0.1) for i in range(n)]
        for i in range(n):
            neighbor[i] = min(max(neighbor[i], bounds[i][0]), bounds[i][1])
        
        value = func(neighbor)

        # Якщо є покращення — переходимо до нового сусіда
        if value < current_value:
            current_point, current_value = neighbor, value

        # Перевіряємо зупинку за умовою точності
        if abs(current_value - value) < epsilon:
            break

    return current_point, current_value



# Simulated Annealing
def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    pass


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
