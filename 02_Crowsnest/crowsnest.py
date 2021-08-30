
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Purpose: To more fully develop the argparse involvement in a program
"""
Author : Ryan M
Date   : 2021-08-29
Purpose: To give a positional response based on a object input
"""
 
import argparse
import os
import sys
 
 
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
 
    parser = argparse.ArgumentParser(
        description='Crows Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
 
    parser.add_argument('word',
                        metavar='word',
                        help='A word')


 
    return parser.parse_args()
 
 
# --------------------------------------------------
def main():
    """echo arguments back to user"""
 
    args = get_args()
    pos_arg = args.word
    if pos_arg[0].upper() in 'AEIOU':
        print(f'Ahoy, Captain, an {pos_arg} off the larboard bow!')
    else:
        print(f'Ahoy, Captain, a {pos_arg} off the larboard bow!')
 
 
# --------------------------------------------------
if __name__ == '__main__':
    main()


