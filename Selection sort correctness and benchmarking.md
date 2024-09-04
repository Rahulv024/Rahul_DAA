Question 2: Argue selection sort correctness. 
-> Loop invariance is used to prove correctness of an algorithm 
It has three main properties,
1. Initialization: It is true prior to the initialization before the first iteration. 
2. Maintenance: using each iteration, the algorithm finds out the smallest element, the unsorted part of the array and swaps it with the first element of that unsorted part. 
3. Termination: When the loop finishes.
Let’s take an example of array [29,10,14,37,13]:
1.	Initialization:
    	Initially i = 0, the subarray is empty.
2.	First Iteration, where i = 0:
    	Let’s find the smallest element from the list [29, 10, 14, 37, 13] which is 10.
    	As 10 is the smallest, let’s swap 10 with 29, so the array looks like: [10, 29, 14, 37, 13].
    	Subarray from the beginning to (i + 1) which is [10], is sorted.
3.	Second Iteration i = 1:
    	Let’s find the smallest element from the list [29, 14, 37, 13] which is 13.
    	As 13 is the smallest, let’s swap 13 with 29, so the array looks like: [10, 13, 14, 37, 29].
    	Subarray from the beginning to (i + 1) which is [10, 13], is sorted.
4.	Third Iteration (i = 2):
    	Let’s find the smallest element from the list [14, 37, 29] which is (14).
    	As 14 is the smallest, let’s swap 14 (no change): [10, 13, 14, 37, 29].
      Subarray from the beginning to (i + 1) which is [10, 13, 14], is sorted.
5.	Fourth Iteration (i = 3):
    	Let’s find the smallest element from the list [37, 29] which is 29.
    	As 29 is the smallest, let’s swap 29 with 37: [10, 13, 14, 29, 37].
    	Subarray from the beginning to (i + 1) which is [10, 13, 14, 29], is sorted.
6.	Termination:
    	The outer loop will terminate when i=4.
    	At this point, the entire list [10,13,13,29,37] is sorted.
  	

Question 3: Benchmark the runtime of each algorithm. Your benchmarks should include information about your computer (ram, cpu etc.) and be run with various input sizes; from small (array of size 5,10,20) all the way up to large arrays (where your computer is struggling). I should at the very least see a plot of time vs input size n. Feel free to use benchmarking software.
System Information:
Processor: Intel64 Family 6 Model 170 Stepping 4, Genuine Intel
RAM: 15.520217895507812 GB
Python Version: 3.12.5
Plot of time vs input sizes

![image](https://github.com/user-attachments/assets/a5570cec-7a29-47cb-a3c3-0db02c8723b2)

