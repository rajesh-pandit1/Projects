import argparse
import numpy as np
import dnnlib
import dnnlib.tflib as tflib
import re
import sys

import projector
import prentrained_networks
from training import dataset
from training import misc

def main():
    parser = argparse.ArgumentParser(description='''StyleGAN2 projector.
           Run 'python %(prog)s <subcommand> ---help' for subcommand help.''',
           epilog=_examples,
formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(help='Sub-commands', dest='command')

    args = parser.parse_args()
    subcmd = args.command
    if subcmd is None:
        print('Error: missing subcommand. Re-run with --help for usage.')
        sys.exit(1)

if __name__ == "__main__":
    main()
   