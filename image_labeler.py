import cv2, os

# Create initial window
cv2.namedWindow("image_labeler")
i = -1 #number of image

# We need to get all the paths for the images to later load them
imagepaths = []
files = os.listdir() # Lists files in workspace
for f in files:
  if f.endswith("png"): #We want only the images
    imagepaths.append(f)

for path in imagepaths:
    i += 1
    img = cv2.imread(path, 0)
    cv2.imshow("image_labeler", img)

    k = chr(cv2.waitKey())
    if k == 'y':
        cv2.imwrite("Crater"+str(i)+".png", img)
        print("Crater")
    elif k == 'n':
        cv2.imwrite("NoCrater"+str(i)+".png", img)
        print("No Crater")
    elif k == 'q':
        print("Exiting")
        break

cv2.destroyAllWindows()