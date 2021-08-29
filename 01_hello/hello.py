#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Purpose: To test the hello py script
"""
Def: Just a basic 'hello world' program as prescribed by the book. Just 
being thorough :) 

Version2: added the argument parsing module in order to handle -h

Version3: added the def main and __name__ check as is standard with most 
well written python programs. This is done in case 

Version4: added seperate get_args() function to process arguments
"""
import argparse

def get_args():
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument('-n','--name',metavar='name',default='World',help='Name to greet',)
    args = parser.parse_args()

def main():
    args = get_args()

    print('Hello, ' + args.name + '!') # This also doubles as the commenting tutorial.

if __name__ == '__main__':
    main()