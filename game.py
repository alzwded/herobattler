#!/usr/bin/env python3
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
# 
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>.

from enum import Enum
from math import sqrt
import random

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    PURPLE = 4
    YELLOW = 5

COLOR_MODIFIERS = {
    Color.RED : {
        Color.RED : 1,
        Color.GREEN : 2,
        Color.BLUE : 0.8,
        Color.PURPLE : 1,
        Color.YELLOW : 1
    },
    Color.GREEN : {
        Color.RED : 0.8,
        Color.GREEN : 1,
        Color.BLUE : 2,
        Color.PURPLE : 1,
        Color.YELLOW : 1
    },
    Color.BLUE : {
        Color.RED : 2,
        Color.GREEN : 0.8,
        Color.BLUE : 1,
        Color.PURPLE : 0, 
        Color.YELLOW : 0
    },
    Color.PURPLE : {
        Color.RED : 1,
        Color.GREEN : 1,
        Color.BLUE : 1,
        Color.PURPLE : 1,
        Color.YELLOW : 2
    },
    Color.YELLOW : {
        Color.RED : 1,
        Color.GREEN : 1,
        Color.BLUE : 1,
        Color.PURPLE : 2,
        Color.YELLOW : 1
    },
}

class SkillTalent:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def target_enemy(self):
        return False

    def aoe(self):
        return False

    def hp(self):
        return False

    def atk(self):
        return False

    def dfn(self):
        return False

    def eva(self):
        return False

    def crit(self):
        return False

    def hp(self):
        return False

# dmg
class FireArrow(SkillTalent):
    def __init__(self):
        super().__init__("Fire Arrow")

    def target_enemy(self):
        return True

    def hp(self):
        return True

class Mindflay(SkillTalent):
    def __init__(self):
        super().__init__("Mindflay")

    def target_enemy(self):
        return True

    def hp(self):
        return True

class Smite(SkillTalent):
    def __init__(self):
        super().__init__("Smite")

    def target_enemy(self):
        return True

    def hp(self):
        return True

class Bash(SkillTalent):
    def __init__(self):
        super().__init__("Bash")

    def target_enemy(self):
        return True

    def hp(self):
        return True

class Backstab(SkillTalent):
    def __init__(self):
        super().__init__("Backstab")

    def target_enemy(self):
        return True

    def hp(self):
        return True

class AimedShot(SkillTalent):
    def __init__(self):
        super().__init__("AimedShot")

    def target_enemy(self):
        return True

    def hp(self):
        return True

# DMG
class FireBall(SkillTalent):
    def __init__(self):
        super().__init__("Fire Ball")

    def target_enemy(self):
        return True

    def aoe(self):
        return True

    def hp(self):
        return True

# DMG
class Blizzard(SkillTalent):
    def __init__(self):
        super().__init__("Blizzard")

    def target_enemy(self):
        return True

    def aoe(self):
        return True

    def hp(self):
        return True

class Whirlwind(SkillTalent):
    def __init__(self):
        super().__init__("Whirlwind")

    def target_enemy(self):
        return True

    def aoe(self):
        return True

    def hp(self):
        return True

# CHARM
class Terror(SkillTalent):
    def __init__(self):
        super().__init__("Terror")

    def target_enemy(self):
        return True

    def aoe(self):
        return True

    def atk(self):
        return True

    def eva(self):
        return True

class BellyDance(SkillTalent):
    def __init__(self):
        super().__init__("Belly Dance")

    def target_enemy(self):
        return True

    def aoe(self):
        return True

    def atk(self):
        return True

    def eva(self):
        return True


# charm
class Charm(SkillTalent):
    def __init__(self):
        super().__init__("Charm")

    def target_enemy(self):
        return True

    def atk(self):
        return True

    def eva(self):
        return True

class Intimidate(SkillTalent):
    def __init__(self):
        super().__init__("Intimidate")

    def target_enemy(self):
        return True

    def atk(self):
        return True

    def eva(self):
        return True

class SuppressiveFire(SkillTalent):
    def __init__(self):
        super().__init__("SuppressiveFire")

    def target_enemy(self):
        return True

    def atk(self):
        return True

    def eva(self):
        return True

# debuff
class Weaken(SkillTalent):
    def __init__(self):
        super().__init__("Weaken")

    def target_enemy(self):
        return True

    def dfn(self):
        return True

    def crit(self):
        return True

class Frostbite(SkillTalent):
    def __init__(self):
        super().__init__("Frostbite")

    def target_enemy(self):
        return True

    def dfn(self):
        return True

    def crit(self):
        return True

