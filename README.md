<p align=center><img src="https://media.giphy.com/media/ZIzN7YWNuTUYg/giphy.gif"/></p>

# Running Thief Problem

[![](https://img.shields.io/github/v/release/janmenne/Running-Thief-Problem?style=flat-square)](https://github.com/jmne/Running-Thief-Problem/releases)
[![](https://img.shields.io/github/issues/janmenne/Running-Thief-Problem?style=flat-square)](https://github.com/jmne/Running-Thief-Problem/issues)
[![](https://img.shields.io/github/issues-pr/janmenne/Running-Thief-Problem?style=flat-square)](https://github.com/jmne/Running-Thief-Problem/pulls)
[![](https://img.shields.io/github/license/janmenne/Running-Thief-Problem?style=flat-square)](https://github.com/jmne/Running-Thief-Problem/blob/main/LICENSE)
[![](https://img.shields.io/github/languages/code-size/janmenne/Running-Thief-Problem?style=flat-square)](https://github.com/jmne/Running-Thief-Problem/tree/main/src)
[![Code Check](https://github.com/janmenne/Running-Thief-Problem/actions/workflows/code-check.yml/badge.svg)](https://github.com/janmenne/Running-Thief-Problem/actions/workflows/code-check.yml)
[![Generate Documentation](https://github.com/jmne/Running-Thief-Problem/actions/workflows/generate-docs.yml/badge.svg)](https://github.com/jmne/Running-Thief-Problem/actions/workflows/generate-docs.yml)


This problem is about a thief, that has to rob a set of houses in different streets. <br>
He has a backpack that is capable of a specified amount of loot and should get the most in the shortest time (way).<br>
We used Dijkstra to measure the distance between a house and the end house. Then an algorithm builds a value that represents worth/weight/distance. <br>
This algorithm takes the best route and builds our path from house to house.

How exactly do we solve the problem?<br>
In our approach, we start with importing and preparing the problem models that are in the [src / data](src/data)
can be found. Each .txt document represents a graph, where k is the maximum weight and n is the number of nodes.<br>
Example of a .txt:
```
#META
name = Problem 0
k = 6
N = 5
#NODES
1   (1,1)  (1,3)  [2,3]
2   (0,4)  (2,1)  
3   (4,2)  (2,4)  [1,2,4]
4   (2,2)  (3,3)  [2,3,5]
5   (5,5)  (2,2)  [2,4]	
#EOF
```

The graph is defined more precisely in the #EOF section. Each line begins with the name of the node (e.g. 1), the coordinates
of the node (x, y), value and weight of the loot (value, weight), as well as the other nodes that can be reached from this node (e.g. [1,3]).

The [FileManager.py](src/FileManager.py) class provides the basic read-in functionality and is called in the [Graph.py](src/Graph.py) class using the import_data function.
This creates a new graph instance from the predefined problem / data models, which is used as the data basis in the further course.

To solve the given problem, we first use the Dijkstra algorithm from the [Graph.py](src/Graph.py) class to find the fastest route from each node
to be able to find a target node. This procedure is carried out using the shortest_path function.

Now, however, we need another decision criterion in order to find the most effective way for us. In this case we opted for a weighted solution
The value of the prey, the weight of the prey and the distance to the target point - the WDG value. This is calculated as follows:
```
WDG = Value / Weigth / Distance
```
This value is calculated for each edge in the graph. Basically, the higher the WDG value of a route, the better.
The algorithm will therefore always "greedy" decide on the passable route with the largest WDG value.

If at the end the optimal route is found, the algorithm compares the ratio of value to weight (value / weight) for each prey that can be found on the route at a junction.
Taking into account the upper weight limit (defined as maximum weight k in the problem model), the algorithm now adds the prey with the largest W / G value to the "backpack" in descending order of size and then terminates according to our optimal solution.


## Installation

Just download the [Package](https://github.com/janmenne/Running-Thief-Problem/releases/latest) and run the

```bash
RTP.exe
```

## Usage

```
After installing and running the program will return the perfect way for the before specified RTP.
```

## License
[GNU General Public License v3.0](https://github.com/jancodet/Running-Thief-Problem/blob/main/LICENSE)

## Stats

[![Readme Card Statistics](https://github-readme-stats.vercel.app/api/pin/?username=jmne&repo=Running-Thief-Problem)](https://github.com/jmne/Running-Thief-Problem/)

