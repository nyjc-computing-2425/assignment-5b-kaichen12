# Part 1
def read_csv(filename):
    # Type your code below
    """    
    takes in a filename and processes its contents
    
    Parameter
    ---------
    filename: str
        name of a file
    
    Returns
    -------
    tuple
        tuple in the format (header, data)
    """
    data = []
    with open(filename,'r') as f:
        header = f.readline().strip().split(',')
        for line in f:
            record = line.strip().split(',')
            record[0] = int(record[0])
            record[3] = int(record[3])
            data.append(record)
    return header, data


# Part 2
def filter_gender(enrolment_by_age, sex):
    # Type your code below
    """
    Parameter
    ---------
    enrolment_by_age:list
    list of year age sex enrolemnt

    sex: str
    MF or F

    Returns
    -------
    nested list in the format[[year,age,enrolment],[...]]
    """
    filtered_data = []
    for rec in enrolment_by_age:
        if rec[2] == sex:
            new_list = [rec[0], rec[1], rec[3]]
            filtered_data.append(new_list)
    
    return filtered_data


# Part 3
def sum_by_year(enrolment_data):
    """
    parameter
    ---------
    enrolment_data : list

    returns
    -------
    tuple
        tuple in the format[[year, number of enrolment],[...],...]
    """
    # Type your code below
    year_list = []
    sum_list = []
    sum = 0
    year_list.append(enrolment_data[0][0])
    for rec in enrolment_data:
        year = rec[0]
        if year not in year_list:
            year_list.append(year)
            sum_list.append(sum)
            sum = 0
        sum += rec[2]
    sum_list.append(sum)
    enrolment_by_year = []
    for i in range(len(year_list)):
        enrolment_by_year.append([year_list[i],sum_list[i]])
    return enrolment_by_year
        


# Part 4
def write_csv(filename, header, data):
    # Type your code below
    """
    parameters
    ---------
    filename : str
        the name of the file to be written to
    header : list
        a list containing the header
    data : list
        a list of lists containing the data to be written to the file
        
    returns
    -------
    int
        the number of records written to the file
    """

    with open(filename, 'w') as f:
        output = ','.join(header) + '\n'
        f.write(output)

        count = 0
    
        for rec in data:
            output = f'{rec[0]},{rec[1]}\n'
            f.write(output)
            count += 1
    return count





# TESTING
# You can write code below to call the above functions
# and test the output
# jupyter notebook --notebook-dir='h:'

# header, enrolment_data = read_csv('pre-u-enrolment-by-age.csv')
# print(filter_gender(enrolment_data, 'MF'))
# print(read_csv('pre-u-enrolment-by-age.csv'))
# print(sum_by_year(enrolment_data))