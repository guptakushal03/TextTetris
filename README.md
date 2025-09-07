# Console Tetris Game

A Python console-based Tetris clone where blocks fall, and the player can rotate, move, and place pieces to clear rows and score points. The game features a **next piece preview**, **scoring**, **high score tracking**, and a **game over screen**.

---

## Features

* **Classic Tetris gameplay** in the console.
* **Piece Movement**:

  * Move left: `a`
  * Move right: `d`
  * Rotate: `w`
  * Fast drop: `s`
  * Pause: `Spacebar`
* **Next Piece Preview**: Always shows the next piece at the top, taking up 3 rows for consistent layout.
* **Scoring**:

  * +1 point for successfully placing a piece
  * +10 points for completing a row
* **High Score Tracking**: Tracks the highest score achieved during the session.
* **Game Over Screen**: Shows current and high scores and allows restarting by pressing any key.
* **Stable UI**: Board size remains fixed, preventing layout shifts as pieces fall.

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

4. Play the game using the controls listed above.

---

## Controls

| Key     | Action           |
| ------- | ---------------- |
| `w`     | Rotate piece     |
| `a`     | Move piece left  |
| `s`     | Fast drop        |
| `d`     | Move piece right |
| `Space` | Pause game       |

---

## Gameplay Mechanics

* Pieces appear randomly from a predefined set of shapes.
* The **next piece** is displayed at the top while the current piece is falling.
* When a row is completely filled, it is cleared, and all blocks above fall down.
* The game continues until a new piece cannot spawn at the top row.
* Upon game over, the **final score** and **high score** are displayed, and the player can restart the game.

---

## Extending the Game

Possible enhancements:

* Add **colors** for different Tetris pieces.
* Implement **levels** with increasing falling speed.
* Add a **hold piece feature** to store a piece for later.
* Save **high score to a file** to persist between sessions.
* Add **sound effects** for row completion and game over.

---

## Screenshot

```
Score: 15

Next:
[ ][ ][ ]
[ ][ ][ ]
[ ][ ][ ]


+------------------------------+
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                        [ ]   |
|                        [ ]   |
|                        [ ]   |
+------------------------------+
```

---

## Author

Kushal Gupta

---
