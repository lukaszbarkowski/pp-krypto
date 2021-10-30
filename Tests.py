from rich.console import Console
from rich.style import Style

console = Console()

failStyle = Style(color="red", bold=True)
passStyle = Style(color="green", bold=True)


def passTest():
    console.print("Passed\n", style=passStyle)


def failTest():
    console.print("Failure\n", style=failStyle)


def singleBitTest(bits, debug):
    zeros = bits.count("0")
    ones = bits.count("1")

    if debug:
        print("Zera:", zeros)
        print("Jedynki:", ones)

    if 9725 < ones < 10275:
        passTest()
    else:
        failTest()


expectedMinSeriesValues = {
    1: 2315,
    2: 1114,
    3: 527,
    4: 240,
    5: 103,
    6: 103,
}
expectedMaxSeriesValues = {
    1: 2685,
    2: 1386,
    3: 723,
    4: 384,
    5: 209,
    6: 209,
}


def seriesTest(bits, debug):
    dict = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }
    lastbit = None
    seriesLength = 0

    for b in bits:
        if lastbit is not None:
            if lastbit == b:
                seriesLength += 1
            elif seriesLength > 0:
                if seriesLength >= 6:
                    dict[6] = dict[6] + 1
                else:
                    dict[seriesLength] = dict[seriesLength] + 1

                seriesLength = 0

        lastbit = b

    isTestSuccessfull = True

    for key, value in dict.items():
        if not (expectedMinSeriesValues[key] < value < expectedMaxSeriesValues[key]):
            isTestSuccessfull = False

        if debug:
            print("Seria ", key, ": ", value)

    if isTestSuccessfull:
        passTest()
    else:
        failTest()


def longSeriesTest(bits, debug):
    index = 0
    nextIndex = 1
    longestSeries = 0
    currentSeries = 1
    value = bits[0]

    for i in bits:
        if nextIndex < len(bits):
            if value is bits[nextIndex]:
                currentSeries += 1
                if currentSeries > longestSeries:
                    longestSeries = currentSeries
                    value = i
            if value is not bits[nextIndex]:
                currentSeries = 1
                value = bits[nextIndex]
        index += 1
        nextIndex += 1

    if debug:
        print("Najdluzsza seria:", longestSeries)

    if longestSeries < 26:
        passTest()
    else:
        failTest()


def pokerTest(bits, debug):
    n = 4
    dict = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
        13: 0,
        14: 0,
        15: 0,
    }
    for i in range(0, len(bits), n):
        value = int(bits[i : i + n], 2)
        dict[value] = dict[value] + 1

    quaterOfLength = len(bits) / 4

    x = 16 / (quaterOfLength)
    suma = 0
    for key, value in dict.items():
        suma += value * value
        if debug:
            print("Liczba", key, ": ", value)

    testResult = x * suma - quaterOfLength

    if debug:
        print("Wynik: ", testResult)

    if 2.16 < testResult < 46.17:
        passTest()
    else:
        failTest()
