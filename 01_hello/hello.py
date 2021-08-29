#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Purpose: To test the hello py script
"""
Def: Just a basic 'hello world' program as prescribed by the book. Just 
being thorough :) 

Version2: added the argument parsing module in order to handle -h

"""
import argparse

parser = argparse.ArgumentParser(description="Say Hello")
parser.add_argument('-n','--name',metavar='name',default='World',help='Name to greet',)
args = parser.parse_args()

print('Hello, ' + args.name + '!') # This also doubles as the commenting tutorial.