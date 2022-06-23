# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define idni = Character("[playername]", color="#9cb2ff")
define sis = Character("Minami", color="#faf1be")
define drug = Character("Suzune", color="#ad795a")
define idol = Character("Sana", color="#bf2424")
define dead = Character("Aoi", color="#8cdb84")

define dude = Character("[dudename]", color="#eaeaea")

define idollast = "Asakura"
define druglast = "Hanaoka"
define deadlast = "Yumeno"

define winter = "Yuki"
define karina = "Rina"
define giselle = "Jia"
define ningning = "Nene"

define sis_flag = 0
define drug_flag = 0
define idol_flag = 0
define dead_flag = 0

init:
    transform flip:
        xzoom -1.0

    transform halfsize:
        zoom 0.5

    transform bigger:
        zoom 1.5

    transform biggerer:
        zoom 1.75

    transform normal:
        xpos 700
        ypos 200

    transform normalright:
        xpos 1150
        ypos 200

    transform normalleft:
        xpos 250
        ypos 200

    transform biggernormal:
        xpos 600
        ypos 100

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    stop music fadeout 1.0
    scene black with fade

    "Hello."

    $ check = 1
    while check == 1:
        $ playername = renpy.input("Would you tell me your given name?")
        $ playername = playername.strip() or "Masaki"

        if playername == "Yuuto":
            $ dudename = "Makoto"
        else:
            $ dudename = "Yuuto"

        $ familyname = renpy.input("How about your family name?")
        $ familyname = familyname.strip() or "Takashima"

        if familyname == "Kanzaki":
            $ dudelast = "Uehara"
        else:
            $ dudelast = "Kanzaki"

        menu:
            "Is [familyname] [playername] your name?"

            "Yes.":
                $ check = 0

            "No.":
                $ check = 1

    "Welcome, [playername]."
    "I'm so glad you could make it."
    "For the sake of my creator, I hope you have a good time."

    scene black with fade

    "???" "..."
    "???" "...?"
    "???" "...!?"


    $ renpy.music.set_volume(0.3, 0, channel='sound')
    play sound "audio/thud.mp3"
    "Wha!?" with vpunch

    scene bedroom with fade
    "With a sudden thump, I'm suddenly in a world of pain."

    $ renpy.music.set_volume(0.05, 0, channel='music')
    play music "audio/mosswood.mp3" loop

    show minami at normal with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    sis "Hey, [playername]! Wake up or else I'm gonna replace your toothpaste with wasabi."
    "Geez..."
    "What kind of monster is she?"
    idni "I'm up, I'm up..."
    "I blink, desperately trying to get my bearings."
    "The usual softness of my bed is nowhere to be found. Instead, I slowly realize that I'm actually lying on the cold hard floor of my room."
    "Thanks to my {i}wonderful{/i} younger sister, I'm given a rather abrupt awakening..."
    "That's [sis.name]. With my bedsheets in hand, it's clear to see that she had violently ripped them off my bed, taking me down to the floor in the process."
    "Already in her uniform, it's clear that she's excited to start her first day in high school."
    sis "Come on, I don't want to be late."
    "..."
    idni "Maybe next time, wake me up normally."
    sis "Hmm?"
    sis "I tried that, but you still wouldn't wake up."
    "..."
    "Is she for real...?"
    idni "At least wake me up in a way that doesn't hurt..."
    idni "Thanks to you, I'm gonna be in too much pain to get to school anyway."
    sis "Quit being a baby and get up."
    idni "Fine..."
    "With a grunt, I slowly got to my feet. As I stretched out my back, I couldn't help but feel a rather uncomfortable soreness around where my body hit the floor."
    sis "Hurry up and get dressed. Unless you {i}want{/i} me to leave you behind."
    hide minami with dissolve
    "Without even waiting for me to respond, she casually left my room."
    "..."
    "As you can see, my sister is very..."
    "Assertive..."

    scene black with fade

    "I slowly make my way over to the bathroom and wash up for the morning."
    "The entire time, [sis.name] yells at me to hurry up from her seat on the living room couch."

    scene living room with fade
    show minami at normal with dissolve

    "By the time I'm dressed in my uniform, she's already at the door, ready to go."

    menu:
        sis "Hurry up, [playername]!"

        "I'm coming.":
            $ sis_flag += 1
            idni "I'm coming, geez."
            idni "Can't you be a little patient? We're not even late."
            sis "Boys like assertive girls, [playername]."
            idni "Who told you that nonsense?"
            sis "People smarter than you. Now hurry up, or else we'll be late for real!"
            idni "Can I at least have some breakfast?"
            sis "No time."
            "..."

            stop music fadeout 1.0
            jump schoolTogether

        "Just leave without me.":
            $ idol_flag += 1
            idni "Just leave without me if you're gonna be so impatient."
            sis "Eh?" with vpunch
            sis "Me? Alone? But what if I get lost along the way?"
            sis "What if something terrible happens to me? It'll be all your fault!"
            idni "It's only a few blocks away."
            idni "If something really does happen to you, then I'll {i}definitely{/i} miss you when you're gone."
            "The moment those words leave my mouth, I instantly regret saying them."
            "No doubt offended, [sis.name]'s face turns sour."
            sis "Rude."
            sis "That's why you're still single!"
            hide minami with dissolve
            "With the slam of the front door, [sis.name] storms out of the house." with vpunch
            "... Maybe I should have gone with her after all..."
            idni "Hey, wait up!"

            stop music fadeout 1.0
            jump schoolAlone