class Overpower(SkillTalent):
    def __init__(self):
        super().__init__("Overpower")

    def target_enemy(self):
        return True

    def dfn(self):
        return True

    def crit(self):
        return True

class Feint(SkillTalent):
    def __init__(self):
        super().__init__("Feint")

    def target_enemy(self):
        return True

    def dfn(self):
        return True

    def crit(self):
        return True

class ShieldBash(SkillTalent):
    def __init__(self):
        super().__init__("Shield Bash")

    def target_enemy(self):
        return True

    def dfn(self):
        return True

    def crit(self):
        return True

# DEBUFF
class DarkCloud(SkillTalent):
    def __init__(self):
        super().__init__("Dark Cloud")

    def target_enemy(self):
        return True

    def aoe(self):
        return True

    def dfn(self):
        return True

    def crit(self):
        return True

class EntanglingRoots(SkillTalent):
    def __init__(self):
        super().__init__("Entangling Roots")

    def target_enemy(self):
        return True

    def aoe(self):
        return True

    def dfn(self):
        return True

    def crit(self):
        return True

# heal
class Heal(SkillTalent):
    def __init__(self):
        super().__init__("Heal")

    def hp(self):
        return True

# HEAL
class Miracle(SkillTalent):
    def __init__(self):
        super().__init__("Miracle")

    def aoe(self):
        return True

    def hp(self):
        return True

class NaturesReward(SkillTalent):
    def __init__(self):
        super().__init__("Nature's Reward")

    def aoe(self):
        return True

    def hp(self):
        return True

# shield
class Shield(SkillTalent):
    def __init__(self):
        super().__init__("Shield")

    def dfn(self):
        return True

class ReleaseBeast(SkillTalent):
    def __init__(self):
        super().__init__("Release Beast")

    def dfn(self):
        return True

# SHIELD
class Barrier(SkillTalent):
    def __init__(self):
        super().__init__("Shield")

    def aoe(self):
        return True

    def dfn(self):
        return True

# buff
class Strengthen(SkillTalent):
    def __init__(self):
        super().__init__("Strengthen")

    def atk(self):
        return True

# BUFF
class Inspire(SkillTalent):
    def __init__(self):
        super().__init__("Inspire")

    def aoe(self):
        return True

    def atk(self):
        return True

class Tonic(SkillTalent):
    def __init__(self):
        super().__init__("Tonic")

    def aoe(self):
        return True

    def atk(self):
        return True

# evade
class Evade(SkillTalent):
    def __init__(self):
        super().__init__("Evade")

    def eva(self):
        return True

class Jig(SkillTalent):
    def __init__(self):
        super().__init__("Jig")

    def eva(self):
        return True

# EVADE
class Shroud(SkillTalent):
    def __init__(self):
        super().__init__("Shroud")

    def aoe(self):
        return True

    def eva(self):
        return True

# crit
class Focus(SkillTalent):
    def __init__(self):
        super().__init__("Focus")

    def crit(self):
        return True

# CRIT
class Song(SkillTalent):
    def __init__(self):
        super().__init__("Song")

    def aoe(self):
        return True

    def crit(self):
        return True

class Enhancement(SkillTalent):
    def __init__(self):
        super().__init__("Enhancement")

    def aoe(self):
        return True

    def crit(self):
        return True

class Hero:
    def __init__(self, name, rank, color, skill, talent):
        self.name = name
        self.rank = rank
        self.color = color
        self.skill = skill
        self.talent = talent
        self.__is_dead = self.name == '<Nobody>'

    def __str__(self):
        return "{} (Rank {} {}): {}/{}".format(
                self.name,
                self.rank,
                self.color,
                self.skill,
                self.talent
               )

    def is_dead(self):
        return self.__is_dead

