from django.shortcuts import render
from .models import Quiz
from django.http import JsonResponse
from hitcount.views import HitCountMixin
from hitcount.models import HitCount 



# Home view
def index(request):
    return render(request, 'index.html')

def pinyin_quiz2(request):
    return render(request, 'pinyin_quiz2.html')

def pinyin_quiz3(request):
    return render(request, 'pinyin_quiz3.html')

def pinyin_quiz4(request):
    return render(request, 'pinyin_quiz4.html')

def pinyin_quiz5(request):
    return render(request, 'pinyin_quiz5.html')

def pinyinmatchtones1(request):
    return render(request, 'pinyinmatchtones1.html')

def pinyinmatchtones2(request):
    return render(request, 'pinyinmatchtones2.html')

def pinyinmatchtones3(request):
    return render(request, 'pinyinmatchtones3.html')

def pinyinmatchtones4(request):
    return render(request, 'pinyinmatchtones4.html')

def pinyinmatchtones5(request):
    return render(request, 'pinyinmatchtones5.html')

def pinyinmatchtones6(request):
    return render(request, 'pinyinmatchtones6.html')

def pinyinmatchtones7(request):
    return render(request, 'pinyinmatchtones7.html')

def pinyinmatchtones8(request):
    return render(request, 'pinyinmatchtones8.html')

def pinyinmatchtones9(request):
    return render(request, 'pinyinmatchtones9.html')

def pinyinmatchtones10(request):
    return render(request, 'pinyinmatchtones10.html')

def pinyinmatchtones11(request):
    return render(request, 'pinyinmatchtones11.html')

def pinyinmatchtones12(request):
    return render(request, 'pinyinmatchtones12.html')

def pinyinmatchtones13(request):
    return render(request, 'pinyinmatchtones13.html')

def pinyinmatchtones14(request):
    return render(request, 'pinyinmatchtones14.html')

def pinyinmatchtones15(request):
    return render(request, 'pinyinmatchtones15.html')

def pinyinmatchtones16(request):
    return render(request, 'pinyinmatchtones16.html')

def pinyinmatchtones17(request):
    return render(request, 'pinyinmatchtones17.html')

def pinyinmatchtones18(request):
    return render(request, 'pinyinmatchtones18.html')

def pinyinmatchtones19(request):
    return render(request, 'pinyinmatchtones19.html')

def pinyinmatchtones20(request):
    return render(request, 'pinyinmatchtones20.html')

def pinyinmatchtones21(request):
    return render(request, 'pinyinmatchtones21.html')

def pinyinmatchtones22(request):
    return render(request, 'pinyinmatchtones22.html')

def pinyinmatchtones23(request):
    return render(request, 'pinyinmatchtones23.html')

def pinyinmatchtones24(request):
    return render(request, 'pinyinmatchtones24.html')

def pinyinmatchtones25(request):
    return render(request, 'pinyinmatchtones25.html')

def pinyinmatchtones26(request):
    return render(request, 'pinyinmatchtones26.html')

def pinyinmatchtones27(request):
    return render(request, 'pinyinmatchtones27.html')

def pinyinmatchtones28(request):
    return render(request, 'pinyinmatchtones28.html')

def pinyinmatchtones29(request):
    return render(request, 'pinyinmatchtones29.html')

def pinyinmatchtones30(request):
    return render(request, 'pinyinmatchtones30.html')

def pinyinmatchtones31(request):
    return render(request, 'pinyinmatchtones31.html')

def pinyinmatchtones32(request):
    return render(request, 'pinyinmatchtones32.html')

def pinyinmatchtones33(request):
    return render(request, 'pinyinmatchtones33.html')

def pinyinmatchtones34(request):
    return render(request, 'pinyinmatchtones34.html')

def pinyinmatchtones35(request):
    return render(request, 'pinyinmatchtones35.html')

def pinyinmatchtones36(request):
    return render(request, 'pinyinmatchtones36.html')

def pinyinmatchtones37(request):
    return render(request, 'pinyinmatchtones37.html')

