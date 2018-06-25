import math
import random
import numpy as np
from matplotlib import pyplot as plt


# """ Class with methods for excercises"""


def mc_sine(N, rand_numbers):
	sum = 0
	for k in range(1, N):
		sum += math.sin(rand_numbers[k])
	return (1.0 / float(N)) * sum


def std_dev(N,rand_numbers):
	sum = 0.0
	for k in range(1, N):
		sum += math.sin(rand_numbers[k])
	result = (1.0 / float(N)) * sum

	scale = 1.0 / (float(N) * float(N - 1))
	tmp = 0
	for k in range(1, N):
		tmp += (math.sin(rand_numbers[k]) - result) ** 2
	return math.sqrt(scale * tmp)


def multi_dim_analytical(dim):
	return (2.0 / math.pi) ** dim


def sin_mult(x):
	result = 1
	for a in x:
		# print("SIN " + str(a) + "  " + str(x))
		result *= math.sin(float(a))
	# print("FUNCTION sin_mult  " + str(result))
	return result


def multi_dim_approach(N, random_numbers, dimensions):
	sum = 0
	for k in range(1, N):
		# print(randomNumbers[k : k + dim])
		sum += sin_mult(random_numbers[k: k + dimensions])
	return sum / float(N)


def plot_results(x, y, title, scale, xlabel, ylabel, *args, **kwargs):
	plt.plot(x, y, label=title)
	plt.yscale(scale) #linear or log
	# print(count())
	if not args:
		pass
	else:
		plt.plot(args[0], args[1], label=args[2])

	plt.legend()
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.show()

# @staticmethod
def get_random(N_max):
	return np.random.rand(N_max) * math.pi
