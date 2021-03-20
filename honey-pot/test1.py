# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the 'minimizeBias' function below.
# #
# # The function is expected to return an INTEGER.
# # The function accepts INTEGER_ARRAY ratings as parameter.

# def minimizeBias(ratings):
#     # sort the ratings
#     # O(nlogn)
#     ratings.sort()
#     total_bias = 0
#     start = 0
#     # loop over all ratings and update the total bias
#     # O(n)
#     while start < len(ratings) - 1:
#         player_1_rating = ratings[start]
#         player_2_rating = ratings[start+1]

#         bias = player_2_rating - player_1_rating
#         total_bias += bias
#         start += 2
    
#     return total_bias


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     ratings_count = int(input().strip())

#     ratings = []

#     for _ in range(ratings_count):
#         ratings_item = int(input().strip())
#         ratings.append(ratings_item)

#     result = minimizeBias(ratings)

#     fptr.write(str(result) + '\n')

#     fptr.close()


['aswvgdpaisrvieefgplakmdxceaettwtqokrgnsmjshcrsdkijuyubrcdawvcacpnbhtymxlueyjbivxjjejcltlbspymhstzgvakfmazcoabpsfwgzgdiwonjjyylcwbtldi', 'blydokdejsxthgvotwsyctdzqpsyusvjtuozmzjrwfyqlokczqayqbplfxtxezwbaqxcvdvabiauwtocyrzhwntfeimdkgissrofnwvxbiqqgmxwikhlibduxspcdfyllklhfijjwntbyi', 'dorsnkxgsdiluzyaxvbuuttcnnslbhalbzl', 'dpdhnwcwfnxyqsfcebyntnrgazdqjopxyrntbrhanoqidjxqjfvkyxigwwjlvftjbmutapvcwrgpgbsvmpktjtouiedtiskncqmlhzxhwnleqfiswryuwtjmaszhisfg', 'dpyvspanizoioareqxumndfovosolqukuqedztiyxrvqzxnahwjikakgvppuomchdxcbjjzgfbcxuxltytavtcvoogdpapduvoxjisojrsggix', 'ffkjpfdjohgvjzqjeoduuadbdfaiqzqbwftlchcydnftjyhlducfznwlzwegagjuubqfdprtpbijhznvakozooxuaaxjunlviyxbwcnyrlarjopggyzsdeaucqdmuoqlwhvafwdawwdanqjpbvexbkkmjtbqoivojqvhnbh', 'gkskrydycvnolegdxyzhkhwqgnmozuxbzaefnlcnvoqt', 'hfsxpiljfurfpcmzgbmxjctdimhbkapmdsfzqlfohfwqhqgbdqvjsgzehgacetjrhmwfldxfvxraqnhymiszdazjusfauabwmyegwefdxukmo', 'idthirkitdtfkaylgyjgxsjtwjtsdjgyavleifrzwxpqueuxdmcshhioscanzlwsafzkkmipirtfbmkttcsyknpexymmsykvnkxzgburhyimafpnmawhsokqhrphlvkfvqpkseisrkhmynjntxgevqzdiq', 'jcnfwrtjqfujmpcjpfccjjyjbyvgoxdkrizxofzpcixrwytzxpgwblsriekvriyclyiikfjfyubnnjklpjbrawdopetkzdlnsuyedbr', 'nucobgczdsynpwlmswgyo', 'qa', 'roshyprxualodxepwkdoldxadwfytpigzbakztzutpaviqihnmdiiasgjiskxidnxofivpaeweqtmxfzbszbrhcgwiddjlwrfadlpnoydurbntsmfdzwdtrfzdiq', 'sqtakohgdhbpazssebjoogwwhkpsqvbzluqhjzjsljzraiqkorfkpayudgdmtsmpfybriyamhgyqzqfctskjjyawyzhmdeqtwtmiwnwrjtfloubdttduerzgcvekakcwernldifwnljrdwodgqacottqetvbdwafhenakphlnfmseooll', 'tqeqdsvgljqzmwspcpzxebrvhwqbkrntlyaatlxwqhwjwhlqddwirvvfqetidccfcmtcrijqoedwkomhfmmyihhxluxdfnsrlshakyiirlgzhelbkosfwnjuwmxlvsdufwfsetciljrloxwylqtftipceneisgmmltnabfavaojjiauouwcsu', 'tygjwhphkgccwnnykucfoikcuidxpgohluvsxiumtqwgiazdbbacxbvteja', 'vcexqjatwbxjehnkcblhmbpmrseoiwbutxqkqtbsjpcyvwufzpnqmbrftnkbdpzcvvynrplypwgehetgpxjwjpwcpykispwfibjhbpzrzqdeehrzatbknzpdipidhiesjylrwktlxjcivhy', 'wchptbpfdomqwwvyuxljusonfynrjsmyhcyizlnhnmmpcbazevacvdyjfnlseiboxgkwjibuzqwldfxzflnitiytuzweemxzmelbfwofmvp', 'wmtephbjjztetkjgvshvrcncxkoopdepfaxdyyucwuaktvrihgbraioxxzmybcrtcstecgawlulnrvebfdukqceqkteybutrdeegqimburvciuejrcglghqyyzfryuamhhhhegbvpnvzbgkfmpdquclggqbdutiofgrlexgjsqlsouzknmqiop', 'wxweswnrucaaiekhznvyisduyepvddkeyzsyxcirwmuojhfczkmdqehprsjojdknlhvayzlomjwpwrxwrvsuuvaqgpysjukurgyzrhiehpwvhfclfazoxutcqehnkpcthoijnbiuxeoivwbjyqegpageiomcwnrlxxmiit', 'xwixxfrrvlbhmdrogsokxlurnqrxvzzyaqcpudnskuzmasbtudauxxxrpdtjyupez', 'yhbugiahkqkqr', 'zkrcxgagwosikssnqnpafpsqlrulvdhdpladwppeclxttstxusa', 'zwwbkseciohdhpvhjtvsnvhagaxgkywicfmpfqooukcqdvnpdsnplevsluutahthfumtiyhifcituzmsdwrisbwgynytyruymhbthrwtdjgevphcufwbnxtswcjzpfxeaplujdditpljnagxgcbnktpafmltzslnmsgunqdlh']


