import arcade
import arcade.gui
from enums.moves import MovesN3

def draw_square(xStart, yStart, color):
    arcade.draw_rectangle_filled(xStart, yStart, 50, 50, color)


def write_text(xStart, yStart, text):
    arcade.draw_text(text, xStart, yStart, arcade.color.CREAM)


def write_movement(xCoordinate, yCoordinate, movement):
    if movement is not None:
        write_text(xCoordinate, yCoordinate, "Last Movement: " + MovesN3(movement).name)
        return
    write_text(xCoordinate, yCoordinate, "No last movement")


class Rubik_Visualizer():

    def __init__(self, manager):
        self.window = arcade.open_window(800, 800, "Rubik Cube")
        self.uimanager = arcade.gui.UIManager()
        self.uimanager.enable()
        self.current_node = 0
        self.manager = manager
        self.solution = None
        self.front_color = arcade.color.WHITE
        self.top_color = arcade.color.BLUE
        self.back_color = arcade.color.YELLOW
        self.left_color = arcade.color.OUTRAGEOUS_ORANGE
        self.right_color = arcade.color.RED
        self.bottom_color = arcade.color.GREEN
        self.color_dictionary = {0: self.front_color, 1: self.top_color, 2: self.left_color, 3: self.bottom_color,
                                 4: self.right_color, 5: self.back_color}

    def visualize(self):
        arcade.start_render()
        self.draw_node(self.manager.visited[self.current_node])
        self.draw_next_node_button("Next node")
        self.draw_go_to_solution("Go to solution")
        arcade.finish_render()
        arcade.run()

    def draw_next_node_button(self, text):
        next_node = arcade.gui.UIFlatButton(text=text, width=200)
        next_node.on_click = self.on_click_next_node
        self.uimanager.add(arcade.gui.UIAnchorWidget(anchor_x="right", anchor_y="bottom", child=next_node))
        self.uimanager.draw()

    def draw_go_to_solution(self, text):
        go_to_solution = arcade.gui.UIFlatButton(text=text, width=200)
        go_to_solution.on_click = self.on_click_go_to_solution
        self.uimanager.add(arcade.gui.UIAnchorWidget(anchor_x="right", align_y=60, anchor_y="bottom", child=go_to_solution))
        self.uimanager.draw()

    def on_click_go_to_solution(self, event):
        self.current_node = len(self.manager.visited) - 2
        self.solution = self.manager.visited[self.current_node]
        self.on_click_next_node(event)

    def on_click_next_node(self, event):
        arcade.start_render()
        self.current_node += 1
        if self.current_node < len(self.manager.visited):
            self.draw_node(self.manager.visited[self.current_node])
            self.solution = self.manager.visited[self.current_node]
            self.draw_next_node_button("Next node")
        elif self.solution.parent is not None:
            self.solution = self.solution.parent
            self.draw_node(self.solution)
            self.draw_next_node_button("Parent node")
        else:
            arcade.close_window()
            return
        arcade.finish_render()

    def draw_node(self, node):
        self.draw_cube(node.state)
        write_movement(20, 780, node.lastMovement)
        write_text(20, 760, "Depth: " + str(node.deep))
        write_text(20, 740, "Weight: " + str(node.weight))

    def draw_cube(self, cube):
        n = self.manager.n
        center_x_coordinate = 235
        center_y_coordinate = 400
        square_size = 70 * n
        self.draw_face(cube[0], center_x_coordinate, center_y_coordinate)
        self.draw_face(cube[1], center_x_coordinate, center_y_coordinate + square_size)
        self.draw_face(cube[2], center_x_coordinate - square_size, center_y_coordinate)
        self.draw_face(cube[3], center_x_coordinate, center_y_coordinate - square_size)
        self.draw_face(cube[4], center_x_coordinate + square_size, center_y_coordinate)
        self.draw_face(cube[5], center_x_coordinate + square_size * 2, center_y_coordinate)

    def draw_face(self, face_matrix, xStart, yStart):
        x_coordinate = xStart
        y_coordinate = yStart
        for i in range(self.manager.n):
            for j in range(self.manager.n):
                draw_square(x_coordinate, y_coordinate,
                            self.color_dictionary[face_matrix[(self.manager.n - i) * self.manager.n - 1 - j]])
                x_coordinate = x_coordinate + 60
            y_coordinate = y_coordinate + 60
            x_coordinate = x_coordinate - 60 * self.manager.n
