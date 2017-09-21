from django.db import models

class NA_Pros(models.Model):
    summoner_ID = models.IntegerField(primary_key=True)
    summoner_name = models.CharField(max_length=16)
    last_match_ID = models.IntegerField(null=True)

#class EUW_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class EUNE_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class KR_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class JP_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class BR_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class RU_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class LAN_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class LAS_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class OCE_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)

#class TR_Pros(models.Model):
#    summoner_ID = models.IntegerField(primary_key=True)
#    summoner_name = models.CharField(max_length=16)
#    last_match_ID = models.IntegerField(null=True)
