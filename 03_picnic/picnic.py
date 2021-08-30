
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Purpose: To more fully develop the argparse involvement in a program
"""
Author : Ryan M
Date   : 2021-08-29
Purpose: To more fully develop the argparse involvement in a program
"""
 
import argparse
import os
import sys
 
 
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""
 
    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
 
    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')
 
    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')
 
    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)
 
    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default=None)
 
    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')
 
    return parser.parse_args()
 
 
# --------------------------------------------------
def main():
    """echo arguments back to user"""
 
    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional
 
    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')
 
 
# --------------------------------------------------
if __name__ == '__main__':
    main()