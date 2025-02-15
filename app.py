import turtle
import cv2
import numpy as np

# Ask the user for two image file paths
image1_path = input("Enter the first image file name (e.g., image1.png): ")
image2_path = input("Enter the second image file name (e.g., image2.png): ")

# Load and process the first image
image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
image1 = cv2.resize(image1, (500, 500))  # Resize for better clarity
image1 = cv2.adaptiveThreshold(image1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)
contours1, _ = cv2.findContours(image1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Load and process the second image
image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)
image2 = cv2.resize(image2, (500, 500))  # Resize for better clarity
image2 = cv2.adaptiveThreshold(image2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)
contours2, _ = cv2.findContours(image2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Set up Turtle
screen = turtle.Screen()
screen.bgcolor("white")  # Keep background white
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("black")

# Function to draw contours with Turtle
def draw_contour(contour, shift_x):
    t.penup()
    first_point = contour[0][0]
    t.goto(first_point[0] - 300 + shift_x, 250 - first_point[1])  # Adjust position to center and shift
    t.pendown()
    
    for point in contour:
        x, y = point[0]
        t.goto(x - 300 + shift_x, 250 - y)

# Draw the first image on the left (-300 shift)
for contour in contours1:
    draw_contour(contour, -300)

# Draw the second image on the right (+300 shift)
for contour in contours2:
    draw_contour(contour, 300)

t.hideturtle()
turtle.done()
