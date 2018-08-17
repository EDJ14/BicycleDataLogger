#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)

# This shoul turn on the LED
GPIO.setup(12, GPIO.OUT) 
GPIO.output(12, GPIO.HIGH)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(16, GPIO.FALLING)

subprocess.check_call(['rosnode', 'klll', '-a'], shell=False)
# -h stands for --power-off
subprocess.check_call(['shutdown', '-h', 'now'], shell=False)
