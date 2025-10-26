# Complementary DNA
# Given a string representing a DNA sequence, return its complementary strand using the following rules:
# 
# DNA consists of the letters "A", "C", "G", and "T".
# The letters "A" and "T" complement each other.
# The letters "C" and "G" complement each other.
# For example, given "ACGT", return "TGCA".

def complementary_dna(strand):

        complementary_strand = []

        for character in strand:
                
                if character == "A":
                        complementary_strand.append("T")
                if character == "T":
                        complementary_strand.append("A")
                if character == "G":
                        complementary_strand.append("C")
                if character == "C":
                        complementary_strand.append("G")
        
        complementary_strand = "".join(complementary_strand)

        return complementary_strand