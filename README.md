# WHO Data Finder

Python-Scripts Repo for Datafinder Project

There are many websites that provide interesting information in CSV format. We will be using the World Health Organization’s (WHO) website to download some information on Tuberculosis. You can go here to get it: http://www.who.int/tb/country/data/download/en/.

This repo has two data file attachments.

Data dictionary : File containing headers/categories
Notifications : Actual data, country wise, year wise for various categories. 

Write a tool in Python that will process the above files and find "business intelligence".

A sample run :

``` Console
./python datafinder.py --country/-cn <ISO2_COUNTRY_NAME> --dataset/-ds <DATA_SET_NAME> --category/-ct <VARIABLE_NAME> --year/-yr <YEAR> --datafile <DATAFILE>
```

Mandatory CLI args:
--country
--dataset
--category

Optional
--year

Sample output
``` Console
Country : COUNTRY
Year : YEAR
Category : VALUE
```
Or
``` Console
Country : COUNTRY
YEAR 1: VALUE 1
YEAR 2: VALUE 2
YEAR 3: VALUE 3
YEAR 4: VALUE 4
.... and so on.
```

If Year is not provided via CLI args, show values for all years for the given Category and Country.

************************************

Test Case 1:

 python datafinder.py -cn AF -ds notification -ct new_sp -yr 1997

Output:
``` Console
 COUNTRY: AF
 YEAR: 1997
 CATEGORY [ New pulmonary smear-positive cases (not used after 2012) ]: 618
```
************************************

Test Case 2:

 python datafinder.py -cn AF -ds notification -ct new_sp

Output:
``` Console
 COUNTRY: AF
 CATEGORY [ New pulmonary smear-positive cases (not used after 2012) ]
 1980 : DNP
 1981 : DNP
 1982 : DNP
 1983 : DNP
 1984 : DNP
 1985 : DNP
 1986 : DNP
 1987 : DNP
 1988 : DNP
 1989 : DNP
 1990 : DNP
 1991 : DNP
 1992 : DNP
 1993 : DNP
 1994 : DNP
 1995 : DNP
 1996 : DNP
 1997 : 618
 1998 : 1833
 1999 : 1669
 2000 : 2892
 2001 : 4639
 2002 : 6509
 2003 : 6510
 2004 : 8273
 2005 : 9949
 2006 : 12468
 2007 : 13213
 2008 : 13136
 2009 : 12497
 2010 : 12947
 2011 : 13789
 2012 : 13319
 2013 : DNP
 2014 : DNP
```
