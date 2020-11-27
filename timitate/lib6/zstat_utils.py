from pysc2.lib import ABILITY_ID, UNIT_TYPEID, UPGRADE_ID


BUILD_ORDER_ABILITY_CANDIDATES = [
    ABILITY_ID.BUILD_HATCHERY.value,
    ABILITY_ID.BUILD_SPINECRAWLER.value,
    ABILITY_ID.BUILD_SPORECRAWLER.value,
    ABILITY_ID.BUILD_EXTRACTOR.value,
    ABILITY_ID.BUILD_SPAWNINGPOOL.value,
    ABILITY_ID.BUILD_EVOLUTIONCHAMBER.value,
    ABILITY_ID.BUILD_ROACHWARREN.value,
    ABILITY_ID.BUILD_BANELINGNEST.value,
    ABILITY_ID.MORPH_LAIR.value,
    ABILITY_ID.BUILD_HYDRALISKDEN.value,
    ABILITY_ID.BUILD_LURKERDENMP.value,
    ABILITY_ID.BUILD_SPIRE.value,
    ABILITY_ID.BUILD_NYDUSNETWORK.value,
    ABILITY_ID.BUILD_NYDUSWORM.value,
    ABILITY_ID.BUILD_INFESTATIONPIT.value,
    ABILITY_ID.MORPH_HIVE.value,
    ABILITY_ID.MORPH_GREATERSPIRE.value,
    ABILITY_ID.BUILD_ULTRALISKCAVERN.value,
    ABILITY_ID.TRAIN_QUEEN.value,
    ABILITY_ID.TRAIN_ZERGLING.value,
    ABILITY_ID.TRAIN_BANELING.value,
    ABILITY_ID.TRAIN_ROACH.value,
    ABILITY_ID.MORPH_RAVAGER.value,
    ABILITY_ID.TRAIN_HYDRALISK.value,
    ABILITY_ID.MORPH_LURKER.value,
    ABILITY_ID.TRAIN_INFESTOR.value,
    ABILITY_ID.TRAIN_SWARMHOST.value,
    ABILITY_ID.TRAIN_ULTRALISK.value,
    ABILITY_ID.MORPH_OVERSEER.value,
    ABILITY_ID.MORPH_OVERLORDTRANSPORT.value,
    ABILITY_ID.TRAIN_MUTALISK.value,
    ABILITY_ID.TRAIN_CORRUPTOR.value,
    ABILITY_ID.MORPH_BROODLORD.value,
    ABILITY_ID.TRAIN_VIPER.value,
]

BUILD_ORDER_OBJECT_CANDIDATES = [
    UNIT_TYPEID.ZERG_HATCHERY.value,
    UNIT_TYPEID.ZERG_SPINECRAWLER.value,
    UNIT_TYPEID.ZERG_SPORECRAWLER.value,
    UNIT_TYPEID.ZERG_EXTRACTOR.value,
    UNIT_TYPEID.ZERG_SPAWNINGPOOL.value,
    UNIT_TYPEID.ZERG_EVOLUTIONCHAMBER.value,
    UNIT_TYPEID.ZERG_ROACHWARREN.value,
    UNIT_TYPEID.ZERG_BANELINGNEST.value,
    UNIT_TYPEID.ZERG_LAIR.value,
    UNIT_TYPEID.ZERG_HYDRALISKDEN.value,
    UNIT_TYPEID.ZERG_LURKERDENMP.value,
    UNIT_TYPEID.ZERG_SPIRE.value,
    UNIT_TYPEID.ZERG_NYDUSNETWORK.value,
    UNIT_TYPEID.ZERG_NYDUSCANAL.value,
    UNIT_TYPEID.ZERG_INFESTATIONPIT.value,
    UNIT_TYPEID.ZERG_HIVE.value,
    UNIT_TYPEID.ZERG_GREATERSPIRE.value,
    UNIT_TYPEID.ZERG_ULTRALISKCAVERN.value,
    UNIT_TYPEID.ZERG_QUEEN.value,
    UNIT_TYPEID.ZERG_ZERGLING.value,
    UNIT_TYPEID.ZERG_BANELING.value,
    UNIT_TYPEID.ZERG_ROACH.value,
    UNIT_TYPEID.ZERG_RAVAGER.value,
    UNIT_TYPEID.ZERG_HYDRALISK.value,
    UNIT_TYPEID.ZERG_LURKERMP.value,
    UNIT_TYPEID.ZERG_INFESTOR.value,
    UNIT_TYPEID.ZERG_SWARMHOSTMP.value,
    UNIT_TYPEID.ZERG_ULTRALISK.value,
    UNIT_TYPEID.ZERG_OVERSEER.value,
    UNIT_TYPEID.ZERG_OVERLORDTRANSPORT.value,
    UNIT_TYPEID.ZERG_MUTALISK.value,
    UNIT_TYPEID.ZERG_CORRUPTOR.value,
    UNIT_TYPEID.ZERG_BROODLORD.value,
    UNIT_TYPEID.ZERG_VIPER.value,
]

