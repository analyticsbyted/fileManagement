import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame and exclude the root folder
df = pd.read_csv("folder_info.csv")

# Specify the root folder to exclude (change this to your root folder)
root_folder = "C:\\"  # Change to your root folder path

# Filter out the root folder
df = df[df["Path"] != root_folder]

# Convert folder sizes from bytes to megabytes
df["Size (MB)"] = df["Size"] / 1_048_576  # 1 MB = 1,048,576 bytes

# Summary Statistics
folder_size_mean = df["Size (MB)"].mean()
folder_size_median = df["Size (MB)"].median()
folder_size_max = df["Size (MB)"].max()
folder_count_mean = df["File Count"].mean()

print("Summary Statistics:")
print(f"Mean Folder Size: {folder_size_mean:.2f} MB")
print(f"Median Folder Size: {folder_size_median:.2f} MB")
print(f"Maximum Folder Size: {folder_size_max:.2f} MB")
print(f"Mean File Count: {folder_count_mean:.2f}")

# Top N Largest Folders
top_10_largest_folders = df.nlargest(10, "Size (MB)")
print("\nTop 10 Largest Folders:")
print(top_10_largest_folders)


# Correlation between Folder Size and File Count
correlation = df["Size (MB)"].corr(df["File Count"])
print("\nCorrelation between Folder Size and File Count:")
print(f"Correlation Coefficient: {correlation:.2f}")

# Histogram of Folder Sizes
plt.figure(figsize=(10, 6))
plt.hist(df["Size (MB)"], bins=50, edgecolor="k", alpha=0.7)  # Increase the number of bins to 50
plt.title("Distribution of Folder Sizes (MB)")
plt.xlabel("Folder Size (MB)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()


# Filtering: Folders with Size > 1 GB
large_folders = df[df["Size (MB)"] > 1024]  # 1 GB = 1024 MB
print("\nFolders with Size > 1 GB:")
print(large_folders)

# Export Large Folders to a CSV file
large_folders.to_csv("large_folders.csv", index=False)
