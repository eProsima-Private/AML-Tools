#!python3
import sys
import amldl
from pathlib import Path
import platform

if platform.system() == "Windows":
    os.system('color')

class clrs:
    title = "\033[34m"
    section = "\033[32m"
    error = "\033[31m"
    hl = "\033[33m"
    end = "\033[0m"

def printEmbeddingSummary(embeddingFile:str) -> None:
    # Load embedding
    embedding = amldl.load_embedding(embeddingFile)

    # Output embedding constants and duples
    print(f"{clrs.title}Summary - {embeddingFile}{clrs.end}")
    print(f"{clrs.section}Constants{clrs.end}")
    print(f"  {embedding['constantsNames']}")

    print(f"{clrs.section}Positive Duples{clrs.end}")
    for idx, (l, r) in enumerate(embedding["positiveDuples"]):
        left = [embedding['constantsNames'][e] for e in l]
        right = [embedding['constantsNames'][e] for e in r]
        print(f"{idx+1:>4d}. {l} {clrs.hl}<{clrs.end} {r}")
        print(f"      {left} {clrs.hl}<{clrs.end} {right}")

    print(f"{clrs.section}Negative Duples{clrs.end}")
    for idx, (l, r) in enumerate(embedding["negativeDuples"]):
        left = [embedding['constantsNames'][e] for e in l]
        right = [embedding['constantsNames'][e] for e in r]
        print(f"{idx+1:>4d}. {l} {clrs.hl}≮{clrs.end} {r}")
        print(f"      {left} {clrs.hl}≮{clrs.end} {right}")


if __name__ == "__main__":

    embeddingFile = "example_01.py"
    printEmbeddingSummary(embeddingFile)

    embeddingFile = "example_02.py"
    printEmbeddingSummary(embeddingFile)

    embeddingFile = "example_03.py"
    printEmbeddingSummary(embeddingFile)
