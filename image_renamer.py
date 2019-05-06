import os 

# Use a big number on the first run, so it doesn't conflict
# Then run it again with 0
i = 0
j = 0

# We need to get all the paths for the images to later load them
imagepaths = []
files = os.listdir(".") # Lists files in workspace
for f in files:
  if f.endswith("png"): #We want only the images
    imagepaths.append(f)

print(imagepaths)

for path in imagepaths:
    if path[:6] == "Crater":
        try:
            os.rename("./" + path, "./" + "Crater" + str(i) + ".png")
            i += 1
        except:
            i += 1
    else:
        try:
            os.rename("./" + path, "./" + "NoCrater" + str(j) + ".png")
            j += 1
        except:
            j += 1