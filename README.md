# TextTetris

**Classic Tetris experience in your terminal — play, score, and challenge yourself!**

---

## What is Console Tetris Game?

This is a **Python-based console Tetris game** where blocks fall, and the player can **move, rotate, and place pieces** to clear rows and earn points. The game includes **next piece preview, scoring, high score tracking, and a game over screen**, all within a stable console UI.

No installation beyond Python is needed — just run the game in your terminal!

---

## Key Features

* **Classic Tetris Gameplay:** Move, rotate, and drop pieces to clear rows.
* **Next Piece Preview:** Always shows the upcoming piece at the top for a consistent layout.
* **Scoring & High Score:** Earn points for placing pieces and clearing rows; track your highest score during the session.
* **Game Over Screen:** Displays current and high scores, and lets you restart immediately.
* **Stable Console UI:** The board size remains fixed, preventing layout shifts as pieces fall.

---

## How to Play

### Controls

| Key   | Action       |
| ----- | ------------ |
| w     | Rotate piece |
| a     | Move left    |
| s     | Fast drop    |
| d     | Move right   |
| Space | Pause game   |

### Gameplay Mechanics

* Pieces appear randomly from a set of predefined shapes.
* The next piece is displayed at the top while the current piece falls.
* Complete a row to clear it, and all blocks above fall down.
* The game ends when a new piece cannot spawn at the top row.
* On game over, your final score and high score are displayed. Press any key to restart.

---

## Requirements

* Python 3.x
* Windows (uses `msvcrt` for key input)
* Terminal or command prompt capable of clearing the screen (`cls` command)

---

## How to Run

1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Run the game:

```bash
python main.py
```

4. Play the game using the controls above.

---

## Optional Enhancements

* Add colors for different pieces.
* Implement levels with increasing speed.
* Add a “hold piece” feature.
* Save high score to a file.
* Add sound effects for row completion and game over.

---

## Screenshot Example

```
Score: 15

Next:
[ ][ ][ ]
[ ][ ][ ]
[ ][ ][ ]

+-------------------------------+
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|                               |
|          [ ][ ][ ]            |
|          [ ]            [ ]   |
|                         [ ]   |
| [ ][ ][ ]   [ ]   [ ][ ][ ][ ]|
+------------------------- -----+
```

---

## Contact

**Kushal Gupta**

* Email: [guptakushal2003@gmail.com](mailto:guptakushal2003@gmail.com)
* Portfolio: [guptakushal03.github.io/TechFolio](https://guptakushal03.github.io/TechFolio)
