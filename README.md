# cart-pole
Modelling the cart pole (Inverted Pendulum) dynamic system using python.

<p align="center">
    <img src="https://raw.githubusercontent.com/shambu09/cart-pole/main/res/output.gif" alt="cart pole visualization"/>
</p>


### Install the dependencies
```
pip install -r requirements.txt
```

### Run
```
python app.py
```

### Images to Video
```
ffmpeg -r 60 -i %d.png -vb 20M ../sample.mpg
```

### Video to GIF
```
ffmpeg -ss 30 -t 15 -i sample.mpg -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```
