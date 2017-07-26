#include <iostream> 
#include <vector>
#include <math.h> 

using namespace std;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	long tray_radius, coin_radius;
	double angle, hipotenuse, opposite, coins_fit;

	while(cin >> tray_radius){
		cin >> coin_radius;

		hipotenuse = tray_radius - coin_radius;
		opposite = coin_radius;

		if(tray_radius < coin_radius || tray_radius < 0 || coin_radius < 0){
			printf("Coin cannot fit in the tray.\n");
			return 0;
		}

		if(opposite/hipotenuse <= 1 && opposite/hipotenuse >= -1){
			angle = 2*asin(opposite/hipotenuse);
			coins_fit = floor(2*M_PI/angle);
			printf("%.0f coins of size %lu will fit the inner rim of a tray of size %lu.\n", coins_fit, coin_radius, tray_radius);
		} else {
			printf("1 coin of size %lu will fit the inner rim of a tray of size %lu.\n", coin_radius, tray_radius);
		}

	}
	
	return 0;
}