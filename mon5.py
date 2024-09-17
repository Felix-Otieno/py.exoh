def canVote2(age, citizen):
    if (age >= 18) and citizen:
        print("Eligible to vote")
        return True
    else:
        print("Not eligible to vote")
        return False
canVote2(21, True)
canVote2(17, False)

# # Define the canVote2 function
# def canVote2(age, citizen):
#     if (age >= 18) and citizen:
#         print("Eligible to vote")
#         return True
#     else:
#         print("Not eligible to vote")
#         return False

# # Call the function with test values (these should be outside the function definition)
# canVote2(21, True)  # This should print "Eligible to vote"
# canVote2(17, False)  # This should print "Not eligible to vote"
