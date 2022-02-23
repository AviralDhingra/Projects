import time

tic = time.perf_counter()  # Start Time
# your_program() 			  # Your code here
toc = time.perf_counter()  # End Time
# Print the Difference Minutes and Seconds
print(
    f"Build finished in {(toc - tic)/60:0.0f} minutes {(toc - tic)%60:0.0f} seconds")
# For additional Precision
print(f"Build finished in {toc - tic:0.4f} seconds")
