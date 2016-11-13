Andreas Karpasitis
Intro to Coding
Invaderers Assignment Documentation

As per the assignments instructions, I changed some colour options in the shaders and altered the speed and size of the invaders. However, since I’ve never done any coding before in my life, it was quite difficult to read and understand the code, let alone changing it without crashing the app.

Initially, the first but least significant to the changes I’ve made, were to the art and sound of the game. I tried not to increase the size of the project, so I used the same scale as the original gifs to create 32x32 colour sprites for the invaders, which I turned into enemy spacecraft with bright red colour, and turned the player ship into an identical design but in bright blue to match the turquoise border I changed in the shaders code. I also downloaded free sound wavs from freesound.org and changed the audio to fit more into a space dog fight theme.Although these changes don’t have anything to do with the code, they are more pleasing than the blandness of the original source.

After a week of failing to alter the code by myself, I decided to ask for assistance form more experienced colleagues. With the help of Matthew Duddington, Luke Sanderson and Luis Bannette of the MSc program, I managed to figure out the basic syntax of the code in the ivaderers example. The guys also helped me with adding a code for vertical movement to my player ship. However, I realised that the code they provided was incomplete as the ship would fly off out of the world’s bounds. Instead of asking them for help, I decided to utilise the existing code, and figure out a solution by myself. By doing so I wanted to prove to myself that I could at least get the grasp of some aspects of the code. It took me several hours of tweaking but I stitched together a collision code that forbade the ship from crossing the borders, using the predefined parameters already in place.

if (is_key_down(key_up)) {
   sprites[ship_sprite].translate(0, +ship_speed);
if (sprites[ship_sprite].collides_with(sprites[first_border_sprite + 1])) {
   sprites[ship_sprite].translate(0, -ship_speed);
				}
			}
if (is_key_down(key_down)) {
   sprites[ship_sprite].translate(0, -ship_speed);
if (sprites[ship_sprite].collides_with(sprites[first_border_sprite + 0])) {
   sprites[ship_sprite].translate(0, +ship_speed);
				}
			}
		}

I experimented a bit more. Sometimes using one ship against one ship by altering the generation algorithm for the number of invaders “num_columns * num rows”, but I kept going back to the original number because it seemed more fun. One thing I left in, however, was continuous fire from my ship. Having continuous fire was less of a hassle than having to keep pressing the spacebar to fire.

altered: 
(else if (is_key_going_down(‘ ’)) {

to:
(else if (is_key_down(' ')) {
for (int i = 0; i != num_missiles; ++i) {
if (!sprites[first_missile_sprite + i].is_enabled()) {

Finally, as the delivery date closed in, I tried to further tweak some of the code, but unfortunately I still need some more practice with C++ in order to create a game from scratch. Most of my attempts to add a menu screen were a bit catastrophic. The game kept not loading properly, so I decided to not to save those attempts in favour of a more stable product. Hopefully by the end of the semester, or by next year, I’ll be able to create original lines of code without the aid of my classmates or the internet.