['yhbugiahkqkqr', 'tygjwhphkgccwnnykucfoikcuidxpgohluvsxiumtqwgiazdbbacxbvteja', 'jcnfwrtjqfujmpcjpfccjjyjbyvgoxdkrizxofzpcixrwytzxpgwblsriekvriyclyiikfjfyubnnjklpjbrawdopetkzdlnsuyedbr', 'xwixxfrrvlbhmdrogsokxlurnqrxvzzyaqcpudnskuzmasbtudauxxxrpdtjyupez', 'tqeqdsvgljqzmwspcpzxebrvhwqbkrntlyaatlxwqhwjwhlqddwirvvfqetidccfcmtcrijqoedwkomhfmmyihhxluxdfnsrlshakyiirlgzhelbkosfwnjuwmxlvsdufwfsetciljrloxwylqtftipceneisgmmltnabfavaojjiauouwcsu', 'aswvgdpaisrvieefgplakmdxceaettwtqokrgnsmjshcrsdkijuyubrcdawvcacpnbhtymxlueyjbivxjjejcltlbspymhstzgvakfmazcoabpsfwgzgdiwonjjyylcwbtldi', 'idthirkitdtfkaylgyjgxsjtwjtsdjgyavleifrzwxpqueuxdmcshhioscanzlwsafzkkmipirtfbmkttcsyknpexymmsykvnkxzgburhyimafpnmawhsokqhrphlvkfvqpkseisrkhmynjntxgevqzdiq', 'qa', 'dpdhnwcwfnxyqsfcebyntnrgazdqjopxyrntbrhanoqidjxqjfvkyxigwwjlvftjbmutapvcwrgpgbsvmpktjtouiedtiskncqmlhzxhwnleqfiswryuwtjmaszhisfg', 'vcexqjatwbxjehnkcblhmbpmrseoiwbutxqkqtbsjpcyvwufzpnqmbrftnkbdpzcvvynrplypwgehetgpxjwjpwcpykispwfibjhbpzrzqdeehrzatbknzpdipidhiesjylrwktlxjcivhy', 'wchptbpfdomqwwvyuxljusonfynrjsmyhcyizlnhnmmpcbazevacvdyjfnlseiboxgkwjibuzqwldfxzflnitiytuzweemxzmelbfwofmvp', 'nucobgczdsynpwlmswgyo', 'zwwbkseciohdhpvhjtvsnvhagaxgkywicfmpfqooukcqdvnpdsnplevsluutahthfumtiyhifcituzmsdwrisbwgynytyruymhbthrwtdjgevphcufwbnxtswcjzpfxeaplujdditpljnagxgcbnktpafmltzslnmsgunqdlh', 'ffkjpfdjohgvjzqjeoduuadbdfaiqzqbwftlchcydnftjyhlducfznwlzwegagjuubqfdprtpbijhznvakozooxuaaxjunlviyxbwcnyrlarjopggyzsdeaucqdmuoqlwhvafwdawwdanqjpbvexbkkmjtbqoivojqvhnbh', 'blydokdejsxthgvotwsyctdzqpsyusvjtuozmzjrwfyqlokczqayqbplfxtxezwbaqxcvdvabiauwtocyrzhwntfeimdkgissrofnwvxbiqqgmxwikhlibduxspcdfyllklhfijjwntbyi', 'gkskrydycvnolegdxyzhkhwqgnmozuxbzaefnlcnvoqt', 'wxweswnrucaaiekhznvyisduyepvddkeyzsyxcirwmuojhfczkmdqehprsjojdknlhvayzlomjwpwrxwrvsuuvaqgpysjukurgyzrhiehpwvhfclfazoxutcqehnkpcthoijnbiuxeoivwbjyqegpageiomcwnrlxxmiit', 'nbpgsapntlqlz', 'hfsxpiljfurfpcmzgbmxjctdimhbkapmdsfzqlfohfwqhqgbdqvjsgzehgacetjrhmwfldxfvxraqnhymiszdazjusfauabwmyegwefdxukmo', 'sqtakohgdhbpazssebjoogwwhkpsqvbzluqhjzjsljzraiqkorfkpayudgdmtsmpfybriyamhgyqzqfctskjjyawyzhmdeqtwtmiwnwrjtfloubdttduerzgcvekakcwernldifwnljrdwodgqacottqetvbdwafhenakphlnfmseooll', 'dorsnkxgsdiluzyaxvbuuttcnnslbhalbzl', 'zkrcxgagwosikssnqnpafpsqlrulvdhdpladwppeclxttstxusa', 'roshyprxualodxepwkdoldxadwfytpigzbakztzutpaviqihnmdiiasgjiskxidnxofivpaeweqtmxfzbszbrhcgwiddjlwrfadlpnoydurbntsmfdzwdtrfzdiq', 'wmtephbjjztetkjgvshvrcncxkoopdepfaxdyyucwuaktvrihgbraioxxzmybcrtcstecgawlulnrvebfdukqceqkteybutrdeegqimburvciuejrcglghqyyzfryuamhhhhegbvpnvzbgkfmpdquclggqbdutiofgrlexgjsqlsouzknmqiop', 'dpyvspanizoioareqxumndfovosolqukuqedztiyxrvqzxnahwjikakgvppuomchdxcbjjzgfbcxuxltytavtcvoogdpapduvoxjisojrsggix', 'wchptbpfdomqwwvyuxljusonfynrjsmyhcyizlnhnmmpcbazevacvdyjfnlseiboxgkwjibuzqwldfxzflnitiytuzweemxzmelbfwofvmp', 'aswvgdpaisrvieefgplakmdxceaettwtqokrgnsmjshcrsdkijuyubrcdawvcacpnbhtymxlueyjbivxjjejcltlbspymhstzgvakfmazcoabpsfwgzgdiwonjjyylcwtidlb', 'wchptbpfdomqwwvyuxljusonfynrjsmyhcyizlnhnmmpcbazevacvdyjfnlseiboxgkwjibuzqwldfxzflnitiytuzweemxzmelbfwvfmop', 'dpyvspanizoioareqxumndfovosolqukuqedztiyxrvqzxnahwjikakgvppuomchdxcbjjzgfbcxuxltytavtcvoogdpapduvoxjisojsxrgig', 'tqeqdsvgljqzmwspcpzxebrvhwqbkrntlyaatlxwqhwjwhlqddwirvvfqetidccfcmtcrijqoedwkomhfmmyihhxluxdfnsrlshakyiirlgzhelbkosfwnjuwmxlvsdufwfsetciljrloxwylqtftipceneisgmmltnabfavaojjiauowusuc', 'tqeqdsvgljqzmwspcpzxebrvhwqbkrntlyaatlxwqhwjwhlqddwirvvfqetidccfcmtcrijqoedwkomhfmmyihhxluxdfnsrlshakyiirlgzhelbkosfwnjuwmxlvsdufwfsetciljrloxwylqtftipceneisgmmltnabfavaojjiauowuusc', 'wmtephbjjztetkjgvshvrcncxkoopdepfaxdyyucwuaktvrihgbraioxxzmybcrtcstecgawlulnrvebfdukqceqkteybutrdeegqimburvciuejrcglghqyyzfryuamhhhhegbvpnvzbgkfmpdquclggqbdutiofgrlexgjsqlsouzknqpmoi', 'roshyprxualodxepwkdoldxadwfytpigzbakztzutpaviqihnmdiiasgjiskxidnxofivpaeweqtmxfzbszbrhcgwiddjlwrfadlpnoydurbntsmfdzwdtzdiqfr', 'wmtephbjjztetkjgvshvrcncxkoopdepfaxdyyucwuaktvrihgbraioxxzmybcrtcstecgawlulnrvebfdukqceqkteybutrdeegqimburvciuejrcglghqyyzfryuamhhhhegbvpnvzbgkfmpdquclggqbdutiofgrlexgjsqlsouzknqompi', 'vcexqjatwbxjehnkcblhmbpmrseoiwbutxqkqtbsjpcyvwufzpnqmbrftnkbdpzcvvynrplypwgehetgpxjwjpwcpykispwfibjhbpzrzqdeehrzatbknzpdipidhiesjylrwktlxjicyvh', 'wchptbpfdomqwwvyuxljusonfynrjsmyhcyizlnhnmmpcbazevacvdyjfnlseiboxgkwjibuzqwldfxzflnitiytuzweemxzmelbfwvopfm', 'zkrcxgagwosikssnqnpafpsqlrulvdhdpladwppeclxtttusasx', 'jcnfwrtjqfujmpcjpfccjjyjbyvgoxdkrizxofzpcixrwytzxpgwblsriekvriyclyiikfjfyubnnjklpjbrawdopetkzdlnsyreubd', 'zwwbkseciohdhpvhjtvsnvhagaxgkywicfmpfqooukcqdvnpdsnplevsluutahthfumtiyhifcituzmsdwrisbwgynytyruymhbthrwtdjgevphcufwbnxtswcjzpfxeaplujdditpljnagxgcbnktpafmltzslnmshdlnqgu', 'sqtakohgdhbpazssebjoogwwhkpsqvbzluqhjzjsljzraiqkorfkpayudgdmtsmpfybriyamhgyqzqfctskjjyawyzhmdeqtwtmiwnwrjtfloubdttduerzgcvekakcwernldifwnljrdwodgqacottqetvbdwafhenakphlnfmsolloe', 'yhbugiakqrqhk', 'gkskrydycvnolegdxyzhkhwqgnmozuxbzaefnlctnoqv', 'ffkjpfdjohgvjzqjeoduuadbdfaiqzqbwftlchcydnftjyhlducfznwlzwegagjuubqfdprtpbijhznvakozooxuaaxjunlviyxbwcnyrlarjopggyzsdeaucqdmuoqlwhvafwdawwdanqjpbvexbkkmjtbqoivojvhbnqh', 'aswvgdpaisrvieefgplakmdxceaettwtqokrgnsmjshcrsdkijuyubrcdawvcacpnbhtymxlueyjbivxjjejcltlbspymhstzgvakfmazcoabpsfwgzgdiwonjjyylcwibldt', 'wmtephbjjztetkjgvshvrcncxkoopdepfaxdyyucwuaktvrihgbraioxxzmybcrtcstecgawlulnrvebfdukqceqkteybutrdeegqimburvciuejrcglghqyyzfryuamhhhhegbvpnvzbgkfmpdquclggqbdutiofgrlexgjsqlsouzkoinqpm', 'hfsxpiljfurfpcmzgbmxjctdimhbkapmdsfzqlfohfwqhqgbdqvjsgzehgacetjrhmwfldxfvxraqnhymiszdazjusfauabwmyegwefkdomux', 'dorsnkxgsdiluzyaxvbuuttcnnslblablhz', 'nbpgsapqlzltn', 'vcexqjatwbxjehnkcblhmbpmrseoiwbutxqkqtbsjpcyvwufzpnqmbrftnkbdpzcvvynrplypwgehetgpxjwjpwcpykispwfibjhbpzrzqdeehrzatbknzpdipidhiesjylrwktlxjhivcy', 'idthirkitdtfkaylgyjgxsjtwjtsdjgyavleifrzwxpqueuxdmcshhioscanzlwsafzkkmipirtfbmkttcsyknpexymmsykvnkxzgburhyimafpnmawhsokqhrphlvkfvqpkseisrkhmynjntxgeziqvdq', 'tqeqdsvgljqzmwspcpzxebrvhwqbkrntlyaatlxwqhwjwhlqddwirvvfqetidccfcmtcrijqoedwkomhfmmyihhxluxdfnsrlshakyiirlgzhelbkosfwnjuwmxlvsdufwfsetciljrloxwylqtftipceneisgmmltnabfavaojjiauowucus', 'zkrcxgagwosikssnqnpafpsqlrulvdhdpladwppeclxttsxtsau', 'nucobgczdsynpwlmywgso', 'dpyvspanizoioareqxumndfovosolqukuqedztiyxrvqzxnahwjikakgvppuomchdxcbjjzgfbcxuxltytavtcvoogdpapduvoxjisojsgxrig', 'gkskrydycvnolegdxyzhkhwqgnmozuxbzaefnlctvqon', 'aq', 'aq', 'jcnfwrtjqfujmpcjpfccjjyjbyvgoxdkrizxofzpcixrwytzxpgwblsriekvriyclyiikfjfyubnnjklpjbrawdopetkzdlnsybderu', 'dorsnkxgsdiluzyaxvbuuttcnnslblbzahl', 'idthirkitdtfkaylgyjgxsjtwjtsdjgyavleifrzwxpqueuxdmcshhioscanzlwsafzkkmipirtfbmkttcsyknpexymmsykvnkxzgburhyimafpnmawhsokqhrphlvkfvqpkseisrkhmynjntxgidqqevz', 'wchptbpfdomqwwvyuxljusonfynrjsmyhcyizlnhnmmpcbazevacvdyjfnlseiboxgkwjibuzqwldfxzflnitiytuzweemxzmelbfwomvfp', 'wxweswnrucaaiekhznvyisduyepvddkeyzsyxcirwmuojhfczkmdqehprsjojdknlhvayzlomjwpwrxwrvsuuvaqgpysjukurgyzrhiehpwvhfclfazoxutcqehnkpcthoijnbiuxeoivwbjyqegpageiomcwnrmlxtixi', 'roshyprxualodxepwkdoldxadwfytpigzbakztzutpaviqihnmdiiasgjiskxidnxofivpaeweqtmxfzbszbrhcgwiddjlwrfadlpnoydurbntsmfdzwdtrqfdzi', 'aq', 'tygjwhphkgccwnnykucfoikcuidxpgohluvsxiumtqwgiazdbbacxetvbaj', 'wxweswnrucaaiekhznvyisduyepvddkeyzsyxcirwmuojhfczkmdqehprsjojdknlhvayzlomjwpwrxwrvsuuvaqgpysjukurgyzrhiehpwvhfclfazoxutcqehnkpcthoijnbiuxeoivwbjyqegpageiomcwnrmiilxxt', 'zkrcxgagwosikssnqnpafpsqlrulvdhdpladwppeclxttsuaxst', 'jcnfwrtjqfujmpcjpfccjjyjbyvgoxdkrizxofzpcixrwytzxpgwblsriekvriyclyiikfjfyubnnjklpjbrawdopetkzdlnsydeubr', 'zwwbkseciohdhpvhjtvsnvhagaxgkywicfmpfqooukcqdvnpdsnplevsluutahthfumtiyhifcituzmsdwrisbwgynytyruymhbthrwtdjgevphcufwbnxtswcjzpfxeaplujdditpljnagxgcbnktp