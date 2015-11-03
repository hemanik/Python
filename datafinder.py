#!/usr/bin/env python

import csv 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-cn', '--country', help="specify the country")
parser.add_argument('-ds', '--dataset', help="specify the dataset file")
parser.add_argument('-ct', '--category', help="specify the category")
parser.add_argument('-yr', '--year', help="specify the year")
parser.add_argument('--datafile', nargs=2, help="specify two files")

try:
     args = parser.parse_args()

     if args.country and args.dataset and args.category :

         with open('TB_notifications_2015-10-29.csv', 'rb') as file1, \
              open('TB_data_dictionary_2015-10-29.csv', 'rb') as file2 :

             reader1 = csv.DictReader(file1)
             reader2 = csv.DictReader(file2)
       
             value = "DNP"    
             
             print"COUNTRY:", args.country

             if args.year :
                  print"YEAR:", args.year
      	          for row1 in reader1:
                      if args.country in row1['iso2'] and args.year in row1['year']:
                           value = row1[args.category]
                           if value == '' or value == 0:
                              value = "DNP"
                           break   
       
                  for row2 in reader2:
                      if args.category in row2['variable_name']:
                           print "CATEGORY [", row2['definition'], "]:", value
                           break
             else :
                  for row2 in reader2:
                      if args.category in row2['variable_name']:
                           print "CATEGORY [", row2['definition'], "]"
                           break
         
                  for row1 in reader1:
                      if args.country in row1['iso2']:
                          value = row1[args.category]
                          year  = row1['year'] 
                          if value == '' or value == 0:
                             value = "DNP"   

                          print year, ":", value

     else:
          print "Invalid Arguments. Check help."
                                           
except argparse.ArgumentError, exc:
     print exc.message

except IOError:  
     print "Cannot open input files."

except Exception, e:
     print ("Error: %s" %e)  

