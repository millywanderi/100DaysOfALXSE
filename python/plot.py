#!/usr/bin/python3
"""Ploting using Matplotlib"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def generate_plot():
    """Generates a plot"""
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    plt.plot(x, y)  # Create a line plot
    
    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Plot')

    plt.savefig('plot.png')  # Show the plot

generate_plot()
