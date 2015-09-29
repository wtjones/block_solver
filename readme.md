



Board Format
------------

The data part of the file looks like this:

```
0,0,0,
0,0,0,
8,8,8,

0,0,0,
0,0,0,
8,8,8,

0,0,0,
0,0,0,
8,8,8
```

The possible grid is a cube, with each section separated by an extra newline as a y coordinate slice. The first 9 numbers represent the top row of the cube. In this example, the front side of the cube are cells with a value of 8.

Internally the coordinate system is right-handed. The front cells each have a z value of 2 (zero based). The top row cells each have a y value of 2. The origin is the bottom back left of the cube, represented by the first 0 of the 3rd section.

