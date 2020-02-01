#include <iostream>
#include <string>
#include <sstream>
#include <ctime>
#include <cstdlib>
#include <new>

using namespace std;

const int SIZE = 3;

void displayBoard(string **b);
bool userFirst();
bool currentPlayerWon(string **b, string symbol);


int main(){
  string** board;
  int count;
  int SIZE = 3;
  board = new string*[SIZE];

  //create dynamic 2D array
  for (int i = 0; i < SIZE; i++){
    board[i] = new string[SIZE];
  }

  //populate dynamic 2D array
  for (int i = 0; i < SIZE; i++){
    for (int j = 0; j < SIZE; j++){
      board[i][j] = count;
      count ++;
    }
  }

  int position_id = 1;
  for (int i=0; i< SIZE; i++) {
    for (int j=0; j < SIZE; j++) {
        board[i][j] = to_string(position_id);
        position_id++;
    }
  }

  //Initial game output
  cout << "Welcome to Tic-Tac-Toe" << endl;

  bool userTurn = userFirst();
  if (userTurn == true) {
    cout << "Player goes first!" << endl;
  } else {
    cout << "Computer goes first!" << endl;
  }

  //Loop for turn taking in game
  int positionsRemaining = SIZE * SIZE;
  bool userWon = false;
  bool computerWon = false;

  //runs as long as there is positions left
  while ((positionsRemaining > 0)
        && (!userWon) && (!computerWon)) {
      displayBoard(board);

      //User's turn
      if (userTurn) {
        bool validMove = false;
        while (!validMove) {
          int position_id;
          cout << "Enter a position: ";
          cin >> position_id;
          if ((position_id <= (SIZE*SIZE))
              && (position_id > 0)) {
            int row = (position_id-1)/SIZE;
            int col = (position_id-1)%SIZE;
            //cout << "row = " << row << " col = " << col << endl;
            if ((board[row][col] != "X")
                && (board[row][col] != "O")) {
                  board[row][col] = "X";
                  validMove = true;
            } else {
              cout << "Position already used. Try again." << endl;
            }

          } else {
            cout << "Position invalid. Try again." << endl;
          }
        }
        positionsRemaining--;
        userWon = currentPlayerWon(board, "X");
        userTurn = false;
      }

      //Computer's turn
      else {
        bool validMove = false;
        while (!validMove) {
            int row = rand()%SIZE;
            int col = rand()%SIZE;
            if ((board[row][col] != "X")
                && (board[row][col] != "O")) {
                  board[row][col] = "O";
                  validMove = true;
            }
        }
        positionsRemaining--;
        computerWon = currentPlayerWon(board, "O");
        userTurn = true;
      }
  }

  //Display game result
  displayBoard(board);
  if (userWon) {
    cout << "Congratulations! You have won!" << endl;
  } else if (computerWon) {
    cout << "The computer has won. Try again." << endl;
  } else {
    cout << "Out of moves. Try again." << endl;
  }

  //delete each component of array
  for (int i = 0; i < SIZE; i++){
    delete [] board[i];
  }
  //delete entire array
  delete [] board;
}

//function prints original board
void displayBoard(string **b) {
  cout << "Tic-tac-toe board:" << endl << endl;
  for (int i=0; i< SIZE; i++) {
    for (int j=0; j < SIZE; j++) {
        cout << b[i][j] << "\t";
    }
    cout << endl;
  }
  cout << endl;
}

//checks to see who goes first
bool userFirst() {
  //set seed for random number generation
  srand(time(NULL));

  //generate a random number- 0 for computer, 1 for user
  int num = rand()%2;
  if (num == 0) {
    return false;
  }
  return true;
}

//Return true if player/computer with symbol (X or O) has won
bool currentPlayerWon(string **b, string symbol) {
  //Horizontal case
  //Loop through each row
  for (int i=0; i < SIZE; i++) {
    bool rowWinDetected = true;
    //Check all positions in row and see if they are the same symbol
    for (int j = 0; j < SIZE; j++) {
      if (b[i][j] != symbol) {
        rowWinDetected = false;
      }
    }
    if (rowWinDetected) {
      return true;
    }
  }

  //Vertical case
  //Loop through each column
  for (int i=0; i < SIZE; i++) {
    bool colWinDetected = true;
    //Check all positions in column and see if they are the same symbol
    for (int j = 0; j < SIZE; j++) {
      if (b[j][i] != symbol) {
        colWinDetected = false;
      }
    }
    if (colWinDetected) {
      return true;
    }
  }

  //Diagonal case #1
  bool diagonal1WinDetected = true;
  for (int i=0; i < SIZE; i++) {
    if (b[i][i] != symbol) {
      diagonal1WinDetected = false;
    }
  }
  if (diagonal1WinDetected) {
    return true;
  }

  //Diagonal case #2
  bool diagonal2WinDetected = true;
  for (int i=0; i < SIZE; i++) {
    if (b[(SIZE-1)-i][i] != symbol) {
      diagonal2WinDetected = false;
    }
  }
  if (diagonal2WinDetected) {
    return true;
  }

  //otherwise win not diagonal2WinDetected
  return false;

}
