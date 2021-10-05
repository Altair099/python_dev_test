population_density = sorted([8.56, 3.5, 139, 32, 23.6, 2.8, 375])

print("Average density: ", sum(population_density) / len(population_density))
print("Minimum density: ", population_density[0])
print("Maximum density: ", population_density[len(population_density) - 1])
print("Three countries with maximum density: ", population_density[len(population_density) - 3:])
