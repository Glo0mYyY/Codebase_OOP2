class Tier():
    def machen_sound(self):
        print("Tier macht Sound")
        
class Hund(Tier):
    def machen_sound(self):
        print("Wuff")

class Katze(Tier):
    def machen_sound(self):
        print("Miau")

def mach_tier_sound(tier):
    tier.machen_sound()

tier1 = Tier()
tier2 = Hund()
tier3 = Katze()

mach_tier_sound(tier1)
mach_tier_sound(tier2)
mach_tier_sound(tier3)