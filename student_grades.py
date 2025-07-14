import statistics
import matplotlib.pyplot as plt

# Dictionary of student names and their marks
marks = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Eva": 78
}

# Extract marks
scores = list(marks.values())

# Mean, Median
mean = statistics.mean(scores)
median = statistics.median(scores)

print("Mean:", mean)
print("Median:", median)

# Top scorer
topper = max(marks, key=marks.get)
print("Top Scorer:", topper, "with", marks[topper])

# Students below average
below_avg = [name for name, score in marks.items() if score < mean]
print("Students below average:", below_avg)

# Standard deviation
std_dev = statistics.stdev(scores)
print("Standard Deviation:", std_dev)

# Plot bar chart
plt.bar(marks.keys(), marks.values(), color='skyblue')
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.axhline(mean, color='red', linestyle='--', label=f'Mean ({mean:.1f})')
plt.legend()
plt.tight_layout()
plt.savefig("chart.png")  # Save chart as image
plt.show()

# Sort students by marks (descending)
sorted_marks = sorted(marks.items(), key=lambda x: x[1], reverse=True)
print("\nSorted Students by Marks:")
for name, score in sorted_marks:
    print(f"{name}: {score}")
