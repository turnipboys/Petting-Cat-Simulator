# Dazzling Robot 7/9
# This is a program that simulates petting a cat :)

speed = 2.5
x = 0.0
y = 0.0
xCat = 0.0
yCat = 0.0

# Hidden button variables
rectX = 400.0
rectY = 100.0
rectW = 500
rectH = 500

font = None

def setup():
    global catImg, handImg, handImgRotate, pupil1Img, pupil2Img, purrImg1, purrImg2, x, y, xCat, yCat, font, rectX, rectY, rectW, rectH
    size(1280, 720) # canvas size
    
    # This is for the wiggling animation later
    x = width/2
    y = height/2
    
    # This takes the measurement of the canvas size and halves it
    # Keeps cat centered on canvas
    xCat = width/2
    yCat = height/2
    
    # All of the image files I'm loading in
    catImg = loadImage("cat.png") 
    handImg = loadImage("hand.png")
    handImgRotate = loadImage("hand2.png")
    pupil1Img = loadImage("pupil 1.png")
    pupil2Img = loadImage("pupil 2.png")
    purrImg1 = loadImage("catPurr1.png")
    purrImg2 = loadImage("catPurr2.png")
    
    font = createFont("Another Danger.otf", 60) # Import font & set font size
    textFont(font)
    
def draw():
    global x, y, rectX, rectY, rectW, rectH
    background(0, 153, 204) # blue background color
    
    textSize(60) # sets font size
    
    timerHand = millis()/500 # counting time for the hand animation
    timerHand = timerHand%2
    
    timerPurr = millis()/1000
    timerPurr = timerPurr%2
    
    imageMode(CENTER) # This will center the images
    
    if mouseX > rectX and mouseX < rectX+rectW and mouseY > rectY and mouseY < rectY+rectH:
        if mousePressed == True: # When mouse is pressed
            # Purring text
            fill(255) # white color
            text("purr", x-300, y-200)
            text("purr", x+300, y+300)
            text("purr", x-200, y+150)
            
            # Wiggling animation
            x += random(-speed, speed)
            y += random(-speed, speed)
            x = constrain(x, 0, width)
            y = constrain(y, 0, height)
            
            # Cat meowing animation
            if timerPurr == 0:
                image(purrImg1, x, y, 400, 400) # cat closes mouth
            else:
                image(purrImg2, x, y, 400, 400) # cat opens mouth
                textSize(30)
                text("meow", x+200, y+200)
            
            # Hand petting animation
            if timerHand == 0: # If an even amount of seconds have passed
                image(handImgRotate, mouseX, mouseY, 200, 200)
            else:
                image(handImg, mouseX, mouseY, 200, 200)
        else:
            image(catImg, xCat, yCat, 400, 400) # Draws cat image
            
            # Eyes that follow the mouse. I took this from Jesse :P
            pushMatrix()
            mx1 = map(mouseX, 0, width, 250, 285)
            my1 = map(mouseY, 0, height, 390, 405)
            translate(mx1, my1)
            image(pupil1Img, 300, -50, 50, 50) # left pupil
            image(pupil2Img, 450, -50, 50, 50) # right pupil
            popMatrix()
            
            image(handImg, mouseX, mouseY, 200, 200) # This is the hand attached to cursor
                
    else:
        image(catImg, xCat, yCat, 400, 400) # Draws cat image
        
        # Eyes that follow the mouse. I took this from Jesse :P
        pushMatrix()
        mx1 = map(mouseX, 0, width, 250, 285)
        my1 = map(mouseY, 0, height, 390, 405)
        translate(mx1, my1)
        image(pupil1Img, 300, -50, 50, 50) # left pupil
        image(pupil2Img, 450, -50, 50, 50) # right pupil
        popMatrix()
            
        image(handImg, mouseX, mouseY, 200, 200) # This is the hand attached to cursor
    
    # Invisible button that determines if you are touching cat or not so you can pet it
    noStroke()
    noFill()
    rect(rectX, rectY, rectW, rectH)
