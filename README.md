# Snake Water Gun Game 🐍💧🔫

This is a simple command-line Python game inspired by the classic **Rock-Paper-Scissors**, but with a twist:

- 🐍 Snake drinks water
- 💧 Water damages gun
- 🔫 Gun kills snake

You play against the computer, and the outcome is decided by the rules below.

---

## 🕹️ Game Rules

| Your Choice | Computer Choice | Result     |
|-------------|------------------|------------|
| Snake       | Water            | You win 🏆 |
| Snake       | Gun              | You lose ❌|
| Water       | Gun              | You win 🏆 |
| Water       | Snake            | You lose ❌|
| Gun         | Snake            | You win 🏆 |
| Gun         | Water            | You lose ❌|
| Same        | Same             | It's a draw 🤝|

---

## 📦 How to Run

1. Make sure you have **Python installed** (any version >= 3.6).
2. Save the following code in a file called `game.py`.
3. Run the game using the command:

```bash
python game.py
