
MUTATE_STR = "aaabaaac"
STEP = 4  # step size of mutant seeds

# Mutant seeds
def mutateSeeds(seed):
    seed_len = len(seed)
    # Substitution of bytes for seed mutation
    sub_list = []
    endnum = STEP+seed_len%STEP
    for i in range(0, seed_len-endnum, STEP):
        sub_list.append(seed[0:i]+MUTATE_STR+seed[i+len(MUTATE_STR):seed_len])
    sub_list.append(seed[0:seed_len-endnum]+MUTATE_STR[0:endnum])

    # Insert byte for seed variation
    insert_list = []
    for i in range(0, seed_len, STEP):
        insert_list.append(seed[0:i]+MUTATE_STR+seed[i:seed_len])
    insert_list.append(seed+MUTATE_STR)
    print(sub_list, insert_list)
    mutate_seed_list = sub_list + insert_list


    return mutate_seed_list

if __name__ == "__main__":
    mutateSeeds("1234567812345678")