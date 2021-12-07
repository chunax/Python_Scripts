import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os


nouveau_Anime_Episode_Name = ""
one_Piece_link = 'https://dbanimes.co/one-piece-'
fire_force_link = 'https://dbanimes.co/fire-force-saison-2-'
man_no_Inochi_link = 'https://dbanimes.co/100-man-no-inochi-no-ue-ni-ore-wa-tatteiru-'
akudama_drive_link = 'https://dbanimes.co/akudama-drive-'
dragon_quest_link = 'https://dbanimes.co/dragon-quest-the-adventure-of-dai-'
climbing_girls_link = 'https://dbanimes.co/iwa-kakeru-climbing-girls-'
yi_nian_yong_heng_link = 'https://dbanimes.co/yi-nian-yong-heng-'
moriarty_link = 'https://dbanimes.co/yuukoku-no-moriarty-saison-2-'
gymnastics_samourai_link = 'https://dbanimes.co/the-gymnastics-samurai-'
ikebukuro_link = 'https://dbanimes.co/ikebukuro-west-gate-park-'
noblesse_link = 'https://dbanimes.co/noblesse-'
the_day_i_became_a_god_link = 'https://dbanimes.co/the-day-i-became-a-god-'
munou_na_nana_link = 'https://dbanimes.co/munou-na-nana-'
SNK_link = 'https://dbanimes.co/shingeki-no-kyojin-saison-4-'
promised_neverland_link = 'https://dbanimes.co/the-promised-neverland-saison-2-'
hortensia_saga_link = 'https://dbanimes.co/hortensia-saga-'
soukou_musume_senki_link = 'https://dbanimes.co/soukou-musume-senki-'
slime_link = 'https://dbanimes.co/tensei-shitara-slime-datta-ken-saison-2-'
gotoubun_no_hanayome_link = 'https://dbanimes.co/gotoubun-no-hanayome-saison-2-'
back_arrow_link = 'https://dbanimes.co/back-arrow-'
sk8_the_infinity_link = 'https://dbanimes.co/sk8-the-infinity-'
mushoku_tensei_link = 'https://dbanimes.co/mushoku-tensei-jobless-reincarnation-'
kemono_jihen_link = 'https://dbanimes.co/kemono-jihen-'
a_will_eternal_link = 'https://dbanimes.co/a-will-eternal-'
horimiya_link = 'https://dbanimes.co/horimiya-'
dr_stone_link = 'https://dbanimes.co/dr-stone-saison-2-'
kumo_desu_ga_nani_ka_link = 'https://dbanimes.co/kumo-desu-ga-nani-ka-'
nanatsu_no_taizai_link = 'https://dbanimes.co/nanatsu-no-taizai-saison-4-'
mha_link = 'https://dbanimes.co/my-hero-academia-saison-5-episode-'
fruit_basket_link = 'https://dbanimes.co/fruits-basket-the-final-'
demon_slayer_link = 'https://dbanimes.co/demon-slayer-kimetsu-no-yaiba-saison-2-episode-'

