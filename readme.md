# Bingo Generator

This bingo generator was created to help create free, printable bingo cards. My ideas for this project started because my family wanted affordable bingo cards they could use during family events.

The Python script generates Markdown files containing a page of four bingo cards each. Using Pandoc, the script generates HTML files, using `bingostyle.css` to ensure each file has consistent formatting.

## How the script and Markdown work

The script uses a command-line tool called Pandoc to create bingo cards using Markdown.

First, the script generates a list of numbers, categorizing each set of numbers into B, I, N, G, and O, the five common letters found in bingo. It then shuffles the list, ensuring that the numbers are random.

Based on these numbers, the script generates a Markdown file formatted as a table. The script puts four bingo cards in one `.md` file, arranged in a 2x2 grid. This was achieved by creating a table with eleven columns and using a center row as a separator, and using `<br>` to separate the two tables.

## Dependencies

This script needs Pandoc to work. Under Linux, Pandoc can be installed by using your package manager in your Linux distribution. On macOS, please use Homebrew. Windows users will need to install Windows Subsystem for Linux, as this program is only compatible with Linux/Unix.

## System Requirements

This Python program was tested on Ubuntu/Debian on Raspberry Pi, but it will work with other Unix-like and Linux operating systems, including macOS. On Windows, I recommend installing and using Windows Subsystem for Linux.

## Needs Work

### CSS Formatting

So far, I have done my best to create a visually appealing `bingostyle.css` file, which formats the cards. However, due to my visual impairment, I am unable to determine if the formatting of the bingo cards is visually correct. Your assistance in helping with bingo card formatting and adding a visually appealing style is greatly appreciated!

### Switching from Markdown to HTML

The current implementation of this script uses Markdown, which requires the Pandoc command-line tool to convert to HTML. To avoid dependencies that might require use of a specific operating system, future versions of this program should create the HTML in code.

All contributions are welcome!