def pinyinmatchtones38(request):
    return render(request, 'pinyinmatchtones38.html')

def pinyinmatchtones39(request):
    return render(request, 'pinyinmatchtones39.html')

def pinyinmatchtones40(request):
    return render(request, 'pinyinmatchtones40.html')

def pinyinmatchtones41(request):
    return render(request, 'pinyinmatchtones41.html')

def amharic_numerals_match(request):
    return render(request, 'amharic_numerals_match.html')

def amharic_numerals_written(request):
    return render(request, 'amharic_numerals_written.html')

def english_names_to_amharic_matching3(request):
	return render(request, 'english_names_to_amharic_matching3.html')

def english_names_to_amharic_matching2(request):
	return render(request, 'english_names_to_amharic_matching2.html')

def ethiopian_names_match3(request):
	return render(request, 'ethiopian_names_match3.html')

def ethiopian_names_match2(request):
	return render(request, 'ethiopian_names_match2.html')

def ethiopian_cities_in_amharic(request):
	return render(request, 'ethiopian_cities_in_amharic.html')

def ethiopian_regions_in_amharic(request):
	return render(request, 'ethiopian_regions_in_amharic.html')

def ethiopian_names_match1(request):
	return render(request, 'ethiopian_names_match1.html')

def english_names_to_amharic_matching1(request):
	return render(request, 'english_names_to_amharic_matching1.html')

def famous_ethiopians_in_amharic(request):
	return render(request, 'famous_ethiopians_in_amharic.html')

def amharic_eng(request):
	return render(request, 'amharic_eng.html')

def eng_spelling_quiz1(request):
	return render(request, 'eng_spelling_quiz1.html')

def chinese_scrambled_pinyin(request):
	return render(request, 'chinese_scrambled_pinyin.html')

def romaji_to_hiragana1(request):
	return render(request, 'romaji_to_hiragana1.html')

def romaji_to_hiragana2(request):
	return render(request, 'romaji_to_hiragana2.html')

def hiragana_to_romaji2(request):
	return render(request, 'hiragana_to_romaji2.html')

def hiragana_to_romaji1(request):
	return render(request, 'hiragana_to_romaji1.html')

def japanese_eng(request):
	return render(request, 'japanese_eng.html')

def eng_spelling_quiz_2(request):
	return render(request, 'eng_spelling_quiz_2.html')

def yi_pinyin_to_yi_numeral_match(request):
	return render(request, 'yi_pinyin_to_yi_numeral_match.html')

def yi_listening_to_numerals(request):
	return render(request, 'yi_listening_to_numerals.html')

def yi_numeral_yi_to_arabic_numeral_match(request):
	return render(request, 'yi_numeral_yi_to_arabic_numeral_match.html')

def yi_zh(request):
	return render(request, 'yi_zh.html')

def yi_1_pinyin_to_character_match(request):
	return render(request, 'yi_1_pinyin_to_character_match.html')

def yi_1_listening_match_to_pinyin(request):
	return render(request, 'yi_1_listening_match_to_pinyin.html')

def yi_1_listening_match_to_charaters(request):
	return render(request, 'yi_1_listening_match_to_charaters.html')

def yi_1_character_to_pinyin_match(request):
	return render(request, 'yi_1_character_to_pinyin_match.html')

def eng_to_bengla_scrambled(request):
	return render(request, 'eng_to_bengla_scrambled.html')

def bengali(request):
	return render(request, 'bengali.html')

def eng_extra_letter_quiz1(request):
	return render(request, 'eng_extra_letter_quiz1.html')

def mhe(request):
	return render(request, 'mhe.html')

def mhe_1_colors_scrambled(request):
	return render(request, 'mhe_1_colors_scrambled.html')

def mhe_1_colors_extra_scrambled(request):
	return render(request, 'mhe_1_colors_extra_scrambled.html')

def mhe_2_animals_extra_scrambled(request):
	return render(request, 'mhe_2_animals_extra_scrambled.html')

def mhe_2_animals_scrambled(request):
	return render(request, 'mhe_2_animals_scrambled.html')

