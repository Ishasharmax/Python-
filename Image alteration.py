'''
Name: Isha Sharma
Date: 12/11/17
Purpose: Create a program that prompts a user to enter an image name for a P3
PPM image that is located in the same directory as the program. The program will then prompt
the user to choose between a minimum of 5 options
'''
def readPPM(filename):
    '''
    Purpose: This functions reads a P3 PPM and returns a list of lists of lists
    containting pixel values. The lists are y, x, and c where c is color channel
    0 for red
    1 for green
    2 for blue
    Args: image name
    Return: 3D list of pixels in [y][x][c] format
    '''
    f = open(filename,"r")
    lines = f.readlines()

    type=lines[0]
    if lines[1][0]=="#":
        offset=1
    else:
        offset=0
    size=lines[1+offset].split()

    width=int(size[0])
    height=int(size[1])
    print("width=",width," height=",height)
    
    depth=int(lines[2+offset])

    print ("Work in progress...please wait")

    image=[]
    row=[]
    allValues=[]
    for i in range(3+offset,len(lines)):
        temp = lines[i].split()
        for j in range(len(temp)):
            allValues.append(int(temp[j]))
    pixel=[]
    for x in range(len(allValues)):
        pixel.append(int(allValues[x]))
        if (len(pixel)==3):
            row.append(pixel)
            pixel=[]
            if (len(row)%width==0):
                image.append(row)
                row=[]
    f.close()
    return image

def writePPM(filename,image):
    '''
    Purpose: This functions takes a ppm image stored in the format of a 3D list [y][x][c] where
    c is color channel
    0 for red
    1 for green
    2 for blue
    and writes a plain text P3 style PPM image under the name filename
    Args: image name, image data
    Return: none
    '''
    height=len(image)
    width=len(image[0])
    
    f = open(filename,"w")
    f.write("P3\n")
    f.write(str(width)+" "+str(height)+"\n")
    f.write("255\n")
    for y in range(len(image)):
        for x in range(len(image[y])):
            for c in range(len(image[y][x])):
                f.write(str(image[y][x][c])+" ")
            f.write("\n")

    f.close()


    
def userInputOption(options):
    '''
    Purpose: give user options
    Args: image
    Returns: option 1, option 2, or option 3
    '''
    print("Here are your options:")
    for x in range(len(options)):
        print("option:",x+1,options[x])
    choice=input("choose an option:")
    if(choice=="1" or choice=="hopeify"):
        return choice
    elif(choice=="2" or choice=="flip"):
        return choice
    elif(choice=="3" or choice== "checkerboard"):
        return choice
    elif(choice=="4" or choice=="save"):
        return choice
    else:
        print("not an option")
        choice=input("choose an option:")

        
def hopeify(image):
    '''
    Purpose: convert image into 4 colors based on the brightness
    Args: an image
    Returns: color moderation of the image in four colours
    '''
    image2=[]
    print ("Work in progress....")
    for y in range(len(image)):
        row=[]
        for x in range(len(image[y])):
            pixel=[0,0,0]
            if(image[y][x][1]>250):
                pixel=[255,255,255]
            elif (image[y][x][1]>238):
                pixel=[72,61,139]
            elif (image[y][x][1]>173):
                pixel=[173,216,230]
            elif (image[y][x][1]>104):
                pixel=[220,220,220]
            else:
                pixel=[235,10,55]
            row.append(pixel)
        image2.append(row)
    print ("Image altered")
    return image2
                               
def flip(image):
    '''
    Purpose:Flip the image horizontally so that it is a mirror image of itself
    Args: an image
    Returns: horizontal flip of image
    '''
    print ("Work in progress....")
    width=len(image)
    height=len(image[0])
    newPic=[]
    for x in range(width):
        row=[]
        for y in range(height):
            pixel=[]
            for i in range(3):
                pixel.append(image[x][(height-1)-y][i])
            row.append(pixel)
        newPic.append(row)
    print ("Image altered")
    return newPic

def invertPixel(image):
    newIm=image
    out=[0,0,0]
    newIm[0]=255-newIm[0]
    newIm[1]=255-newIm[1]
    newIm[2]=255-newIm[2]
    return newIm

def checkerboard(height, width, image):
    '''
    Purpose: Turns  the image into a 10x10 checkerboard of itself where light squares are the original image and dark squares are the image inverted
    Args: an image
    Returns: checkerboard of the image entered
    '''
    print ("Work in progress....")
    height=len(image)
    width=len(image[0])

    bool=True
    row=0

    for x in range(width):
        row+=1
        for y in range(height):
            if bool==True:
                image[y][x]=invertPixel(image[y][x])
            for z in range(11):
                if (y>height/10*z):
                    image[y][x]=invertPixel(image[y][x])
        if (row>width/10):
            bool=not(bool)
            row=0
        newImage=image
    print ("Image altered")
    return newImage
                
    
def save(image):
    '''
    Purpose:saves the converted image
    Args: return from checkerboard function
    Returns: saved file of image
    '''
    name=input("what would like to name your file? (SAVE WITH PPM EXTENSION):")
    return writePPM(name,image)
    
def main():
    '''
    Purpose: runs the program
    Args: none
    Returns: none
    '''
    image=input("Enter the image: ")
    print ("Dimensions of the image are:")
    image=readPPM(image)
    height=len(image)
    width=len(image[0])
    print ("Options are :'hopeify','flip','checkerboard','save','Quite'")
    choice=input("What you want to do?")
    while(choice!="done"):
        if (choice=="hopeify"):
            work=hopeify(image)
            writePPM("imagetest.ppm",work)
            savingImage=input("Do you want to save this image?(Yes/No): ")
            if savingImage=="Yes":
                save(hopeify(image))
                print ("file saved!")
                return savingImage
            else:
                choice=input("What you want to do next?: 'hopeify','flip','checkerboard','save','Quite'")
        elif (choice=="checkerboard"):
            work=checkerboard(height, width, image)
            writePPM("imagetest.ppm",work)
            savingImage=input("Do you want to save this image?(Yes/No): ")
            if savingImage=="Yes":
                save(hopeify(image))
                print ("file saved!")
                return savingImage
            else:
                choice=input("What you want to do next?: 'hopeify','flip','checkerboard','save','Quite'")
        elif (choice=="flip"):
            work=flip(image)
            writePPM("imagetest.ppm",work)
            savingImage=input("Do you want to save this image?(Yes/No): ")
            if savingImage=="Yes":
                save(hopeify(image))
                print ("file saved")
                return savingImage
            else:
                choice=input("What you want to do next?: 'hopeify','flip','checkerboard','save','Quite'")
        elif (choice=="save"):
            save(image)
            if done=="Yes":
                print ("file saved!")
                choice=input("What you want to do next?: 'hopeify','flip','checkerboard','save','Quite'")
    while (choice=="Quite"):
        save(image)
        print ("Conversion ended")       
main()

