#include <iostream>
#include <fstream>
#include <random>
#include <math.h>
#include <ctime>


using namespace std;

int main () {
	ranlux48_base gen;
	default_random_engine e1;

	ofstream myfile;
	myfile.open("random_data.txt");
	uniform_real_distribution<double> uni_dist(0,M_PI);

	for (int i = 0; i < 100000; ++i)
	{
		myfile << uni_dist(gen) << " ";
	}
  	
  	myfile.close();
  	cout << "asfas";
	double randomArray[1000000];
	double ranluxArray[1000000];

  clock_t begin = clock();


	for (int i = 0; i < 1000000; ++i)
	{
		randomArray[i] = uni_dist(gen);
		// randomArray[i] = uni_dist(e1);
	}
	clock_t end = clock();
	double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
	cout << "default random: " <<  elapsed_secs << endl;

	// 5. Measure time for random() generation and ranlux generation of 1.000.000 samples

	return 0;
}