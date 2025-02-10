import random
import tkinter as tk
from tkinter import messagebox

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = None
        self.y = None

    def __repr__(self):
        return f"Rectangle({self.width}x{self.height} @ ({self.x}, {self.y}))"

class Plate:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rectangles = []

    def add_rectangle(self, rect):
        # Find the best position for the rectangle
        best_x, best_y = 0, 0
        placed = False

        while not placed:
            # Check if the rectangle fits at (best_x, best_y)
            if (best_x + rect.width <= self.width and
                best_y + rect.height <= self.height):
                # Check for collisions with existing rectangles
                collision = False
                for existing_rect in self.rectangles:
                    if (best_x < existing_rect.x + existing_rect.width and
                        best_x + rect.width > existing_rect.x and
                        best_y < existing_rect.y + existing_rect.height and
                        best_y + rect.height > existing_rect.y):
                        collision = True
                        break

                if not collision:
                    # Place the rectangle
                    rect.x = best_x
                    rect.y = best_y
                    self.rectangles.append(rect)
                    placed = True
                else:
                    # Move to the right
                    best_x += 1
            else:
                # Move to the next row
                best_x = 0
                best_y += 1

            # If we run out of space, break
            if best_y + rect.height > self.height:
                break

        return placed

    def __repr__(self):
        return f"Plate({self.width}x{self.height}) with {len(self.rectangles)} rectangles"

def generate_random_rectangles(num_rectangles, max_width, max_height):
    return [Rectangle(random.randint(1, max_width), random.randint(1, max_height))
            for _ in range(num_rectangles)]

class RectangleNestingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rectangle Nesting")

        # Define plate size
        self.plate_width = 400
        self.plate_height = 400

        # Generate random rectangles
        self.num_rectangles = 10
        self.max_rect_width = 100
        self.max_rect_height = 100
        self.rectangles = generate_random_rectangles(self.num_rectangles, self.max_rect_width, self.max_rect_height)

        # Sort rectangles by area (largest first)
        self.rectangles.sort(key=lambda r: r.width * r.height, reverse=True)

        # Create plate
        self.plate = Plate(self.plate_width, self.plate_height)

        # Canvas for drawing
        self.canvas = tk.Canvas(root, width=self.plate_width, height=self.plate_height, bg="white")
        self.canvas.pack()

        # Button to execute next step
        self.next_button = tk.Button(root, text="Next", command=self.next_step)
        self.next_button.pack()

        # Index for tracking which rectangle to place next
        self.current_rectangle_index = 0

        # Draw initial state
        self.draw_plate()
        self.draw_rectangles()

    def draw_plate(self):
        # Draw the plate boundary
        self.canvas.create_rectangle(0, 0, self.plate_width, self.plate_height, outline="black")

    def draw_rectangles(self):
        # Draw placed rectangles
        for rect in self.plate.rectangles:
            self.canvas.create_rectangle(
                rect.x, rect.y,
                rect.x + rect.width, rect.y + rect.height,
                fill="lightblue", outline="black"
            )

        # Draw unplaced rectangles
        for i in range(self.current_rectangle_index, len(self.rectangles)):
            rect = self.rectangles[i]
            self.canvas.create_rectangle(
                10, self.plate_height + 20 + (i - self.current_rectangle_index) * 30,
                10 + rect.width, self.plate_height + 20 + (i - self.current_rectangle_index) * 30 + rect.height,
                fill="lightcoral", outline="black"
            )

    def next_step(self):
        if self.current_rectangle_index < len(self.rectangles):
            rect = self.rectangles[self.current_rectangle_index]
            if self.plate.add_rectangle(rect):
                self.current_rectangle_index += 1
                self.canvas.delete("all")
                self.draw_plate()
                self.draw_rectangles()
            else:
                messagebox.showinfo("Info", f"Cannot place rectangle: {rect}")
        else:
            messagebox.showinfo("Info", "All rectangles have been placed.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RectangleNestingApp(root)
    root.mainloop()