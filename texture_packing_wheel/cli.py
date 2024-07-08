"""Command-line interface for deppth functionality"""
import os
import argparse

from .texture_packing_wheel import build_atlases

def main():
  parser = argparse.ArgumentParser(prog='hades_texture_pack', description='Format images into an atlas and manifest for packing with deppth')
  # subparsers = parser.add_subparsers(help='The action to perform', dest='action')

  # Pack parser
  # pack_parser = subparsers.add_parser('pack', help='Pack images into an atlas and manifest', aliases=['pk'])
  parser.add_argument('-s', '--source', metavar='source', default='MyPackage', type=str, help='The directory to recursively search for images in, default is current folder')
  parser.add_argument('-t', '--target', metavar='target', default='ModAuthor-MyPackage', help='Filenames created will start with this plus a number')
  parser.add_argument('-dP', '--deppthpack', metavar='deppthpack', default='True', help='Automatically Pack your images and Manifest using deppth')
  parser.add_argument('-iH', '--includehulls', metavar='includehulls', default = "False", help='Set to anything if you want hull points computed and added')
  parser.set_defaults(func=cli_pack)

  args = parser.parse_args()
  args.func(args)

def cli_pack(args):
  source = args.source
  target = args.target

  deppth = True
  if args.deppthpack != "True":
    deppth = False

  hulls = False
  if args.includehulls != "False":
    hulls = True

  build_atlases(source, target, deppth, hulls)