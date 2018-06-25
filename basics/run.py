# python 3 script for 1. laboratory classes from Monte Carlo Methods course
#

import utility as ut

def task1(nmax, random_numbers, steps_count = 20):
	results = []

	# steps_count = 20
	step = nmax / steps_count
	val_list = range(1, nmax, int(step))

	for k in val_list:
		tmp = ut.mc_sine(k, random_numbers)
		results.append(tmp)
	prec_result = [ut.multi_dim_analytical(1)] * len(results)
	# ut.plot_results(val_list, results, "Simulation", "log", "Number of samples", "Integral value", \
	#                 val_list,prec_result, "Analytical")
	print(results[:-1])

def task2(nmax, random_numbers, steps_count = 20):
	results = []

	# steps_count = 20
	step = nmax / steps_count
	val_list = range(2, nmax, int(step))

	for k in val_list:
		tmp = ut.std_dev(k, random_numbers)
		results.append(tmp)
	# prec_result = [ut.multi_dim_analytical(1)] * len(results)
	ut.plot_results(val_list, results, "std_dev Simulation", "log", "Number of samples", "Integral value")

def task3(nmax, random_numbers, dim):
	results = []

	# steps_count = 20
	val_list = range(1, dim)
	prec_results = []

	for k in val_list:
		print("simul:" + str(ut.multi_dim_approach(nmax, random_numbers, k)))
		print("precise:" + str(ut.multi_dim_analytical(k)))

		tmp = ut.multi_dim_approach(nmax, random_numbers, k)
		results.append(tmp)
		prec_results.append(ut.multi_dim_analytical(k))

	results = ut.np.asarray(results)
	prec_results = ut.np.asarray(prec_results)
	diff = results - prec_results
	ut.plot_results(val_list, diff, "multidim Simulation", "linear", "Dimensions", "Difference value")

def task4(nmax, random_numbers, dim, steps_count=20):
	print("--task1")
	task1(nmax,random_numbers)

	print("--task2")
	task2(nmax, random_numbers)

	print("--task3")
	task3(nmax, random_numbers,dim)

if __name__ == "__main__":

	Nmax = 100000
	randomNumbers = ut.get_random(Nmax)
	task1(Nmax, randomNumbers)
	# task2(Nmax, randomNumbers)
	# task3(Nmax, randomNumbers, dim=10)
	# result = ut.multi_dim_approach(50000, randomNumbers, 5)
	# ut.calculus_multi_prec(5)
	ranlux48 = ut.np.loadtxt("random_data.txt")
	# task4(Nmax, ranlux48, dim=10)
	# print(len(ranlux48))

