Project Report: Solving the Arrow Maze Problem using Graph Traversal
1. Introduction
The objective of this project is to model the Arrow Maze problem as a graph and utilize a known graph traversal algorithm to find a route from the top-left arrow to the bullseye located at the bottom-right corner. The problem entails navigating through a field of arrows (red or blue) where each arrow indicates a direction of movement. The traversal must follow the direction of the arrows, switching between red and blue arrows, until reaching the bullseye. Handling loops and revisiting nodes within a path are essential aspects of solving this problem.

2. Program
The project is implemented in Python, with multiple Python files organized under the main file Project2.py. The project adheres to specific requirements regarding file structure and command-line parameters:

File Structure: The implementation utilizes multiple Python files, all managed and executed from Project2.py.
Graph Structure and Traversal: While any graph structure and traversal algorithm are permitted, built-in graph functions are prohibited. Therefore, custom implementations of the graph structure and traversal algorithm are required.
Command-line Parameters: The program expects two command-line parameters: the input file name and the output file name. For example:
python Project2.py input.txt output.txt

2.1 Comments
In lieu of a formal report, comments play a crucial role in this project's evaluation. Detailed comments are required, particularly for functions, methods, and classes, to demonstrate a clear understanding of the implemented code. While not every variable or line requires comments, the code should be well-documented to ensure clarity and maintainability.

2.2 Input File Format
The program reads input from a file with a specific format. The input file begins with two positive integers indicating the number of rows (r) and columns (c) of the maze. Subsequently, each row contains color and directional information for each arrow in the maze. Each value represents the color (R for red, B for blue) and direction (N, E, S, W, NE, SE, SW, NW) of the arrow. The bulls-eye is represented by the letter O, always located in the bottom-right corner of the maze.

3. Conclusion
In conclusion, this project aimed to solve the Arrow Maze problem using graph traversal techniques. Through careful implementation and adherence to project requirements, a solution was developed to efficiently navigate through the maze of arrows and reach the bullseye. The utilization of custom graph structures and traversal algorithms demonstrated a comprehensive understanding of graph theory and algorithmic problem-solving.