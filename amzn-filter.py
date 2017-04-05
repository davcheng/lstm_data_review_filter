import csv

# filter csv based on other values in a line
def main():
    with open("Amazon_Unlocked_Mobile_copy.csv") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            # if row[]
            # row[4]
            if row[3]>4:
                with open("five_star_reviews.txt", "a") as output_file:
                    output_file.write(row[4])
                    output_file.write("\n")

if __name__ == "__main__":
    main()
