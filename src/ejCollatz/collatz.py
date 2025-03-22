import matplotlib.pyplot as plt

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

collatz_data = {n: collatz_steps(n) for n in range(1, 10001)}

plt.figure(figsize=(10, 6))
plt.scatter(collatz_data.values(), collatz_data.keys(), s=1, color='blue')
plt.xlabel("Iteraciones hasta converger")
plt.ylabel("Número inicial")
plt.title("Número de iteraciones para converger en la conjetura de Collatz")
plt.grid(True, linestyle='--', linewidth=0.5)
plt.show()
