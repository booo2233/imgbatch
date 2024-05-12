import os
import subprocess


def mp4_mov_fun():
    mp4_files = None
    break0 = 0
    while True:
        path = input(r"input the path to mp4 video example--->C:\my_mp4_video:")
        try:
          os.chdir(path)
        
        except FileNotFoundError:
           print("====Invalid-path-try-again======")
           continue
        except OSError:
           print("====Invalid-path-try-again======")
           continue
        
        else:
           for i, files in enumerate(os.listdir()):
              if files.endswith(".mp4"):
                     mp4_files = files
                     ffmpeg_com = [
                         "ffmpeg",
                         "-i",
                         mp4_files,
                         "-c:v",
                         "h264_cuvid",
                         "-b:v",
                         "1M",
                         f"mov{i}.mov"     
                     ] 
                     try:
                      subprocess.run(ffmpeg_com, check=True)
                     except Exception as e:
                        print(f"oops Let's try again error--->{e}")
                        continue
                     else:
                        print("Success👌👌👌")
                        break0+=1
                     
        if break0 > 0:
           
           break
           

