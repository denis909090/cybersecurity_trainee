ip_list = ["192.168.1.1", "192.168.1.2", "10.0.0.1", "10.0.0.2", "172.16.0.1", "8.8.8.8", "8.8.4.4"]

for i in ip_list:
    if '192.168' in i:
        print(i)

# Create a list
colors = ["red", "green", "blue"]
# Print the first item
print(colors[0])
# Change the second item to "yellow"
colors[1] = "yellow"
# Add "purple" to the end
colors.append('purple')
# Remove "red"
colors.remove('red')
# Print the list
print(colors)