BUILD_ORDER_BUILDING_OBJECT_CANDIDATES = [
    UNIT_TYPEID.ZERG_HATCHERY.value,
    UNIT_TYPEID.ZERG_SPINECRAWLER.value,
    UNIT_TYPEID.ZERG_SPORECRAWLER.value,
    UNIT_TYPEID.ZERG_EXTRACTOR.value,
    UNIT_TYPEID.ZERG_SPAWNINGPOOL.value,
    UNIT_TYPEID.ZERG_EVOLUTIONCHAMBER.value,
    UNIT_TYPEID.ZERG_ROACHWARREN.value,
    UNIT_TYPEID.ZERG_BANELINGNEST.value,
    UNIT_TYPEID.ZERG_LAIR.value,
    UNIT_TYPEID.ZERG_HYDRALISKDEN.value,
    UNIT_TYPEID.ZERG_LURKERDENMP.value,
    UNIT_TYPEID.ZERG_SPIRE.value,
    UNIT_TYPEID.ZERG_NYDUSNETWORK.value,
    UNIT_TYPEID.ZERG_NYDUSCANAL.value,
    UNIT_TYPEID.ZERG_INFESTATIONPIT.value,
    UNIT_TYPEID.ZERG_HIVE.value,
    UNIT_TYPEID.ZERG_GREATERSPIRE.value,
    UNIT_TYPEID.ZERG_ULTRALISKCAVERN.value,
]

EFFECT_ABILITY_CANDIDATES = [
    ABILITY_ID.EFFECT_ABDUCT.value,
    ABILITY_ID.EFFECT_INJECTLARVA.value,
    ABILITY_ID.EFFECT_TRANSFUSION.value,
    ABILITY_ID.EFFECT_VIPERCONSUME.value,
    ABILITY_ID.EFFECT_NEURALPARASITE.value,
    ABILITY_ID.EFFECT_PARASITICBOMB.value,
    ABILITY_ID.EFFECT_CAUSTICSPRAY.value,
    ABILITY_ID.EFFECT_CONTAMINATE.value,
    ABILITY_ID.EFFECT_BLINDINGCLOUD.value,
    ABILITY_ID.EFFECT_CORROSIVEBILE.value,
    ABILITY_ID.EFFECT_FUNGALGROWTH.value,
    ABILITY_ID.EFFECT_INFESTEDTERRANS.value,
    ABILITY_ID.EFFECT_LOCUSTSWOOP.value,
    ABILITY_ID.EFFECT_SPAWNLOCUSTS.value,
    ABILITY_ID.EFFECT_SPAWNCHANGELING.value,
    ABILITY_ID.EFFECT_EXPLODE.value,
]

