#include <vector>
#include <iostream> 
#include <math.h> 

using namespace std;
const int inf = 1 << 30;
 
// given adjacency matrix adj, finds shortest path from A to B
vector<int> dijk(int A, int B, vector< vector<int> > adj) {
  int n = adj.size();
  vector<int> dist(n);
  vector<bool> vis(n);
  vector<int> predecesors(n, -1);
 
  for(int i = 0; i < n; ++i) {
	dist[i] = inf;
  }
  dist[A] = 0;
 
  for(int i = 0; i < n; ++i) {
	int cur = -1;
	for(int j = 0; j < n; ++j) {
	  if (vis[j]) continue;
	  if (cur == -1 || dist[j] < dist[cur]) {
		cur = j;
	  }
	}
 
	vis[cur] = true;
	for(int j = 0; j < n; ++j) {
	  int path = dist[cur] + adj[cur][j];
	  if (path < dist[j]) {
		dist[j] = path;
		predecesors[j] = cur;
	  }
	}
  }
 
  // return dist[B];
  return predecesors;
}


int main(){
	ios::sync_with_stdio(false);
	// cin.tie(NULL);
	int points, routes, start, destination, x, y, weight;

	cin >> points >> routes;
	cin >> start >> destination;

	vector< vector<int> > adj(points, vector<int>(points, 0));

	for (int i = 0; i < routes; ++i){
	  	cin >> x >> y;
	  	cin >> weight;
	  	adj[x][y] = weight;
  	}

  	vector<int> predecesors = dijk(start, destination, adj);

  	if(predecesors[destination] == -1){
  		cout << -1 << endl;
  		return 0;
  	}

  	//delete nodes of actual path
  	for (int i = 0; i < predecesors.size(); ++i)
	{
		if(predecesors[i] != -1)
			adj[predecesors[i]][i] = inf;
	}

  	predecesors = dijk(start, destination, adj);

  	if(predecesors[destination] == -1){
  		cout << -1 << endl;
  		return 0;
  	}


  	for (int i = 0; i < predecesors.size(); ++i)
  	{
  		cout << predecesors[i] << " " << endl;
  	}

  	int cost = 0;
  	int dest = destination;
  	while(dest != -1){
  		int pred = predecesors[dest];
  		printf("pred: %d, dest: %d, cost: %d\n", pred, dest, cost);
  		cout.flush();
  		cost += adj[pred][dest];
  		dest = pred;
  	}

  	cout << cost << endl;

  	return 0;


}