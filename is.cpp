#include <iostream>
#include <vector>
#include <cstdlib> // rand(), srand()
#include <ctime> // time()
#include <chrono> // for time measure

using namespace std;
using namespace std::chrono;

void insertion_sort(vector<int>& arr) {
    for(int i=1;i<arr.size();i++) {
        int key=arr[i];
        int j=i-1;
        while(j>=0 && arr[j] > key) {
            arr[j+1] = arr[j];
            j=j-1;
        }
        arr[j+1] = key;
    }
}

vector<int> generate_array(int n, int a, int b) {
    vector<int> arr(n);
    for(int i=0;i<n;i++) {
        arr[i] = a + rand() % (b - a + 1);
    }
    return arr;
}

int main() {
    srand(time(0));
    vector<int> sizes = {100,200,500,1000,2000,5000};
    for(int n : sizes) {
        vector<int> arr=generate_array(n, 0, 10000);
        auto start = high_resolution_clock::now();
        insertion_sort(arr);
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<milliseconds>(stop-start);
        cout<<"Array size: "<<n<<" -> Time: "<<duration.count()<<"ms"<<endl;
    }
    return 0;
}