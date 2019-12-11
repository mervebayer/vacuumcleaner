import nltk

nltk.download('punkt')
        

commands = "Suck. Move right. Move left. Do nothing."
        
tokenized_commands = nltk.sent_tokenize(commands)
        
        #for commands in tokenized_commands:
         #   print(commands)
            
            
def cleaning_agent(location, statusA, statusB):
    score=0
    if location == 'A':
        if statusA == 'Dirty':
            print('Suck.')
            statusA = 'Clean'
            score +=2
            print(score)
            print('Move right.')
            score -=1
            print(score)
            location='B'

            if statusB=='Dirty':
                print('Suck.')
                statusB = 'Clean'
                score +=2
                print(score)
                print('Do nothing.')

            elif statusB=='Clean':
                print('Do nothing.')
        else:
            location='B'
            score-=1
            print("Go right.")
            print(score)
                    
            if statusB=='Dirty':
                print('Suck')
                score+=2
                print(score)
                statusB='Clean'
                print("Do nothing.")
            
    elif location=='B':
        if statusB == 'Dirty':
            print('Suck.')
            score +=2
            print(score)
            statusB = 'Clean'
            print('Move left.')
            score -=1
            print(score)
            statusB = 'Clean'
            location = 'A'
            if statusA=='Dirty':
                print('Suck')
                score+=2
                print(score)
                statusA='Clean'
                print("Do nothing.")
            elif statusA=='Clean':
                print('Do nothing.')
                
        else:
            location= 'A'
            print('Move Left.')
            score-=1
            print(score)
            
            if statusA=='Dirty':
                print('Suck.')
                score+=2
                print(score)
                statusA= 'Clean'
                print('Do nothing.')
                
                    
    return location,statusA, statusB, score
        
        
for commands in tokenized_commands:
           
    #cleaning_agent('A' , 'Clean' ,'Dirty')
    #cleaning_agent('A' , 'Dirty' ,'Clean')
    #cleaning_agent('B' , 'Clean' ,'Dirty')
    #cleaning_agent('B' , 'Dirty' ,'Clean') 
    #cleaning_agent('A' , 'Dirty' ,'Dirty')          
    cleaning_agent('B' , 'Dirty' ,'Dirty')       
                    
                