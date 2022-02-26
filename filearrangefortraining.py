#if not loop p225 direct
#make direct
#add p225 voice
# import shutil
# import os
# directory = "."
# for i in range(225,377):
# 	if not os.path.exists("/"+i):
# 		os.makedirs("/"+i)
# 	for filename in os.scandir(directory):
#          if filename.is_file():
#             print(filename.path)
#         # print(str(file))
#         # speaker = file.split("_")[1] == i
#         # if speaker == i:
#         #     source = "."
#         #     destination = "i"
#         #     shutil.move(source,destination)

#     for filename in os.listdir(directory):
#         f = os.path.join(directory, filename)
#     # checking if it is a file
#         if os.path.isfile(f):
#             print(f.split("_")[1])



# #if not loop p225 direct
# #make direct
# #add p225 voice
# # import shutil
# # import os
# # for i in range(225,377):
# # 	if not os.path.exists('p'+ str(i)):
# # 		os.makedirs('p'+ str(i))
# # 	path = os.walk(".")
# # 	for root, directories, files in path:
# # 		for file in files:         
# # 			speaker = file.split("_")[1] == i
# # 			if speaker == i:
# # 				source = "."
# # 				destination = "i"
# # 				shutil.move(source,destination)

import shutil
import os
directory = "."

for i in range(225,377):
	if not os.path.exists('p'+ str(i)):
		os.makedirs('p'+ str(i))
	# for filename in os.scandir(directory):
    #      if filename.is_file():
    #         print(str(filename).split("_"))
            # speaker = filename.path.split("_")[1]
            # if speaker == i:
            #    source = "."
            #    destination = "i"
            #    shutil.move(source,destination)
	for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
        # checking if it is a file
            if os.path.isfile(f):
                print(f[18:22])
                speaker=str(f[18:22])
                if speaker == i:   
                    source = str(speaker)+".npy"             
                    destination = str(speaker)+"/"+str(speaker)+".npy"    
                    shutil.move(source,destination)