# Dijkstra’s Shortest Path for Indian Cities

## Overview
This program computes the shortest distances between cities using Dijkstra’s Algorithm.

It reads a CSV file containing city connections (origin, destination, and distance), builds a graph, and calculates the minimum distance from a given source city to all other cities.

## Dataset Format
The CSV file (indian-cities-dataset.csv) should have the following columns:

Origin,Destination,Distance
CityA,CityB,100
CityB,CityC,200

- Origin: Starting city
- Destination: Connected city
- Distance: Distance in kilometers

## How It Works
1. Reads the CSV file and builds a graph (adjacency list)
2. Uses Dijkstra’s algorithm with a priority queue (heapq)
3. Computes shortest distances from the source city
4. Prints the results

## How to Run

1. Place the dataset at:
   Question1/indian-cities-dataset.csv

2. Run the program:
   python your_script_name.py

3. Enter a source city when prompted:
   Enter the source city: Delhi

## Example Output
Shortest distances from Delhi:
Mumbai: 1400 km
Chennai: 2200 km
Kolkata: 1500 km

## Requirements
- Python 3.x
- No external libraries needed

## Notes
- City names must match exactly with the CSV file
- The graph is undirected (two-way connections)
- Unreachable cities will have distance = inf