﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image sylvie smile = "sylvie2_smile.png"
image sylvie surprised = "sylvie2_surprised.png"
image daHouse = "whitehouse.jpg"
image heaven = "star.png"
image arven_girl = "eileen_orb.png"
image cavern = "cave.jpg"
image magic = "magic.png"
image movie = Movie(size=(800, 600), xpos=0, ypos=0, xanchor=0, yanchor=0)

# Declare characters used by this game.
define arven = Character('Arven', color="#c8ffc8")
define doom = Character('Doom Machine', color="#ff0000")
define wiz = Character('Wizard', color="#00ff00")
define thepres = Character('The President', color="#0000ff")
define thehouse = Character('The White House', color="#1111ff")
define rocket = Character('Rocket', color="ffffff")
define unspeakableHorror = Character('Unspeakable Horror', color="f0f0f0")

# The game starts here.
label start:
    play music "sunflower-slow-drag.ogg" loop
    scene daHouse
    show sylvie smile

    wiz "Arven finally arrives at the White House, after an long, arduous, and unimaginably weird journey."

    thehouse "Hi Arven!"
    show sylvie surprised

    arven "Prepare for battle!!!!!!"
    show sylvie smile

    thehouse "Okay!"
    # (Rocket launches)

    menu:
        "Put on robe and wizard hat":
             jump win

        "Put on cosplay":
             jump hentai

        "Ascend to Godhood. Show the mortals true fear.":
            jump heaven

    label win:
        rocket "The end, everyone lives happily ever after"
        jump marry

    label heaven:
        arven "There are worlds beyond this one. I will collapse them all into one, and then Senpai shall finally notice me."

        arven "The end is upon us."

        thehouse "Wait Arven! If you reap reality's harvest, then we can't go to the cultural festival!"

        arven "I no longer need cultural festivals. I can collapse infinite maid cafes into each other in a wheel that turns through all seven senses forever. There will also be Pocky."

        arven "Infinite pocky."

        thehouse "Fine, if it's what you want. But...before you merge and purge all that ever was..."

        thehouse "I have a confession."

        thehouse "A love confession. Of loving you."

        thehouse "We should date."

        arven "I never knew White House. Well, I kind of knew, because you always stare at me at lunch."

        arven "I'm into you too, White House."

        arven "Unfortunately, there's a hotter White House in Reality A45. So I'm going to have to go ahead and shatter the barrier between universes."

        menu:
            "Forget that white house and go breakdance":
                jump ArvenDestroyerofWorlds
            "Eat pockey":
                jump Eat
            "Say goodbye":
                jump JumpyJumpJump

    label hentai:
        wiz "The end, everyone lives happily ever after"
        jump marry

    label marry:
        play movie "shuttle.ogv"
        show movie with dissolve

        show sylvie smile at center with dissolve
        "Well, time to do pushups"
    
    label ArvenDestroyerofWorlds:
   
        arven "Alright, a little stretching...some warm up footwork...Time for flares."

        wiz "Arven plants his arm. As the first leg of his flare swings towards the sky, the heavens crash down."

        arven "Flares are when you collapse reality into an uninhabitable hellscape, right?"

        scene cavern

        wiz "Cities fall, and oceans rise. That one coffee shop you like shuts down, and is replaced with a Starbucks. That Starbucks is then razed during riots, which are only quelled when an Earthquake swallows New York City, and spits it back out into the atmosphere. The remains of the city land on Beijing, a phenomenon the government blames on the upstart hedgehog party. The Hedgehog Party are labeled terrorists, and a bounty is put on both their membership and all the hedgehogs in the Chinese countryside, which totally exist. Over time, hedgehog hunting becomes the dominant trade of Northern China. Hedgehog pelts are the main driver of a vibrant artistic culture, used as both materials for fashion designers and raw canvas for a bold new generation of painters. One day, a young hedgehog hunter named Arnold Wei awakens. He's the son of a hedghehog hunter, who is the son of another hedgehog hunter. While skewering the morning's catch, he finds a stray artifact. A perfectly preserved shoe. He doesn't know what kind of person it belonged too, but it must have some value. He takes it to the appraiser, where he learned it once belonged to an ancient tribe called 'Dance Breakers.' No one knows what became of the Dance Breakers, but many blame them for the Great Sundering. The appraiser returns the shoe to Arnold, and tells him he should destroy it if he is wise. Arnold agrees in person, but hides the shoe underneath his bed. Something about it calls to him. Maybe the force that unmade the world, can remake it anew. Anyway, he starts learning some sick flips."
#New game plus as Arnold

        arven "...."

        arven "(runs away)"

        unspeakableHorror "hey baby"

        arven "Hi!!!"

        unspeakableHorror "nice flares."

        arven "cool man, thanks."

        unspeakableHorror "I liked the part where you destroyed everything I ever loved."

        arven "Thanks, the trick is remembering to keep your legs spread."

        unspeakableHorror "Really? Because mine are pretty wide but I can never get around more than twice."

        arven "You're probably not kicking your main leg hard enough, you really want to focus on that initial sweep."

        unspeakableHorror "What about hand placement?"

        arven "It's tricky. You don't want to be too slow, but you want to give it enough time for your legs to get the proper lift. For that the only real solution is practice, it comes with time."

        unspeakableHorror "That's great advice! I wish my friends were still alive for me to tell them. Are halos similar?"

#menu going through flare steps, testing if you were paying attention

    label Eat:
        scene heaven
        show arven_girl
        arven "Victory is mine."

    label JumpyJumpJump:
        show cavern
        arven "forever..."

    return