one_Piece = 'One Piece '
liste_One_Piece = one_Piece.split()
man_no_Inochi = '100-man No Inochi No Ue Ni Ore Wa Tatteiru '
liste_Man = man_no_Inochi.split()
fire_force = 'Fire Force Saison 2 '
liste_FireForce = fire_force.split()
ikebukuro = 'Ikebukuro West Gate Park '
liste_Ikebukuro = ikebukuro.split()
akudama_drive = 'Akudama Drive '
liste_akudama_drive = akudama_drive.split()
dragon_quest = 'Dragon Quest The Adventure Of Dai '
liste_dragon_quest = dragon_quest.split()
climbing_girls = 'Iwa Kakeru! Climbing Girls '
liste_climbing_girls = climbing_girls.split()
yi_nian_yong_heng = 'Yi Nian Yong Heng '
liste_yi_nian_yong_heng = yi_nian_yong_heng.split()
moriarty = 'Yuukoku No Moriarty Saison 2 '
liste_moriarty = moriarty.split()
gymnastics_samourai = 'The Gymnastics Samurai '
liste_gymnastics_samourai = gymnastics_samourai.split()
noblesse = 'Noblesse '
liste_noblesse = noblesse.split()
the_day_i_became_a_god = 'The Day I Became A God '
liste_the_day_i_became_a_god = the_day_i_became_a_god.split()
munou_na_nana = 'Munou Na Nana '
liste_munou_na_nana = munou_na_nana.split()
SNK = 'Shingeki No Kyojin Saison 4 '
liste_SNK = SNK.split()
promised_neverland = 'The Promised Neverland Saison 2 '
liste_promised_neverland = promised_neverland.split()
hortensia_saga = 'Hortensia Saga '
liste_hortensia_saga = hortensia_saga.split()
soukou_musume_senki = 'Soukou Musume Senki '
liste_soukou_musume_senki = soukou_musume_senki.split()
slime = 'Tensei shitara Slime Datta Ken (Saison 2) '
liste_slime = slime.split()
gotoubun_no_hanayome = 'Gotoubun No Hanayome Saison 2 '
liste_gotoubun_no_hanayome = gotoubun_no_hanayome.split()
back_arrow = 'Back Arrow '
liste_back_arrow = back_arrow.split()
sk8_the_infinity = 'SK8 The Infinity '
liste_sk8_the_infinity = sk8_the_infinity.split()
mushoku_tensei = 'Mushoku Tensei: Jobless Reincarnation '
liste_mushoku_tensei = mushoku_tensei.split()
kemono_jihen = 'Kemono Jihen '
liste_kemono_jihen = kemono_jihen.split()
horimiya = 'Horimiya '
liste_horimiya = horimiya.split()
a_will_eternal = 'A Will Eternal '
liste_a_will_eternal = a_will_eternal.split()
dr_stone = 'Dr.STONE Saison 2 '
liste_dr_stone = dr_stone.split()
kumo_desu_ga_nani_ka = 'Kumo Desu Ga, Nani Ka? '
liste_kumo_desu_ga_nani_ka = kumo_desu_ga_nani_ka.split()
nanatsu_no_taizai = 'Nanatsu No Taizai Saison 4 '
liste_nanatsu_no_taizai = nanatsu_no_taizai.split()
mha = 'My Hero Academia Saison 5 Episode '
liste_mha = mha.split()
fruit_basket = 'Fruits Basket: The Final '
liste_fruit_basket = fruit_basket.split()
demon_slayer = 'Demon Slayer : Kimetsu no Yaiba Saison 2 Episode '
liste_demon_slayer = demon_slayer.split()

URL = 'https://dbanimes.co/'
vostfr_link = '-vostfr/'
vostfr_Episode = ' Vostfr'
grand_Vostfr = ' VOSTFR'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36'}