HEROES = [
    Hero("Saint", 3, Color.YELLOW, Inspire(), Miracle()),
    Hero("Priest", 2, Color.YELLOW, Shield(), Miracle()),
    Hero("Deacon", 2, Color.YELLOW, Heal(), Inspire()),
    Hero("Paladin", 1, Color.YELLOW, Shield(), Smite()),
    Hero("Monk", 1, Color.YELLOW, Evade(), Strengthen()),
    Hero("Zealot", 1, Color.YELLOW, Focus(), Heal()),

    Hero("Daemon", 3, Color.PURPLE, Intimidate(), DarkCloud()),
    Hero("Dark Magician", 2, Color.PURPLE, Weaken(), Shroud()),
    Hero("Wralock", 2, Color.PURPLE, Weaken(), DarkCloud()),
    Hero("Assassin", 1, Color.PURPLE, Evade(), Backstab()),
    Hero("Sniper", 1, Color.PURPLE, Focus(), Evade()),
    Hero("Gnuman", 1, Color.PURPLE, AimedShot(), SuppressiveFire()),

    Hero("Pyromancer", 3, Color.RED, FireArrow(), FireBall()),
    Hero("Templar", 2, Color.RED, ShieldBash(), Whirlwind()),
    Hero("Bard", 2, Color.RED, Inspire(), Song()),
    Hero("Hunter", 1, Color.RED, Focus(), Evade()),
    Hero("Fencer", 1, Color.RED, Feint(), Focus()),
    Hero("Barbarian", 1, Color.RED, Strengthen(), Bash()),

    Hero("Geomancer", 3, Color.GREEN, Strengthen(), Barrier()),
    Hero("Druid", 2, Color.GREEN, EntanglingRoots(), NaturesReward()),
    Hero("Defender", 2, Color.GREEN, Shield(), Barrier()),
    Hero("Beastmaster", 1, Color.GREEN, Charm(), ReleaseBeast()), # review this later
    Hero("Swordsman", 1, Color.GREEN, Focus(), Feint()),
    Hero("Gladiator", 1, Color.GREEN, Overpower(), Bash()),

    Hero("Hydromancer", 3, Color.BLUE, Frostbite(), Blizzard()),
    Hero("Alchemist", 2, Color.BLUE, Enhancement(), Tonic()),
    Hero("Dancer", 2, Color.BLUE, Jig(), BellyDance()),
    Hero("Witch", 1, Color.BLUE, Charm(), Weaken()),
    Hero("Psionic", 1, Color.BLUE, Weaken(), Mindflay()),
    Hero("Slinger", 1, Color.BLUE, Focus(), AimedShot()),

    Hero("<Nobody>", 0, Color.YELLOW, Heal(), Heal())
]

# (dups, levels)
HERO_COLLECTION = [
    (1, 1),
    (0, 0),
    (0, 0),
    (4, 3),
    (0, 0)
]

# maybe this should just be "screens"
class Phase(Enum):
    NEWACCOUNT = 0
    PREPARE_ADVENTURE = 1
    PRE_BATTLE = 2
    IN_BATTLE = 3
    ADVENTURE_DONE = 4

class Buffs:
    def __init__(self):
        self.atk = 0
        self.dfn = 0
        self.eva = 0
        self.crit = 0

    def __str__(self):
        return "{}+a {}+d {}+e {}+c".format(
            self.atk,
            self.dfn,
            self.eva,
            self.crit)

class Stats:
    def __init__(self, rank, dups, levels):
        duppow = pow(1.1, dups-1)
        self.hpmax = (100 + 10 * levels) * sqrt(rank) * duppow
        self.hp = self.hpmax
        self.turnsUntilSkill = random.randint(2, 3)
        self.resource = 0
        self.atk = (10 + levels - 1) * sqrt(rank) * duppow
        self.dfn = (10 + levels - 1) * sqrt(rank) * duppow
        self.eva = 25 #%
        self.crit = 25 #%

    def __str__(self):
        return "{:.0f}/{:.0f}hp {}/3sk {}/4tl {:.0f}a {:.0f}d {:.0f}e {:.0f}c".format(
            self.hp, self.hpmax,
            4 - self.turnsUntilSkill,
            self.resource,
            self.atk,
            self.dfn,
            self.eva,
            self.crit)

    def resetTurnsUntilSkill(self):
        self.turnsUntilSkill = random.randint(2, 3)

