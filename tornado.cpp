#include <iostream> 
#include <vector>
#include <math.h> 

using namespace std;

int posts_status[10000];


int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int concrete_posts;

	cin >> concrete_posts;

	do{
	
		bool isEmpty = false;
		int startPoint = -1;
		for (int i = 0; i < concrete_posts; ++i)
		{
			cin >> posts_status[i];
			if(posts_status[i] && startPoint < 0){
				startPoint = i;
			}
		}

		if(startPoint < 0)
			printf("%d", (int)ceil(concrete_posts/2));

		int needed_to_restore = 0;
		int count_empty = 0;
		int index = startPoint;
		bool hasCicled = false;
		while(index != startPoint && !hasCicled){
			if(!posts_status[index]){
				count_empty++;
			} else{
				needed_to_restore += count_empty/2;
				count_empty = 0;
			}
				
			if(index == concrete_posts-1){
				index = -1;
				hasCicled = true;
			}

			index++;
		}

		needed_to_restore += count_empty/2;

		cout << "needed to restore: "<< needed_to_restore << endl;
		cin >> concrete_posts;
	} while(concrete_posts);
	

	return 0;
}