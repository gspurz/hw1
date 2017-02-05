#
# hw1pr3.py
#
# Graham Spurzem

"""
Just run main() and make sure that the 'subs.csv' file is in
the same directory!

The example created from main() is included in the HTML_annotater_example.html file

NOTE: When copying and pasting from Python, unwanted breaks in the HTML output may appear due to
the size limits of the text editor window. Just find and delete the breaks and the code will
appear as intended.
"""

import csv

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
# annotate_text_starter
#
#   Shows off how to style portions of an input text
#   This does not actually use the annotations dictionary (but you will...)
#
def annotate_text( text, subs ):
    """ this is a letter-by-letter (instead of word-by-word)
        text-annotater. It makes the 'z' characters in the input text bright red.
        It also changes the '\n' characters to "<br>"

        It does not use the annotations dictionary (but you'll want to!)
        It is not general (but you'll build a general template engine!)

    """
    new_html_string = ''
    new_html_string += '<!DOCTYPE html>\n'
    new_html_string += '<html>\n'
    new_html_string += '<body>\n'
    new_html_string += '<p>\n'
    text = text.split()
    for word in text:
            if word in subs.keys():
                new_word = '<span style="color:{0};" title="{2}">{1}</span>'.format("red", word, subs[word]) + ' '
            elif word == '\n':  # handle new lines...
                new_word = "<br>"
            else:
                new_word = word + ' '

            new_html_string += new_word 
    new_html_string += '</p>\n'
    new_html_string += '</body>\n'
    new_html_string += '</html>'
    print(new_html_string)


#
# Dictionary creator
#

def makeDict(filename):
    """ reads in csv file with substitutions and outputs a dictionary of word-substitution pairs"""
    list_of_rows = readcsv(filename)
    d = {}
    for row in list_of_rows:
        d[row[0]] = row[1]
    return d

#
# main()
#

def main():
    annotate_text('In ancient times, a candidate during a debate would try to come off as honest and genuine and make global promises that were never kept. This angered many people and created an unknown amount of tension between them and the government. Since then, years have passed and we have the same problems.',makeDict('subs.csv'))


# Larger example for testing...


#
# Here are the text and dictionary of substitutions used in hamlet_substitution.html
#
# Note that we don't give away the template engine here (there'd be nothing left!) 
#
# Inspired by
# http://nfs.sparknotes.com/hamlet/page_50.html
#

HAMLET_A1S4 = """
The king doth wake tonight and takes his rouse,
Keeps wassail and the swaggering upspring reels,
And, as he drains his draughts of Rhenish down,
The kettle-drum and trumpet thus bray out
The triumph of his pledge.
"""

#
# this would be read in from a csv file and constructed
#
# Again, we don't give that function (it's the hw!)
HAMLET_SUBS = { "doth":"does", "rouse":"partying", 
                "wassail":"drinks",
                "reels":"dances", "rhenish":"wine", 
                "bray":"blare", "pledge":"participation"}



#
# You can see the output in  hamlet_substitution.html
#