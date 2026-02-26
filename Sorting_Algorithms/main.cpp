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

void print_auto_duration(high_resolution_clock::duration d) {
    auto ns = duration_cast<nanoseconds>(d).count();
    if(ns < 1000) {
        cout <<ns <<" ns"<<endl;
    } else if(ns < 1'000'000) {
        cout << ns / 1000.0 << " μs"<<endl; // microseconds
    } else if(ns < 1'000'000'000) {
        cout << ns / 1'000'000.0 << " ms"<<endl;
    } else {
        cout << ns / 1'000'000'000.0 << " s"<<endl;
    }
}

void timing(vector<int>& sizes) {
    srand(time(0));
    for(int n : sizes) {
        vector<int> arr = generate_array(n, 0, 10000);
        auto start = high_resolution_clock::now();
        insertion_sort(arr);
        auto stop = high_resolution_clock::now();
        auto duration = stop - start;
        cout<<"Array size: "<<n<<" -> Time: "<<fixed<< setprecision(2);
        print_auto_duration(duration);
    }
}

int main() {
    vector<int> sizes = {100,200,500,1000,2000,5000,10000,20000,50000,100000,200000,500000};
    timing(sizes);
    return 0;
}