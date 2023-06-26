name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
                "Ben liked playing a pickup game of basketball after school. Being in middle school, he spent a lot of the day sitting at a desk, so an hour or so running up and down the court gave him energy. When the game was over, he grabbed his sweatshirt and wiped the sweat from his neck. 'Where are you going?'\n"
                "'Got to run home to shower before I pick up my little sister from her afterschool program,' Ben told his friend Mikey as he made his way off the basketball court.\n\n"
                "Ben headed toward his apartment building, listening to music. When he rounded the corner, Ben saw that his street was lined with City trucks, utility vehicles, orange cones, and wooden barriers. A police cruiser was parked behind one of the barriers, its lights flashing. The garbled sound of two-way radios was everywhere. And a strange, rushing, whooshing made the block sound less like the city and more like a riverside. What in the world was going on? Ben climbed the front stairs of a neighboring building to get a better look.\n"
                "In the middle of the intersection, by the entrance to his apartment building, a burbling, gurgling mound of water seemed to boil up out of the street. Water was rushing everywhere. 'Kid! Hey, kid!' Ben looked down and saw a man in a green vest pointing up at him with a walkie-talkie. 'You live in one of these buildings? I’m with the Community Emergency Response Team,' the man with the walkie-talkie said, holding up his ID badge. 'See, it’s written as ‘CERT’ on my badge. The name’s O’Meara.'\n"
                "'What’s going on, Mr. O’Meara?' Ben asked. '\n"
                "and ben can go to a friend's house or can go up to his apartment."
                ).lower()

if answer == "friend's house":
    answer = input("""
                    “I think I’ll go to my friend’s house,” Ben told Mr. O’Meara. “I can stay there until my parents are off work.”
                    “Has your family designated an emergency meeting place? How will they know where you are?”
                    “They’ll know I’m with Marcus,” Ben insisted. But he wasn’t certain. He figured he could call his mother or father from Marcus’s house.
                    Just then, the warning beep of a backhoe reversing down the street sounded. As they watched the backhoe, Mr. O’Meara spoke: “Listen, kid, you get yourself wherever your family has agreed is a safe meeting place. You can’t stay here. The water’s been shut off to this building, and the power has been turned off.”
                    “No worries,” Ben said. “Thanks, I’m out of here.”
                    Quickly slipping his headphones back on, Ben walked to Marcus’s apartment. Maybe he and Marcus could play some video games or head back to the basketball court. He reached Marcus’s brownstone and raced up the stairs.
                    “Hey, what are you doing here?” Marcus asked as he opened the door.
                    “I had nowhere else to go. You ought to see my street. It’s crazy!”
                    “Why? What happened?” Marcus asked, stepping aside to let Ben in.
                    “Water main break and the power’s out,” Ben replied, dropping his backpack inside the door. “They wouldn’t let me stay. So I thought I’d come here. Is that okay?” Ben asked, turning to Marcus’s mom.
                    “Sure, that’s fine. But do your parents know you’re here?” she asked. “And what about your sister?”
                    Marcus’s mother got her phone and handed it to Ben. “I think you need to call them right away and tell them where you are.” Ben’s mother picked up on the first ring. She’d just gotten a call from a neighbor about the water main break and was worried about where Ben was. She quickly reminded him where to go and that he needed to make sure he had his Go Bag like they’d practiced.
                    “I have to go,” he told Marcus. “Need to go back to my apartment and get my Go Bag before I meet my family.” Ben headed out the door and straight back to his apartment building. He kept his eyes open for Mr. O’Meara or another CERT member, knowing they would help if needed. Ben decides to go up to where? his apartment?
                    """
                    ).lower()

elif answer == "his apartment":
    answer = input("“I need to go up to my apartment,” Ben told Mr. O’Meara. “I have some things I need to get up there. My family has a meeting place written on an emergency card that’s on our refrigerator. And I have a Go Bag.”\n"
               "Mr. O’Meara smiled. “That’s great, Ben. You’re probably not going to be able to stay here tonight, so having a Go Bag is a smart idea. I’ll take you in through the back entrance to your building. Then you can go up to your apartment and get what you need.”\n"
               "Ben and Mr. O’Meara walked together past a barricade where a police officer stood with a clipboard and a radio. Ben gave her his name and apartment number and was cleared to be escorted into the building. Then another CERT member walked with him up to his floor.\n"
               "Ben unlocked the door and went inside. Alone in his apartment, it felt good to be in a safe, familiar place after the hubbub on the street. He went to the window and looked down. He could see the gaping hole, the white water rushing out on the street, and the emergency workers going in every direction. Maybe I’ll just watch the action for a few minutes, Ben thought. But he also knew he had to get his Go Bag and look on the refrigerator to remind himself where his family’s emergency meeting place is.")
            
else:
    print("Not a valid option. You lose.")

