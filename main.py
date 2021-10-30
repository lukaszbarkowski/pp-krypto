import sympy
import random
import Tests
from rich.console import Console
import argparse
from pathlib import Path

console = Console()

DEFAULT_N = 20000


def next_usable_prime(x):
    p = sympy.nextprime(x)
    while p % 4 != 3:
        p = sympy.nextprime(p)
    return p


def runTests(bits, debug):
    console.print("[bold magenta]Test pojedynczych bitów:[/bold magenta]")
    Tests.singleBitTest(bits, debug)

    console.print("[bold magenta]Test serii:[/bold magenta]")
    Tests.seriesTest(bits, debug)

    console.print("[bold magenta]Test długiej serii:[/bold magenta]")
    Tests.longSeriesTest(bits, debug)

    console.print("[bold magenta]Test pokerowy:[/bold magenta]")
    Tests.pokerTest(bits, debug)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d",
        default=False,
        dest="debug",
        action="store_const",
        const=True,
        help="Debug informations",
    )

    parser.add_argument("-f", type=str, dest="input", help="path to input file")

    parser.add_argument("-o", type=str, dest="output", help="path to output file")

    parser.add_argument(
        "-l", default=DEFAULT_N, type=int, dest="length", help="length of the output"
    )

    args = parser.parse_args()

    debug = args.debug
    inputFile = args.input
    outputFile = args.output
    outputLength = args.length

    x = 3 * 10 ** 10
    y = 4 * 10 ** 10

    seed = random.randint(1, 1e10)

    bits = ""

    p = next_usable_prime(x)
    q = next_usable_prime(y)
    M = p * q

    x = seed

    for _ in range(outputLength):
        x = x * x % M
        b = x % 2
        bits += str(b)

    if outputFile:
        Path("output/").mkdir(parents=True, exist_ok=True)
        with open("output/" + outputFile, "w") as text_file:
            text_file.write(bits)

    if debug:
        print(bits)

    if outputLength == DEFAULT_N:
        runTests(bits, debug)
