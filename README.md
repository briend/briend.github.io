# Brien Dieterle

[My Gallery](https://www.flickr.com/photos/briend/)

[My Videos](https://www.youtube.com/user/briendieterle)

[My Projects](https://github.com/briend)


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

Traditional artists don't do work in terms of HSB, RGB, CMYK, etc.  They work in (Tints, Tones, Shades)[https://en.wikipedia.org/wiki/Tints_and_shades]
## Subtractive vs Additive Color Mixing
