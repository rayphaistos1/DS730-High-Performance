#!/usr/bin/env python
#Be sure the indentation is correct and also be sure the line above this is on the first line
 
import sys
 
def main(argv):
  
  #create dictionary storing the month, country, and customer ID as the collective key value, and the purchance Amount currently being read in
  MCI_Dict = {}
  
  #create dictionary storing the highest purchaseTally for a given month and country combination
  MCSaleDict = {}
  
  for line in sys.stdin:
    line = line.strip()
    monthCountryID, purchaseAmount = line.split('\t', 1)
    monthCountry, customerID = monthCountryID.split(':',1)
	month, country = monthCountry.split(',',1)
	purchaseAmount= float(purchaseAmount)
    
	
	# update key value pairs for the unique month-country-customerID key and the total purchaseTally for that customer for that country for that month as the value. If the key is not in the dictionary
	# it is added, and initialized with the current line read in amount
	
	if monthCountryID in MCI_Dict:
	  MCI_Dict[monthCountryID] += purchaseAmount
	else:
	  MCI_Dict.update({monthCountryID : purchaseAmount})
	
	# assign value for the current tally amount for that unique Customer ID for that unique month-country combination
	purchaseTally = MCI_Dict[monthCountryID]
	  
	# updating dictionary that tracks the months for each country as the key, and the high expenditure amount.  Once the key-value pair has been updated, if the list of customer ID's with the highest expenditure amount
	# for that pair has changed, it is printed out. This results in a 'rolling basis' updating and printing of the highest spenders for each month and country combination. 
	
	
	
	if monthCountry in MCSaleDict:
	
	  rawHighInfo = MCSaleDict[monthCountry]
	  highExpenditureAmount, previousID = rawhighInfo.split(':',1)
	  highExpenditureAmount = float(highExpenditureAmount)
	  
	  if purchaseTally >  highExpenditureAmount:
		highAmountWithCustomerIDs = str(purchaseTally) + ":" + customerID
		MCSaleDict[monthCountry] = [highAmountWithCustomerIDs]
		print(month, ",", country, ":", customerID))
	  else if  purchaseTally ==  highExpenditureAmount:
	    MCSaleDict[monthCountry] = MCSaleDict[monthCountry] + "," + customerID
		listedID = previousID + ',' + customerID
	    print(month, ",", country, ":", listedID))
	else:
	  highAmountWithCustomerIDs = str(purchaseTally) + ":" + customerID
	  MCSaleDict.update({monthCountryID : highAmountWithCustomerIDs})
	  print(month, ",", country, ":", customerID))
	  
	
#Note there are two underscores around name and main
if __name__ == "__main__":
  main(sys.argv)
