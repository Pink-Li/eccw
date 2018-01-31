#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Manage command line interface.
"""

import argparse


from eccw import __version__, __authors__
from eccw.shared.file_management import open_pdf


def options_parser() :
    """Parse options given with the execute command line."""

    #create a parser object
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False,
        description=
            "    ECCW - Exact Critical Coulomb Wedge, Version {0}\n"
            "(c) 2016-2018 {1}\n"
            "\n"
            "ECCW is a Qt interface using python package 'eccw' to"
            " compute and draw the exact solution of critical Coulomb"
            " wedge (as Dahlen 1984 and Yuan et al. 2015)\n".format(
                __version__, 
                ", ".join(__authors__)
                ),
        usage="eccw [-h|--help] [-d|--doc] [-V|--version]",
        )

    # Optional arguments.
    optarg = parser.add_argument_group(title="-"*30+"\nOPTIONAL ARGUMENT", description="")

    optarg.add_argument(
        '-h', '--help',
        action='help',
        help="show this help message and exit\n\n"
        )

    optarg.add_argument(
        '-V', '--version',
        action='version',
        version=__version__,
        help="show program's version number and exit\n\n"
        )

    optarg.add_argument(
        '-d', '--doc',
        dest="doc",
        action='store_true',
        help="show complete documentation and exit\n\n"
        )

    inputoptions = parser.parse_args() #parse the command line from the shell using arguments defined in the parser object

    if inputoptions.doc is True :
        open_pdf("/eccw/documentation/ECCW.pdf")
        exit()

    return inputoptions


if __name__ == "__main__":

    inputoptions = options_parser()
    print("run can start")

