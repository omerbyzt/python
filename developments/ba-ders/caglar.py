# -*- coding: utf-8 -*-
 
r"""
file_renamer.py
python file_renamer.py "C:\Users\caglar.toklu\Desktop\Python_egitim_part1\dosyalar"
 
https://docs.python.org/3/
https://docs.python.org/3/py-modindex.html
https://docs.python.org/3/library/index.html
"""
 
import glob
import os
import sys
 
def show_usage():
    print(r"""
böyle kullan:
python file_renamer.py "C:\Users\caglar.toklu\Desktop\dosyalar"    
parametre, bir directory olmalidir.
    """)
 
def build_new_file_name(old_file_name):
    """
    c:\a\b\c\d
    head: c:\a\b\c
    tail: d
 
    c:\a\b\c\d\d1.txt
    head: c:\a\b\c\d
    tail: d1.txt
 
    https://docs.python.org/3/library/os.path.html#module-os.path
    """
    head, tail = os.path.split(old_file_name)
    # TODO: tail'deki string'i rename et.
    # TODO: head ile yeni tail'i join et
    # TODO: bu halini dondur.
 
def process_dir(target_dir):
    def build_file_list():
        file_list_inner = glob.glob(pattern)
        return file_list_inner
 
    # pattern = target_dir + "\*.*"
    pattern = os.path.join(target_dir, "*.*")
    file_list = build_file_list()
    # print(file_list)
    for old_file_name in file_list:
        new_file_name = build_new_file_name(old_file_name)
        print(old_file_name)
        print(new_file_name)
        print()
 
def main():
    # print(sys.argv)
    # print(type(sys.argv))
    if len(sys.argv) == 2:
        target_dir = sys.argv[1]
        try:
            if not os.path.isdir(target_dir):
                msg = target_dir
                raise NotADirectoryError(msg)
            process_dir(target_dir)
        except NotADirectoryError as err1:
            print("Directory not found: ", err1)
            show_usage()
    else:
        show_usage()
 
main()