label schoolTogether:

    play music "audio/crack that case.mp3" loop
    scene other street with fade
    show minami at normal with dissolve
    sis "Aren't you glad that your cute little sister is finally in the same school as you?"
    idni "No."
    sis "Not even a little?"
    idni "Not at all."
    sis "Heartless."
    "[sis.name] has always been a handful. Even back when we were kids, she was always the needier one."
    "Growing up, I just had to accept that she was our parents' favoured child, and that she'd get her way more often than I would."
    "Now that she's in high school..."
    "I don't have the luxury of not having to see her at school anymore."
    idni "You better not get into any trouble."
    sis "Me? Trouble?"
    "[sis.name] jeers at me sarcastically, trying her best to get a rise out of me."
    sis "You get into way more trouble than I do."
    idni "That's because you're the one making me take the fall whenever you do something you're not supposed to!"
    sis "Oh yeah."
    sis "Thank's [playername], I really appreciate it!"
    hide minami with dissolve
    "With a cheeky smile, she quickens her pace to get a little bit of distance between the two of us."
    "For as long as I could remember, [sis.name] has always been one to joke around with me."
    "... Usually at my expense..."
    "Now that she's in high school, my gut's telling me that it's only gonna get worse."
    idni "... I really hope every day isn't like this..."
    "I mutter to myself, but in reality, I know that this is par for the course."
    show minami at halfsize, center with dissolve
    sis "Hurry up. [playername]! I don't want to be late because of you!"
    idni "I'm coming, I'm coming..."
    hide minami with dissolve
    "And with that, our first time walking to school together since middle school picked up right where it left off..."


    jump atSchool


