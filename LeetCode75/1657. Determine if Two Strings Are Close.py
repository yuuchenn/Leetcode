       occurence1,occurence2 = {}, {}
        if len(word1) != len(word2):
            return False
        else:
            for oc1 in word1:
                occurence1[oc1] = occurence1.get(oc1,0)+1
            for oc2 in word2:
                occurence2[oc2] = occurence2.get(oc2,0)+1
            # nums the same
            # keys the same 
            for keys in occurence1.keys():
                if keys not in occurence2.keys():
                    return False
            occr2_list = list(occurence2.values())
            for val in occurence1.values():
                if val in occr2_list:
                    occr2_list.remove(val)
                else : 
                    return False
        return True