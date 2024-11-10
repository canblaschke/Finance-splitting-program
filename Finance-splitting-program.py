import numpy as np
import pytest
from unittest.mock import patch

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
        
    Example:
        project_data = create_new_list(number_of_participants)
    """
    

    collaboration_matrices = {}
    

    print('Enter the name of your project:')
    name_of_project = input('Name of project: ')
    
    print('Enter the names of participants:')
    

    for i in range(number_of_participants):
        participant_name = input(f'Participant {i + 1}: ')
        

        matrix = np.zeros((1, number_of_participants), dtype=object)
        

        collaboration_matrices[participant_name] = matrix
    

    project_data = {name_of_project: collaboration_matrices}
    

    print(f"\nProject: {name_of_project}")
    for key, value in collaboration_matrices.items():
        print(f"{key}:\n{value}")
    
    return project_data

@patch('builtins.input', side_effect=['TestProject', 'Can', 'Blaschke'])
def test_create_new_list(mock_input):
    number_of_participants = 2
    project_data = create_new_list(number_of_participants)

    expected_matrix = np.zeros((1, number_of_participants), dtype=object)

    assert 'TestProject' in project_data
    assert len(project_data['TestProject']) == number_of_participants
    assert project_data['TestProject']['Can'].shape == expected_matrix.shape
    assert project_data['TestProject']['Blaschke'].shape == expected_matrix.shape



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

@patch('builtins.input', side_effect=['Alice', 'True', 'True'])
def test_create_and_add_new_transaction(mock_input):
    number_of_participants = 2
    project_data = {
        "TestProject": {
            "Alice": np.zeros((1, number_of_participants), dtype=object),
            "Bob": np.zeros((1, number_of_participants), dtype=object)
        }
    }
    name_of_project = "TestProject"
    Size_of_transaction = 100.0
    Kind_of_transaction = 1 
    Npeopleparttaking = 2

    create_and_add_new_transaction(
        project_data, name_of_project, Size_of_transaction, Kind_of_transaction, Npeopleparttaking
    )

    expected_matrix = np.array([[50, 50]])

    assert np.array_equal(project_data[name_of_project]["Alice"][1], expected_matrix[0])



def print_debts_for_everyone(project_data, name_of_project):
    """
    Function allows users to retrieve all the data stored in a given project
    dictionary. This gives users an overview of how much each participant owes 
    the other participants.
    
    Parameters:
        project_data (dict): The project data dictionary that was defined by
                            the function create_new_list(a)
        name_of_project (str): Name of the project defined by input to the
                              function create_new_list(a)
                                 
    Returns:
        Current financial overview is returned, with all recorded data of a given project.
    """
    
    if name_of_project in project_data:
        participants = project_data[name_of_project]
    else:
        print(f"Project '{name_of_project}' not found.")
        return
    
    print(f"Printing debts for each participant in project '{name_of_project}':\n")
    
    for owner, matrix in participants.items():
        print(f"Amounts owed to {owner}:")
        for col_idx, participant_name in enumerate(participants):
            if participant_name != owner:
                debt_amount = np.sum(matrix[:, col_idx])
                if debt_amount > 0:
                    print(f"{participant_name} owes {owner} the sum of: {debt_amount}")
                elif debt_amount < 0:
                    print(f"{owner} owes {participant_name} the sum of: {-debt_amount}")
        

def test_print_debts_for_everyone(capsys):
    project_data = {
        "TestProject": {
            "Alice": np.array([[50, -50]]),
            "Bob": np.array([[-50, 50]])
        }
    }
    name_of_project = "TestProject"

    print_debts_for_everyone(project_data, name_of_project)

    captured = capsys.readouterr()

    assert "Alice owes Bob the sum of: 50" in captured.out
    assert "Bob owes Alice the sum of: 50" in captured.out

