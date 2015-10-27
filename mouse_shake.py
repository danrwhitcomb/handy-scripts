#!/usr/local/bin/python

import pyautogui
from time import sleep
import argparse
from math import floor

MOUSE_MOVE = 1
SLEEP = 0.0001
SHAKES = 10

def do_shake():
	currentX, currentY = pyautogui.position()
	for i in range(SHAKES):
		if i % 2 == 0:
			pyautogui.moveTo(currentX + MOUSE_MOVE, currentY + MOUSE_MOVE)
		else:
			pyautogui.moveTo(currentX - MOUSE_MOVE, currentY - MOUSE_MOVE)

		sleep(SLEEP)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("interval", type=float)
	parser.add_argument("time", type=float)
	args = parser.parse_args()

	if args.interval > args.time:
		print("Error: Interval cannot be greater than time")
		quit()

	num = int(floor(args.time / args.interval))
	for i in range(num):
		sleep(args.interval)
		do_shake()

	print("Mouse shaking has completed")
	print("Exiting...")


if __name__ == "__main__":
	main()