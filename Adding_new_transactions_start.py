import numpy as np

def create_new_list(number_of_participants):
    
    """
    Starts a new financing project by collecting data on the number and names of participants, 
    as well as naming the project.
    
    This information is gathered through user input.
    
    Parameters:
        number_of_participants(int): Number of participants for the creation of a new collaboration matrix.
        
    Returns:
        A dictionary with the project name and the collaboration matrix - an overview of the entire financial situation.
    """
    
    # Here I create a dictionary to store each participant's matrix
    collaboration_matrices = {}
    
    # Here I give my project a name
    print('Enter the name of your project:')
    name_of_project = input('Name of project: ')
    
    print('Enter the names of participants:')
    
    # Here I create an empty matrix for each participant
    for i in range(number_of_participants):
        participant_name = input(f'Participant {i + 1}: ')  # Input participant's name
        
        # Here I create a new empty matrix for each participant
        matrix = np.empty((1, number_of_participants), dtype=object)
        
        # Here I add the matrix to the collaboration_matrices dictionary
        collaboration_matrices[participant_name] = matrix
    
    # Here I create the project data dictionary
    project_data = {name_of_project: collaboration_matrices}
    
    # Here I print the matrices to confirm
    print(f"\nProject: {name_of_project}")
    for key, value in collaboration_matrices.items():
        print(f"{key}:\n{value}")
    
    return project_data

def create_and_add_new_transaction(project_data, name_of_project, Size_of_transaction, Kind_of_transaction):
    
    if name_of_project in project_data:
       participants = project_data[name_of_project]
       number_of_participants = len(participants)  # Determine the number of participants
    else:
       print(f"Project '{name_of_project}' not found.")
       return
   
   # Calculate shared price per participant
    Shared_price = Size_of_transaction / number_of_participants
   
   # Determine the transaction type
    if Kind_of_transaction == 1:
       Add_value = Shared_price * 1
    elif Kind_of_transaction == 2:
       Add_value = Shared_price * -1
    else:
       print('Kind of transaction not defined... Sorry! Our program is too simple for you, but we are working on making it more advanced!')
       return
   
   # Identify the person who carried out the transaction
    print('Who carried out the transaction?')
    who_transacted = input('Enter the name of the person who carried out the transaction: ')
   
   # Confirm the participants involved in the transaction
    print("Who was involved in this transaction? For the following participants, enter 'True' if they should partake and 'False' if not." )
   
    new_transaction = [0] * number_of_participants
   
    for idx, participant in enumerate(participants):
        partaking = input(f"Was {participant} involved? (True/False): ")
        if partaking.lower() == 'true':
           new_transaction[idx] = Add_value
    
    print(new_transaction)
    