class HeroInstance:
    def __init__(self, hero, dups, levels, stats = None, buffs = None):
        self.hero = hero
        self.dups = dups
        self.levels = levels
        if buffs is None:
            self.buffs = Buffs()
        else:
            self.buffs = buffs
        if stats is None:
            self.stats = Stats(hero.rank, dups, levels)
        else:
            self.stats = stats

    def __str__(self):
        return "{} *{} +{}: {} ({})".format(
            self.hero if not self.hero.is_dead() else '<Nobody>',
            self.dups,
            self.levels,
            self.stats,
            self.buffs)

    def resetBuffs(self):
        self.buffs = Buffs()

    def __attack(self, enemy, scale = 1.0, special = False):
        BASE_DAMAGE=45
        if enemy.hero.is_dead():
            return

        color_modifier = COLOR_MODIFIERS[self.hero.color][enemy.hero.color]

        eva = enemy.stats.eva * pow(1.1, self.buffs.eva)
        #if not special and random.randint(1, 100) < eva:
        if random.randint(1, 100) < eva:
            return
        crit = self.stats.crit * pow(1.1, self.buffs.crit)
        crit_modifier = 1
        if special:
            crit_modifier = 2
        elif random.randint(1, 100) < crit:
            crit_modifier = 2
        atk = self.stats.atk * pow(1.1, self.buffs.atk)
        dfn = enemy.stats.dfn * pow(1.1, enemy.buffs.dfn)
        atk_dfn_modifier = atk / dfn
        enemy.stats.hp = enemy.stats.hp - crit_modifier * atk_dfn_modifier * BASE_DAMAGE * scale
        if(enemy.stats.hp < 0):
            enemy.stats.hp = 0
            enemy.hero = HEROES[len(HEROES)-1]
        if(enemy.stats.hp > enemy.stats.hpmax):
            enemy.stats.hp = enemy.stats.hpmax
        enemy.stats.resource = enemy.stats.resource + 1

    def __skill(self, enemyc, enemy2, enemy3, hero2, hero3):
        self.__skilltalent(self.hero.skill, enemyc, enemy2, enemy3, hero2, hero3)
        self.stats.resetTurnsUntilSkill()
        self.stats.resource = self.stats.resource + 2
        hero2.stats.resource = hero2.stats.resource + 1
        hero3.stats.resource = hero3.stats.resource + 1

    def __talent(self, enemyc, enemy2, enemy3, hero2, hero3):
        #print('pre-skilltalent: ', self, hero2, hero3, enemyc, enemy2, enemy3)
        self.__skilltalent(self.hero.talent, enemyc, enemy2, enemy3, hero2, hero3)
        self.stats.resource = 0
        #print('post-skilltalent: ', self, hero2, hero3, enemyc, enemy2, enemy3)

    def __skilltalent(self, skilltalent, enemyc, enemy2, enemy3, hero2, hero3):
        if skilltalent.target_enemy():
            if skilltalent.aoe():
                heroes = [(enemyc, 1), (enemy2, 0.5), (enemy3, 0.5)]
            else:
                heroes = [(enemyc, 1)]
            if skilltalent.hp():
                for t in heroes:
                    h, m = t
                    self.__attack(h, m, True)
            if skilltalent.atk():
                for t in heroes:
                    h, m = t
                    h.buffs.atk = h.buffs.atk - 1
            if skilltalent.dfn():
                for t in heroes:
                    h, m = t
                    h.buffs.dfn = h.buffs.dfn - 1
            if skilltalent.crit():
                for t in heroes:
                    h, m = t
                    h.buffs.crit = h.buffs.crit - 1
            if skilltalent.eva():
                for t in heroes:
                    h, m = t
                    h.buffs.eva = h.buffs.eva - 1
        else:
            if skilltalent.aoe():
                heroes = [(self, 1), (hero2, 0.5), (hero3, 0.5)]
            else:
                heroes = [(self, 1)]
            if skilltalent.hp():
                for t in heroes:
                    h, m = t
                    self.__attack(h, -m, True)
            if skilltalent.atk():
                for t in heroes:
                    h, m = t
                    h.buffs.atk = h.buffs.atk + 1
            if skilltalent.dfn():
                for t in heroes:
                    h, m = t
                    h.buffs.dfn = h.buffs.dfn + 1
            if skilltalent.crit():
                for t in heroes:
                    h, m = t
                    h.buffs.crit = h.buffs.crit + 1
            if skilltalent.eva():
                for t in heroes:
                    h, m = t
                    h.buffs.eva = h.buffs.eva + 1

    def __basic_attack(self, enemyc):
        self.__attack(enemyc)
        self.stats.turnsUntilSkill = self.stats.turnsUntilSkill - 1

    def act(self, enemyc, enemy2, enemy3, hero2, hero3):
        if self.hero.is_dead():
            raise Exception('{} is dead'.format(self))
            return
        #print('pre-act: ', self, hero2, hero3, enemyc, enemy2, enemy3)
        if self.stats.resource >= 4:
            self.__talent(enemyc, enemy2, enemy3, hero2, hero3)
        elif self.stats.turnsUntilSkill == 0:
            self.__skill(enemyc, enemy2, enemy3, hero2, hero3)
        else:
            self.__basic_attack(enemyc)
        #print('post-act: ', self, hero2, hero3, enemyc, enemy2, enemy3)

class BattleState(Enum):
    ONGOING = 0
    WON = 1
    LOST = 2

