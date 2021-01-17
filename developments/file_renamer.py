# -*- coding: utf-8 -*-

# pylint: disable=C0111


r"""
file_renamer.py
python file_renamer.py "C:\Users\omerb\OneDrive\Masaüstü\dosyalar"
"""
import re
import glob
import os
import sys


def show_usage():
    print(r"""
        böyle kullan:
        python file_renamer.py "C:\Users\omerb\OneDrive\Masaüstü\dosyalar"
        parametre, bir directory olmalıdır
    """)


def convert_ascii(char):
    switcher = { 
        "ö": "o", 
        "ı": "i", 
        "ş": "s", 
        "Ç": "C",
        "ç": "c",  
        "Ş": "S", 
        "Ü": "U",
        "İ": "I" 
    } 
    return switcher.get(char, "_") 
    

def build_new_file_name(old_file_name):
    head, tail = os.path.split(old_file_name)
    new_file_name_tail = ""
    for tail_char in tail:
        if (re.sub('[ -~]', '', tail_char)) != "":   #   non-ascii
            new_file_name_tail += convert_ascii(tail_char)
        else:
            new_file_name_tail += tail_char
        
    return os.path.join(head,new_file_name_tail)


def process_dir(target_dir):
    def build_fil_list():
        file_list_inner = glob.glob(pattern)
        return file_list_inner


    pattern = os.path.join(target_dir, "*.*")
    file_list = build_fil_list()
    for old_file_name in file_list:
        new_file_name = build_new_file_name(old_file_name)
        print("eski -> ", old_file_name)
        print("yeni -> ", new_file_name)
        os.rename(old_file_name, new_file_name)
        print()


def main():
    if len(sys.argv) == 2:
        target_dir = sys.argv[1]
        try:
            if not os.path.isdir(target_dir):
                msg = target_dir
                raise NotADirectoryError(msg)
            process_dir(target_dir)
        except NotADirectoryError as err1:
            print("Direcory not found : ", err1)
            show_usage()
    else:
        show_usage()

main()
