'''
Have the function StringCalculate(str) take the str parameter being passed and evaluate the mathematical expression within in. 
The double asterisks (**) represent exponentiation.
For example, if str were "(2+(3-1)*3)**3" the output should be 512. Another example: if str is "(2-0)(6/2)" the output should be 6. 
There can be parenthesis within the string so you must evaluate it properly according to the rules of arithmetic. 
The string will contain the operators: +, -, /, *, (, ), and **. If you have a string like this: #/#*# or #+#(#)/#, then evaluate from left to right. 
So divide then multiply, and for the second one multiply, divide, then add. The evaluations will be such that there will not be any decimal operations, 
so you do not need to account for rounding.
'''

def StringCalculate(strParam):
  s = []
  for i in range(len(strParam)-1):
    if strParam[i] == ')' and strParam[i+1] == '(':
      s.append(strParam[i])
      s.append('*') 

    elif (strParam[i]).isdigit() == True and strParam[i+1] == '(':
      s.append(strParam[i])
      s.append('*') 


    else:
      s.append(strParam[i])
    

  
  s.append(strParam[-1])
  strParam = ''.join(s)

  
  return int(eval(strParam))

# keep this function call here 
print(StringCalculate(input()))
