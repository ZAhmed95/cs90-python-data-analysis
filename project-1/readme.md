# Project 1

**Due:** 11:59 PM on Sunday 04/07/19

This file contains your instructions for project 1.

Contained in this folder are two other files: 'data.csv' and 'project1.py'

The 'data.csv' file contains the data we will use for this project.

The 'project1.py' file contains the code structure of the project. It does some basic things like import the packages you will use and read the data from the file, but **most importantly**, it contains a skeleton outline of some empty functions that **you** have to fill in.

Don't alter the names of any of the functions in the code. Each function tells you exactly what kind of arguments it expects to receive, and exactly what the return value from that function should look like. This strict structure is to make sure you stay on track, and it serves as checkpoints.

## Project Description

For this project, you are the head of the Bigmart Sales Analysis team, and it is your job to create a prediction model that can accurately predict the total yearly sales of any given item at any given store.

Listed below are the usual 5 steps of a data analysis task:

1. Hypothesis Generation
2. Data Exploration
3. Data Cleaning
4. Feature Engineering
5. Model Creation

For this project, you will write code to accomplish steps 1-4. Step 5, model creation, will be in Project 2.

## Data Structure

The data you have access to contains 12 columns:

1. Item_Identifier: the ID of an item
2. Item_Weight: the weight (in pounds) of the item
3. Item_Fat_Content: the fat content of an item
4. Item_Visibility: the percentage of display area given to this item
5. Item_Type: the category of this item
6. Item_MRP: the maximum retail price of this item (think of this as unit price)
7. Outlet_Identifier: the ID of a store
8. Outlet_Establishment_Year: year in which this store opened
9. Outlet_Size: size of the store
10. Outlet_Location_Type: category of the area this store is in
11. Outlet_Type: category of this store
12. Item_Outlet_Sales: total 2013 sales for this item at this store (**output column**)

## Project Instructions

Below, steps 1-4 of data analysis are listed, and in each section you will be given a task.

NOTE 1: there is no task for Step 1: Hypotheses Generation; it's already been done for you. In an actual data analysis task, you would of course come up with your own hypotheses, but since this is just a project, you will work with some existing hypotheses.

For steps 2-4, each step has one or more already defined empty function declarations in the code that you will have to fill in. Each step's section will give you the details. **Note that some questions do not require you to write any code**.

**Project submission**: once you have filled out the template project1.py file with your own answers, copy and paste the code into the "Project 1" Assignment in repl.it, and hit submit. Just like with normal assignments, you have an *unlimited* number of submissions until the deadline, so it is in your best interest to submit anything you want feedback on, instead of waiting to submit the whole thing at the end.

### Step 1: Hypotheses Generation

Here are the hypotheses we will test in this project:

1. **Utility**: items that are used more regularly usually sell more than products only used in specific circumstances.
2. **Store Capacity**: larger stores can obviously hold more items, so they should sell more.
3. **Display Area**: the more visible an item is, the more likely it is to be sold.
4. **City Type**: stores located in more affluent and urban areas should have higher total sales.
5. **Store Age**: older stores should sell more, due to an established reputation.
6. **Item Weight**: lighter items should sell more, due to convenience of carrying them by hand.
7. **Maximum Retail Price**: cheaper items should sell more in general (but does the increased amount sold outweigh the lower profit per item?)

### Step 2: Data Exploration

This step involves manually looking through the data to find anything that needs to be cleaned, refactored, fixed, etc. In the 'Data Exploration' section in project1.py, answer the following questions:

1. How many unique values are in each column?
2. Which columns contain numerical data, and which columns contain categorical data? (No code)
3. Which columns contain null values?
4. Do any columns contain nonsensical data? (No code)
5. Do any columns contain values that can be merged? (No code)

### Step 3: Data Cleaning

This step requires you to fix any problems or inconsistencies you found in the data during step 2.

1. Fill in any numerical null values with the group average.
2. Fill in any categorical null values with the group mode.
3. Fill in any nonsensical values the same way as above.
4. Combine any values that can be merged.

### Step 4: Feature Engineering

1. Create an 'Outlet_Age' column, which contains how many years a store has operated since its establishment up to 2013.
2. Create dummy columns for each categorical feature.