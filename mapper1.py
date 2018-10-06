#!/usr/bin/env python
#Be sure the indentation is identical and also be sure the line above this is on the first line
 
import sys
import re
 
def main(argv):
  header = sys.stdin.readline() # skip header line
  line = sys.stdin.readline()
  
  while line:
        
    transactionMetrics = line.split(',')
	
	#variables list
	invoiceNo = str(transactionMetrics[0])
	country = str(transactionMetrics[7]])
	customerID = str(transactionMetrics[6])
	unitPrice = float(transactionMetrics[5])
	invoiceDate = str(transactionMetrics[4])
	quantity = float(transactionMetrics[3])
	
	#stripping month out of date and setting up as two digit presentation
	invoiceDate = invoiceDate.split('/')
	invoiceMonth = invoiceDate[0]
	
	#determining total transaction purchase amount
	purchaseAmount = unitPrice * quantity
	
	if len(invoiceMonth) == 1:
	  invoiceMonth = '0' + invoiceMonth
	
	if ((invoiceNo[0] == 'c') or (customerID == '')):
	  pass
	else:
	  print(invoiceMonth + "," +  country + ":" + customerID + "\t" +purchaseAmount)
	
	line = sys.stdin.readline()
#Note there are two underscores around name and main
if __name__ == "__main__":
  main(sys.argv)
