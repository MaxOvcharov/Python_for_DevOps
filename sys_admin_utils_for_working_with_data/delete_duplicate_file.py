#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class Delete(object):
    """
    Here some methods of how you can to delete duplicate files:
    1) Interactive method with Y/N questions;
    2) Imitation of deleting duplicate files;
    3) Silent deleting duplicate files;
    """
    def __init__(self, file):
        self.file = file

    def interactive_del(self):
        """Interactive method with Y/N questions"""
        print('\n' + '-/-' * 20 + '\n')
        inp = input("Do you realy want to dalete %s - [N]/Y: " % self.file)
        if inp.upper() == 'Y' or inp.upper() == 'YES':
            try:
                os.remove(self.file)
                print('DELETING FILE: %s \033[32m[OK]\033[0m' % self.file)
            except Exception as e:
                print('DELETING FILE: %s \033[31m[FAIL]\033[0m - ERROR: %s' % (self.file, e))
        else:
            print('DELETING FILE: %s \033[93m[SKIP]\033[0m' % self.file)
        return

    def del_imitation(self):
        """Imitation of deleting duplicate files"""
        print('\n' + '-/-' * 20 + '\n')
        print('DELETING FILE: %s \033[93m[NOT DELETED]\033[0m' % self.file)
        return

    def silent_del(self):
        """Silent deleting duplicate files"""
        print('\n' + '-/-' * 20 + '\n')
        try:
            os.remove(self.file)
            print('DELETING FILE: %s \033[32m[OK]\033[0m' % self.file)
        except Exception as e:
            print('DELETING FILE: %s \033[31m[FAIL]\033[0m - ERROR: %s' % (self.file, e))
        return

if __name__ == '__main__':
    from duplicate_file_finder import find_duplicates
    # Default path for find_duplicates() is /tmp
    print('\n--  START --\n')
    duplicates = find_duplicates()
    for duplicate in duplicates:
        delete_duplicates = Delete(duplicate)
        delete_duplicates.interactive_del()
        # delete_duplicates.del_imitation()
        # delete_duplicates.silent_del()
    print('\n--  THE END --\n')
