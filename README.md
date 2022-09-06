# listinator

Create a word list from a given text file.
Will strip all punctuation out of words and remove duplicates.
Can optionally set min or max word length with --min/-m and --max/-M respectively.
Values are inclusive. Set both to same value to include only words of that length.

example:
`python3 main.py --min 8 --max 8 --source ~/my_file.txt` will return only those words from my_file.txt which are 8 characters long.

Use `--help` for help.