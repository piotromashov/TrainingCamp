#include <iostream> 
#include <vector>

using namespace std;

int list[200000];

int binaryUpperSearch(int query, int size) {
	int first = 0;
	int last = size - 1;
	while (first <= last) {
		int midpoint = (first+last)/2;
		if (list[midpoint] >= query && (midpoint == 0 || list[midpoint-1] < query)) {
			return midpoint;
		} else {
			if (query < list[midpoint]) {
				last = midpoint - 1;
			} else {
				first = midpoint + 1;
			}
		}
	}
	return -1;
}

int main(){
	ios::sync_with_stdio(false);

	int total_doners, total_queries, doner, query;
	
	cin >> total_doners;
	// int doners[total_doners];
	int donersAccumulated = 0;
	for (int i = 0; i < total_doners; ++i) {
		cin >> doner;
		donersAccumulated += doner;
		list[i] = donersAccumulated;
	}

	cin >> total_queries;
	for (int i = 0; i < total_queries; ++i) {
		cin >> query;
		int found = binaryUpperSearch(query, total_doners);
		if (found >= 0) {
			cout << found+1 << "\n";
		} else {
			cout << "none" << "\n";
		}

	}
	return 0;
}