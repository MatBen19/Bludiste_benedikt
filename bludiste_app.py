import tkinter as tk
from tkinter import filedialog
import os
from bludiste import Bludiste
from bludiste_view import BludisteView
from bludiste_dao_factory import BludisteDaoFactory
from robot import Robot
from robot_view import RobotView


class BludisteApp:
    def __init__(self, root, window_width, window_height):
        self.root = root
        self.window_sirka = window_width
        self.window_vyska = window_height

        # Create a frame for the canvas and button panel
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.button_frame = tk.Frame(self.root, width=150, bg="lightgrey")
        self.button_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Add the "Vyber bludiště" button
        self.vyber_button = tk.Button(self.button_frame, text="Vyber bludiště", command=self.novy_bludiste)
        self.vyber_button.pack(pady=20)

        # Initialize maze-related variables
        self.bludiste = None
        self.view = None
        self.robot = None
        self.robot_view = None

    def novy_bludiste(self):
        """Allows the user to select a new maze and displays it."""
        cesta_k_souboru = self.vyber_soubor()

        if cesta_k_souboru:
            # Load and process the maze
            dao = BludisteDaoFactory.get_bludiste_dao(cesta_k_souboru)
            bludiste_data = dao.nacti_bludiste(cesta_k_souboru)

            # Create Bludiste instance
            self.bludiste = Bludiste(bludiste_data)

            # If a previous view exists, clear it
            if self.view:
                self.view.canvas.destroy()

            # Create BludisteView
            self.view = BludisteView(self.canvas_frame, self.bludiste, self.window_sirka, self.window_vyska)
            self.view.vykresli()

            # Calculate tile dimensions
            sirka_policka = self.window_sirka // self.bludiste.get_sirka()
            vyska_policka = self.window_vyska // self.bludiste.get_vyska()

            # Create Robot and RobotView
            self.robot = Robot(color="blue")
            self.robot_view = RobotView(self.robot, sirka_policka, vyska_policka)

            # Draw the robot on the starting position
            self.robot_view.vykresli(self.view.canvas)

            # Solve the maze in memory
            self.robot.vyres_bludiste(self.bludiste)

    def vyber_soubor(self):
        """Opens a file dialog to select a maze file."""
        slozka = os.path.dirname(__file__)

        # File selection dialog
        soubor = filedialog.askopenfilename(
            title="Vyberte soubor",
            initialdir=slozka,
            filetypes=[("Podporované soubory", "*.txt;*.xml;*.csv")]
        )

        return soubor


# Spusteni aplikace
def main():
    root = tk.Tk()
    root.title("Bludiště App")

    # Rozmery okna
    window_width = 600
    window_height = 450

    # Create an instance of the app
    app = BludisteApp(root, window_width, window_height)

    # Start the main loop
    root.mainloop()


if __name__ == "__main__":
    main()