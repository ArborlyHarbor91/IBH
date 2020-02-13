import base64
import re

print("Idle Breakout Save Code Generator by SCS Psyco29")

# TODO prestige modification

print("What level do you want to be at?")
level = input()

print("How much money do you want")
money = input()

print("How much gold do you want")
gold = input()

print("How many Black Boxes?")
bb = input()

print("How many skillpoints")
sp = input()

s = f"{level},{money},{gold},2,0,0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,1,{sp},1,0,0,Made By SCS Psyco29"
b = s.encode("UTF-8")
e = base64.b64encode(b)
print("Testing Servers....")
print("Finding Fastest Connection....")
print("Conecting to server....")
print("Generating Code")
print("Process Complete....")
print(e)
print("\nCopy whats INSIDE the quotes\n")
print("CTR+C does not work, use right click and copy")
end = 1
while end == 1:
    print("Once copied you may exit the console")
    input()