def mhe_3_action_verbs_scrambled(request):
	return render(request, 'mhe_3_action_verbs_scrambled.html')

def mhe_3_action_verbs_extra_scrambled(request):
	return render(request, 'mhe_3_action_verbs_extra_scrambled.html')

def abcd_sorting_game(request):
	return render(request, 'abcd_sorting_game.html')

def test(request):
	return render(request, 'test.html')

def mhe_5_body_parts_extra_scrambled(request):
	return render(request, 'mhe_5_body_parts_extra_scrambled.html')

def mhe_5_body_parts_scrambled(request):
	return render(request, 'mhe_5_body_parts_scrambled.html')

def mhe_6_lego_house_extra_scrambled(request):
	return render(request, 'mhe_6_lego_house_extra_scrambled.html')

def mhe_6_lego_house_scrambled(request):
	return render(request, 'mhe_6_lego_house_scrambled.html')

def abcd_scrambled_words(request):
	return render(request, 'abcd_scrambled_words.html')

def image_quiz(request):
	return render(request, 'image_quiz.html')

def mhe_7_classroom_scrambled(request):
	return render(request, 'mhe_7_classroom_scrambled.html')

def mhe_7_classroom_extra_scrambled(request):
	return render(request, 'mhe_7_classroom_extra_scrambled.html')

def mhe_7_classroom_image_quiz(request):
	return render(request, 'mhe_7_classroom_image_quiz.html')

def mhe_31_school_supplies_scrambled(request):
	return render(request, 'mhe_31_school_supplies_scrambled.html')

def mhe_31_school_supplies_extra_scrambled(request):
	return render(request, 'mhe_31_school_supplies_extra_scrambled.html')

def mhe_31_school_supplies_image_quiz(request):
	return render(request, 'mhe_31_school_supplies_image_quiz.html')

def mhe_29_baby_extra_scrambled(request):
	return render(request, 'mhe_29_baby_extra_scrambled.html')

def mhe_29_baby_image_quiz(request):
	return render(request, 'mhe_29_baby_image_quiz.html')

def mhe_29_baby_scrambled(request):
	return render(request, 'mhe_29_baby_scrambled.html')
	
def business_vocabulary_primary(request):
	return render(request, 'business_vocabulary_primary.html')

def business_vocabulary_primary_extra_letter(request):
	return render(request, 'business_vocabulary_primary_extra_letter.html')

def english_for_subjects(request):
	return render(request, 'english_for_subjects.html')

def mhe_30_clothes_image_quiz(request):
	return render(request, 'mhe_30_clothes_image_quiz.html')

def mhe_30_clothes_scrambled(request):
	return render(request, 'mhe_30_clothes_scrambled.html')

def mhe_30_clothes_extra_scrambled(request):
	return render(request, 'mhe_30_clothes_extra_scrambled.html')

def mhe_11_vehicles_extra_scrambled(request):
	return render(request, 'mhe_11_vehicles_extra_scrambled.html')

def mhe_11_vehicles_image_quiz(request):
	return render(request, 'mhe_11_vehicles_image_quiz.html')

def mhe_11_vehicles_scrambled(request):
	return render(request, 'mhe_11_vehicles_scrambled.html')

def mhe_8_general_foods_extra_scrambled_yellow_letters(request):
	return render(request, 'mhe_8_general_foods_extra_scrambled_yellow_letters.html')

def mhe_8_general_foods_image_quiz(request):
	return render(request, 'mhe_8_general_foods_image_quiz.html')

def mhe_8_general_foods_extra_scrambled(request):
	return render(request, 'mhe_8_general_foods_extra_scrambled.html')

def mhe_6_spring_fruit_image_quiz(request):
	return render(request, 'mhe_6_spring_fruit_image_quiz.html')

def mhe_6_spring_fruit_extra_scrambled(request):
	return render(request, 'mhe_6_spring_fruit_extra_scrambled.html')

def mhe_6_spring_fruit_scrambled_yellow_letters(request):
	return render(request, 'mhe_6_spring_fruit_scrambled_yellow_letters.html')

