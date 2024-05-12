from app.mp4_mov import *
from app.mov_mp4 import *
from app.avi_mp4 import *
while True:
    input_output = input("Input to output format(syntax-->.mp4_.mov) or q to quit:")
    
    if input_output == ".mp4_.mov":
       mp4_mov_fun()
    elif input_output == ".mov_.mp4":
       mov_mp4_fun()
    elif input_output == ".avi_.mp4":
       mov_mp4_fun()      
    elif input_output == "q":
       quit()   
    else:
        print("Invalid input try again")
        continue