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
        matrix = np.empty((10, number_of_participants), dtype=object)
        
        # Here I add the matrix to the collaboration_matrices dictionary
        collaboration_matrices[participant_name] = matrix
    
    # Here I create the project data dictionary
    project_data = {name_of_project: collaboration_matrices}
    
    # Here I print the matrices to confirm
    print(f"\nProject: {name_of_project}")
    for key, value in collaboration_matrices.items():
        print(f"{key}:\n{value}")
    
    return project_data
