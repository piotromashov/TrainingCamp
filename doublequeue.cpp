#include <algorithm>
#include <iostream>
#include <iterator>
#include <avl/set.h>

using namespace std;
const int inf = 1 << 30;


int main(){
	// ios::sync_with_stdio(false);
	// cin.tie(NULL);




	avl::set<int> my_set;

	
	

    my_set.insert(5);

    avl::multiset<int> my_mset;
    
    my_mset.insert(2);
    my_mset.insert(3);
    my_mset.insert(2);

    /* Now it should print:
            2
            2
            3
    */
    std::copy(my_mset.begin(), my_mset.end(), std::ostream_iterator<int>(std::cout, "\n"));
}