def yi_script_table(request):
	return render(request, 'yi_script_table.html')

def mhe_19_insects_image_quiz(request):
	return render(request, 'mhe_19_insects_image_quiz.html')
    
def quiz_list(request):
    quiz_list = Quiz.objects.all()
    return render(request,'quiz_list.html',{'quiz_list':quiz_list})

def quiz_list_api(request,id):
    quiz_list = Quiz.objects.get(id=id)
    data = {
        'data' : quiz_list.data
    }
    return JsonResponse(data)

def quiz_details(request, slug):
    quiz = Quiz.objects.get(slug=slug)
    hit_count_obj = HitCount.objects.get_for_object(quiz)
    hit_count = HitCountMixin()
    hit_count.hit_count(request, hit_count_obj)
    hit_count_obj.refresh_from_db()  # Refresh the object to get updated values
    return render(request, 'quiz_details.html', {'quiz': quiz, 'hit_count_obj': hit_count_obj})


def mhe_07_vegetables_image_quiz(request):
	return render(request, 'mhe_07_vegetables_image_quiz.html')
	
def quiz_mhe_07_vegetables_scrambled(request):
    # Fetch the quiz object and any other necessary data
    quiz = Quiz.objects.get(slug='mhe_07_vegetables_scrambled')
    # Pass the quiz object to the template
    return render(request, 'quiz_details.html', {'quiz': quiz})

def quiz_mhe_07_vegetables_extra_scrambled_yellow_letters(request):
    # Fetch the quiz object and any other necessary data
    quiz = Quiz.objects.get(slug='mhe_07_vegetables_extra_scrambled_yellow_letters')
    # Pass the quiz object to the template
    return render(request, 'quiz_details.html', {'quiz': quiz})

def quiz_mhe_07_vegetables_scrambled(request):
    # Fetch the quiz object and any other necessary data
    quiz = Quiz.objects.get(slug='mhe_07_vegetables_scrambled')
    # Pass the quiz object to the template
    return render(request, 'quiz_details.html', {'quiz': quiz})

def quiz_mhe_07_vegetables_scrambled_yellow_letters(request):
    # Fetch the quiz object and any other necessary data
    quiz = Quiz.objects.get(slug='mhe_07_vegetables_scrambled_yellow_letters')
    # Pass the quiz object to the template
    return render(request, 'quiz_details.html', {'quiz': quiz})

def mhe_35_summer_clothes_image_quiz(request):
	return render(request, 'mhe_35_summer_clothes_image_quiz.html')
	
def pinyin_quiz6(request):
	return render(request, 'pinyin_quiz6.html')

def eng_quiz3(request):
	return render(request, 'eng_quiz3.html')

def eng_quiz4(request):
	return render(request, 'eng_quiz4.html')

def mhe_22_illness_scrambled(request):
	return render(request, 'mhe_22_illness_scrambled.html')

def mhe_22_illness_image_quiz(request):
	return render(request, 'mhe_22_illness_image_quiz.html')
	
def mhe_22_illness_image_quiz(request):
	return render(request, 'mhe_22_illness_image_quiz.html')

def mhe_24_numbers_1_to_12_image_quiz(request):
	return render(request, 'mhe_24_numbers_1_to_12_image_quiz.html')

def mhe_24_numbers_1_to_12_scrambled_letters(request):
	return render(request, 'mhe_24_numbers_1_to_12_scrambled_letters.html')

def mhe_24_numbers_1_to_12_scrambled_extra_letters(request):
	return render(request, 'mhe_24_numbers_1_to_12_scrambled_extra_letters.html')

def mhe_24_numbers_1_to_12_yellow_scrambled_letters(request):
	return render(request, 'mhe_24_numbers_1_to_12_yellow_scrambled_letters.html')

def mhe_24_numbers_1_to_12_yellow_scrambled_extra_letters(request):
	return render(request, 'mhe_24_numbers_1_to_12_yellow_scrambled_extra_letters.html')










