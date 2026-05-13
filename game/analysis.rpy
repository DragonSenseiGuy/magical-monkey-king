## Three Views of the Monkey King
## How Confucius, Laozi, and the Buddha would judge Wukong's behavior.
##
## NOTE on citations: this project is a visual novel, not a book, so it does
## not have page numbers. Each scene of the story is numbered on screen
## (top right corner) as "Scene 1," "Scene 2," and so on. The teachers below
## cite those scene numbers as the equivalent of page numbers.

# ---------------------------------------------------------------------------
# Characters
# ---------------------------------------------------------------------------

define confucius = Character("Confucius", color="#a8d8ff")
define laozi = Character("Laozi", color="#b8f0c0")
# `buddha` is already defined in script.rpy

# ---------------------------------------------------------------------------
# Portrait images for the three teachers
# ---------------------------------------------------------------------------

image confucius_sprite:
    "images/confucius.png"
    zoom 0.55
    yalign 1.0
    xalign 0.5

image laozi_sprite:
    "images/laozi.png"
    zoom 0.6
    yalign 1.0
    xalign 0.5

image buddha_sprite:
    "images/buddha.png"
    zoom 0.6
    yalign 1.0
    xalign 0.5

# Reusable visual tags for clear "right" / "wrong" labels.
define LBL_WRONG = "{color=#ff7070}{b}[WRONG, by this teaching]{/b}{/color}"
define LBL_RIGHT = "{color=#90ee90}{b}[RIGHT, by this teaching]{/b}{/color}"

# ---------------------------------------------------------------------------
# Entry point: short bridge from the main story into the analysis menu.
# ---------------------------------------------------------------------------

label philosophy_intro:

    $ current_scene = ""
    hide screen scene_indicator

    scene bg buddha
    with fade

    centered "{size=+10}{b}Three Views of the Monkey King{/b}{/size}\n\n{size=-2}Wukong's story has been told for centuries in China.\nThree great teachers would each judge him very differently.\nLet us hear from each of them in turn.{/size}"

    jump philosophy_menu


label philosophy_menu:

    scene bg buddha
    with fade

    menu:
        "Choose a teacher to consult."

        "Confucius: on order, respect, and one's place in society":
            call confucius_view
            jump philosophy_menu

        "Laozi: on the Way, simplicity, and harmony with nature":
            call laozi_view
            jump philosophy_menu

        "The Buddha: on craving, ego, and the end of suffering":
            call buddha_view
            jump philosophy_menu

        "I have heard from all three. End the project.":
            jump true_end


# ===========================================================================
# CONFUCIUS
# ===========================================================================

