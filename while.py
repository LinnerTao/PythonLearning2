numbers=[12,14,324,534,34,45]
event=[]
odd=[]
while len(numbers)>0:
    number=numbers.pop()
    if(number%2==0):
        event.append(number)

    else:
        odd.append(number)
i=0
while(i<len(event)):
    print('the event is:',event.pop())