RESEARCH_ABILITY_CANDIDATES = [
    ABILITY_ID.RESEARCH_BURROW.value,
    ABILITY_ID.RESEARCH_CENTRIFUGALHOOKS.value,
    ABILITY_ID.RESEARCH_CHITINOUSPLATING.value,
    ABILITY_ID.RESEARCH_GLIALREGENERATION.value,
    ABILITY_ID.RESEARCH_MUSCULARAUGMENTS.value,
    ABILITY_ID.RESEARCH_NEURALPARASITE.value,
    ABILITY_ID.RESEARCH_TUNNELINGCLAWS.value,
    ABILITY_ID.RESEARCH_GROOVEDSPINES.value,
    ABILITY_ID.RESEARCH_PATHOGENGLANDS.value,
    ABILITY_ID.RESEARCH_PNEUMATIZEDCARAPACE.value,
    ABILITY_ID.RESEARCH_EVOLVEANABOLICSYNTHESIS2.value,
    ABILITY_ID.RESEARCH_ZERGFLYERARMORLEVEL1.value,
    ABILITY_ID.RESEARCH_ZERGFLYERARMORLEVEL2.value,
    ABILITY_ID.RESEARCH_ZERGFLYERARMORLEVEL3.value,
    ABILITY_ID.RESEARCH_ZERGFLYERATTACKLEVEL1.value,
    ABILITY_ID.RESEARCH_ZERGFLYERATTACKLEVEL2.value,
    ABILITY_ID.RESEARCH_ZERGFLYERATTACKLEVEL3.value,
    ABILITY_ID.RESEARCH_ZERGGROUNDARMORLEVEL1.value,
    ABILITY_ID.RESEARCH_ZERGGROUNDARMORLEVEL2.value,
    ABILITY_ID.RESEARCH_ZERGGROUNDARMORLEVEL3.value,
    ABILITY_ID.RESEARCH_ZERGMELEEWEAPONSLEVEL1.value,
    ABILITY_ID.RESEARCH_ZERGMELEEWEAPONSLEVEL2.value,
    ABILITY_ID.RESEARCH_ZERGMELEEWEAPONSLEVEL3.value,
    ABILITY_ID.RESEARCH_ZERGMISSILEWEAPONSLEVEL1.value,
    ABILITY_ID.RESEARCH_ZERGMISSILEWEAPONSLEVEL2.value,
    ABILITY_ID.RESEARCH_ZERGMISSILEWEAPONSLEVEL3.value,
    ABILITY_ID.RESEARCH_ZERGLINGADRENALGLANDS.value,
    ABILITY_ID.RESEARCH_ZERGLINGMETABOLICBOOST.value,
]

RESEARCH_OBJECT_CANDIDATES = [
    UPGRADE_ID.BURROW.value,
    UPGRADE_ID.CENTRIFICALHOOKS.value,
    UPGRADE_ID.CHITINOUSPLATING.value,
    UPGRADE_ID.GLIALRECONSTITUTION.value,
    UPGRADE_ID.EVOLVEMUSCULARAUGMENTS.value,
    UPGRADE_ID.NEURALPARASITE.value,
    UPGRADE_ID.TUNNELINGCLAWS.value,
    UPGRADE_ID.EVOLVEGROOVEDSPINES.value,
    UPGRADE_ID.INFESTORENERGYUPGRADE.value,
    UPGRADE_ID.OVERLORDSPEED.value,
    UPGRADE_ID.EVOLVEANABOLICSYNTHESIS.value,
    UPGRADE_ID.ZERGFLYERARMORSLEVEL1.value,
    UPGRADE_ID.ZERGFLYERARMORSLEVEL2.value,
    UPGRADE_ID.ZERGFLYERARMORSLEVEL3.value,
    UPGRADE_ID.ZERGFLYERWEAPONSLEVEL1.value,
    UPGRADE_ID.ZERGFLYERWEAPONSLEVEL2.value,
    UPGRADE_ID.ZERGFLYERWEAPONSLEVEL3.value,
    UPGRADE_ID.ZERGGROUNDARMORSLEVEL1.value,
    UPGRADE_ID.ZERGGROUNDARMORSLEVEL2.value,
    UPGRADE_ID.ZERGGROUNDARMORSLEVEL3.value,
    UPGRADE_ID.ZERGMELEEWEAPONSLEVEL1.value,
    UPGRADE_ID.ZERGMELEEWEAPONSLEVEL2.value,
    UPGRADE_ID.ZERGMELEEWEAPONSLEVEL3.value,
    UPGRADE_ID.ZERGMISSILEWEAPONSLEVEL1.value,
    UPGRADE_ID.ZERGMISSILEWEAPONSLEVEL2.value,
    UPGRADE_ID.ZERGMISSILEWEAPONSLEVEL3.value,
    UPGRADE_ID.ZERGLINGATTACKSPEED.value,
    UPGRADE_ID.ZERGLINGMOVEMENTSPEED.value,
]

