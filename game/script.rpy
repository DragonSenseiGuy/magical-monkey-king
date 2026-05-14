## The Legend of the Monkey King
## A short visual novel retelling the tale of Sun Wukong.

# ---------------------------------------------------------------------------
# Characters
# ---------------------------------------------------------------------------

define narrator = Character(None, what_color="#f5f5f5")
define wukong = Character("Sun Wukong", color="#ffd24a")
define monkey = Character("Monkey", color="#c1a37a")
define master = Character("Master Subhodi", color="#9ad1ff")
define dragon = Character("Dragon King", color="#7af0c0")
define jade = Character("Jade Emperor", color="#ffe680")
define officer = Character("Heavenly Officer", color="#cccccc")
define buddha = Character("Buddha", color="#f7c873")

# ---------------------------------------------------------------------------
# Images
# ---------------------------------------------------------------------------

image bg mountain = "images/bg_mountain.png"
image bg cave = "images/bg_cave.png"
image bg temple = "images/bg_temple.png"
image bg heaven = "images/bg_heaven.png"
image bg peach = "images/bg_peach.png"
image bg battle = "images/bg_battle.png"
image bg buddha = "images/bg_buddha.png"

image wukong:
    "images/monkey.png"
    zoom 0.7
    yalign 1.0
    xalign 0.5

# ---------------------------------------------------------------------------
# Scene-number indicator (used so the analysis section can cite scenes,
# acting as the "page numbers" for this game)
# ---------------------------------------------------------------------------

default current_scene = ""

screen scene_indicator():
    if current_scene:
        frame:
            xalign 0.99 yalign 0.02
            background Solid("#000000bb")
            padding (12, 6)
            text current_scene size 18 color "#ffe680"

# ---------------------------------------------------------------------------
# Story
# ---------------------------------------------------------------------------

