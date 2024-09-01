from os import system as cmd
from random import shuffle

def bingoGen():
    """Generates a bingo card in Markdown format."""
    b, i, n, g, o = ([x for x in range(y, y + 15)] for y in range(1, 76, 15))
    for x in (b, i, n, g, o):
        shuffle(x)

    bingoLines = ["| B | I | N | G | O | "*2+"|", "| ----- " * 11 + "|"]

    for x in range(5):
        temp = ""
        if x == 2:
            for y in range(x, 10, 5):
                temp += f"| {b[y]} | {i[y]} | | {g[y]} | {o[y]} | "
        else:
            for y in range(x, 10, 5):
                temp += f"| {b[y]} | {i[y]} | {n[y]} | {g[y]} | {o[y]} | "

        bingoLines.append(temp.strip())

    return "\n".join(bingoLines)


for e in range(9):
    with open("bingo.md", "w") as f:
        f.write(bingoGen() + "\n\n<br><br>\n\n" + bingoGen())

    cmd(f"pandoc -s bingo.md -o bingo{e}.html --css bingostyle.css")
    cmd("rm bingo.md")
