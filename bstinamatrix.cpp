#include <iostream> 
#include <vector>
#include <math.h> 

using namespace std;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int table_size, discard;
	cin >> table_size;

	int matrix[table_size-1][table_size-1];

	for (int i = 0; i < table_size-1; ++i)
	{
		cin >> discard;
		for (int j = 0; j < table_size-1; ++j)
		{
			cin >> matrix[i][j];
			cout << matrix[i][j] << " ";
		}

		cout << "\n";
	}

	
	

	return 0;
}