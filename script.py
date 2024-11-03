import os

def create_lab_structure():
    lab_name = "lab_" + input("Lab number: ").zfill(2)
    num_files_1_input = input("Nº files in block_01: ")
    num_files_2_input = input("Nº files in block_02: ")
    num_files = [int(num_files_1_input), int(num_files_2_input)]
  
    # Define the main directory path
    main_dir = os.path.join(lab_name)
    
    # Define subfolder names
    subfolders = ['block_01', 'block_02']
    # Create the main directory if it doesn't exist
    os.makedirs(main_dir, exist_ok=True)
    
    # Loop through each subfolder
    for index, subfolder in enumerate(subfolders):

      if(num_files[index]):        
        # Define subfolder path
        subfolder_path = os.path.join(main_dir, subfolder)
        # Create the subfolder
        os.makedirs(subfolder_path, exist_ok=True)
      
        # Create the specified number of files in each subfolder
        for i in range(1, num_files[index] + 1):
          # Define the file path with the desired naming convention
          file_path = os.path.join(subfolder_path, f"test-{str(i).zfill(2)}.py")
          
          
          # Read the template from the specified file
          with open('./test-template.py', 'r') as file:
            template = file.read()
          
          # Write the template content to the file
          with open(file_path, 'w') as file:
            file.write(template)
                
    print(f"Folder structure created at: {main_dir}")

create_lab_structure()