def findNewEpisodes():
    global nouveauEpisodeAnimeName
    one_Piece_Episode = 0
    man_No_Inochi_Episode = 0
    fire_Force_Episode = 0
    akudama_drive_Episode = 0
    dragon_quest_Episode = 0
    climbing_girls_Episode = 0
    yi_nian_yong_heng_Episode = 0
    moriarty_Episode = 0
    gymnastics_samourai_Episode = 0
    ikebukuro_Episode = 0
    noblesse_Episode = 0
    the_day_i_became_a_god_Episode = 0
    munou_na_nana_Episode = 0
    SNK_Episode = 0
    promised_neverland_Episode = 0
    hortensia_saga_Episode = 0
    soukou_musume_senki_Episode = 0
    slime_Episode = 0
    gotoubun_no_hanayome_Episode = 0
    back_arrow_Episode = 0
    sk8_the_infinity_Episode = 0
    mushoku_tensei_Episode = 0
    kemono_jihen_Episode = 0
    horimiya_Episode = 0
    a_will_eternal_Episode = 0
    dr_stone_Episode = 0
    kumo_desu_ga_nani_ka_Episode = 0
    nanatsu_no_taizai_Episode = 0
    mha_Episode = 0
    fruit_basket_Episode = 0
    demon_slayer_Episode = 0

    one_Piece_Bool = False
    man_no_Inochi_Bool = False
    fire_force_Bool = False
    akudama_drive_Bool = False
    dragon_quest_Bool = False
    climbing_girls_Bool = False
    yi_nian_yong_heng_Bool = False
    moriarty_Bool = False
    gymnastics_samourai_Bool = False
    ikebukuro_Bool = False
    noblesse_Bool = False
    the_day_i_became_a_god_Bool = False
    munou_na_nana_Bool = False
    SNK_bool = False
    promised_nerverland_Bool = False
    hortensia_saga_Bool = False
    soukou_musume_senki_Bool = False
    slime_Bool = False
    gotoubun_no_hanayome_Bool = False
    back_arrow_Bool = False
    sk8_the_infinity_Bool = False
    mushoku_tensei_Bool = False
    kemono_jihen_Bool = False
    horimiya_Bool = False
    a_will_eternal_Bool = False
    dr_stone_Bool = False
    kumo_desu_ga_nani_ka_Bool = False
    nanatsu_no_taizai_Bool = False
    mha_Bool = False
    fruit_basket_Bool = False
    demon_slayer_Bool = False

    f = open(r"/mnt/c/Users/maxim/Documents/Python_Scripts/animeEpisode.txt", 'r')
    for line in f:
        newline = line.split()
        egal = 0
        for i in newline:
            if i != '=':
                egal = egal+1
            if(newline[:egal-1] == liste_akudama_drive):
                akudama_drive_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_Ikebukuro):
                ikebukuro_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_One_Piece):
                one_Piece_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_gymnastics_samourai):
                gymnastics_samourai_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_climbing_girls):
                climbing_girls_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_dragon_quest):
                dragon_quest_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_FireForce):
                fire_Force_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_moriarty):
                moriarty_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_yi_nian_yong_heng):
                yi_nian_yong_heng_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_Man):
                man_No_Inochi_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_noblesse):
                noblesse_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_the_day_i_became_a_god):
                the_day_i_became_a_god_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_munou_na_nana):
                munou_na_nana_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_SNK):
                SNK_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_promised_neverland):
                promised_neverland_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_hortensia_saga):
                hortensia_saga_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_soukou_musume_senki):
                soukou_musume_senki_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_slime):
                slime_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_gotoubun_no_hanayome):
                gotoubun_no_hanayome_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_back_arrow):
                back_arrow_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_sk8_the_infinity):
                sk8_the_infinity_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_mushoku_tensei):
                mushoku_tensei_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_kemono_jihen):
                kemono_jihen_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_horimiya):
                horimiya_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_a_will_eternal):
                a_will_eternal_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_dr_stone):
                dr_stone_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_kumo_desu_ga_nani_ka):
                kumo_desu_ga_nani_ka_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_nanatsu_no_taizai):
                nanatsu_no_taizai_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_mha):
                mha_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_fruit_basket):
                fruit_basket_Episode = int(newline[len(newline)-1])
            if(newline[:egal-1] == liste_demon_slayer):
                demon_slayer_Episode = int(newline[len(newline)-1])

    f.close()
    new_akudama_drive_episode = akudama_drive + \
        str(akudama_drive_Episode) + vostfr_Episode
    new_ikebukuro_episode = ikebukuro + str(ikebukuro_Episode) + vostfr_Episode
    new_one_piece_episode = one_Piece + str(one_Piece_Episode) + grand_Vostfr
    new_gymnastics_samourai_episode = gymnastics_samourai + \
        str(gymnastics_samourai_Episode) + vostfr_Episode
    new_climbing_girls_episode = climbing_girls + \
        str(climbing_girls_Episode) + vostfr_Episode
    new_dragon_quest_episode = dragon_quest + \
        str(dragon_quest_Episode) + vostfr_Episode
    new_fire_force_episode = fire_force + \
        str(fire_Force_Episode) + vostfr_Episode
    new_moriarty_episode = moriarty + str(moriarty_Episode) + grand_Vostfr
    new_yi_nian_yong_heng_episode = yi_nian_yong_heng + \
        str(yi_nian_yong_heng_Episode) + vostfr_Episode
    new_man_no_Inochi_episode = man_no_Inochi + \
        str(man_No_Inochi_Episode) + vostfr_Episode
    new_noblesse_episode_bis = noblesse + str(noblesse_Episode) + ' VOSTFR'
    new_the_day_i_became_a_god_episode = the_day_i_became_a_god + \
        str(the_day_i_became_a_god_Episode) + vostfr_Episode
    new_munou_na_nana_episode = munou_na_nana + \
        str(munou_na_nana_Episode) + vostfr_Episode
    new_SNK_episode = SNK + str(SNK_Episode) + vostfr_Episode
    new_promised_neverland_episode = promised_neverland + \
        str(promised_neverland_Episode) + vostfr_Episode
    new_hortensia_saga_episode = hortensia_saga + \
        str(hortensia_saga_Episode) + vostfr_Episode
    new_soukou_musume_senki_episode = soukou_musume_senki + \
        str(soukou_musume_senki_Episode) + vostfr_Episode
    new_slime_episode = slime + str(slime_Episode) + grand_Vostfr
    new_gotoubun_no_hanayome_episode = gotoubun_no_hanayome + \
        str(gotoubun_no_hanayome_Episode) + vostfr_Episode
    new_back_arrow_episode = back_arrow + \
        str(back_arrow_Episode) + vostfr_Episode
    new_sk8_the_infinity_episode = sk8_the_infinity + \
        str(sk8_the_infinity_Episode) + vostfr_Episode
    new_mushoku_tensei_episode = mushoku_tensei + \
        str(mushoku_tensei_Episode) + grand_Vostfr
    new_kemono_jihen_episode = kemono_jihen + \
        str(kemono_jihen_Episode) + vostfr_Episode
    new_horimiya_episode = horimiya + str(horimiya_Episode) + vostfr_Episode
    new_a_will_eternal_episode = a_will_eternal + \
        str(a_will_eternal_Episode) + vostfr_Episode
    new_dr_stone_episode = dr_stone + str(dr_stone_Episode) + vostfr_Episode
    new_kumo_desu_ga_nani_ka_episode = kumo_desu_ga_nani_ka + \
        str(kumo_desu_ga_nani_ka_Episode) + vostfr_Episode
    new_nanatsu_no_taizai_episode = nanatsu_no_taizai + \
        str(nanatsu_no_taizai_Episode) + vostfr_Episode
    new_mha_episode = mha + str(mha_Episode) + grand_Vostfr
    new_fruit_basket_episode = fruit_basket + \
        str(fruit_basket_Episode) + vostfr_Episode
    new_demon_slayer_episode = demon_slayer + str(demon_slayer_Episode) + grand_Vostfr


    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.findAll('a')
    titleList = []
    for titre in title:
        titleList.append(titre.text)
    for i in range(len(titleList)):
        if(titleList[i] == new_akudama_drive_episode):
            akudama_drive_Bool = True
            nouveau_Anime_Episode_Name = 'Akudama Drive'
            link = akudama_drive_link + \
                str(akudama_drive_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_ikebukuro_episode):
            ikebukuro_Bool = True
            nouveau_Anime_Episode_Name = 'Ikebukuro'
            link = ikebukuro_link + str(ikebukuro_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_one_piece_episode):
            one_Piece_Bool = True
            nouveau_Anime_Episode_Name = 'One Piece'
            link = one_Piece_link + str(one_Piece_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_gymnastics_samourai_episode):
            gymnastics_samourai_Bool = True
            nouveau_Anime_Episode_Name = 'Gymnastics Samourai'
            link = gymnastics_samourai_link + \
                str(gymnastics_samourai_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_climbing_girls_episode):
            climbing_girls_Bool = True
            nouveau_Anime_Episode_Name = 'Climbing Girls'
            link = climbing_girls_link + \
                str(climbing_girls_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_dragon_quest_episode):
            dragon_quest_Bool = True
            nouveau_Anime_Episode_Name = 'Dragon Quest'
            link = dragon_quest_link + str(dragon_quest_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_fire_force_episode):
            fire_force_Bool = True
            nouveau_Anime_Episode_Name = 'Fire Force'
            link = fire_force_link + str(fire_Force_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_moriarty_episode):
            moriarty_Bool = True
            nouveau_Anime_Episode_Name = 'Moriarty'
            link = moriarty_link + str(moriarty_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_yi_nian_yong_heng_episode):
            yi_nian_yong_heng_Bool = True
            nouveau_Anime_Episode_Name = 'Yi Nian Yong Heng'
            link = yi_nian_yong_heng_link + \
                str(yi_nian_yong_heng_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_man_no_Inochi_episode):
            man_no_Inochi_Bool = True
            nouveau_Anime_Episode_Name = '100-man No Inochi No Ue Ni Ore Wa Tatteiru'
            link = man_no_Inochi_link + \
                str(man_No_Inochi_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_noblesse_episode_bis):
            noblesse_Bool = True
            nouveau_Anime_Episode_Name = 'Noblesse'
            link = noblesse_link + str(noblesse_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_the_day_i_became_a_god_episode):
            the_day_i_became_a_god_Bool = True
            nouveau_Anime_Episode_Name = 'The Day I Became A God'
            link = the_day_i_became_a_god_link + \
                str(the_day_i_became_a_god_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_munou_na_nana_episode):
            munou_na_nana_Bool = True
            nouveau_Anime_Episode_Name = 'Munou Na Nana'
            link = munou_na_nana_link + \
                str(munou_na_nana_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_SNK_episode):
            SNK_bool = True
            nouveau_Anime_Episode_Name = 'SNK'
            link = SNK_link + str(SNK_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_promised_neverland_episode):
            promised_nerverland_Bool = True
            nouveau_Anime_Episode_Name = 'The Promised Neverland'
            link = promised_neverland_link + \
                str(promised_neverland_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_hortensia_saga_episode):
            hortensia_saga_Bool = True
            nouveau_Anime_Episode_Name = 'Hortensia Saga'
            link = hortensia_saga_link + \
                str(hortensia_saga_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_soukou_musume_senki_episode):
            soukou_musume_senki_Bool = True
            nouveau_Anime_Episode_Name = 'Soukou Musume Senki'
            link = soukou_musume_senki_link + \
                str(soukou_musume_senki_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_slime_episode):
            slime_Bool = True
            nouveau_Anime_Episode_Name = 'Slime'
            link = slime_link + \
                str(slime_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_gotoubun_no_hanayome_episode):
            gotoubun_no_hanayome_Bool = True
            nouveau_Anime_Episode_Name = 'Gotoubun no hanayome'
            link = gotoubun_no_hanayome_link + \
                str(gotoubun_no_hanayome_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_back_arrow_episode):
            back_arrow_Bool = True
            nouveau_Anime_Episode_Name = 'Back Arrow'
            link = back_arrow_link + \
                str(back_arrow_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_sk8_the_infinity_episode):
            sk8_the_infinity_Bool = True
            nouveau_Anime_Episode_Name = 'SK8 The Infinity'
            link = sk8_the_infinity_link + \
                str(sk8_the_infinity_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_mushoku_tensei_episode):
            mushoku_tensei_Bool = True
            nouveau_Anime_Episode_Name = 'Mushoku Tensei'
            link = mushoku_tensei_link + \
                str(mushoku_tensei_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_kemono_jihen_episode):
            kemono_jihen_Bool = True
            nouveau_Anime_Episode_Name = 'Kemono Jihen'
            link = kemono_jihen_link + \
                str(kemono_jihen_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_horimiya_episode):
            horimiya_Bool = True
            nouveau_Anime_Episode_Name = 'Horimiya'
            link = horimiya_link + \
                str(horimiya_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_a_will_eternal_episode):
            a_will_eternal_Bool = True
            nouveau_Anime_Episode_Name = 'A Will Eternal'
            link = a_will_eternal_link + \
                str(a_will_eternal_Episode) + vostfr_link
            send_mail(link)
        if(titleList[i] == new_dr_stone_episode):
            dr_stone_Bool = True
            nouveau_Anime_Episode_Name = 'Dr.Stone'
            link = dr_stone_link + \
                str(dr_stone_Episode) + vostfr_link
            send_mail(link)

        if(titleList[i] == new_kumo_desu_ga_nani_ka_episode):
            kumo_desu_ga_nani_ka_Bool = True
            nouveau_Anime_Episode_Name = 'Kumo Desu Ga, Nani Ka?'
            link = kumo_desu_ga_nani_ka_link + \
                str(kumo_desu_ga_nani_ka_Episode) + vostfr_link
            send_mail(link)

        if(titleList[i] == new_nanatsu_no_taizai_episode):
            nanatsu_no_taizai_Bool = True
            nouveau_Anime_Episode_Name = 'Nanatsu no taizai'
            link = nanatsu_no_taizai_link + \
                str(nanatsu_no_taizai_Episode) + vostfr_link
            send_mail(link)

        if(titleList[i] == new_mha_episode):
            mha_Bool = True
            nouveau_Anime_Episode_Name = 'My Hero Academia'
            link = mha_link + \
                str(mha_Episode) + vostfr_link
            send_mail(link)

        if(titleList[i] == new_fruit_basket_episode):
            fruit_basket_Bool = True
            nouveau_Anime_Episode_Name = 'Fruit Basket'
            link = fruit_basket_link + \
                str(fruit_basket_Episode) + vostfr_link
            send_mail(link)

        if(titleList[i] == new_demon_slayer_episode):
            demon_slayer_Bool = True
            nouveau_Anime_Episode_Name = 'Demon slayer'
            link = demon_slayer_link + \
                str(demon_slayer_Episode) + vostfr_link
            send_mail(link)

    f = open(r"/mnt/c/Users/maxim/Documents/Python_Scripts/animeEpisode.txt", 'r')
    f2 = open(r"/mnt/c/Users/maxim/Documents/Python_Scripts/animeEpisode1.txt", 'w')
    for line in f:
        splitLane = line.split()
        egal = 0
        for i in splitLane:
            if i != '=':
                egal = egal+1
            if((splitLane[:egal-1] == liste_One_Piece) and one_Piece_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_One_Piece) and not one_Piece_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_Man) and man_no_Inochi_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_Man) and not man_no_Inochi_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_FireForce) and fire_force_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_FireForce) and not fire_force_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_akudama_drive) and akudama_drive_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_akudama_drive) and not akudama_drive_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_dragon_quest) and dragon_quest_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_dragon_quest) and not dragon_quest_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_climbing_girls) and climbing_girls_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_climbing_girls) and not climbing_girls_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_yi_nian_yong_heng) and yi_nian_yong_heng_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_yi_nian_yong_heng) and not yi_nian_yong_heng_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_moriarty) and moriarty_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_moriarty) and not moriarty_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_gymnastics_samourai) and gymnastics_samourai_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_gymnastics_samourai) and not gymnastics_samourai_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_Ikebukuro) and ikebukuro_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_Ikebukuro) and not ikebukuro_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_noblesse) and noblesse_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_noblesse) and not noblesse_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_the_day_i_became_a_god) and the_day_i_became_a_god_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_the_day_i_became_a_god) and not the_day_i_became_a_god_Bool):
                f2.write(line)

            elif((splitLane[:egal-1] == liste_munou_na_nana) and munou_na_nana_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif((splitLane[:egal-1] == liste_munou_na_nana) and not munou_na_nana_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_SNK) and SNK_bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_SNK) and not SNK_bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_promised_neverland) and promised_nerverland_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_promised_neverland) and not promised_nerverland_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_hortensia_saga) and hortensia_saga_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_hortensia_saga) and not hortensia_saga_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_soukou_musume_senki) and soukou_musume_senki_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_soukou_musume_senki) and not soukou_musume_senki_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_slime) and slime_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_slime) and not slime_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_gotoubun_no_hanayome) and gotoubun_no_hanayome_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_gotoubun_no_hanayome) and not gotoubun_no_hanayome_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_back_arrow) and back_arrow_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_back_arrow) and not back_arrow_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_sk8_the_infinity) and sk8_the_infinity_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_sk8_the_infinity) and not sk8_the_infinity_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_mushoku_tensei) and mushoku_tensei_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_mushoku_tensei) and not mushoku_tensei_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_kemono_jihen) and kemono_jihen_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_kemono_jihen) and not kemono_jihen_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_horimiya) and horimiya_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_horimiya) and not horimiya_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_a_will_eternal) and a_will_eternal_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_a_will_eternal) and not a_will_eternal_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_dr_stone) and dr_stone_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_dr_stone) and not dr_stone_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_kumo_desu_ga_nani_ka) and kumo_desu_ga_nani_ka_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_kumo_desu_ga_nani_ka) and not kumo_desu_ga_nani_ka_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_nanatsu_no_taizai) and nanatsu_no_taizai_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_nanatsu_no_taizai) and not nanatsu_no_taizai_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_mha) and mha_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_mha) and not mha_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_fruit_basket) and fruit_basket_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_fruit_basket) and not fruit_basket_Bool):
                f2.write(line)

            elif ((splitLane[:egal-1] == liste_demon_slayer) and demon_slayer_Bool):
                last = splitLane[len(splitLane)-1]
                splitLane[len(splitLane)-1] = str(int(last)+1)
                f2.write(" ".join(splitLane))
                f2.write("\n")
            elif ((splitLane[:egal-1] == liste_demon_slayer) and not demon_slayer_Bool):
                f2.write(line)

    f.close()
    f2.close()
    f = open(r"/mnt/c/Users/maxim/Documents/Python_Scripts/animeEpisode.txt", 'w')
    f2 = open(r"/mnt/c/Users/maxim/Documents/Python_Scripts/animeEpisode1.txt", 'r')
    for line in f2:
        f.write(line)
    f.close()
    f2.close()
    os.remove(r"/mnt/c/Users/maxim/Documents/Python_Scripts/animeEpisode1.txt")


def send_mail(animeLink):
    global nouveau_Anime_Episode_Name
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #https://www.youtube.com/watch?v=Bg9r_yLk7VY&t=600s 
    #lien pour un mdp pour les applications avec gmail
    server.login()
    subject = 'New ' + nouveau_Anime_Episode_Name + ' episode realeased'
    body = 'New episode of ' + nouveau_Anime_Episode_Name + \
        ' click on the link to see it ' + animeLink
    msg = 'Subject: {} \n\n{}'.format(subject, body)
    server.sendmail('adresse mail source', 'adresse mail destination', msg)
    print('EMAIL HAS BEEN SENT')
    server.quit()





# while True:
#     findNewEpisodes()
#     time.sleep(3600/2)
findNewEpisodes()