label schoolAlone:
    play music "audio/crack that case.mp3" loop
    scene other street with fade
    "Even though I tried to catch up with [sis.name], she was nowhere to be found."
    "She's always been a handful, even back when we were kids."
    "To be honest, I'm a little worried about her."
    "It doesn't happen often, but sometimes she gets on my nerves a bit too much and I say something that I don't really mean..."
    "I'll have to apologize next time I see her."
    "Even if she gets under my skin sometimes, she's still my sister."

    show sana at normalright with dissolve
    "Hmm?"
    hide sana with dissolve

    "Right in the corner of my eye, someone catches my eye for a second."
    "When I try looking back at her, she's suddenly gone, as if she was never there in the first place."
    "Huh? Am I seeing things?"

    scene black with fade
    stop music fadeout 0.1

    "Confused, I rub at my eyes."
    idni "Maybe I'm still half asleep..."
    "That's weird though. Why would I be seeing {i}her{/i} of all people?"
    "She's in her uniform... Maybe she's actually gonna go to school today."
    "???" "You there."
    scene other street with fade

    play music "audio/sloppy clav.mp3" loop
    show sana at normal with dissolve
    idni "Whoa!"
    "On reflex, I flinch, taking a step back."
    "I can feel my heart rate spike as I let out an involuntary shout."
    "???" "Quit shouting."
    "The one and only [idollast] [idol.name]..."
    idni "... Can I help you?"
    "She's got a reputation around school being someone you shouldn't really get involved with."
    "There's a ton of rumours around her, and I'm not at all interested in finding out if any of them are true or not."
    "It's safe to say that her talking to me right now isn't a good thing."
    idol "Don't look now, but there's a couple guys tailing me."
    idni "What?"
    "I instictively try to move my head to look behind me, only for [idollast] to grab my head."
    idol "I said don't look."
    "With a deep scowl on her face, her grip on my head is as frightening as it is painful."
    idni "Okay... I won't."
    idol "Good boy."
    "Her face softens slightly as she finally lets go of my face."
    idol "We're gonna run for it. If they catch us, you distract them, okay?"

    menu:
        idni "What?"

        "Refuse.":
            idni "No way, leave me alone."
            "[idollast] eyes me with a look I can't quite read before she silently turns around and runs off."
            hide sana with dissolve
            idni "Geez..."
            "What the hell was that about?"
            "???" "Hey you!"
            "Huh?"

            stop music fadeout 0.1
            $ renpy.music.set_volume(0.3, 0, channel='sound')
            play sound "audio/thud.mp3"
            scene black with vpunch

            "Bad End."
            return

        "Hold on.":
            $ idol_flag += 1
            idni "Hey, wait!"

    stop music fadeout 0.1
    "Before I can get another word in, [idollast] grabs onto my wrist and starts running."


    jump atSchool

