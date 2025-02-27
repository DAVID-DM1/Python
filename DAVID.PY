# Importing the mathematical constant pi for circle calculations
from math import pi

def menu():
    print("\nSelect an option:")
    print("1. Calculate area and circumference of a circle")
    print("2. Calculate area and perimeter of a triangle")
    print("3. Calculate area and perimeter of a rectangle")
    print("4. Exit")

def main():
    running = True
    while running:
        menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice == 1:
                # Circle calculations
                radius = float(input("Enter the radius of the circle: "))
                area = pi * radius ** 2  # Area formula: πr²
                circumference = 2 * pi * radius  # Circumference formula: 2πr
                print(f"Area: {area:.2f}, Circumference: {circumference:.2f}")
            
            elif choice == 2:
                # Triangle calculations
                base = float(input("Enter the base length of the triangle: "))
                height = float(input("Enter the height of the triangle: "))
                hypotenuse = float(input("Enter the hypotenuse of the triangle: "))
                area = 0.5 * base * height  # Area formula: (1/2) * base * height
                perimeter = base + height + hypotenuse  # Perimeter formula: sum of all sides
                print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")
            
            elif choice == 3:
                # Rectangle calculations
                width = float(input("Enter the width of the rectangle: "))
                length = float(input("Enter the length of the rectangle: "))
                area = width * length  # Area formula: width * length
                perimeter = 2 * (width + length)  # Perimeter formula: 2(width + length)
                print(f"Area: {area:.2f}, Perimeter: {perimeter:.2f}")
            
            elif choice == 4:
                # Exit the program
                print("Exiting proram... bye!")
                running = False
            
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
