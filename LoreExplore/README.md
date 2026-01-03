# Lore Explorer

Lore Explorer is a Python-based command-line application that allows users to search and explore characters, regions, and vanguards from custom lore data. The goal was to demonstrate Python proficiency, file handling, and modular program design.


## Features
- Search characters, regions, and vanguards by name
- Handling of missing or invalid JSON data
- Continuous search loop with user-controlled exit (quit or exit)
-	Cleanly formatted output for better readability
-	Modular and maintainable code structure


## Technologies Used
- Python 3
- JSON
- File I/O
- Error handling (try/except)
- Modular functions
## How to Run

1. Clone the repository:

```bash
git clone https://github.com/DerrellT/LoreExplore.git
cd LoreExplore
python3 --version
python3 src/lore_explore.py
```

## Example Output: 
```text
------Characters------
Jicho
------Regions------
Rema
------Vanguards------
Elder Eye

Enter a Character, Region or Vanguard from the list above: jicho
Name: Jicho
Traits:
- Timid
- Observant