label confucius_view:

    scene bg temple
    with fade
    show confucius_sprite at center
    with dissolve

    confucius "I am Kongzi. In your country you call me Confucius."
    confucius "I lived in China about twenty-five centuries ago, in a time of war and chaos. I taught that peace begins not with armies, but with how each person treats the people around them."

    confucius "Three of my ideas matter most for understanding this monkey."
    confucius "First, {b}li{/b}: ritual and proper conduct. Bowing to elders, observing ceremonies, behaving the way your role calls for. These small acts hold a society together."
    confucius "Second, {b}ren{/b}: humaneness. Treating others, especially those above and below you, with real care."
    confucius "Third, what I called the {b}rectification of names{/b}: 'Let the ruler be a ruler, the minister a minister, the father a father, the son a son.' Each person should fulfill the role they have been given, before reaching for a greater one."

    confucius "Now let us look at this monkey."

    confucius "{i}Scene 4: At the Master's Temple.{/i}"
    confucius "Wukong did one good thing here. He sought out a teacher, knelt before him, swept his floors, and carried his water for a long time without complaint. The bond between teacher and student is one of the most sacred we have. So far, he behaved well."
    confucius "[LBL_RIGHT] Patient service to the teacher."
    confucius "But the moment he learned a few magical tricks, he began showing off in front of the other students, frightening them and embarrassing his master. The master had to throw him out."
    confucius "A student who shames his teacher breaks the very bond that gives him his learning."
    confucius "[LBL_WRONG] Disrespecting the teacher and disturbing the order of the school."

    confucius "{i}Scene 6: Heaven's Stables.{/i}"
    confucius "The Jade Emperor, the highest authority in heaven, gave Wukong a place. At first he served well. He brushed the heavenly horses until they shone. He took pride in the small task he had been given."
    confucius "[LBL_RIGHT] Performing his duty with care."
    confucius "But the moment he learned the title was a humble one, his pride exploded. He cursed his ruler and stormed out of heaven."
    confucius "I would tell him: a small post performed with honor is the path to a greater one. Storming out because the title is too small is the path to no post at all."
    confucius "[LBL_WRONG] Letting ambition outrun virtue, and disrespecting his ruler."

    confucius "{i}Scene 7: The Peach Garden, the banquet.{/i}"
    confucius "He was not invited to the banquet of the gods. So he tricked one of the goddesses, sent her the wrong way, took her form, and drank wine that was not his."
    confucius "Invitations and ceremonies are not silly. They are li. They are how we tell each other, 'I see your place, and I respect it.' Wukong treated all of that as a joke."
    confucius "[LBL_WRONG] Breaking li, deceiving an honest person, and shaming a sacred ceremony."

    confucius "So what should a person do, if they wish to live a Confucian life?"
    confucius "Respect your teachers. Serve your superiors well. Treat your equals with li. Be patient. Cultivate yourself, every day, into a person whose presence brings calm and order to the room."
    confucius "Do not, like Wukong, demand greatness before you have earned it. That road leads beneath a mountain."

    hide confucius_sprite
    with dissolve
    return


# ===========================================================================
# LAOZI
# ===========================================================================

label laozi_view:

    scene bg mountain
    with fade
    show laozi_sprite at center
    with dissolve

    laozi "I am Laozi. An old man with little to teach. So I will be brief."

    laozi "There is the {b}Dao{/b}, the Way of all things. Water flows downhill. Seasons change. Things are born, and things die. The Dao is simply how the world goes."
    laozi "The wise person does not fight the Dao. They practice {b}wu wei{/b}, which means effortless action. They yield. They live simply. They want little. They are like water, soft and patient, which in time wears down the hardest stone."

    laozi "Now consider the monkey."

    laozi "{i}Scenes 1 and 2: The Mountain and the Hidden Cave.{/i}"
    laozi "Here, in his early life, the monkey was almost a sage without knowing it."
    laozi "He ate fruit. He swam in streams. He played with friends. He had no ambition beyond joy. He lived in a cave behind a waterfall."
    laozi "This is exactly the life I would recommend to anyone."
    laozi "[LBL_RIGHT] Living simply, in harmony with nature, wanting nothing more."

    laozi "{i}Scene 3: Fear of Death.{/i}"
    laozi "Then he watched an older monkey die, and his peace ended."
    laozi "But death is part of the Dao. The leaf falls. The river runs to the sea. To accept this is wisdom. To rage against it is the start of all suffering."
    laozi "From this moment on, every choice he made was a choice against the Dao."
    laozi "[LBL_WRONG] Trying to escape the natural cycle of life and death."

    laozi "{i}Scene 5: The Dragon King's Palace.{/i}"
    laozi "He demanded a weapon that no one else could lift. Why? Because he wanted to be greater than others."
    laozi "I taught that the soft and weak overcome the hard and strong. The sage carries no weapon, because they have no quarrel. Wukong forged his future enemies the moment he picked up that staff."
    laozi "[LBL_WRONG] Grasping after power and ambition."

    laozi "{i}Scene 7: The Peach Garden.{/i}"
    laozi "He was set to guard the peaches. Instead, he ate them all."
    laozi "I once said: 'He who knows when enough is enough will always have enough.' Greed is a fire that no amount of fruit can put out."
    laozi "[LBL_WRONG] Greed in place of contentment."

    laozi "{i}Scene 8: The Heavenly Army.{/i}"
    laozi "He met heaven's soldiers with his staff and broke them all. He thought this was strength."
    laozi "But meeting force with force only invites more force. A Daoist would have yielded, slipped away, vanished into the mist of his own mountain."
    laozi "[LBL_WRONG] Choosing battle over yielding."

    laozi "{i}Scene 9: The Buddha's Bet, and the mountain.{/i}"
    laozi "And so a mountain falls on him. To my eyes, this is not a punishment. It is the Dao quietly returning a restless creature to stillness."

    laozi "If you wish to live well, do this: live simply. Want little. Yield where you can. Do not strive against the natural course of things. Be like water."
    laozi "The monkey could have lived forever in joy on his mountain. Instead he traded that for a mountain on top of him."

    hide laozi_sprite
    with dissolve
    return


