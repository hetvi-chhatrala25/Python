
import numpy as np


class NumPy:

    def __init__(self):
        self.array = np.array([])

    def CheckArray(self):
        if self.array.size == 0:
            print("\nNo array has been created yet.")
            return False
        return True


    def CreateArray(self, dimensions):

        if dimensions == 1:

            n = int(input("Enter the number of elements: "))

            values = input("Enter values: ").split()

            if len(values) != n:
                print("Number of values does not match.")
                return

            values = [int(value) for value in values]

            self.array = np.array(values)

        elif dimensions == 2:

            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))

            values = input("Enter values: ").split()

            if len(values) != rows * columns:
                print("Number of values does not match.")
                return

            values = [int(value) for value in values]

            self.array = np.array(values).reshape(rows, columns)

        elif dimensions == 3:

            layers = int(input("Enter number of layers: "))
            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))

            values = input("Enter values: ").split()

            if len(values) != layers * rows * columns:
                print("Number of values does not match.")
                return

            values = [int(value) for value in values]

            self.array = np.array(values).reshape(
                layers, rows, columns
            )

        print("\nArray Created:")
        print(self.array)

        print("\nArray Properties:")
        print("Shape:", self.array.shape)
        print("Size:", self.array.size)

        self.IndexingSlicing()


    def IndexingSlicing(self):

        if not self.CheckArray():
            return

        while True:

            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")

            choice = int(input("Enter your choice: "))


            if choice == 1:

                if self.array.ndim == 1:

                    index = int(input("Enter index: "))

                    print("Element:")
                    print(self.array[index])

                elif self.array.ndim == 2:

                    row = int(input("Enter row index: "))
                    col = int(input("Enter column index: "))

                    print("Element:")
                    print(self.array[row, col])

                elif self.array.ndim == 3:

                    layer = int(input("Enter layer index: "))
                    row = int(input("Enter row index: "))
                    col = int(input("Enter column index: "))

                    print("Element:")
                    print(self.array[layer, row, col])


            elif choice == 2:

                if self.array.ndim == 1:

                    slicing = input("Enter slicing range: ")

                    start, stop, step = slicing.split(":")

                    start = int(start)
                    stop = int(stop)
                    step = int(step)

                    print("Sliced Array:")
                    print(self.array[start:stop:step])

                elif self.array.ndim == 2:

                    row_range = input("Enter row range: ")
                    column_range = input("Enter column range: ")

                    row_start, row_stop = row_range.split(":")
                    col_start, col_stop = column_range.split(":")

                    row_start = int(row_start)
                    row_stop = int(row_stop)

                    col_start = int(col_start)
                    col_stop = int(col_stop)

                    print("Sliced Array:")
                    print(
                        self.array[
                            row_start:row_stop,
                            col_start:col_stop
                        ]
                    )

                elif self.array.ndim == 3:

                    layer_range = input("Enter layer range: ")
                    row_range = input("Enter row range: ")
                    column_range = input("Enter column range: ")

                    layer_start, layer_stop = layer_range.split(":")
                    row_start, row_stop = row_range.split(":")
                    col_start, col_stop = column_range.split(":")

                    layer_start = int(layer_start)
                    layer_stop = int(layer_stop)

                    row_start = int(row_start)
                    row_stop = int(row_stop)

                    col_start = int(col_start)
                    col_stop = int(col_stop)

                    print("Sliced Array:")
                    print(
                        self.array[
                            layer_start:layer_stop,
                            row_start:row_stop,
                            col_start:col_stop
                        ]
                    )

            elif choice == 3:
                break

            else:
                print("Invalid choice.")


    def MathematicalOperations(self):

        if not self.CheckArray():
            return

        print("\nMathematical Operations:")

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = int(input("Enter your choice: "))

        if choice in [1, 2, 3, 4]:

            values = input("Enter values for second array: ").split()

            if len(values) != self.array.size:
                print("Number of values does not match.")
                return

            values = [int(value) for value in values]

            second_array = np.array(values).reshape(
                self.array.shape
            )

            if choice == 1:

                print("Result:")
                print(self.array + second_array)

            elif choice == 2:

                print("Result:")
                print(self.array - second_array)

            elif choice == 3:

                print("Result:")
                print(self.array * second_array)

            elif choice == 4:

                print("Result:")
                print(self.array / second_array)

        elif choice == 5:

            values = input("Enter values for second array: ").split()

            if len(values) != self.array.size:
                print("Number of values does not match.")
                return

            values = [int(value) for value in values]

            second_array = np.array(values).reshape(
                self.array.shape
            )

            print("Dot Product:")
            print(np.dot(self.array, second_array))

        elif choice == 6:

            values = input("Enter values for second array: ").split()

            if len(values) != self.array.size:
                print("Number of values does not match.")
                return

            values = [int(value) for value in values]

            second_array = np.array(values).reshape(
                self.array.shape
            )

            print("Matrix Multiplication:")
            print(np.matmul(self.array, second_array))

        else:
            print("Invalid choice.")


    def CombineSplit(self):

        if not self.CheckArray():
            return

        print("\nCombine or Split Arrays:")

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            values = input("Enter values for second array: ").split()

            if len(values) != self.array.size:
                print("Number of values does not match.")
                return

            values = [int(value) for value in values]

            second_array = np.array(values).reshape(
                self.array.shape
            )

            print("\nChoose a combining method:")
            print("1. Concatenate")
            print("2. Vertical Stack")
            print("3. Horizontal Stack")

            combine_choice = int(input("Enter your choice: "))

            if combine_choice == 1:

                print("Combined Array:")
                print(
                    np.concatenate(
                        (self.array, second_array)
                    )
                )

            elif combine_choice == 2:

                print("Combined Array:")
                print(
                    np.vstack(
                        (self.array, second_array)
                    )
                )

            elif combine_choice == 3:

                print("Combined Array:")
                print(
                    np.hstack(
                        (self.array, second_array)
                    )
                )

            else:
                print("Invalid choice.")

        elif choice == 2:

            number = int(input("Enter number of parts: "))

            print("Split Array:")
            print(
                np.split(
                    self.array,
                    number
                )
            )

        else:
            print("Invalid choice.")


    def SearchSortFilter(self):

        if not self.CheckArray():
            return

        print("\nSearch, Sort, and Filter:")

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))


        if choice == 1:

            value = int(input("Enter value to search: "))

            index = np.where(self.array == value)

            print("Index:")

            if self.array.ndim == 1:

                print(index[0])

            elif self.array.ndim == 2:

                for i in range(len(index[0])):
                    print(
                        "(",
                        index[0][i],
                        ",",
                        index[1][i],
                        ")"
                    )

            elif self.array.ndim == 3:

                for i in range(len(index[0])):
                    print(
                        "(",
                        index[0][i],
                        ",",
                        index[1][i],
                        ",",
                        index[2][i],
                        ")"
                    )


        elif choice == 2:

            print("\nChoose sorting order:")
            print("1. Ascending")
            print("2. Descending")

            sort_choice = int(
                input("Enter your choice: ")
            )

            if sort_choice == 1:

                print("Sorted Array:")
                print(np.sort(self.array))

            elif sort_choice == 2:

                sorted_array = np.sort(self.array)

                if self.array.ndim == 1:

                    sorted_array = sorted_array[::-1]

                elif self.array.ndim == 2:

                    sorted_array = sorted_array[:, ::-1]

                elif self.array.ndim == 3:

                    sorted_array = sorted_array[:, :, ::-1]

                print("Sorted Array:")
                print(sorted_array)

            else:
                print("Invalid choice.")


        elif choice == 3:

            print("\nChoose a filter condition:")
            print("1. Greater than")
            print("2. Less than")
            print("3. Equal to")
            print("4. Greater than or equal to")
            print("5. Less than or equal to")

            filter_choice = int(
                input("Enter your choice: ")
            )

            value = int(input("Enter value: "))

            if filter_choice == 1:

                print("Filtered Values:")
                print(self.array[self.array > value])

            elif filter_choice == 2:

                print("Filtered Values:")
                print(self.array[self.array < value])

            elif filter_choice == 3:

                print("Filtered Values:")
                print(self.array[self.array == value])

            elif filter_choice == 4:

                print("Filtered Values:")
                print(self.array[self.array >= value])

            elif filter_choice == 5:

                print("Filtered Values:")
                print(self.array[self.array <= value])

            else:
                print("Invalid choice.")

        else:
            print("Invalid choice.")


    def AggregatesStatistics(self):

        if not self.CheckArray():
            return

        print("\nAggregates and Statistics:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            print("Sum:")
            print(np.sum(self.array))

        elif choice == 2:

            print("Mean:")
            print(np.mean(self.array))

        elif choice == 3:

            print("Median:")
            print(np.median(self.array))

        elif choice == 4:

            print("Standard Deviation:")
            print(np.std(self.array))

        elif choice == 5:

            print("Variance:")
            print(np.var(self.array))

        elif choice == 6:

            print("Minimum:")
            print(np.min(self.array))

        elif choice == 7:

            print("Maximum:")
            print(np.max(self.array))

        elif choice == 8:

            percentile = float(
                input("Enter percentile value: ")
            )

            print("Percentile:")
            print(
                np.percentile(
                    self.array,
                    percentile
                )
            )

        elif choice == 9:

            values = input(
                "Enter values for second array: "
            ).split()

            if len(values) != self.array.size:
                print("Number of values does not match.")
                return

            values = [int(value) for value in values]

            second_array = np.array(values).reshape(
                self.array.shape
            )

            print("Correlation:")
            print(
                np.corrcoef(
                    self.array.reshape(-1),
                    second_array.reshape(-1)
                )
            )

        else:
            print("Invalid choice.")


    def MainMenu(self):

        while True:

            print("\nChoose an option:")
            print("1. Create a NumPy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:

                print("\nArray Creation:")

                print("\nSelect the type of array to create:")
                print("1. 1D Array")
                print("2. 2D Array")
                print("3. 3D Array")

                dimensions = int(
                    input("Enter your choice: ")
                )

                if dimensions in [1, 2, 3]:

                    self.CreateArray(dimensions)

                else:

                    print("Invalid choice.")

            elif choice == 2:

                self.MathematicalOperations()

            elif choice == 3:

                self.CombineSplit()

            elif choice == 4:

                self.SearchSortFilter()

            elif choice == 5:

                self.AggregatesStatistics()

            elif choice == 6:

                print("\nThank you for using the NumPy Analyzer!")
                print("Goodbye!")

                break

            else:

                print("Invalid choice.")



print("Welcome to the NumPy Analyzer!")

analyzer = NumPy()

analyzer.MainMenu()

