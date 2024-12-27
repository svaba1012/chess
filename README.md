# Chess

Chess written in python using pygame. It can be played player vs player on local or player vs computer.
Old project refactored and improved.

### Install necessary python modules

```
pip install numpy
pip install pygame
```

### How to play

```
cd chess
python3 chess.py
```

### Places for improvements

- Optimize and improve score evaluation function
- Implement en passant and castling moves
- Implement draw (only kings left on the board and repeating moves)
- Currently board is implemented as matrix 8x8, better way to do it, is using bitboards
- After optimization set bigger depth for minimax
- Change minimax with alphabeta
