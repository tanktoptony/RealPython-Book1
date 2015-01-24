# Define a function, enrollment_stats(), that takes as an input a list of lists where each
# individual list contains three elements: (a) the name of a university, (b) the total number of
# # enrolled students, and (c) the annual tuition fees.
# This function should return two lists: the first containing all of the student enrollment values
# and the second containing all of the tuition fees.
# Next, define a mean() and a median() function. Both functions should take a single list as
# an argument and return the mean and median from the values in each list. Use the return
# values from enrollment_stats() as arguments for each function. Challenge yourself by
# finding a way to sum all the values in a list without using the built-in 'sum()' function for
# calculating the mean.
# At some point you should calculate the total students enrolled and the total tuition paid.


def enrollment_status(enrollment_list):
    student_enrollment= [x[1] for x in enrollment_list]
    tuition = [y[2] for y in enrollment_list]
    return student_enrollment, tuition

def mean(my_mean_list):
    mean_length = len(my_mean_list)
    if mean_length != 0:
        x = 0
        for i in my_mean_list:
            x += i
        return x/mean_length
    else:
        return 'List is empty!'
    

def median(my_median_list):
    my_median_list.sort()
    median_length = len(my_median_list)
    if median_length % 2 != 0:
        return my_median_list[(median_length-1)/2]
    else:
        return ((my_median_list[(median_length / 2)-1] + my_median_list[median_length/2])/2.0)


if __name__=='__main__':

    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]

    totals = enrollment_status(universities)
    total_students = sum(totals[0])
    total_tuition = sum(totals[1])

    print '*' * 20 
    print 'Total student: {}'.format(total_students)
    print 'Total tuition: ${}'.format(total_tuition)
    print 
    print 'Student mean: {}'.format(mean(totals[0]))
    print 'Student median: {}'.format(median(totals[0]))
    print 
    print 'Tuition mean: ${}'.format(mean(totals[1]))
    print 'Tuition median: ${}'.format(median(totals[1]))
    print
