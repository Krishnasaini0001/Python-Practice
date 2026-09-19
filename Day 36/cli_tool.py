# Day 36: building a CLI tool with argparse

import argparse

parser = argparse.ArgumentParser(description="Simple greeting CLI")
parser.add_argument("name", help="Name to greet")
parser.add_argument("--loud", action="store_true", help="Shout the greeting")

args = parser.parse_args()

greeting = f"Hello, {args.name}!"
if args.loud:
    greeting = greeting.upper()

print(greeting)