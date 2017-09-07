# Brien Dieterle

[My Gallery](https://www.flickr.com/photos/briend/) | [My Videos](https://www.youtube.com/user/briendieterle) | [My Projects](https://github.com/briend)


# Problems In Painting

## Contrast Effect

Given what we know about [Simultaneous Contrast](https://en.wikipedia.org/wiki/Contrast_effect), how are we supposed to use these things?

![Color Selection Tool](https://user-images.githubusercontent.com/6015639/30137777-d14ef72a-9319-11e7-91bd-e38c0bbb120e.png)

Corel Painter's "Temporal Colors Palette" gets it somewhat better, as it shows the new color superimposed on your painting as a round "swatch".  However, the interface and the vivid color wheel still impose a significant Contrast Effect upon your color picking decisions:

![Corel Temporal Palette](https://user-images.githubusercontent.com/6015639/30140110-0f4f69e4-9327-11e7-95d6-5351854fec64.png)

It seems that it's impossible to select a color from an interface without the interface also influencing the color selection.  So, why don't we get rid of the interface and allow the color selection to be influenced by the context within the actual painting?  I should add, we don't want to isolate our colors on some virtual palette on another monitor or in another universe: we _want_ the contrast effect _from our painting_ (_not_ our interface or anything else) to influence our color decisions. To achieve this we can place little swatches of color directly on our painting; just like getting paint samples from the home improvement store!  Except here, we can have unlimited swatches for free without getting the authorities involved.

![interface-less color selector](https://user-images.githubusercontent.com/6015639/30137831-0f476df0-931a-11e7-82ce-811f6f67d410.png)

The only problem now is that the interface has to exist somewhere and be operable even when you're not looking at it.   Fortunately, we've long ago invented keyboards and other devices with whole arrays of buttons to choose from.  We can map some buttons to adjust our colors in whatever dimensions we choose.  Hue is an obvious dimension.  What about brightness and saturation?  Then it gets a bit more complicated.

## Color Spaces

Most programs will give you color selectors in the [HSV or HSL](https://en.wikipedia.org/wiki/HSL_and_HSV) color space.  There are [many more models](http://c-128.freeforums.net/thread/94/color-chroma-saturation) to sift through.  The important thing for us is not what the wheels look like. Remember, we just got done talking about how the _interface will blind you_.  What we need is a color model that is intuitive and practical for the artist to use with a few buttons.

Traditional artists don't do work in terms of HSV, RGB, CMYK, etc.  They work usually work in [Tints, Tones, Shades](https://en.wikipedia.org/wiki/Tints_and_shades]), and [Hue](https://en.wikipedia.org/wiki/Hue).  Fortunately, the [HCY](http://chilliant.blogspot.com/2012/08/rgbhcy-in-hlsl.html) colorspace seems to map directly to these dimennsions in a straightforward manner:

Here is the Y (luminosity) component, which directly translates Shades-->Tints:
![Luminosity Ramp](https://user-images.githubusercontent.com/6015639/30140383-f5238706-9328-11e7-8c17-fad92e8d7a3c.png)

Here is the C (chromacity) component, which, as far as I can tell, is a great stand-in for Tones.  A tone is supposed to desaturate to a grey color eventually-- but not just a 50% grey or anything arbitrary.  It should remain a consistent lightness.  Notice how this yellow does _not_ go to bright white, but rather a light grey:
![Chromacity Ramp](https://user-images.githubusercontent.com/6015639/30140486-e7a10404-9329-11e7-8a6a-b8f4459b97ec.png)

Finally, H (hue).  What seems like the most straightforward dimension is actually pretty complex.  The HCY model trys to accomodate for how our eyes respond to light wavelengths differently.  So, when you adjust only the hue you still have a color of similar brightness and chromacity.
![Hue ramp](https://user-images.githubusercontent.com/6015639/30140567-60432c48-932a-11e7-93b3-cad3fe77148a.png)

## Subtractive vs Additive Color Mixing
