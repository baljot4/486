import argparse
from library.statistics import *

#This program accepts cypher text  
#and gets the letter counts for single, pairs, triples and quadruple
#sets of letters


def main():
    #Getting arguemnts from user
    parser = argparse.ArgumentParser(description='Calculates letter frequencies of given cipher text in a cipher file.')
    parser.add_argument('CipherFile',
                        help='The cipher file to analyze.')
    parser.add_argument("-s", "--spaces", action='store_true',
                        help="Counts spaces as a valid cipher character instead of ignoring them."
                             "", required=False)
    parser.add_argument("-p", "--punctuation", action='store_true',
                        help="Counts punctuation as valid cipher characters instead of ignoring them."
                             "", required=False)

    args = parser.parse_args()

    #getting file
    cipherfile = args.CipherFile

    with open(cipherfile, 'r') as cf:
        ciphertext = cf.read()

    #using ngram to figure out sequence 
    cipherlettercounts = build_ngram_counts(ciphertext, 1, args.spaces, args.punctuation)
    cipherdigramcounts = build_ngram_counts(ciphertext, 2, args.spaces, args.punctuation)
    ciphertrigramcounts = build_ngram_counts(ciphertext, 3, args.spaces, args.punctuation)
    cipherquadgramcounts = build_ngram_counts(ciphertext, 4, args.spaces, args.punctuation)

    #prints what we got from functions
    print("**** Cipher Text ****")
    print("")
    print(ciphertext)
    print("")
    #printing out the count for single letters!
    print("Letter Counts:")
    for c in cipherlettercounts:
        print("{0} = {1}".format(c, cipherlettercounts[c]))
    print("")
    #printing out the count of the bunches of two letters
    print("Digram Counts:")
    for c in cipherdigramcounts:
        print("{0} = {1}".format(c, cipherdigramcounts[c]))
    print("")
    #printing the amount of time 3 letters consecutively come up
    print("Trigram Counts:")
    for c in ciphertrigramcounts:
        print("{0} = {1}".format(c, ciphertrigramcounts[c]))
    print("")
    #printing all groups of 4 letters and the counts
    print("Quadgram Counts:")
    for c in cipherquadgramcounts:
        print("{0} = {1}".format(c, cipherquadgramcounts[c]))
    print("")


if __name__ == "__main__":
    main()