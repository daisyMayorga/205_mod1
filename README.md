# 205_mod1

CST 205 Module 1 Team Lab.

Here is the assignment:

Warm Up
Take the code to reduce the red in an image by half and turn it into a function in the program area of JES. Name this function halfRed.
Write a new function called noBlue that removes all of the blue from an image.


Problem 1:
Write a new function called lessRed. This should work a lot like halfRed, but it should take a parameter that gives the percentage by which to reduce the red in the picture. So, for example, the function call lessRed(75) would cause the function to reduce the red in the image by 75%
Rewrite halfRed so that it calls lessRed to do the red reduction for the image.

Problem 2:
No write a function called moreRed that increases the red in each pixel of an image the same way that lessRed decreased red. What might be a potential problem with increasing the red in a pixel? How could you mitigate this issue? Can you tell what JES is doing?

Problem 3:
They say that people who have an overly optimistic outlook on life are seeing things "through rose colored glasses".

Write a function called roseColoredGlasses that makes an image look pink. Think about how you can manipulate the RGB components of each pixel to accomplish this.

Problem 4:
JES has a function called makeLighter that will lighten a color. It takes a color as a parameter and returns the lightened version of that color. This means that if my function call looks like this:

newColor = makeLighter(oldColor)

newColor will contain the lightened version of oldColor

Write a function called lightenUp that uses a for loop to lighten each pixel in a picture. Remember that you can use getColor and setColor to access the color of a pixel

Problem 5:
When I was your age, our phones were connected to our walls and we had to take pictures with this stuff called film. Believe it or not, you would have to take your film to a special place to get developed and wait to get your pictures back. It was pretty barbaric. Anyway, when your film was developed, you got back negatives. These negatives were used to make the prints of your pictures by shining light through them onto special photo paper. That meant that what was on the negative was actually the exact opposite of what would print on the paper (darker parts of the negative would block more light and the resulting part of the picture would be lighter).

Write a function called makeNegative that creates the negative of an original picture. This means you will want to create the opposite value for the red, green and blue of that pixel. How might you get the opposite?
Remember that for each or R, G, and B, the range of acceptable values is 0 to 255
That means the opposite of 0 is 255 and the opposite of 255 is 0
What about for a value in the middle? How might you get the opposite?
Remember that you will need to separately get the opposite for the R, G, and B values

Problem 6:
When your grandparents were your age, not only did they have to use a film camera, they couldn't even get pictures in color. That's right, black and white isn't just a fancy setting on Instagram - it used to be the ONLY way to get pictures. You can simulate a black and white image by converting your color image to gray-scale. It turns out that gray colors occur when the R G and B values for a pixel are all the same. e.g. 0, 0, 0 or 1, 1, 1 ... and so on. To go from a color image to a black and white image, you want to capture the intensity or luminance of a pixel. A rough estimate of luminance is the average of the R, G, and B values for a pixel.

Create a function called BnW that converts each pixel to gray-scale by computing the average of the R G and B values for each pixel and then using that average as the new RGB values for that pixel.
What do you think of the resulting image?
It turns out that to make a really good black and white image, you actually want to weight each of the RG and B slightly differently to account for how the human eye sees each color differently. A better formula for luminace is: R*0.299 + G*0.587 + B*0.114
Write a new function called betterBnW that uses the formula above to convert each pixel to gray-scale.
CHECKPOINT: When you have completely finished with all of the steps of the lab, save your work and submit it in the Assignments section for Lab #3 in text format. I'll want to see all the functions from warm up through problem 6 in one file.

Last modified: Tuesday, 20 December 2016, 1:03 PM
