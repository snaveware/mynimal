from ast import Try
import os, sys
from PIL import Image

size = [300,300]
format = "JPEG"

if (sys.argv[1].strip() == 'help') or (sys.argv[1].strip() == 'h') :
    help = """
 ----- Help -----
 Argument 1: Path to the folder containing images (Required)
 Argument 2: Width of the output images (Optional, Default = 300)
 Argument 3: Height of the output images (Optional, Default = 300)
 Argument 4: Format (optional, Default= PNG)
 """

    print(help)
    os._exit(0)

dir = sys.argv[1]

if len(sys.argv) >= 4 :
    size[0] = int(sys.argv[2])
    size[1] = int(sys.argv[3])

if len(sys.argv) >= 5 :
    format = sys.argv[4].upper()

if not os.path.exists(dir) :
    print(' Error: The directory does not exist \n')
    os._exit(1)

files = os.listdir(dir)
filesWithErrors = []
if len(files) <1 : 
    print('Error: the directory is empty \n')
    os._exit(1)


print('\n Working...\n')
outDir = dir + "_"+str(size[0])+"X"+str(size[1])

if(not os.path.exists(outDir)) :
    os.mkdir(outDir)

for infile in files :
    path = dir +'/'+ infile
    

    outfile = outDir + "/"+ os.path.splitext(infile)[0] +'_'+ str(size[0]) +"X"+ str(size[1]) +"."+ format.lower() 
    
    if (path != outfile) and (path.endswith(('png','jpg','gif','jfif','jpeg','PNG','JPG','JPEG','GIF'))):
        try:
            with Image.open(path) as im:
                im = im.convert('RGB')
                im.thumbnail(tuple(size))
                im.save(outfile, format)
        except OSError:
            errorMessage = "Error creating " + str(size[0]) + "X" + str(size[1]) + " image for " + infile + '\n'
            print(errorMessage)
            filesWithErrors.append((path,outfile))

if len(filesWithErrors) < 1 :
    print('\n All Good🥱 \n') 
else:
    for file in filesWithErrors :
        with Image.open(file[0]) as im:
            im = im.convert('RGB')
            im.thumbnail(tuple(size))
            im.save(file[1], format)