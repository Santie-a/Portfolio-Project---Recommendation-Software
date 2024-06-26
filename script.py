from functions import welcome, goodbye, get_data, get_genre, get_recommendations, get_decition, print_recommendation
from DoublyLinkedList import DoublyLinkedList

if __name__ == '__main__':
	# Collecting the data from the CSV file using the function and adding it to the DoublyLinkedList data structure
	data = get_data("vgsales.csv")
	data_DLL = DoublyLinkedList()
	for row in data:
		data_DLL.add_to_tail(row)

	# Greeting the user
	welcome()

	# Getting the genre to be used
	genre = get_genre(data_DLL)
	if genre:
		# Getting and printing the default recommendations
		recommendations = get_recommendations(genre, data_DLL)
		current_node = recommendations.head_node
		while current_node is not None:
			print_recommendation(current_node.value)
			current_node = current_node.get_next_node()

		# Loop to ask the user if they would like to see more recommendations
		range_recommendations = [0, 10]
		while True:
			decition = get_decition("Would you like to see more recommendations?\nType 'y' to countinue or 'e' to exit the program: ", ['y', 'e'])
			if decition == "y":
				range_recommendations[0] += 10
				range_recommendations[1] += 10
				recommendations = get_recommendations(genre, data_DLL, range_recommendations=range_recommendations)
				current_node = recommendations.head_node
				if current_node == None:
					print("There are no more recommendations!")
					break
				while current_node is not None:
					print_recommendation(current_node.value)
					current_node = current_node.get_next_node()
				
			elif decition == "e":
				break

	# Saying goodbye to the user
	goodbye()