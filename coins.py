# name of student: Lukas Bellaart
# number of student: 99068241
# purpose of program: om wisselgeld terug te geven in de juiste hoeveelheid munten
# function of program: (toch hetzelfde als purpose?)
# structure of program: while loop om te kijken of change en coinValue groter dan 0 is, vervolgens uitrekenen hoeveel geld er teruggegeven moet worden

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

vijfhonderdcent = 0
driehonderdcent = 0
tweehonderdcent = 0
vijftigcent = 0
twintigcent = 0
tiencent = 0
vijfcent = 0
tweecent = 0
eencent = 0

if change > 0: #
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cent did you return? ')) #
      if coinValue == 500:
        vijfhonderdcent += nrCoinsReturned
      elif coinValue == 300:
        driehonderdcent += nrCoinsReturned
      elif coinValue == 200:
        tweehonderdcent += nrCoinsReturned
      elif coinValue == 50:
        vijfhonderdcent += nrCoinsReturned
      elif coinValue == 20:
        twintigcent += nrCoinsReturned
      elif coinValue == 10:
        tiencent += nrCoinsReturned
      elif coinValue == 5:
        vijfcent += nrCoinsReturned
      elif coinValue == 2:
        tweecent += nrCoinsReturned
      else:
        eencent += nrCoinsReturned

      change -= nrCoinsReturned * coinValue #

# comment on code below: 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
  print("Geld terug gegeven.")
  print(" ----------------------------------------------------")
  print("|  5 eurocenten          : "+str(vijfhonderdcent))
  print("|  3 eurocenten          : "+str(driehonderdcent))               
  print("|  2 eurocenten          : "+str(tweehonderdcent))   
  print("|  50 centen             : "+str(vijftigcent))    
  print("|  20 centen             : "+str(twintigcent))       
  print("|  10 centen             : "+str(tiencent))         
  print("|  5 centen             : "+str(vijfcent))     
  print("|  2 centen             : "+str(tweecent))           
  print("|  1 centen             : "+str(eencent))           
  print('----------------------------------------------------\n')       
else:
  print("Geld terug gegeven.")
  print(" ----------------------------------------------------")
  print("|  5 eurocenten          : "+str(vijfhonderdcent))
  print("|  3 eurocenten          : "+str(driehonderdcent))               
  print("|  2 eurocenten          : "+str(tweehonderdcent))   
  print("|  50 centen             : "+str(vijftigcent))    
  print("|  20 centen             : "+str(twintigcent))       
  print("|  10 centen             : "+str(tiencent))         
  print("|  5 centen             : "+str(vijfcent))     
  print("|  2 centen             : "+str(tweecent))           
  print("|  1 centen             : "+str(eencent))           
  print('----------------------------------------------------\n')  
  print('done')