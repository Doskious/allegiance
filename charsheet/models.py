from django.db import models
from django.utils import timezone
from cms.models.pluginmodel import CMSPlugin


#class CharAttack(models.Model):
#    attack_name
#    attack_thit
#    attack_damg
#    attack_crit
#
#    def __unicode__(self):
#        return u'{0}'.format(self.attack_name)
#
#
#class CharSkill(models.Model):
#    skill_name
#    skill_bons
#
#    def __unicode__(self):
#        return u'{0}'.format(self.skill_name)


class CharSheet(CMSPlugin):
    char_name = models.CharField(max_length=50, default='Stranger')
#    char_clas
#    char_race
#    char_init
#    char_fort
#    char_refl
#    char_will
#    char_ac_s
#    char_ac_f
#    char_ac_t
#    char_acft
#    char_hp_m
#    char_bab
#    char_cmb
#    char_str
#    char_dex
#    char_con
#    char_int
#    char_wis
#    char_cha

    def __unicode__(self):
        return u'{0}'.format(self.char_name)
