import shutil
import os

currfile = input("Enter File Name: ")
destiloc = input("Enter Directory Name: ")

try:
    shutil.move(currfile, destiloc)
    print(f'file "{currfile}" is copied in "{destiloc}" Successfully.')
except Exception as e:
    print(e)