label atSchool:

    scene hallway with fade
    if sis_flag == 1:
        "After an unfortunately lively walk to school, [sis.name] and I parted ways as she headed to the auditorium for the new first year's entrance ceremony."
        show dude at bigger, normal with dissolve
        "???" "Yo! [playername]!"
        idni "[dudename], what's up?"
        dude "Not much. How was your break?"
        idni "Pretty good. Took some time to chill."
        "This guy is [dudelast] [dudename]."
        "We happened to get seated next to each other last year so naturally we became friends."
        dude "You should have come with me, man."
        idni "Oh really?"
        dude "Yeah, I got to finally catch one of Esper's concerts."
        idni "Oh right... That group you won't shut up about."
        dude "Ayo, watch how you speak on their name."
        dude "They've only been around for a few months but they're gonna be huge, let me tell you."
        "... Evidently, he's a huge fan of idols..."
        "He's a nice guy, but he's not afraid to wear his interests on his sleeve."
        dude "Tell me you've at least heard their new song."
        idni "New song?"
        dude "..."
        "[dudename] looks at me like I'm something he scraped off his shoe."
        dude "Make sure you're free this weekend. You're coming to see them with me."
        idni "I'm not buying a ticket."
        dude "I'll buy one for you then."
        idni "... Fine, as long as you're paying..."

        $ renpy.music.set_volume(0.5, 0, channel='sound')
        play sound "audio/bell.mp3"

        "Finally freeing me from this conversation, the bell rings signalling the start of the school day."
        idni "Tell me the details later. Let's just get to class."
        dude "Sounds good to me."

    else:
        play music "audio/crack that case.mp3" loop
        "After an unplanned morning run, I managed to make it to school in one piece..."
        "But I'm not out of the woods yet."
        show sana at normal with dissolve
        idol "Thanks."
        "I struggle to catch my breath, while [idollast] in comparison hasn't even broken a sweat."
        "Is this girl even a human? How is she not exhausted?"
        "Was there even people following her around in the first place?"

        idni "I think you might've broken my wrist."
        "A searing pain shoots through where [idollast] had been grabbing onto me. Even the skin's a little red."
        "I try to twist my wrist around, but even the slightest movement makes me want to die."
        idol "You're fine. I made sure to be gentle."
        idni "Gentle my ass..."
        idol "Getting beaten up by those guys would've been way more painful."
        idni "..."

        show dude at bigger, normalleft with dissolve
        "???" "Yo! [playername]!"
        idni "[dudename], what's up?"
        "Please please please please please please please please please please please please please please please please please get me out of this situation, I'm begging you."
        "This guy is [dudelast] [dudename]."
        "We happened to get seated next to each other last year so naturally we became friends."
        "... So maybe he can help me out here..."
        "[dudename] looks over to [idollast] standing next to me with a blank look on his face."
        dude "Is this your girlfriend?"
        "I'm doomed."
        dude "Did you get a girlfriend without telling me?"
        "Suddenly, [idollast]'s face morphs into a smile..."
        "A sick, twisted, evil looking smile."
        idol "That's right, I'm his girlfriend."
        idni "..."
        idni "Actually, she's not—"

        $ renpy.music.set_volume(0.5, 0, channel='sound')
        play sound "audio/bell.mp3"

        "I'm interrupted by the sound of the bell."
        idol "I'll see you after class then, right?"
        "With another sick smile, she reaches out for my hand and gives it a squeeze before walking away."
        hide sana with dissolve
        "..."
        scene black with fade
        "What am I going to do now...?"
        "Something tells me that [idollast] isn't gonna let me go easily."

    scene classroom with fade

    "As we walk into our new classroom, it's already buzzing with activity."
    "Our homeroom teacher isn't here yet, so the entire class is taking the opportunity to get acquainted with each other."
    "The classroom is already dotted with several friend groups."
    "It's a new year, and now that we're second years, the excitement is contageous."
    "However, in the middle of it all, there seems to be one individual above it all."

    show suzune at normal with dissolve

    "[druglast] [drug.name]."
    "Top of the class, and an elegant beauty for sure."
    "She's got this refined air around her... Almost ethereal."
    "It's as if she isn't walking through life, but simply gliding through it with ease."
    "I've seen her test scores and school ranking from last year."
    "The only way I could describe it is insanity."
    "I've never seen anybody get so many perfect scores in my life."
    "... Certainly not me..."
    "I missed out on the smart."
    idni "Maybe if I'm lucky, I could bum some notes off her."

    hide suzune with dissolve

    "With the sound of the door sliding open, the class quiets down slightly."

    show aoi at normal with dissolve
    "Walking through the door is a young woman, dressed up in an outfit I can only describe as..."
    "... Maybe just a little distracting..."
    "She just excudes maturity and confidence as she walks, as if making it clear who is in charge as the sound of her high heels against the floor threatens to send chills down my spine."
    "???" "Alright, settle down class."
    dead "My name is [deadlast] [dead.name], and I will be your homeroom teacher for this year."
    dead "I see many familiar faces here so I'm sure many of you already know me. For those who may not know me too well, I look forward to teaching all of you."
    dead "Now first thing's firth, wem usth bleh..."
    "[deadlast]-sensei trips over her words, leaving behind a deafening silence."
    "At first I'm not quite sure what's going on, but after a few seconds, muffled laughter can be heard from all around the class."
    "Classmate A" "You haven't changed at all, [dead.name]-sensei."
    dead "It's [dead.name]-sensei..."
    dead "Ah! No, it's [deadlast]-sensei!"
    "Following another slip-up, the rest of the class joins in with the laughter."
    "[deadlast]-sensei's face flushes bright red as she desperately tries to regain her composure."
    "Though with seemingly all hope lost, her shoulder slump down as she makes no effort to hide her dejection."
    dead "I even practiced my speech in the mirror this morning..."
    "Classmate B" "It's okay! We like the clumsy [dead.name]-sensei more than the serious one."
    dead "That's not the point!"
    dead "How are you all supposed to take me seriously if I'm always screwing up!"
    "..."
    "Needless to say, I'm a little stunned."
    "I've never had a teacher so... \nFlustered..."
    "... It's kinda cute..."
    dead "A-anyway! Class introductions!"
    "Desperate to move on, she points to the student at the far front corner of the room."
    dead "You first! Who are you?"

    scene black with fade
    "And with that, a rather amusing homeroom begins with each of us giving our own introductions."
    "I just wish the rest of the morning could be described the same way."
    "After all, school is school, and it's not always fun."

    $ renpy.music.set_volume(0.5, 0, channel='sound')
    play sound "audio/bell.mp3"
    scene classroom with fade


    "As lunch time rolls around, it starts to hit me how hungry I am..."
    "With [sis.name] rushing me this morning, I didn't even get the chance to have any breakfast."
    if idol_flag > sis_flag:
        "... And all that running didn't help anything either..."

        menu:
            "What should I do for lunch?"

            "Go apologize to [sis.name].":
                $ sis_flag += 1
                jump minamiDayOne

            "Try \"getting to know\" [drug.name].":
                $ drug_flag += 1
                jump suzuneDayOne

            "Ask [deadlast]-sensei some questions about the lectures.":
                $ dead_flag += 1
                jump aoiDayOne

            "Wander around the halls.":
                $ idol_flag += 1
                jump sanaDayOne

    else:
        menu:
            "What should I do for lunch?"

            "Go see what [sis.name] is up to.":
                $ sis_flag += 1
                jump minamiDayOne

            "Try \"getting to know\" [drug.name].":
                $ drug_flag += 1
                jump suzuneDayOne

            "Ask [deadlast]-sensei some questions.":
                $ dead_flag += 1
                jump aoiDayOne


