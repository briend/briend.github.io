# Brien Dieterle

[My Gallery](https://www.flickr.com/photos/briend/) | [My Videos](https://www.youtube.com/user/briendieterle) | [My Projects](https://github.com/briend)


# Problems In Painting

## Contrast Effect

The 3 grey rectangles below are identical and have no color, yet the square on the left appears bluish, and the right appears reddish.

![Contrast Effect](https://user-images.githubusercontent.com/6015639/30140938-e5338892-932c-11e7-9b34-949dd61dfe26.png)

The illusion above is only noticeable because of the way the colors are arranged, however _everything_ we see is being affected by this same exact phenomenon.  Given what we know about [Simultaneous Contrast](https://en.wikipedia.org/wiki/Contrast_effect), how are we supposed to mix and choose colors with a high degree of control when the actual _tools_ interfere with the vision process?

![Color Selection Tool](https://user-images.githubusercontent.com/6015639/30137777-d14ef72a-9319-11e7-91bd-e38c0bbb120e.png)   ![Painter's palette](https://user-images.githubusercontent.com/6015639/30223050-217a9118-947e-11e7-83b5-818725827c2d.png)  ![Computer Palette](https://user-images.githubusercontent.com/6015639/30229421-b9aaafc8-9496-11e7-9cf0-e21645444138.png)

One option is to simply get used to it, and [develop rules](http://www.artistsnetwork.com/medium/pastel/the-contrast-effect-important-rules-for-landscape-painting) to help guide your color selections, and knowing that "nothing is what it is until it has a relationship", as Richard McKinley says in the linked article.
Corel Painter's "Temporal Colors Palette" (below) seems to understand this somewhat, as it shows the new color superimposed on your painting as a round "swatch".  However, the interface with the vivid color wheel still imposes a significant Contrast Effect upon your color picking decisions, how could it _not_?

![Corel Temporal Palette](https://user-images.githubusercontent.com/6015639/30222803-0976bdae-947d-11e7-9ec6-e6464f1e53e8.png) ![Corel Temporal Palette in context](https://user-images.githubusercontent.com/6015639/30229320-3f722718-9496-11e7-87f0-0a5a407bbf7f.png)

It seems that it's impossible to select a color from an interface without the interface also influencing the color selection.  Does this explain our tendency to select rather overly saturated colors?  Is this one reason why so many digital paintings "look digital"? 

Why don't we just get rid of the interface and allow the color selection to be influenced by the context within the actual painting?  I should add, we don't want to isolate our colors on some virtual palette on another monitor or in another universe: we _want_ the contrast effect _from our painting_ (_not_ our interface or anything else) to influence our color decisions. To achieve this we can place little swatches of color directly on our painting; just like getting paint samples from the home improvement store!  Except here, we can have unlimited swatches for free without getting the authorities involved.

![interface-less color adjuster](https://user-images.githubusercontent.com/6015639/30137831-0f476df0-931a-11e7-82ce-811f6f67d410.png) ![interface-less color adjuster](https://user-images.githubusercontent.com/6015639/30229508-1c2ec38c-9497-11e7-92e9-fef6453fbc9a.png)

The only problem now is that the interface has to exist somewhere and be operable even when you're not looking at it.   Fortunately, we've long ago invented keyboards and other devices with whole arrays of buttons to choose from.  We can map some buttons to adjust our colors in whatever dimensions we choose.  Hue is an obvious dimension.  What about brightness and saturation?  Then it gets a bit more complicated.

## Color Spaces

Most programs will give you color selectors in the [HSV or HSL](https://en.wikipedia.org/wiki/HSL_and_HSV) color space.  There are [many more models](http://c-128.freeforums.net/thread/94/color-chroma-saturation) to sift through.  The important thing for us is not what the wheels look like. Remember, we just talked about how the _interface will blind you_ through the Contrast Effect.  That includes any kind of color wheel.  What we need is a color model that is intuitive and practical for the artist to use with a few buttons; "out of sight, _in_ the mind".

Traditional artists don't (generally) think or work in terms of HSV, RGB, CMYK, etc.  They work usually work in [Tints, Tones, Shades](https://en.wikipedia.org/wiki/Tints_and_shades]), and [Hue](https://en.wikipedia.org/wiki/Hue).  HSV and many other don't really seem translate into this type of model.  For instance, in HSV, the "value" scale doesn't actually go from black to white.  Neither HSV nor HSL seem to give you Tones, either; a pure red will desaturate to "white" in the HSV model, and HSL will always produce a 50% grey tone no matter if you start with a pure red or a pure yellow.

Fortunately, the [HCY](http://chilliant.blogspot.com/2012/08/rgbhcy-in-hlsl.html) colorspace seems to map directly to these dimensions in a straightforward manner:

Below is the Y (luminosity) component, which directly translates Shades-->Tints:

![Luminosity Ramp](https://user-images.githubusercontent.com/6015639/30140383-f5238706-9328-11e7-8c17-fad92e8d7a3c.png)

Here, below, is the C (chromacity) component, which, as far as I can tell, is a great stand-in for Tones.  A tone is supposed to desaturate to a grey color eventually-- but not just a 50% grey or anything arbitrary.  It should remain a consistent lightness.  Notice how this yellow does _not_ go to bright white, but rather a light grey:

![Chromacity Ramp](https://user-images.githubusercontent.com/6015639/30140486-e7a10404-9329-11e7-8a6a-b8f4459b97ec.png)

Finally, below is H (hue).  What seems like the most straightforward dimension is actually pretty complex.  The HCY model trys to accomodate for how our eyes respond to light wavelengths differently.  So, when you adjust only the hue you still have a color of similar brightness and chromacity.  I started with Yellow, so all the other colors keep that same overall lightness:
![Hue ramp](https://user-images.githubusercontent.com/6015639/30140567-60432c48-932a-11e7-93b3-cad3fe77148a.png)

## Subtractive vs Additive Color Mixing

Perhaps the greatest hurdle facing digital program's approximation of traditional media is the fact that almost any program works in a method better suited for [lights](https://en.wikipedia.org/wiki/Additive_color) instead of paints.  That is, light bulbs and lasers instead of actual pastel chalks, oil paints, acrylics, etc.  In other words, it's completely backwards and upside-down.

If you think you might be clever and force RGB into some kind of [subtractive](https://en.wikipedia.org/wiki/Subtractive_color) mode by simply multiplying your colors together instead of adding them, or switching RGB with RYB primares. . . you're going to have a [bad time](https://user-images.githubusercontent.com/6015639/30145745-5bcdb14c-9348-11e7-91bb-201747b398d3.png).  Most colors will blend to horrible greys or even blacks unless you use precisely the colors Cyan, Magenta, and Yellow (RGB) or Orange, Green, and Magenta (RYB):

![Subtractive Mixing](https://user-images.githubusercontent.com/6015639/30145885-6d4f4d26-9349-11e7-983f-607494f1d3cd.png)

Scott Burns describes the problem in [much more detail](http://scottburns.us/subtractive-color-mixture/) and, helpfully, provides a rather [elegant solution](http://scottburns.us/reflectance-curves-from-srgb/).  I can't say I understand the math at all, but the premise is to essentially synthesize a plausible physical "pigment primary" for every possible color in the sRGB color space.  That may sound impressive, having 16,777,216 pure pigments to work with.  However, you would never go to the art store and buy a tube of pure "slightly beige off-white" paint to go with your collection of 50,000 very slightly different colored tubes of paint back home.

Rather, instead we have something quite a bit more than 360 tubes of paint, if you consider each degree on the wheel.  I'm not even sure how to calcuate how many, but I'm sure it is in the thousands.  This represents our color wheel of pure pigments.

So, instead of an RGB color like yellow, which is 1,1,0, we'd have an entire "reflectance curve" which is essentially the same thing except thirty-six numbers instead of three.  This curve describes what percentage of light is reflected back to the eye for each 10 nanometer slice of the visible light spectrum.  So, black would be all zeros (or very close to zero) and white would be a bunch of higher values, with some approaching 1.0 (even white light needs to have a "curve", so it can't be all 1.0).  As Scott explains, there are infinite varieties of curves that could produce the same color, but nature seems to like "rounded off" curves that have gentle slopes.  This [formula](http://scottburns.us/wp-content/uploads/2015/04/ILLSS.txt) to find these curves is the great gift Scott has given us to make this work.  Thanks Scott!!

The challenge is that it took my computer over a day to generate reflectance curves for the entire sRGB spectrum (256^3), so doing this real-time is not likely without GPU acceleration and much faster processors.  Fortunately, we can precalcuate the whole thing before-hand, and store it as a text file.  On disk it consumes 12GB of space, but "only" 2.4 Gigabytes of RAM when loaded.  Fifteen or twenty years ago this would seem totally ludicrous, but today any mid-range computer with 4GB of system memory can probably handle this and still have some left over for actually, you know, making Art.

So now with this enormous lookup table loaded we can fairly quickly swap out RGB values with reflectance curves, mix them together "like paint" and convert that back to RGB again.

What difference does it make? One of the most striking examples to look at is blending Yellow and Blue.  When you blend Yellow and Blue light, you actually arrive at a neutral gray or even white color.  This is how many LED lamps work; a blue LED combined with a yellow phosphorus coating to combine to give you a normal-looking whitish light.  This isn't how most programs mix colors, though.  For some reason that isn't entirely clear, we are accustomed to mixing the colors without doing gamma correction, so our "mixed light" is darker than it ought to be.  I get the impression this was a happy accident and computer programmers thought it looked "close enough" to some sort of true subtractive blending of pigments or inks.

Here now are three very different way to mix colors on the computer.
From left to right.  Linear Light Additive mixing, Typical Standard Additive mixing, and Scott Burns' Subtractive mixing:

![Mixing Comparison](https://user-images.githubusercontent.com/6015639/30146472-255839fc-934d-11e7-96ae-b8420716ea4b.png)

Clearly, the subtractive mode is more familar and pleasant for anyone interested in painting.  However, it's not that additive mixing has no use.  If you really want to paint rainbows, you probably want Linear Light additive mixing since you are literally trying to mimic light.  Here's a another comparison of a hue shift through HCY.  From top to bottom we have Linear Additive, Standard Additive, and Subtractive:

![hue shift image](https://user-images.githubusercontent.com/6015639/30147782-056b3556-9355-11e7-95d2-75f44d511f8b.png)

Linear Additive stays very bright and vivid, while the other two modes are more dim.  The Standard Additive and Subtractive modes don't seem very different here, which is probably why the Standard Additive is considered "good enough" for most programmers and artists.  Also, when doing a hue shift like this, we're only blending adjacent hues.  The benefits of subtractive modeling really start to show when you blend complementary or more disparate hues, or varying tints/tones/shades. Hopefully Scott Burns' model will become the new "good enough" until we reach the next breakthrough in simulating pigments.
