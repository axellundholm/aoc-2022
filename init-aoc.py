import argparse, subprocess, time

parser = argparse.ArgumentParser(description='Set up AoC python environment')

parser.add_argument('day', metavar='day', type=int, help = 'which day to initialize')

args = parser.parse_args()

subprocess.run(['mkdir', str(args.day).zfill(2)])

subprocess.run(['cp', 'day-0.py', str(args.day).zfill(2) + '/day-' + str(args.day) + '.py'])

subprocess.run(['touch', 'test-input'], cwd=str(args.day).zfill(2) + '/')

subprocess.run(['aoc', 'd', '-d', str(args.day)], cwd=str(args.day).zfill(2) + '/')