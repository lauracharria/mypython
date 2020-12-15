def common_category(my_data, category = "Artist"):
    
    """
    Randomly return a row (DataSet) of a DataFrame; 
    specifically from the category column.
     
    Parameters
    ------------
    my_data : DataFrame (integers, floats, objects)
    category : string, default: "Artist", 
               4 categories: "Robots", "Skills", "Artist", and "Puzzle"
    
    Returns
    ------------
    toy: Dataset, 1 row of the DataFrame
    """

    rows_category = my_data.loc[my_data["Category"] == category]
    toy = rows_category.sample()
    
    return toy

def toy_features(toy_dataset):
    
    """
    Returns the name and description of 1 toy.
    Parameters
    ---------
    toy_dataset: DataSet (integers, floats, objects)
    
    Returns
    ------------
    toy_name: (string)
    toy_description: (string)
    """
    
    toy_name = toy_dataset.iloc[0]["Name of Toy"]
    toy_category = toy_dataset.iloc[0]["Category"]
    
    return toy_name, toy_category

def yes_validation(question, affirmative_list, test = False):
    
    """
    Checks if the child is ready to begin making the wishlist.
    Does not continue until the answer is "yes", and accepts 
    "YES","YeS" and any of its variations.
    Parameters
    ---------
    question: (string) "Are you ready?"
    """
    
    you_shall_pass = False
    # while not you_shall_pass:
    if not test:
        ready = input(question)
    else:
        ready = "Yes"
    
    if ready.lower() in affirmative_list:
        you_shall_pass = True
        
    return you_shall_pass
           
def printing_toy(my_data,category):
    
    """
    Utilizes two functions: common_category and toy_features 
    to randomly select and print a toy from the category received.

    Parameters
    ---------
    my_data: DataFrame (integers, floats, objects)
    category: string, default: "Artist", 
              4 categories: "Robots", "Skills", "Artist", and "Puzzle"
    Returns
    ---------   
    Print statement
    """
        
    my_category = common_category(my_data, category)
    toy_name, toy_category = toy_features(my_category)
    
    if toy_category == "Skills":
        print("Your toy is " + toy_name + " because you like to fix problems with your " + toy_category.lower() + "! :)")
    elif toy_category == "Artist":
        print("Your toy is " + toy_name + " because you like to create as an " + toy_category.lower() + "! :)")
    elif toy_category == "Puzzle":
        print("Your toy is " + toy_name + " because you like to solve " + toy_category.lower() + "s ! :)")
    else:
        print("Your toy is " + toy_name + " because you like to play with " + toy_category.lower() + "! :)")  
        