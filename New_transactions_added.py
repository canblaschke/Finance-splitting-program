import numpy as np

def create_new_list(number_of_participants):
    
    """
    Function starts a new financing project by collecting data on the number 
    and names of participants, as well as naming the project.
    
    This information is gathered through user input.
    
    Parameters:
        number_of_participants(int): Number of participants for the creation 
        of a new collaboration matrix.
        
    Returns:
        A dictionary with the project name and the collaboration matrix - an 
        overview of the entire financial situation.
    """
    

    collaboration_matrices = {}
    

    print('Enter the name of your project:')
    name_of_project = input('Name of project: ')
    
    print('Enter the names of participants:')
    

    for i in range(number_of_participants):
        participant_name = input(f'Participant {i + 1}: ')
        

        matrix = np.empty((1, number_of_participants), dtype=object)
        

        collaboration_matrices[participant_name] = matrix
    

    project_data = {name_of_project: collaboration_matrices}
    

    print(f"\nProject: {name_of_project}")
    for key, value in collaboration_matrices.items():
        print(f"{key}:\n{value}")
    
    return project_data

def create_and_add_new_transaction(project_data, name_of_project, Size_of_transaction, Kind_of_transaction, Npeopleparttaking):
    
    """
    Function allows users to add a new transaction to already existing project 
    data. This is done by collecting the names of participants in the 
    transcation, as well as the size and kind of the transaction.
    
    Parameters:
        project_data (dict): The project data dictionary that was defined by
                            the function create_new_list(a)
        name_of_project (str): Name of the project defined by input to the
                              function create_new_list(a)
        Size_of_transaction (float): Numerical size of financial transaction
        Kind_of_transaction (int):
            1 - expenditure
            2 - income
        Npeopleparttaking (int): The total number of people sharing the 
                                 transaction
                                 
    Returns:
        The new transaction is added to the transaction matrix of the person
        who carried out the transaction, as a new row. This can be reviewed in
        the print of the updated matrix shown in the output, or by retrieving
        the information from the dictionary of the project.
    """
            
    
    if name_of_project in project_data:
       participants = project_data[name_of_project]
       number_of_participants = len(participants)
    else:
       print(f"Project '{name_of_project}' not found.")
       return
   

    Shared_price = Size_of_transaction / Npeopleparttaking
   

    if Kind_of_transaction == 1:
       Add_value = Shared_price * 1
    elif Kind_of_transaction == 2:
       Add_value = Shared_price * -1
    else:
       print('Kind of transaction not defined... Sorry! Our program is too simple for you, but we are working on making it more advanced!')
       return
   

    print('Who carried out the transaction?')
    who_transacted = input('Enter the name of the person who carried out the transaction: ')
   
    
    print("Who was involved in this transaction? For the following participants, enter 'True' if they should partake and 'False' if not." )
    new_transaction = [0] * number_of_participants
   
    for idx, participant in enumerate(participants):
        partaking = input(f"Should {participant} parttake? (True/False): ")
        if partaking.lower() == 'true':
           new_transaction[idx] = Add_value
    
    print(new_transaction)
    
    if who_transacted in participants:
        transactor_matrix = participants[who_transacted]
        

        transactor_matrix = np.append(transactor_matrix, [new_transaction], axis=0)
        

        participants[who_transacted] = transactor_matrix
        
        print(f"Transaction added to {who_transacted}'s matrix.")
    else:
        print(f"Participant '{who_transacted}' not found in the project.")


    print(f"\nUpdated transactions for {who_transacted}:")
    print(participants[who_transacted])
    
    