label start:

    show screen scene_indicator
    $ current_scene = "Scene 1: Born from Stone"

    scene bg mountain
    with fade

    narrator "A long time ago, on top of a mountain covered in flowers and fruit trees, there was a big rock."
    narrator "It had been sitting there forever, soaking up the sun and the moon."
    narrator "Then one day, with a loud crack, the rock just split open."

    show wukong at center
    with dissolve

    narrator "And out jumped a monkey. A whole monkey, made of stone, blinking at the sky."

    wukong "Whoa. Okay. I'm alive. This is great."

    narrator "He spent his days running around the mountain, climbing trees, and making friends with every animal he could find."

    # ----- Finds the cave -----

    $ current_scene = "Scene 2: The Hidden Cave"

    scene bg cave
    with fade
    show wukong at center
    with dissolve

    narrator "One day, he was poking around a big waterfall and decided, why not, and jumped right through it."
    narrator "On the other side was a cave. A real one, dry, cool, with stone tables and even stone beds inside."

    wukong "Hold on. There's a whole place back here. And nobody knows about it but me."

    # ----- Brings the monkeys -----

    narrator "He ran back to the other monkeys, basically bouncing the whole way."

    monkey "Where did you go? You look like you're about to explode."

    wukong "Just follow me! Through the waterfall! Trust me, you have to see this."

    narrator "The other monkeys jumped through one after another and landed in the cave, laughing and falling all over each other."

    # ----- Becomes king -----

    monkey "Hey, whoever found this place should be in charge, right?"

    monkey "Long live the Monkey King!"

    wukong "Okay, okay, I'll take it. From now on, just call me Sun Wukong. The Monkey King."

    # ----- Sets out for immortality -----

    $ current_scene = "Scene 3: Fear of Death"

    scene bg mountain
    with fade
    show wukong at center
    with dissolve

    narrator "Things were good for a long time. Then one night, watching an older monkey die, something hit him."

    wukong "All of this. The cave, my friends, everything. It's all going to end. I'm going to die too."
    wukong "No. There has to be a way around that. And I'm going to find it."

    narrator "So he built a raft and sailed off across the sea, looking for someone who could teach him."

    # ----- Goes to the master -----

    $ current_scene = "Scene 4: At the Master's Temple"

    scene bg temple
    with fade
    show wukong at center
    with dissolve

    narrator "He wandered for a long time before he finally found a quiet mountain where an old wise man lived."

    master "Huh. A monkey came all this way just to knock on my door. What do you want?"

    wukong "I want you to teach me. I don't want to die."

    master "That's a lot to ask. Alright, kneel. Let's see what you've got."

    # ----- He learns -----

    narrator "For a long time, Wukong just swept floors and carried water. Then, late at night, the master started teaching him for real."

    master "I'll teach you how to change your shape. How to ride a cloud. How to jump farther than you can imagine."

    wukong "Look, I can be a fish! A bird! A bug! Watch, I can be YOU!"

    master "Stop messing around. This isn't a magic show."

    # ----- Gets kicked out -----

    narrator "But Wukong couldn't help himself. He kept showing off his new tricks to the other students."

    master "You're scaring them. You won't stop bragging. I want you gone, and don't tell anyone you learned from me."

    wukong "Master, wait, I..."

    master "Go."

    narrator "One jump, and he was back home."

    # ----- Causes ruckus -----

    $ current_scene = "Scene 5: The Dragon King's Palace"

    scene bg cave
    with fade
    show wukong at center
    with dissolve

    narrator "Back on his mountain, Wukong started to get bored. He was strong now, but he didn't have a weapon, and a king should really have a weapon."

    wukong "I want something nobody else can even pick up. That sounds about right for me."

    scene bg battle
    with fade
    show wukong at center
    with dissolve

    narrator "So he dove into the sea and barged straight into the Dragon King's palace."

    dragon "Who do you think you are, just walking in here..."

    wukong "Show me your best weapon. Or I'll start breaking things."

    narrator "The dragons brought out swords and spears, but every one of them snapped the second Wukong gripped it."
    narrator "Finally, kind of desperate, they took him to a huge iron pillar at the bottom of the sea, something nobody had ever even budged."

    wukong "Hmm. ...Shrink!"

    narrator "And just like that, it shrank down to fit in his hand. He said \"grow,\" and it stretched up like a tower."

    wukong "Oh yeah. NOW we're talking."

    # ----- Jade Emperor tests him -----

    $ current_scene = "Scene 6: Heaven's Stables"

    scene bg heaven
    with fade

    narrator "Word about this loud, rowdy monkey eventually made it all the way up to heaven."

    jade "A monkey? Pushing dragons around in their own palace?"

    officer "Your Majesty, maybe if we gave him a small job up here, he'd settle down."

    jade "Fine. Bring him up. I want to see him."

    show wukong at center
    with dissolve

    jade "Monkey. We're giving you a place in heaven. You'll be in charge of our stables."

    wukong "The... the horses? I'm in charge of the HORSES?"

    # ----- Stable guy -----

    narrator "At first, honestly, he kind of loved it. He brushed the heavenly horses until they shone."

    wukong "These are the best horses I've ever seen. And I'm the boss of all of them."

    # ----- Angry it isn't a rank -----

    officer "Just so you know, your title? It's not actually a real rank. It's more of a made-up thing they give to keep you busy."

    wukong "Not a real rank? Are you serious right now?"

    wukong "Tell the emperor I'm not playing this game anymore."

    narrator "He stormed out of heaven, marched back to his mountain, and decided from now on he was going to call himself a king, a proper one, and nobody else got to decide that for him."

    # ----- Becomes peach guy -----

    $ current_scene = "Scene 7: The Peach Garden"

    scene bg peach
    with fade
    show wukong at center
    with dissolve

    narrator "To keep him busy, the Jade Emperor came up with a new job that actually sounded important, putting him in charge of the heavenly peach garden."

    jade "There. Let him guard some peaches. That should keep him out of our hair."

    wukong "Wait, these are the peaches that make you live forever? And I'm guarding them? Just me?"

    # ----- Eats peaches -----

    narrator "He climbed up to the highest branch, picked the biggest, ripest peach, and took a bite."

    wukong "Oh wow. These are amazing. I should probably try them all, you know, just to make sure they're okay."

    narrator "By the end of the week, the garden was basically empty."

    # ----- Bombs the peach party -----

    narrator "Then came the big peach banquet, this huge feast for all the gods. Wukong was, of course, not invited."

    wukong "Not invited. To MY peaches. Okay. We'll see about that."

    narrator "On his way over, he ran into one of the goddesses going to pick peaches for the banquet."

    officer "Excuse me, do you know where the banquet's being held?"

    wukong "Oh! Yeah, actually, they moved it. It's on the other side of the mountain now. You should hurry, you're already kind of late."

    officer "Oh no, thank you so much!"

    narrator "She rushed off in completely the wrong direction. Wukong grinned, shook himself, and shimmered..."
    narrator "...until he looked exactly like her, robes and everything."

    wukong "Heh. Okay. Banquet time."

    narrator "He walked into the empty banquet hall before any of the real guests showed up, and went straight for the jugs of magical wine."

    wukong "Hm. They call this stuff 'laughing juice.' I can kinda see why. Hee, heehee, HAHAHA!"

    narrator "He kept drinking until he was completely wasted. By the time the actual guests started arriving, the disguise had basically melted off."

    officer "Wait, wait, that's not her. That's the MONKEY!"

    wukong "*hic* ...oh. Hi. Okay, bye!"

    # ----- Emperor sends army, monkey wins -----

    $ current_scene = "Scene 8: The Heavenly Army"

    scene bg battle
    with fade
    show wukong at center
    with dissolve

    jade "Enough of this. Send the army. All of them."

    narrator "The whole heavenly army came pouring down from the clouds."
    narrator "Wukong met them on his mountain, swinging his staff, and one after another he just sent them flying."

    wukong "Come on! Who's next? Is that really all you've got?"

    # ----- Boiled, doesn't die -----

    narrator "Eventually they caught him with a magic lasso and dragged him over to a giant furnace."

    officer "Throw him in the cauldron! Let's just burn him until there's nothing left."

    narrator "They left the fire going for ages. When they finally opened the lid..."

    wukong "*cough* ...wow. You really messed up my fur."

    narrator "He burst out, somehow stronger than before, and went tearing through heaven with his staff."

    # ----- Buddha arrives -----

    $ current_scene = "Scene 9: The Buddha's Bet"

    scene bg buddha
    with fade
    show wukong at center
    with dissolve

    narrator "Out of options, the Jade Emperor finally called the one person he thought might actually scare Wukong."

    buddha "Little monkey. What is all this noise about?"

    wukong "Who are you, old man? Move, I'm here to take the Jade Emperor's throne."

    buddha "His throne? That's such a small thing. Tell me, though, how far can you really jump?"

    wukong "One jump? I can go farther than you can even imagine."

    buddha "Alright. Let's make a bet. If you can jump out of the palm of my hand, the throne is yours."

    wukong "Out of your hand? Are you joking? Easiest bet of my life."

    # ----- Gets put under a mountain -----

    narrator "Wukong jumped. He flew past clouds, past stars, all the way to what seemed like the edge of the world."
    narrator "He landed near some huge pillars and, just to make sure everyone knew he'd been there, scratched his name into one of them."

    wukong "Sun Wukong was here! Alright. Time to go collect that throne."

    narrator "He jumped back, and landed right in the middle of Buddha's open palm."

    buddha "Take a look at my finger, little monkey."

    narrator "There, scratched into Buddha's finger in tiny letters, was his own name."

    wukong "...no way."

    buddha "You never actually left."

    narrator "Buddha closed his hand and turned it into a huge mountain, pinning Wukong underneath."

    buddha "Stay here for a while, little monkey. Think about what you've done."

    hide wukong
    with dissolve

    scene bg buddha
    with fade

    narrator "And that's how the Monkey King ended up stuck under a mountain..."
    narrator "...for a very, very long time."

    centered "{size=+10}{b}The End of Part One{/b}{/size}\n{size=-2}But the lesson is just beginning.{/size}"

    jump philosophy_intro
