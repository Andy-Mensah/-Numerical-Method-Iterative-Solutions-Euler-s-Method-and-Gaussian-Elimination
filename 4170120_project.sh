#!/bin/bash
#Enabling permissions
chmod 777 4170120_project.py && chmod 777 4170120_plot.gp
python3 4170120_project.py
mkdir -p data plots
gnuplot 4170120_plot.gp
