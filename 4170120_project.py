#Task 1
#Data sets
bi_arr = []
se_arr = []
newt_arr = []
fx_arr = []


def f(x):
    return x**3 - 3*x**2 + x -1

def derivative_f(x):
    return 3*x**2 - 6*x + 1

def g(x):
    return (3*x**2 -x +1)**(1/3)


def bisection(a, b, tol):
    if f(a) * f(b) >= 0:
       # print("Bisection method fails.")
        return None
    else:
        iterations = 0
        condition = True
        while  condition:  
            midpoint = (a + b) / 2
            bi_arr.append(f(midpoint))
            if f(midpoint) == 0:
                return midpoint
            elif f(a) * f(midpoint) < 0:
                b = midpoint
            else:
                a = midpoint
            
            condition = abs(f(midpoint)) >tol # the stop criteria
            #print(f"Iteration {iterations}: root = {midpoint:.10f} at function {f(midpoint)}")
            iterations += 1

            
        return midpoint

# Initial guesses for bisection method
a = 2
b =  3
tol = 1e-6

bisection(a, b, tol)
# print("Approximate root:", str(root)[:11])
# print( bi_farr)



def secant(x0, x1, tol):
    iterations = 0
    while abs(x1 - x0) > tol:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        se_arr.append(f(x2))
        x0, x1 = x1, x2 
 
        #print(f"Iteration {iterations}: root = {x2:.10f} funtion = {f(x2)}")
        iterations += 1
    return x2


# Initial guesses secant method;
x0 = -2
x1 = 3
tol = 1e-6 

secant(x0, x1, tol)
# print("Approximate root:", str(root)[:11])
# print(se_arr)


def newton_raphson(x0, tol):
    iterations = 0
    while abs(f(x0)) >= tol:
        x1 = x0 - f(x0) / derivative_f(x0)
        newt_arr.append(f(x1))
        #print(f"Iteration {iterations}: root = {x1:.10f} funtion = {f(x1)}")
        iterations += 1
        x0 = x1
    return x1

# Initial guess Newton Raphs's method
x0 = 2
tol = 1e-6

newton_raphson(x0, tol)
# print("Approximate root:", str(root)[:11])
# print(n_arr)


def fixed_point_iteration(x0, tol):
    iterations = 0
    while True:
        x1 = g(x0)
        fx_arr.append(f(x1))
        #print(f"Iteration {iterations}: root = {x1:.10f} funtion = {f(x1)}")
        iterations += 1
        if abs(x1 - x0) < tol:
            break
        x0 = x1
    return x1

# Initial guess fixed_point_iteration
x0 = 2.0
tol = 1e-6

fixed_point_iteration(x0, tol)
# print("Approximate root:", str(root)[:11])
# print(fx_arr)


#making the dat file
with open('data.dat', 'w') as file:
    file.write("Iteration fx_Bisection fx_Secant fx_Newton fx_FixedPoint\n")
    
num_iterations = max(len(bi_arr), len(se_arr), len(newt_arr), len(fx_arr))
with open('data.dat', 'a') as file:
    for i in range(num_iterations):

        output = f"{i}" #string formatting
    
        # Bisection values
        if i < len(bi_arr):
            output += f" {bi_arr[i]}"
        else:
            output += " -"
        
        # Secant values
        if i < len(se_arr):
            output += f" {se_arr[i]}"
        else:
            output += " -"
        
        # Newton values
        if i < len(newt_arr):
            output += f" {newt_arr[i]}"
        else:
            output += " -"
        
        # Fixed-point values
        if i < len(fx_arr):
            output += f" {fx_arr[i]}"
        else:
            output += " -"
        
        file.write(f'{output}\n')

print('TASK 1') 
print('A data.dat file has been created, chk ur dir')



#Task 2
#Data sets
estimated_temps = []
exact_temps = [1635.4,537.26,100.80,32.607,14.806]

def f(t, theta):
    return -2.2067*10**-12 * (theta**4 - 81*10**8)

def euler_method(theta0, t0, h, steps):
    theta = theta0
    t = t0
   
    #Calculating the final temp for a step size 
    for i in range(steps):
        theta += f(t, theta) * h
        t += h
        
    #Appending to the array at (h,theta)     
    estimated_temps.append((h,round(theta,2)))
 
    

# Given step sizes
step_sizes = [480, 240, 120, 60, 30]

# Perform Euler's method for each step size
for h in step_sizes:
    euler_method(1200, 0, h, int(480 / h))

# print(estimated_temps)
#output 


# Write data to euler.dat file
with open('euler.dat', 'w') as file:
   
    file.write("STEP SIZE theta(480) ET\n")
    for i in range(len(exact_temps)):
        line = f"{estimated_temps[i][0]} {estimated_temps[i][1]} {exact_temps[i]}\n"
        file.write(line)


def guassian_elimination():
    print('TASK 3')

    # Coefficient Matrix
    A = [[17, 14, 23], 
         [-7.54, -3.54, 2.7], 
         [6, 1, 3]]

    # Constant Vector
    y = [24.5, 2.352, 14]

    # Step 2: Divide Row 1 by 17 and multiply it by -7.54.
    mut_A = [(elem / 17) * -7.54 for elem in A[0]]
    mut_y = (y[0] / 17) * -7.54
    A[1] = [round(A[1][i] - mut_A[i], 3) for i in range(len(A[1]))]
    y[1] -= mut_y

    # Step 4: Divide Row 1 by 17 and multiply it by 6.
    mut_A = [(elem / 17) * 6 for elem in A[0]]
    mut_y = (y[0] / 17) * 6
    A[2] = [round(A[2][i] - mut_A[i], 3) for i in range(len(A[2]))]
    y[2] -= mut_y

    # Step 6: Use Row 2 as the pivot equation and eliminate Row 3.
    # Divide Row 2 by 2.669 and then multiply it by -3.941.
    mut_A = [(elem / 2.669) * -3.941 for elem in A[1]]
    mut_y = (y[1] / 2.669) * -3.941
    A[2] = [round(A[2][i] - mut_A[i], 3) for i in range(len(A[2]))]
    y[2] -= mut_y

    # Printing the modified coefficient matrix and constant vector
    print("Modified Coefficient Matrix:")
    for row in A:
        print(row)
    print("\nModified Constant Vector:")
    print(y)
    print()

    # Using back substitution to solve the unknown values
    n = len(y)
    x = [0] * n

    for i in range(n - 1, -1, -1):
        sum_term = 0
        for j in range(i + 1, n):
            sum_term += A[i][j] * x[j]
        x[i] = round((y[i] - sum_term) / A[i][i], 3)

    # Printing the solution
    print("Solution:")
    for i in range(n):
        print(f"x_{i+1} = {x[i]}")

    print('\n\n')

# Call the function
guassian_elimination()







 
