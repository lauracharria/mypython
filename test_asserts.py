#check spaces, docstrings, and characters
#check character length on each line
#do PEP8 review
#check extracredit
#check github submission
#fix symbols in dataset and language

#rundown of the notebook and project requirements
#docstrings for test asserts?
#See github project tab
# Use docstrings, supposed to help anyone else, not distract
"""
    - On Anaconda, use pylint my_experiment to check for the syntax and pep8
"""
#Test Assert #1
import pandas as pd
import pytest
import my_skytoy as st
import pylint test_asserts
def test_commmon_category():
    
    test_df = pd.DataFrame({"ID" : [1, 2, 3, 4],
                            "Name of Toy": ["Rubix Cube","Circuit Cubes","Sudoku","Paint Rocks"],
                            "Description": ["Fun times","Electricity is fun","Exercise your mind","Paint your future"],
                            "Vendor": ["amazon", "amazon", "Tundra", "Tundra"],
                            "Category": ["Puzzle", "Robots", "Skills", "Artist"],
                            "Inventory Qty": [1, 2, 3, 4],
                            "Price in USD" : [10.50, 20.54, 30.58, 40.59]})
    
    my_data = st.common_category(test_df)
    assert(my_data["ID"].dtype == int)
    assert(my_data["Inventory Qty"].dtype == int)
    assert(my_data["Price in USD"].dtype == float)
    assert(my_data["Name of Toy"].dtype == object)
    assert(my_data["Description"].dtype == object)
    assert(my_data["Vendor"].dtype == object)
    assert(len(my_data) == 1)
    assert(len(my_data.columns) == 7)
    assert(my_data.at[3,"Name of Toy"] == "Paint Rocks")
    assert(callable(st.common_category))

#Test Assert #2
def test_toy_features():
    
    test_df = pd.DataFrame({"ID" : [1],
                            "Name of Toy": ["Rubix Cube"],
                            "Description": ["Fun times"],
                            "Vendor": ["amazon"],
                            "Category": ["Puzzle"],
                            "Inventory Qty": [1],
                            "Price in USD" : [10.50]})
    
    toy_name, toy_category = st.toy_features(test_df)
    assert(type(toy_name) == str)
    assert(type(toy_category)== str)
    assert(toy_name == "Rubix Cube")
    assert(toy_category == "Puzzle")
    assert(callable(st.toy_features))
    
#Test Assert #3    
def test_yes_validation():
    
    affirmative_list = ["y","fs","si","yes","yep","yas","yeah","sure",
                    "okay", "I am","you bet","for sure","of course",
                    "certainly","absolutely","definitely"]
    test = True
    you_shall_pass = st.yes_validation("Are you ready?",affirmative_list, test)
    assert(type(you_shall_pass)== bool)
    assert(callable(st.yes_validation))
    assert(you_shall_pass== True)
    
#Test Assert #4    
def test_printing_toy():
    
    test_df = pd.DataFrame({"ID" : [1, 2, 3, 4],
                            "Name of Toy": ["Rubix Cube","Circuit Cubes","Sudoku","Paint Rocks"],
                            "Description": ["Fun times","Electricity is fun","Exercise your mind","Paint your future"],
                            "Vendor": ["amazon", "amazon", "Tundra", "Tundra"],
                            "Category": ["Puzzle", "Robots", "Skills", "Artist"],
                            "Inventory Qty": [1, 2, 3, 4],
                            "Price in USD" : [10.50, 20.54, 30.58, 40.59]})
    
    category = "Skills"
    st.printing_toy(test_df,category)   
    assert(callable(st.printing_toy))