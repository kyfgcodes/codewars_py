'''In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).'''

def DNA_strand(dna):
    
    comp_dna = ''
    for i in dna:
       if i == 'A':
           comp_dna += 'T'
       elif i == 'T':
           comp_dna += 'A'

       if i == 'C':
           comp_dna += 'G'
       elif i == 'G':
           comp_dna += 'C'

    return comp_dna


print(DNA_strand('AAAA'))


#Alternate solution

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC")) #translate replaces each char specified in ordern of the char you replace them with
print(DNA_strand('AAAA'))

#Done!!!