label minamiDayOne:
    if idol_flag > sis_flag:
        "I should really go apologize to [sis.name]."
    else:
        "Let's see how [sis.name]'s been handling her first day of high school."

    scene hallway with fade
    "... Or so I say, but it turns out there's someone waiting for me right outside my classroom."
    show minami at normal with dissolve
    sis "Yo!"
    idni "[sis.name]?"
    sis "Took you long enough."

    if idol_flag > sis_flag:
        "[sis.name] doesn't seem at all bothered by what I said to her this morning."
        "Was she not as upset as I thought she was?"
    else:
        "What's she doing here?"

    idni "... Did you need me for something?"
    sis "Well, I knew you'd be worried about your cute little sister, so I thought I'd come by to tell you I'm alright!"
    "[sis.name] flashes a bright smile."
    idni "Oh."
    idni "That's good then. How are you enjoying your first day of high school so far?"
    sis "It's great! I've already got tons of new friends."
    "... Why are you coming to talk to me then...?"
    idni "So why don't you—"
    sis "I thought you might be feeling a little lonely though, so just for today, I'll keep you company!"
    "..."
    idni "Are you sure? What about your—"
    sis "Come on, let's go!"
    "Before I can say anything else, [sis.name] grabs onto my wrist and pulls me along."
    "What's going on?"

    scene cafeteria with fade

    "..."
    show minami at normal with dissolve
    "This isn't what I expected to happen at all."
    "The two of us sit across from each other at a table in the cafeteria as we eat our lunch."
    "Maybe we'd have a quick chat or something, but I wasn't planning on eating with her."
    "But more than that, I feel like there's something going on with her."

    if idol_flag > sis_flag:
        "I was worried before, but now I'm worried about her for an entirely different reason..."
    else:
        "Maybe I'm being a little paranoid, but I can't help but be a little worried about her..."

    idni "Are you sure you want to be eating lunch with me?"
    sis "Why? Don't you {i}love{/i} your sister? We used to eat sometimes back in middle school too, so what's the big deal?"
    sis "Do you think you're too cool to be eating with me now?"
    idni "... No, that's not it."
    sis "Admit it. You actually wanted to eat with me today, right?"
    "..."
    "I will neither confirm or deny that."
    idni "Well, what about all your friends?"
    sis "Oh, is that what you're worried about?"
    sis "I knew my big bro had a soft spot for me!"
    idni "... Not so loud, please..."
    sis "Like I said, I knew you'd be worried about me, so I thought I'd eat with you just for today so that you can see I'm doing fine."
    "[sis.name]'s as energetic as usual."
    "Try as I might, I can't really sense that anything is bothering her. She doesn't seem to be lying at all either."
    idni "If you say so..."
    idni "You were so excited this morning, so I thought maybe you had plans with your friends or something."
    sis "What a softie."
    idni "..."
    "I guess I really do have a soft spot for her..."
    "Even if she can be a handful sometimes."

    jump ending

