from Misc import ad_libs


ind = ad_libs.select_ad_lib()
word_list = ad_libs.prompt_words(ind)
print(ad_libs.build_ad_lib(word_list, ind))
