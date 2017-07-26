#include <iostream> 
#include <vector>
#include <math.h> 

using namespace std;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int table_size;

	while(cin >> table_size && table_size){
		cout << table_size*(table_size+1)*(2*table_size+1)/6 << endl;
	}

	return 0;
}