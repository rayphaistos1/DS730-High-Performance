#!/usr/bin/env python
#Be sure the indentation is correct and also be sure the line above this is on the first line
 
import sys
 
def main(argv):
  
  #Testing off of Jordanias Minicomp
  
  #create dictionary storing the month, country, and customer ID as the collective key value, and the purchance Amount currently being read in
  MCI_Dict = {}
  
  #create dictionary storing the highest purchaseTally for a given month and country combination
  MCSaleDict = {}
  
  for line in sys.stdin:
    line = line.strip()
    monthCountryID, purchaseAmount = line.split('\t', 1)
    monthCountry, customerID = monthCountryID.split(':',1)
	month, country = monthCountry.split(',',1)
	
	month
	
	purchaseAmount= float(purchaseAmount)
    
	
	#update key value pairs as neceessary given current line read in
	
	if monthCountryID in MCI_Dict:
	  MCI_Dict[monthCountryID] += purchaseAmount
	  purchaseTally = MCI_Dict[monthCountryID]
	else:
	  MCI_Dict.update({monthCountryID : purchaseAmount}]
	  purchaseTally = MCI_Dict[monthCountryID]
	  
	  
	# maintain record of the highest expenditure tally for a month and country combination. If the current customer tally is the highest, print the monthCountryID
	
	if monthCountry in MCSaleDict:
	  if purchaseTally > MCSaleDict[monthCountry]:
	    
		######## Needs to add the customer ID as well
		customerIDStackStack = ":" + customerID
		MCSaleDict[monthCountry] = [purchaseTally, customerIDStack]
		
	  else if  purchaseTally == MCSaleDict[monthCountry]:
	    MCSaleDict[monthCountry] = MCSaleDict[monthCountry] + "," + customerID
		MCI_Dict.update({monthCountryID : purchaseAmount}]
		highpurchase = MCI_Dict[monthCountryID]  
		
		print(    key and value   )
	else:
	  MCI_Dict.update({monthCountryID : purchaseAmount}]
	  
	
	
	
	
	
	
	#where I left off, I am sleepy
	
      if current_customerMonth:
        print('%s\t%s' % (current_word, current_count))
      current_count = count
      current_word = word
  if current_word == word:
    print('%s\t%s' % (current_word, current_count))

#Note there are two underscores around name and main
if __name__ == "__main__":
  main(sys.argv)
