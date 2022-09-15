# Animate
```python
# init:
import Animate
```

```python
# class
class animate(Animate.Animate):
    pass
```

```python
# render
an = animate(img, size, fps)  # img: list, size: list, fps: int
an.Video(filename, type1=cv2.VideoWriter_fourcc(*'DIVX')) # filename: str
```