SKILL_ABILITY_CANDIDATES = [
    ABILITY_ID.BUILD_CREEPTUMOR_QUEEN.value,
    ABILITY_ID.BUILD_CREEPTUMOR_TUMOR.value,
]

SKILL_OBJECT_CANDIDATES = [
    UNIT_TYPEID.ZERG_CREEPTUMORQUEEN.value,
    UNIT_TYPEID.ZERG_CREEPTUMOR.value,
]

STAT_ABILITY_CANDIDATES = BUILD_ORDER_ABILITY_CANDIDATES + SKILL_ABILITY_CANDIDATES + \
                          EFFECT_ABILITY_CANDIDATES + RESEARCH_ABILITY_CANDIDATES

STAT_OBJECT_CANDIDATES = BUILD_ORDER_OBJECT_CANDIDATES + SKILL_OBJECT_CANDIDATES

## Count bo order with 1.unit.orders[0], 2.untill unit is built
STAT_BO_ORDER_CANDIDATES = [
    ABILITY_ID.MORPH_LAIR.value,
    ABILITY_ID.MORPH_HIVE.value,
    ABILITY_ID.MORPH_GREATERSPIRE.value,
    ABILITY_ID.TRAIN_QUEEN.value,
    ABILITY_ID.TRAIN_ZERGLING.value,
    ABILITY_ID.TRAIN_BANELING.value,
    ABILITY_ID.TRAIN_ROACH.value,
    ABILITY_ID.MORPH_RAVAGER.value,
    ABILITY_ID.TRAIN_HYDRALISK.value,
    ABILITY_ID.MORPH_LURKER.value,
    ABILITY_ID.TRAIN_INFESTOR.value,
    ABILITY_ID.TRAIN_SWARMHOST.value,
    ABILITY_ID.TRAIN_ULTRALISK.value,
    ABILITY_ID.MORPH_OVERSEER.value,
    ABILITY_ID.MORPH_OVERLORDTRANSPORT.value,
    ABILITY_ID.TRAIN_MUTALISK.value,
    ABILITY_ID.TRAIN_CORRUPTOR.value,
    ABILITY_ID.MORPH_BROODLORD.value,
    ABILITY_ID.TRAIN_VIPER.value,
] + RESEARCH_ABILITY_CANDIDATES
STAT_BO_OBJECT_CANDIDATES = [
    UNIT_TYPEID.ZERG_HATCHERY.value,
    UNIT_TYPEID.ZERG_SPINECRAWLER.value,
    UNIT_TYPEID.ZERG_SPORECRAWLER.value,
    UNIT_TYPEID.ZERG_EXTRACTOR.value,
    UNIT_TYPEID.ZERG_SPAWNINGPOOL.value,
    UNIT_TYPEID.ZERG_EVOLUTIONCHAMBER.value,
    UNIT_TYPEID.ZERG_ROACHWARREN.value,
    UNIT_TYPEID.ZERG_BANELINGNEST.value,
    UNIT_TYPEID.ZERG_HYDRALISKDEN.value,
    UNIT_TYPEID.ZERG_LURKERDENMP.value,
    UNIT_TYPEID.ZERG_SPIRE.value,
    UNIT_TYPEID.ZERG_NYDUSNETWORK.value,
    UNIT_TYPEID.ZERG_NYDUSCANAL.value,
    UNIT_TYPEID.ZERG_INFESTATIONPIT.value,
    UNIT_TYPEID.ZERG_ULTRALISKCAVERN.value,
]


