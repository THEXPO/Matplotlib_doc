import matplotlib.pyplot as plt

x = [1,5,3,7,3,7,5,2,9,6]
y = [10,20,30,40,50,60,70,80,90,100]

#matplotlib styles

#Colors

#Basic short code→ 'r' (red), 'g' (green), 'b' (blue), 'k' (black), 'y' (yellow), 'm' (magenta), 'c' (cyan), 'w' (white).
#Full names → "red", "blue", "orange", etc.
#Hex codes → "#FF5733"
#RGB tuples → (0.1, 0.5, 0.8)

plt.plot(x, y, color="purple")
plt.show()

#Line Styles

#'-' → solid
#'--' → dashed
#'-.' → dash-dot
#':' → dotted

plt.plot(x, y, linestyle="--")
plt.show()

#Markers

#'o' → circle
#'s' → square
#'^' → triangle up
#'x' → X marker
#'*' → star

plt.plot(x, y, marker="x")
plt.show()

#Combining Styles

plt.plot(x, y, "ro--")  # r for red, o for circle, -- for dashed
plt.show()