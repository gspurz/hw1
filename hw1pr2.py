#
# hw1pr2.py
# 
# Graham Spurzem
#

"""
Just run main() to print my HTML table!

With wds.csv in the same directory

NOTE: Output numbers are percentages (see included polished HTML table)
"""

import csv
from collections import *

#
# readcsv is a starting point - it returns the rows from a standard csv file...
#
def readcsv( csv_file_name ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( csv_file_name, newline='' )  # open for reading
        csvrows = csv.reader( csvfile )              # creates a csvrows object

        all_rows = []                               # we need to read the csv file
        for row in csvrows:                         # into our own Python data structure
            all_rows.append( row )                  # adds only the word to our list

        del csvrows                                  # acknowledge csvrows is gone!
        csvfile.close()                              # and close the file
        return all_rows                              # return the list of lists

    except FileNotFoundError as e:
        print("File not found: ", e)
        return []

#
# write_to_csv shows how to write that format from a list of rows...
#  + try   write_to_csv( [['a', 1 ], ['b', 2]], "smallfile.csv" )
#
def write_to_csv( list_of_rows, filename ):
    """ readcsv takes as
         + input:  csv_file_name, the name of a csv file
        and returns
         + output: a list of lists, each inner list is one row of the csv
           all data items are strings; empty cells are empty strings
    """
    try:
        csvfile = open( filename, "w", newline='' )
        filewriter = csv.writer( csvfile, delimiter=",")
        for row in list_of_rows:
            filewriter.writerow( row )
        csvfile.close()

    except:
        print("File", filename, "could not be opened for writing...")


#
# csv_to_html_table
#
#   Shows off how to create an html-formatted string
#   Some newlines are added for human-readability...
#
def csv_to_html_table( csvfilename ):
    """ csv_to_html_table_starter
           + an example of a function that returns an html-formatted string
        Run with 
           + result = csv_to_html_table_starter( "example_chars.csv" )
        Then run 
           + print(result)
        to see the string in a form easy to copy-and-paste...
    """
    list_of_rows = readcsv(csvfilename)
    html_string = '<!DOCTYPE html>\n'
    html_string += '<html>\n'
    html_string += '<body>\n'
    html_string += '<table align="center">\n'    # start with the table tag

    html_string += '<tr bgcolor =lightgrey>\n'
    html_string += '<td><u>Letter</u></td>\n'
    html_string += '<td><u>First letter (%)</u></td>\n'
    html_string += '<td><u>Second letter (%)</u></td>\n'
    html_string += '<td><u>Last letter (%)</u></td>\n'
    html_string += '</tr>\n'
    
    for row in list_of_rows:
        html_string += '<tr>\n'
        for i in range(len(row)):
            if row[i] != '':
                html_string += '<td>'
                html_string += row[i]
                html_string += '</td>\n'
        
        html_string += '</tr>\n'
    html_string += '</table>\n'
    html_string += '</body>\n'
    html_string += '</html>'
    return html_string

#
#
# Letter Analyses
#
#

def main():

    #
    # 1. WEIGHTED counting of first letters!
    #
    def Wcount():
        """ returns a LoL of
            WEIGHTED first-letter counts from 
            the file wds.csv
        """
        LoL = []
        LoR = readcsv( "wds.csv" )  # List of rows
        counts = defaultdict(int)
        for Row in LoR:
            word = str(Row[0])                         # the word is at index 0
            word = word.lower()
            num  = float(Row[1])                       # its num occurrences is at index 1
            weight = float(num/1000000000)             # weight of each word...instances/billion
            first_letter = word[0]                     # the first letter of the word
            if first_letter in 'abcdefghijklmnopqrstuvwxyz':
                add = 1*weight*100                              # giving as a %
                counts[first_letter] += round(add,4)           # add one to that letter's counts

        for key, value in counts.items():
            temp = [key,value]
            LoL.append(temp)
        
        return sorted(LoL)


    #
    # 2. WEIGHTED counting of last letters!
    #
    def WLcount():
        """ returns a LoL of
            WEIGHTED last-letter counts from 
            the file wds.csv
        """
        LoL = []
        LoR = readcsv( "wds.csv" )  # List of rows
        counts = defaultdict(int)
        for Row in LoR:
            word = str(Row[0])                         # the word is at index 0
            word = word.lower()
            num  = float(Row[1])                       # its num occurrences is at index 1
            weight = float(num/1000000000)             # weight of each word...instances/billion
            last_letter = word[-1]                     # the last letter of the word
            if last_letter in 'abcdefghijklmnopqrstuvwxyz':
                add = 1*weight*100
                counts[last_letter] += round(add,4)            # add one to that letter's counts
        counts['j'] = 0
        for key, value in counts.items():
            temp = [key,value]
            LoL.append(temp)
        
        return sorted(LoL)

    #
    # 3. WEIGHTED counting of second letters!
    #
    def WScount():
        """ returns a LoL of
            WEIGHTED second-letter counts from 
            the file wds.csv
        """
        LoL = []
        LoR = readcsv( "wds.csv" )  # List of rows
        counts = defaultdict(int)
        for Row in LoR:
            word = str(Row[0])                         # the word is at index 0
            word = word.lower()
            num  = float(Row[1])                       # its num occurrences is at index 1
            weight = float(num/1000000000)             # weight of each word...instances/billion
            if len(word) >= 2:
                second_letter = word[1]                      # the second letter of the word
                if second_letter in 'abcdefghijklmnopqrstuvwxyz':
                    add = 1*weight*100
                    counts[second_letter] += round(add,4)            # add one to that letter's counts
        counts['j'] = 0                                     
        for key, value in counts.items():
            temp = [key,value]
            LoL.append(temp)
        
        return sorted(LoL)

    #
    # Combine all data
    #

    def combineAll():
        """ combines all letter data obtained above """
        first = Wcount()
        second = WScount()
        last = WLcount()
        LoL = []
        for i in range(len(first)):
            row = first[i] + second[i] + last[i]
            LoL.append(row)
        for i in range(len(LoL)):
            LoL[i][2] = ''                  # remove extra letter labels
            LoL[i][4] = ''
        return LoL


    #final product
    write_to_csv(combineAll(), 'frequencies.csv')
    result = csv_to_html_table( "frequencies.csv" )
    print(result)


    

