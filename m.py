x = input().strip()
if x.isdigit():
    print("IS DIGIT")
else:
  print("ALPHA")
  if x.isupper():
     print("IS CAPITAL")
  else:
     print("IS SMALL")      