class Battle:
    def __init__(self, heroes):
        self.__player_party = heroes[0:3]
        self.__enemy_party = heroes[3:6]
        self.__state = BattleState.ONGOING

    def state(self):
        return self.__state

    def check_winloss(self):
        if self.__state != BattleState.ONGOING:
            return True
        if len([x for x in self.__enemy_party if not x.hero.is_dead()]) == 0:
            self.__state = BattleState.WON
            return True
        if len([x for x in self.__player_party if not x.hero.is_dead()]) == 0:
            self.__state = BattleState.LOST
            return True
        return False

    def __enemy_act_1(self):
        n = random.randint(1, 8)
        if len([x for x in self.__enemy_party if not x.hero.is_dead()]) > 1:
            if n < 2 and not self.__enemy_party[1].hero.is_dead():
                self.__enemy_party = self.__enemy_party[1:3] + self.__enemy_party[0:1]
            elif n < 3 and not self.__enemy_party[2].hero.is_dead():
                self.__enemy_party = self.__enemy_party[2:3] + self.__enemy_party[0:2]
        else:
            n = 8
        return n

    def __enemy_act_2(self, n):
        if n >= 3:
            self.__enemy_party[0].act(self.__player_party[0], self.__player_party[1], self.__player_party[2], self.__enemy_party[1], self.__enemy_party[2])
            return True
        return False

    def __maybe_shift_out_hero(self, party):
        if party[0].hero.is_dead() and not party[1].hero.is_dead():
            party[:] = party[1:3] + party[0:1]
            return True
        elif party[0].hero.is_dead() and not party[2].hero.is_dead():
            party[:] = party[2:3] + party[0:2]
            return True
        return False

    def __maybe_shift_out_player(self):
        return self.__maybe_shift_out_hero(self.__player_party)

    def __maybe_shift_out_enemy(self):
        return self.__maybe_shift_out_hero(self.__enemy_party)

    def attack(self):
        if self.__state != BattleState.ONGOING:
            return
        n = self.__enemy_act_1()
        self.__player_party[0].act(self.__enemy_party[0], self.__enemy_party[1], self.__enemy_party[2], self.__player_party[1], self.__player_party[2])
        if self.check_winloss():
            return

        self.__maybe_shift_out_enemy()

        self.__enemy_act_2(n)
        if self.check_winloss():
            return

        self.__maybe_shift_out_player()

    def shift_left(self):
        if self.__player_party[1].hero.is_dead() and not self.__player_party[2].hero.is_dead():
            return self.shift_right()
        elif self.__player_party[1].hero.is_dead() and self.__player_party[2].hero.is_dead():
            return False
        self.__player_party[:] = self.__player_party[2:3] + self.__player_party[0:2]

        self.__enemy_act_2(self.__enemy_act_1())

        if self.check_winloss():
            return True

        self.__maybe_shift_out_player()

        return True

    def shift_right(self):
        if self.__player_party[2].hero.is_dead() and not self.__player_party[1].hero.is_dead():
            return self.shift_left()
        elif self.__player_party[1].hero.is_dead() and self.__player_party[2].hero.is_dead():
            return False
        self.__player_party[:] = self.__player_party[1:3] + self.__player_party[0:1]

        self.__enemy_act_2(self.__enemy_act_1())

        if self.check_winloss():
            return True

        self.__maybe_shift_out_player()

        return True

def main():
    random.seed()
    for h in HEROES:
        print(h)

    print("Begining fake simulator, as the game isn't built yet")

    h1 = HeroInstance(HEROES[9], 3, 10)
    h2 = HeroInstance(HEROES[1], 2, 5)
    h3 = HeroInstance(HEROES[6], 1, 5)
    e1 = HeroInstance(HEROES[12], 1, 5)
    e2 = HeroInstance(HEROES[9], 2, 15)
    e3 = HeroInstance(HEROES[7], 1, 5)
    instances = [h1 ,h2, h3, e1, e2, e3]

    battle = Battle(instances)

    for h in instances:
        print(h)
    turn = 1

    while battle.state() == BattleState.ONGOING:
        n = random.randint(1, 8)
        if n < 2 and not battle.shift_left():
            n = 8
        elif n < 3 and not battle.shift_right():
            n = 8
        if n >= 3:
            battle.attack()
        print('---- after turn', turn, '----')
        turn = turn + 1
        for h in instances:
            print(h)

    if battle.state() == BattleState.WON:
        print('player party won')
    else:
        print('enemy party won')


if __name__ == "__main__":
    main()