label suzuneDayOne:
    show suzune at normal with dissolve
    "... Or maybe not..."
    "Looking over to [druglast]'s desk, she's already been swarmed by my other classmates."
    "... Looks like that's not happening..."
    hide suzune with dissolve
    show dude at bigger, normal with dissolve

    if idol_flag >= 2:
        dude "What's this? Longingly staring at another girl even though you already have a girlfriend."
        idni "You really think I would ever date {i}[deadlast] [idol.name]{/i} of all people?"
        dude "True enough."
        dude "So, you getting bullied?"
        idni "I guess that's what that is."
        dude "Sounds rough."
        dude "I'd help you out, but..."
        idni "You're the one who asked if she was my girlfriend."
        dude "I thought it would be funny."
        idni "It wasn't."
        dude "Haha, my bad."
        dude "How about this then, there's an Esper show this weekend."
        dude "You should have come with me. It'll cheer you up!"
        idni "Oh right... That group you won't shut up about."
        idni "No thanks."
        dude "Ayo, watch how you speak on their name."
        dude "They've only been around for a few months but they're gonna be huge, let me tell you."
        "Idols idols idols."
        "Is that this guy's solution to everything?"
        dude "Tell me you've at least heard their new song."
        idni "New song?"
        dude "..."
        "[dudename] looks at me like something he scraped off his shoe."
        dude "Make sure you're free this weekend. You're coming to see them with me."
        idni "I'm not buying a ticket."
        dude "I'll buy one for you then."
        idni "... Fine, as long as you're paying..."

    else:
        dude "Ah, I see you've got your eyes on the prize."
        dude "Can't blame you though. She's cute..."
        dude "Not as cute as [ningning] from Esper though."
        dude "Oh, speaking of Esper, you're totally excited for the show this weekend, right?"
        idni "I didn't say anything..."
        dude "You were thinking about them though, right?"
        idni "No."

    dude "Hey, which one's your favourite?"
    dude "Of course, mine is [ningning]-chan, but they're all really cute. [karina]-chan's a good choice too. Some say she's the prettiest one, but I disagree."
    dude "I have a soft spot for [giselle]-chan since she's improved so much. You can tell how hard she's been working."
    dude "I think you might like [winter]-chan though. She has a sorta aloof vibe. You like that, don't you?"
    idni "Sorry, I'm looking for who asked."

    show suzune at normalright with dissolve
    drug "Oh, are you two talking about Esper?"
    dude "You like Esper too, [druglast]-san?"
    drug "I like listening to them when I study."
    idni "Is everyone here an idol fan except me?"
    dude "You're missing out, [playername]."
    idni "Is it really that big of a deal?"
    dude "I'm trying to convince him to come see their show with me this weekend."
    drug "Really?"
    drug "I think it's a lot of fun, so why not go?"
    "As much as I want to disagree, I can't ignore how excited [druglast] looks."
    dude "Right? There's nothing wrong with having fun!"
    dude "That reminds me, who is your favourite member?"
    drug "Good question... I think I'd have to pick [winter]-chan!"
    dude "Oh that's perfect! I think [playername] would really like her to."
    "Which one is [winter] again?"
    dude "As much as I want him to go, it seems like he doesn't want to come with me."
    drug "Well, you can't force anyone."
    dude "True..."
    dude "But maybe he'd go if it were you instead of me."
    idni "What?"

    show aoi at normalleft with dissolve
    dead "[dudelast]-san, you're needed in the staff room."
    dude "Aw for real?"
    dude "Think about it though, [playername]. Not very often you get to go a concert with someone like [druglast]."
    idni "Whatever..."
    hide aoi with dissolve
    hide dude with dissolve
    show suzune at normal with dissolve

    "I can't help but feel like i've been talked at instead of talked to this entire conversation..."
    "Now that [dudename]'s gone, there's nothing but awkward silence between me and [druglast]."
    idni "Don't worry about coming with me or anything, [druglast]-san."
    idni "You don't have to."
    drug "Oh?"
    drug "I think it would be fun to go though."
    drug "It's been a while since I've gone to see one of their shows."
    "..."
    "Seriously?"
    idni "I don't really get the appeal of idols, to be honest with you."
    drug "I get that... I didn't really get it either."
    drug "But sometimes seeing is believing, right?"
    idni "Is that so?"
    drug "I'm sure you'll have fun if you go. I had fun my first time too."
    idni "So you weren't a fan either? Did a friend take you to a concert then?"
    drug "Hmm..."
    "With a mischievous smile, I'm left wondering what she's thinking."
    drug "You could say that!"

    jump ending

