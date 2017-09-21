from django.shortcuts import render
from getpros.models import NA_Pros #, EUW_Pros, EUNE_Pros, KR_Pros, JP_Pros, BR_Pros, RU_Pros, LAN_Pros, LAS_Pros, OCE_Pros, TR_Pros
import cassiopeia as cass

def index(request):
    cass.set_riot_api_key("RGAPI-daa909e6-146f-4c9d-a03a-2ff08bac37be")
    cass.set_default_region("NA")
    na_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5')
#    euw_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='EUW')
#    eune_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='EUNE')
#    kr_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='KR')
#    jp_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='JP')
#    br_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='BR')
#    ru_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='RU')
#    lan_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='LAN')
#    las_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='LAS')
#    oce_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='OCE')
#    tr_challenger_players = cass.get_challenger_league(queue='RANKED_SOLO_5x5', region='TR')

    for p in na_challenger_players:
        obj, created = NA_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
        if created:
            print('Created entry: ' + obj.summoner_name)
        else:
            print('Found entry: ' + obj.summoner_name)
#    for p in euw_challenger_players:
#        obj, created = EUW_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in eune_challenger_players:
#        obj, created = EUNE_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in kr_challenger_players:
#        obj, created = KR_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in jp_challenger_players:
#        obj, created = JP_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in br_challenger_players:
#        obj, created = BR_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in ru_challenger_players:
#        obj, created = RU_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in lan_challenger_players:
#        obj, created = LAN_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in las_challenger_players:
#        obj, created = LAS_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in oce_challenger_players:
#        obj, created = OCE_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in tr_challenger_players:
#        obj, created = TR_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)

    na_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5')
#    euw_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='EUW')
#    eune_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='EUNE')
#    kr_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='KR')
#    jp_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='JP')
#    br_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='BR')
#    ru_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='RU')
#    lan_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='LAN')
#    las_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='LAS')
#    oce_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='OCE')
#    tr_master_players = cass.get_master_league(queue='RANKED_SOLO_5x5', region='TR')

    for p in na_master_players:
        obj, created = NA_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
        if created:
            print('Created entry: ' + obj.summoner_name)
        else:
            print('Found entry: ' + obj.summoner_name)
#    for p in euw_master_players:
#        obj, created = EUW_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in eune_master_players:
#        obj, created = EUNE_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in kr_master_players:
#        obj, created = KR_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in jp_master_players:
#        obj, created = JP_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in br_master_players:
#        obj, created = BR_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in ru_master_players:
#        obj, created = RU_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in lan_master_players:
#        obj, created = LAN_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in las_master_players:
#        obj, created = LAS_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in oce_master_players:
#        obj, created = OCE_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#    for p in tr_master_players:
#        obj, created = TR_Pros.objects.update_or_create(summoner_ID=p.summoner.id, defaults={'summoner_name':p.summoner.name})
#        if created:
#            print('Created entry: ' + obj.summoner_name)
#        else:
#            print('Found entry: ' + obj.summoner_name)
#
    return render(request, 'getpros/header.html')