# ===========================================================================
# BUDDHA
# ===========================================================================

label buddha_view:

    scene bg buddha
    with fade
    show buddha_sprite at center
    with dissolve

    buddha "I am the one you call the Buddha, the awakened one."

    buddha "I taught what I called the {b}Four Noble Truths{/b}."
    buddha "First, life contains suffering."
    buddha "Second, this suffering arises from craving and attachment."
    buddha "Third, there is a way to end it."
    buddha "Fourth, that way is the {b}Eightfold Path{/b}: right view, right intention, right speech, right action, right livelihood, right effort, right mindfulness, and right concentration."
    buddha "I also taught that the self you cling to so tightly is, in truth, an illusion."

    buddha "Now look at this monkey through these eyes."

    buddha "{i}Scene 3: Fear of Death.{/i}"
    buddha "Here is the seed of everything that follows. Wukong saw a friend die and could not bear it. So he set off to escape death itself."
    buddha "He felt the First Noble Truth. He saw that life is suffering. But instead of looking inward and finding the cause, he ran outward, looking for a way to keep what he had forever."
    buddha "The craving to never lose what you love is the very thing that traps you. Every cup of suffering Wukong drinks from this point on is poured by his own attachment to life."
    buddha "[LBL_WRONG] Trying to escape suffering by clinging harder, instead of by letting go."

    buddha "{i}Scene 7: The Peaches and the Laughing Juice.{/i}"
    buddha "Greed and intoxication. He ate every peach he was supposed to guard, then crashed a banquet to drink wine that was not his."
    buddha "Pleasures of the senses are like saltwater. The more you drink, the thirstier you grow. Wukong drank deeply and found no peace."
    buddha "[LBL_WRONG] Surrendering to craving for pleasure."

    buddha "{i}Scene 6: The Stable Keeper's Rage.{/i}"
    buddha "When Wukong learned his title was small, his anger was enormous. But ask yourself: who is being insulted?"
    buddha "There is no fixed 'Wukong' to be wounded. The self he protects so fiercely is an idea, not a thing. All his rage is suffering manufactured by clinging to that idea."
    buddha "[LBL_WRONG] Clinging to ego and reputation."

    buddha "{i}Scene 9: The Buddha's Hand.{/i}"
    buddha "I asked him to leap from the palm of my hand. He flew, by his own count, past stars and clouds, to what he thought was the edge of the world."
    buddha "He scratched his name on a pillar to prove: I was here."
    buddha "But the pillar was my finger. The whole journey took place inside my open hand. He never left."
    buddha "This is the great teaching, if he could hear it: all the great deeds the ego is so proud of are happening within something far larger than the ego ever knew. The 'self' that travels and conquers is the smallest part of what is real."

    buddha "And so the mountain. Not a punishment. {b}Karma{/b}. Each craving, each grasping, each act of ego made the mountain heavier. He built it himself, one desire at a time. Now he carries it."

    buddha "If you wish to be free, do this: see your craving for what it is. Loosen your grip. Let go of your sense of a separate self. Be kind to other beings, because in truth there is no firm wall between you and them."
    buddha "The mountain on Wukong is the mountain on every person who has not yet learned this. Lay it down."

    hide buddha_sprite
    with dissolve
    return


# ===========================================================================
# True ending
# ===========================================================================

label true_end:

    scene bg buddha
    with fade

    centered "{size=+12}{b}The End{/b}{/size}\n\n{size=-2}A school project on Confucianism, Daoism, and Buddhism\nthrough the story of the Monkey King.{/size}"

    return
