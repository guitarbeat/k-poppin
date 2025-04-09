# K-Pop Girl Group Heardle Song Shuffler

This script shuffles the songs in the `songs.js` file for the K-Pop Girl Group Heardle game. It preserves the format of the file while randomizing the order of the songs.

## Features

- Extracts all songs from the songs.js file
- Shuffles them randomly
- Writes them back to the file in the same format
- Option to create a backup of the original file
- Option to set a random seed for reproducibility
- Option to fix malformed songs.js files

## Requirements

- Python 3.6 or higher

## Usage

```bash
python shuffle_songs.py [options]
```

### Options

- `--file FILE`: Path to the songs.js file (default: songs.js)
- `--seed SEED`: Random seed for reproducibility
- `--backup`: Create a backup of the original file
- `--fix`: Attempt to fix malformed songs.js files

### Examples

Shuffle songs in the default songs.js file:
```bash
python shuffle_songs.py
```

Shuffle songs in a specific file:
```bash
python shuffle_songs.py --file path/to/songs.js
```

Shuffle songs with a specific random seed:
```bash
python shuffle_songs.py --seed 42
```

Create a backup of the original file before shuffling:
```bash
python shuffle_songs.py --backup
```

Fix a malformed songs.js file:
```bash
python shuffle_songs.py --fix
```

## How It Works

1. The script reads the songs.js file and extracts all song entries
2. It shuffles the list of songs using Python's random.shuffle function
3. It writes the shuffled songs back to the file, preserving the original format

## Notes

- The script preserves the format of the songs.js file, including comments and whitespace
- If you want to ensure the same shuffle order every time, use the `--seed` option
- It's recommended to use the `--backup` option to create a backup of the original file before shuffling
- If the script fails to extract songs, try using the `--fix` option to attempt to fix the file format

## Troubleshooting

If you encounter any issues:

1. Make sure the songs.js file is in the correct format
2. Check that you have the required permissions to read and write the file
3. Try running the script with the `--backup` option to create a backup before shuffling
4. If the script fails to extract songs, try using the `--fix` option to attempt to fix the file format
5. If the file is severely malformed, you may need to manually fix it before running the script 