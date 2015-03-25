#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

def convert_csv_to_redirect(filepath, result_file_path):
    with open(filepath, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        
        main_struct = "location ~ ^/index.php {\n%s\n\trewrite ^ http://www.teylersmuseum.nl/? permanent;\n}\n"

        rules = ""
        for row in spamreader:
            if row[1] != "?":

                split = row[0].split('?')
                if len(split) > 1:
                    query_string = split[1]

                    rule = "\tif ($args ~ %s) {\n\trewrite ^ %s? permanent;\n\t}\n" %(query_string, row[1])
                    rules += rule

        final_rules = main_struct % (rules)

        print final_rules



    f = open(result_file_path, 'w');
    f.write(final_rules)

if __name__ == "__main__":
    filepath = "/Users/AG/Projects/NewTeylersMuseum/sources/CSVtoRedirect/teylers-redirects.csv"
    result_file_path = "/Users/AG/Projects/NewTeylersMuseum/sources/CSVtoRedirect/teylersmuseum.nl-redirects"

    convert_csv_to_redirect(filepath, result_file_path)