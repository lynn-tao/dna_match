import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Enter two arguments, please!")
        sys.exit(1)

    # Read database file into a variable
    profiles = []
    with open(sys.argv[1]) as file1:
        reader = csv.DictReader(file1)
        header = reader.fieldnames[1:]
        for row in reader:
            profiles.append(row)
    # Read DNA sequence file into a variable
    with open(sys.argv[2]) as file2:
        sequence = file2.read()

    # Find longest match of each STR in DNA sequence
    str_prof = {}
    for item in header:
        str_prof[item] = longest_match(sequence, item)

    # Check database for matching profiles
    for person in profiles:
        flag = True
        for item in header:
            # this person is not a match, keep looping
            if int(person[item]) != int(str_prof[item]):
                flag = False
        # found a match! end the loop early
        if flag:
            print(person['name'])
            sys.exit(0)

    print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
