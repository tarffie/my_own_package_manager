#include <iostream>
#include <fstream>

using namespace std;

int main() {
  ifstream file_path("README.mirrors.txt");

  if(file_path.is_open()) {
    string line;
    while (getline(file_path, line)) {
      cout << line << endl;
      
    }

    file_path.close();

  } else {
    cout << "Failed to open the file." << endl;
  }
  
  
  return 0;
}
