from os import error
import Tests
from bbs import bbs
from rich.console import Console
from rich.style import Style
import argparse
from pathlib import Path
import encryptor

console = Console()

DEFAULT_N = 20000


def runTests(bits, debug):
    console.print("[bold magenta]Test pojedynczych bitów:[/bold magenta]")
    Tests.singleBitTest(bits, debug)

    console.print("[bold magenta]Test serii:[/bold magenta]")
    Tests.seriesTest(bits, debug)

    console.print("[bold magenta]Test długiej serii:[/bold magenta]")
    Tests.longSeriesTest(bits, debug)

    console.print("[bold magenta]Test pokerowy:[/bold magenta]")
    Tests.pokerTest(bits, debug)


def getArgs():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-debug",
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

    parser.add_argument("-m", type=str, dest="message", help="message to encrypt")

    parser.add_argument(
        "-d",
        default=False,
        dest="decrypt",
        action="store_const",
        const=True,
        help="decrypt input message",
    )

    parser.add_argument("-s", type=int, dest="seed", help="seed to input")

    args = parser.parse_args()

    debug = args.debug
    inputFile = args.input
    outputFile = args.output
    outputLength = args.length
    decrypt = args.decrypt
    userSeed = args.seed
    message = args.message

    return (
        debug,
        inputFile,
        outputFile,
        outputLength,
        decrypt,
        userSeed,
        message,
    )


if __name__ == "__main__":
    debug, inputFile, outputFile, outputLength, decrypt, userSeed, message = getArgs()

    if decrypt:
        if inputFile and userSeed:
            data = ""
            with open(inputFile, "r") as file:
                data = file.read()

            seed, bits = bbs(len(data) * 7, userSeed)

            message = encryptor.decrypt(data, bits)

            print(message)
        else:
            raise Exception(
                "Input file(-f) and seed (-s) are required while using decryption"
            )
    else:
        if message is not None:
            outputLength = len(message) * 7

        seed, bits = bbs(outputLength, userSeed)

        if outputFile:
            Path("output/bbs/").mkdir(parents=True, exist_ok=True)
            with open("output/bbs/" + outputFile, "w") as text_file:
                text_file.write(bits)

        if message:
            encryptedMessage = encryptor.encrypt(message, bits)

            console.print("Seed: " + str(seed), style=Style(color="red", bold=True))

            if outputFile:
                Path("output/encryption/").mkdir(parents=True, exist_ok=True)
                with open("output/encryption/" + outputFile, "w") as text_file:
                    text_file.write(encryptedMessage)
                console.print(
                    "Encrypted message save to file.",
                    style=Style(color="green", bold=True),
                )
            else:
                print("Encrypted message:")
                print(encryptedMessage)

        if debug:
            print("Bits:", bits)

        if outputLength == DEFAULT_N:
            runTests(bits, debug)