label aoiDayOne:
    "Even though it's the first day, there's still something I'm not certain on."

    show aoi at normal with dissolve
    idni "Sensei."
    dead "Oh! [familyname]-san, did you have a question?"
    idni "Yes, actually. I know it's still the first day, but I just had to ask..."
    dead "Of course, you can ask me anything!"
    idni "I'll be honest, I've never had a teacher like you before."
    dead "I-is that so?"
    "[deadlast]-sensei's eyes quickly dart from side to side as she seems a little nervous."
    "To be honest, it makes me want to..."
    idni "Can I call you [dead.name]-chan?"
    dead "Wh-what? Absolutely not! It's [deadlast]-sensei!"
    "[deadlast]-sensei's face turns a bright red as she pouts, clearly not happy with me calling her by her first name..."
    "It's kinda..."
    idni "Cute..."
    dead "C-cute!?"
    idni "Ah! D-did I say that out loud?"
    dead "[familyname]-san, I hope you don't make it a habit to tease older women..."
    "Her tone sounds stern and imposing, but her flustered face tells a different story."
    idni "I wouldn't do something like that, [dead.name]-chan."
    dead "Th-there you go again!"
    idni "Ah, my bad..."
    dead "[familyname]-san, I suggest you be careful, or else—"
    "Suddenly, [deadlast]-sensei brings her hand up to her mouth to cut herself off."
    idni "... Or else?"
    dead "Staff room, after school!"

    hide aoi with dissolve
    "Before she can say anything else, she hurriedly storms off."
    "This time, her footsteps aren't the calm and composed ones she used to walk into class this morning."
    "Oddly enough though, my heart feels just a little bit lighter now."
    idni "Maybe I should tease her again..."

    jump ending


