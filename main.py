import turtle
import cv2
import numpy as np

# Prompt user to input image filename
image_path = input("Enter the image file name (with extension, e.g., image.png): ")  

# Load the image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, (500, 500))  # Resize for better clarity

# Apply Adaptive Threshold to keep black regions
image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)

# Find contours of black regions
contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Set up Turtle
screen = turtle.Screen()
screen.bgcolor("white")  # Keep background white
t = turtle.Turtle()
t.speed(0)
t.pensize(2)
t.color("black")

# Function to draw contours with Turtle
def draw_contour(contour):
    t.penup()
    first_point = contour[0][0]
    t.goto(first_point[0] - 250, 250 - first_point[1])  # Adjust position to center
    t.pendown()
    
    for point in contour:
        x, y = point[0]
        t.goto(x - 250, 250 - y)

# Draw each contour (keeping necessary black areas)
for contour in contours:
    draw_contour(contour)

t.hideturtle()
turtle.done()
