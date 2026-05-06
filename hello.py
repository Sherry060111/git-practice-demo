try:    
  name=input("What is your name?")
  print(f"Hello,{name}!")
except Exception as e:
  print ("出错了："，e)  