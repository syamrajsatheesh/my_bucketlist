import pickle





class EditFile:

    def __init__(self, path, data=None):
        self.data = data
        self.path = path

    def write_to_file(self, key, value):
            
            try:
                # Load existing data from the pickle file
                with open(self.path, 'rb') as file:
                    data = pickle.load(file)
            except (FileNotFoundError, EOFError):
                # Handle the case where the file is not found or is empty
                data = {}

            # Append new data to the existing data
            data[key] = value

            # Write the updated data back to the pickle file
            with open(self.path, 'wb') as file:
                pickle.dump(data, file)
            return data
    

    def overwrite_file(self):

        with open(self.path, 'wb') as file:
            pickle.dump(self.data, file)



    def read_from_file(self):

        try:
            with open(self.path, 'rb') as file:
                self.data = pickle.load(file)

            return self.data
        
        except FileNotFoundError:
            print(f"File '{self.path}' not found.")


