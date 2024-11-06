#TASK 1

# Set the terminal type and output file
set terminal png size 2035,1024
set output 'plot.png'

set title "iterations vrs iterative f(x)s"
set xlabel "iterations"
set ylabel "iterative method's f(x)"
# Plot the data from data.dat using specified columns and plot settings
plot "data.dat" using 1:2 title "Iteration vs Bisection" w lp,\
     "" using 1:3 title "Iteration vs Secant" lt 8 lc 12 w lp,\
     "" using 1:4 title "Iteration vs Newton" lt 4 lc 2 w lp,\
     "" using 1:5 title "Iteration vs Fixed Iter" lt 3 lc 6 w lp




#TASK 2

set terminal png size 2035,1024
set output "euler.png"

# Set plot title and axis labels
set title "Euler's Method: Exact vs Estimated Temperatures"
set xlabel "Step Size"
set ylabel "Temperature (K)"

# Plot data points with lines connecting them
plot "euler.dat" using 1:2 w lp lc 3 title "Exact Temperatures", \
     "euler.dat" using 1:3 w lp lc 8 title "Estimated Temperatures"
