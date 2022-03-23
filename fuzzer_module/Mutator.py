
from fuzzer_module.Fuzzconfig import *

def getMutStr(length: int) -> str:
    mut_str = "AAABAAACAAADAAAEAAAFAAAGAAAHAAAIAAAJAAAKAAALAAAMAAANAAAOAAAPAAAQAAARAAASAAATAAAUAAAVAAAWAAAXAAAYAAAZ" \
              "BBBABBBCBBBDBBBEBBBFBBBGBBBHBBBIBBBJBBBKBBBLBBBMBBBNBBBOBBBPBBBQBBBRBBBSBBBTBBBUBBBVBBBWBBBXBBBYBBBZ" \
              "CCCACCCBCCCDCCCECCCFCCCGCCCHCCCICCCJCCCKCCCLCCCMCCCNCCCOCCCPCCCQCCCRCCCSCCCTCCCUCCCVCCCWCCCXCCCYCCCZ" \
              "DDDADDDBDDDCDDDEDDDFDDDGDDDHDDDIDDDJDDDKDDDLDDDMDDDNDDDODDDPDDDQDDDRDDDSDDDTDDDUDDDVDDDWDDDXDDDYDDDZ" \
              "EEEAEEEBEEECEEEDEEEFEEEGEEEHEEEIEEEJEEEKEEELEEEMEEENEEEOEEEPEEEQEEEREEESEEETEEEUEEEVEEEWEEEXEEEYEEEZ" \
              "FFFAFFFBFFFCFFFDFFFEFFFGFFFHFFFIFFFJFFFKFFFLFFFMFFFNFFFOFFFPFFFQFFFRFFFSFFFTFFFUFFFVFFFWFFFXFFFYFFFZ" \
              "GGGAGGGBGGGCGGGDGGGEGGGFGGGHGGGIGGGJGGGKGGGLGGGMGGGNGGGOGGGPGGGQGGGRGGGSGGGTGGGUGGGVGGGWGGGXGGGYGGGZ" \
              "HHHAHHHBHHHCHHHDHHHEHHHFHHHGHHHIHHHJHHHKHHHLHHHMHHHNHHHOHHHPHHHQHHHRHHHSHHHTHHHUHHHVHHHWHHHXHHHYHHHZ" \
              "IIIAIIIBIIICIIIDIIIEIIIFIIIGIIIHIIIJIIIKIIILIIIMIIINIIIOIIIPIIIQIIIRIIISIIITIIIUIIIVIIIWIIIXIIIYIIIZ" \
              "JJJAJJJBJJJCJJJDJJJEJJJFJJJGJJJHJJJIJJJKJJJLJJJMJJJNJJJOJJJPJJJQJJJRJJJSJJJTJJJUJJJVJJJWJJJXJJJYJJJZ" \
              "KKKAKKKBKKKCKKKDKKKEKKKFKKKGKKKHKKKIKKKJKKKLKKKMKKKNKKKOKKKPKKKQKKKRKKKSKKKTKKKUKKKVKKKWKKKXKKKYKKKZ" \
              "LLLALLLBLLLCLLLDLLLELLLFLLLGLLLHLLLILLLJLLLKLLLMLLLNLLLOLLLPLLLQLLLRLLLSLLLTLLLULLLVLLLWLLLXLLLYLLLZ" \
              "MMMAMMMBMMMCMMMDMMMEMMMFMMMGMMMHMMMIMMMJMMMKMMMLMMMNMMMOMMMPMMMQMMMRMMMSMMMTMMMUMMMVMMMWMMMXMMMYMMMZ" \
              "NNNANNNBNNNCNNNDNNNENNNFNNNGNNNHNNNINNNJNNNKNNNLNNNMNNNONNNPNNNQNNNRNNNSNNNTNNNUNNNVNNNWNNNXNNNYNNNZ" \
              "OOOAOOOBOOOCOOODOOOEOOOFOOOGOOOHOOOIOOOJOOOKOOOLOOOMOOONOOOPOOOQOOOROOOSOOOTOOOUOOOVOOOWOOOXOOOYOOOZ" \
              "PPPAPPPBPPPCPPPDPPPEPPPFPPPGPPPHPPPIPPPJPPPKPPPLPPPMPPPNPPPOPPPQPPPRPPPSPPPTPPPUPPPVPPPWPPPXPPPYPPPZ" \
              "QQQAQQQBQQQCQQQDQQQEQQQFQQQGQQQHQQQIQQQJQQQKQQQLQQQMQQQNQQQOQQQPQQQRQQQSQQQTQQQUQQQVQQQWQQQXQQQYQQQZ" \
              "RRRARRRBRRRCRRRDRRRERRRFRRRGRRRHRRRIRRRJRRRKRRRLRRRMRRRNRRRORRRPRRRQRRRSRRRTRRRURRRVRRRWRRRXRRRYRRRZ" \
              "SSSASSSBSSSCSSSDSSSESSSFSSSGSSSHSSSISSSJSSSKSSSLSSSMSSSNSSSOSSSPSSSQSSSRSSSTSSSUSSSVSSSWSSSXSSSYSSSZ" \
              "TTTATTTBTTTCTTTDTTTETTTFTTTGTTTHTTTITTTJTTTKTTTLTTTMTTTNTTTOTTTPTTTQTTTRTTTSTTTUTTTVTTTWTTTXTTTYTTTZ" \
              "UUUAUUUBUUUCUUUDUUUEUUUFUUUGUUUHUUUIUUUJUUUKUUUL"
    if length > 2048:
        raise Exception("Error: Mutate string length exceeds limit.")
    return mut_str[0:length]



def mutateSeeds(seed: str, filepath: str, label: str) -> 'list[StructSeed]':
    """
    Replace and add strings for variant input according to the sliding window.
    @param seed:
    @param filepath:
    @param label:
    @return:
    """
    seed_len = len(seed)
    mutate_listq = []
    # Substitution of bytes for seed mutation
    endnum = MUT_STEP + seed_len % MUT_STEP
    for i in range(0, seed_len-endnum, MUT_STEP):
        mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                       str(seed[0:i] + MUT_STR + seed[i + len(MUT_STR):seed_len]),
                                       MUT_TYPE_SUB,
                                       [idx for idx in range(i, i + len(MUT_STR)+1)]))
    mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                   str(seed[0:seed_len-endnum] + MUT_STR[0:endnum]),
                                   MUT_TYPE_SUB,
                                   [idx for idx in range(seed_len - endnum, seed_len+1)]))

    # Insert byte for seed variation
    for i in range(0, seed_len, MUT_STEP):
        mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                       str(seed[0:i] + MUT_STR + seed[i:seed_len]),
                                       MUT_TYPE_INSERT,
                                       [idx for idx in range(i, i + len(MUT_STR)+1)]))
    mutate_listq.append(StructSeed(filepath+getMutfilename(label),
                                   str(seed + MUT_STR),
                                   MUT_TYPE_INSERT,
                                   [idx for idx in range(seed_len, seed_len + len(MUT_STR)+1)]))
    # print(mutate_listq)
    return mutate_listq


def mutateSelectChar(seed: str, filepath: str, label: str, loc_list) -> list:
    """
    Mutate one character at a time.
    @return:
    """
    mutate_listq = []



    return mutate_listq



if __name__ == "__main__":
    mutate_seed_list = mutateSeeds("12345678123456789", "", "1")
    print(mutate_seed_list)
