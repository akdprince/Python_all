#calling an external module from another module

# import myModule
# myModule.hello_anik("Anik Kumar Das")
# myModule.bye_anik("Wrishab Kumar Das")

#import/User specific part of code from another module

from myModule import person1
print(person1["name"], person1["age"])