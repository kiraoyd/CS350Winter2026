#include <iostream>
#include <vector>

int main() {
    //change these values to change the size of the matrix:
    int rows = 3;
    int cols = 4;

    int arr[rows][cols];

    //initialize matrix
    for (int i=0; i<rows; ++i) {
        for (int j=0; j<cols; ++j) {
            arr[i][j] = i * cols + j + 1; //Assign values
        }
    }

    //print matrix
    for (int i=0; i<rows; ++i){
        for(int j=0; j<cols; ++j){
            std::cout << arr[i][j] << " ";
        }
        std::cout << arr[i][j] << " ";
    }

    //using a vector of vectors
    std::vector<std::vector<int>> matrix(rows, std::vector<int>(cols));

    //Initialize the matrix
    for (int i=0; i< rows; ++i) {
        for (int j = 0; j<cols; ++j) {
            matrix[i][j] = i * cols + j + 1; //assign values
        }
    }

    //print the matrix
    for (int i=0; i<rows; ++i) {
        for(int j=0; j<cols; ++j){
            std::cout << matrix[i][j] << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}