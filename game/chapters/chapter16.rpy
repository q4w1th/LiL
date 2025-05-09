label stage_chapter16:

    if (number_stages_completed_in_quest["chapter1"] == 6): 

        stop music fadeout 2.0
        play music school

        show chap1611 with fade
        pause 2.0

        $ quick_menu = True

        yuno "I'm really not feeling this retake... This is why I shouldn't have done it."

        show chap1612 with dissolve

        ayumi "Yuno-chan, I think 'not feeling it' is not the main reason why you don't want to be here."

        show chap1613 with dissolve

        yuno "What are you talking about?"

        show chap1614 with dissolve

        ayumi "You should've controlled yourself!"

        show chap1615 with dissolve

        yuno "Ayumi-chan, don't nag... I have everything under control."

        show chap1616 with dissolve

        ayumi "By the way, [mc_name], you know that the retake is oral, right?"
        mc "?!"

        show chap1617 with dissolve

        ayumi "E-e-eh... I can see from your expression that you didn't know that?"
        ayumi "Well, don't panic, it's not that scary!"

        show chap1618 with dissolve

        yuno "Hehe... Maybe the newbie wanted to trick again?"
        yuno "But even if he wanted to, it won't work now. Especially with Kato-sensei."

        show chap1619 with dissolve

        ayumi "Oh, why are you scaring him like that? Everything will be fine!"
        ayumi "Well, let's go!"

        $ quick_menu = False

        show screen mid_text("The retake is oral... I'm so screwed...") with fade
        scene black
        pause 2.0
        show screen mid_text("You with your classmates stay at corridor.") with fade
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1621 with Fade(0.0, 0.0, 0.5)

        stop music fadeout 2.0
        play music bgm

        $ quick_menu = True

        ayumi "So... Who's going first?"

        show chap1622 with dissolve

        yuno "Who-who, newbie, of course."

        menu: 
            "But I don't know how to...":
                $ yunoaff = yunoaff
                show chap1623 with dissolve
                yuno "Haha, okay, you scaredy-cat. Fine, I'll go."
            "Me? Well... okay.":
                $ yunoaff += 1
                show chap1623 with dissolve
                yuno "Ha-ha, don't be afraid... Well, I'll go, the sooner, the better."

        $ quick_menu = False

        show screen mid_text("Yuno goes to the classroom.") with fade
        scene black 
        pause 1.5
        show screen mid_text("...") with fade
        pause 1.0
        show screen mid_text("Then return...") with fade
        pause 1.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1624 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        ayumi "Well, how was it?"

        show chap1625 with dissolve

        yuno "Excellent. The questions were quite easy this time."

        menu:
            "I wish I could do that...":
                $ yunoaff = yunoaff
            "Well done, I thought only Ishito and Takahashi were good at biology...":
                $ yunoaff -= 1
                show screen affection_hint_minus("-1 to Yuno's relationship!") with moveintop
                pause 1.0
                hide screen affection_hint_minus with moveouttop

        show chap1626 with dissolve

        ayumi "Well... Now it's my turn!"

        show screen mid_text("Ayumi goes to the classroom.") with fade
        scene black 
        pause 1.5
        show screen mid_text("...") with fade
        pause 1.0
        show screen mid_text("Then return...") with fade
        pause 1.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1627 with Fade(0.0, 0.0, 0.5)

        yuno "Excellent?"

        show chap1628 with dissolve

        ayumi "Oh, no."
        ayumi "I made one mistake."

        show chap1629 with dissolve

        yuno "Haha, well, no worries. The main thing is, you passed."

        show chap16210 with dissolve

        ayumi "So, [mc_name], it's your turn!"
        ayumi "We'll be waiting for you outside!"

        $ quick_menu = False

        show screen mid_text("You at classroom...") with fade
        scene black 
        pause 1.5
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1631 with Fade(0.0, 0.0, 0.5)

        akira "[mc_name], right? Come on in. Let's get this over with."

        show screen mid_text("You enter the classroom, takes the retake, but unfortunately, doesn't pass.") with fade
        scene black 
        pause 3.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        show chap1632 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        akira "I'll give you the minimum passing grade, considering you're an exchange student."
        akira "But I highly recommend taking up my offer for tutoring. It might help you catch up."
        mc "Thank you, Akira-sensei. I'll take you up on that offer."

        $ quick_menu = False

        show screen mid_text("You enter the school entrance.") with fade
        scene black 
        pause 2.0
        show screen mid_text("Ayumi and Yuno is waiting for you.") with fade
        pause 2.0
        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        stop music fadeout 2.0
        play music school

        show chap1641 with Fade(0.0, 0.0, 0.5)

        $ quick_menu = True

        mc "Hey!! Now that the retake is over, what do you say we go out again?"

        show chap1642 with dissolve

        yuno "Sounds good to me!"
        ayumi "Sure, why not?"

        show screen mid_text("You call to Akane and Rei to ask they about hang out.") with fade
        scene black 
        pause 2.5
        show screen mid_text("They agreed.") with fade
        pause 1.5
        show screen mid_text("You think that next day will be good to hang out.") with fade
        pause 2.5
        show screen mid_text("You go home.") with fade

        hide screen mid_text with Fade(0.5, 0.0, 0.0)

        $ quest_next_stage(id = "chapter1")
        $ quick_menu = False

        call change_location("house") from _call_change_location_1
        call wait(4) from _call_wait_6

        stop music fadeout 2.0
        play music bgm

    return