label sanaDayOne:
    scene hallway with fade
    "I don't really have anything to do. Maybe I'll head over to the cafeteria."


    idol "What's up, {i}boyfriend{/i}."
    "..."
    "I've made a huge mistake."
    show sana at normal with dissolve
    idni "[idollast]..."
    idol "No way, how you know my name?"
    "I really don't want to have a conversation with her."
    idni "..."
    idni "You've got a reputation around school."
    idol "Shit, really?"
    "[idollast] looks absolutely dumbfounded."
    "... Is she serious?"
    idni "Anyway, I don't remember agreeing to go out with you so just leave me alone."
    "Staying around her for any longer can't possibly lead to anything good happening."
    "I try to walk away from [idollast] only to get my arm yanked back." with vpunch
    idol "I'm not done talking to you."
    "She looks at me through squinted eyes, no doubt pissed off at me."
    "..."
    "This isn't how I thought I would die."

    scene black with fade

    "With me as hostage, [idollast] dragged me along as she headed towards an empty classroom."
    "As we passed through the halls, I recieved many sympathetic looks from those who happened to see me."
    "No doubt, they saw what kind of situation I was in and came to the same conclusion as I did."
    "I wasn't making it home alive."

    scene classroom with fade

    $ renpy.music.set_volume(0.3, 0, channel='sound')
    play sound "audio/thud.mp3"
    "The door slams shut behind us as [idollast] practically throws me into the empty classroom."
    "In this moment, my mind races."
    "How am I going to get out of this?"
    show sana at normal with dissolve
    idol "You. What's your name."
    idni "... [familyname]..."
    idol "[familyname]."
    idni "Yeah..."
    "Suddenly, [idollast] sits against one of the empty desks and lets out a big sigh."
    idol "Geez."
    idol "It's so embarrassing when someone knows your name but you don't know theirs."
    "Uh..."
    idol "Nice to meet you, [familyname]."
    idol "... I'd introduce myself, but you seem to already know who I am."
    "..."
    idni "What's going on?"
    "[idollast] looks at me, confused."
    idol "What do you mean?"
    idni "Why did you bring me here?"
    idol "Hallways are too crowded."
    idol "Besides, I wanted to ask you a few things."

    "Suddenly, [idollast] gets up from one of the desks and walks right up to me."
    "I instinctively, step back as she gets closer."
    "As she takes a step towards me, I take a step back until..."
    play sound "audio/thud.mp3"
    "I'm backed up against the wall." with vpunch

    show sana at bigger, normal with dissolve
    idol "What are they saying about me?"
    "Too close!"
    idni "I uhh..."
    idol "You look like you're scared shitless, so it must be some pretty nasty rumours, right?"
    idni "..."
    show sana at biggerer, biggernormal with dissolve
    "A smile creeps onto her face as she gets even closer to me."
    idol "I won't bite."
    idol "Unless you want me to~"
    idni "Too close..."
    "My voice ends up coming out kinda choked and squeaky."
    "Hearing my pathetic cry, [idollast] breaks into a laugh before backing off."
    show sana at normal with dissolve
    idol "This is kinda fun."
    "I stand there in awkward silence as [idollast] continues to laugh at me."
    idol "Look, I don't know what they're saying about me, but I'm not gonna hurt you or anything so relax."
    "..."
    "Easier said than done."
    idni "I just don't want any trouble, alright?"
    idol "Oh, are you still shook from this morning?"
    idol "You don't gotta worry about those guys, okay? It's all good now."
    idni "All good now?"
    idni "Why were they even chasing you in the first place?"
    idol "I must've pissed them off or something, I dunno."
    idni "..."
    idol "Don't look at me like that, alright?"
    idni "Can I go now?"
    idol "Nope!"
    idol "You still gotta tell me what they're saying about me."
    "..."
    "Maybe it would've been better if she had just beaten me up."

    jump ending

label ending:
    stop music fadeout 0.1
    scene black with fade
    "Thank you for reading the Salad VN demo."
    "I dunno when I'll finish the whole thing lol"
    "Go read through all the other choices now."

    return
