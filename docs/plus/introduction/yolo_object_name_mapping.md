# Yolo Object Name Mapping

After executing yolo related examples, there will be a class number shown in every bounding boxes.

```bash
sudo ./kl520_demo_app_yolo_inference
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK

starting inference loop 100 times:
.........................................

detectable class count : 80
box count : 6
Box 0 (x1, y1, x2, y2, score, class) = 75.0, 106.0, 181.0, 363.0, 0.965001, 0
Box 1 (x1, y1, x2, y2, score, class) = 78.0, 192.0, 184.0, 373.0, 0.485309, 1
Box 2 (x1, y1, x2, y2, score, class) = 226.0, 127.0, 405.0, 343.0, 0.998286, 2
Box 3 (x1, y1, x2, y2, score, class) = 174.0, 159.0, 256.0, 222.0, 0.410430, 2
Box 4 (x1, y1, x2, y2, score, class) = 53.0, 142.0, 104.0, 184.0, 0.367214, 2
Box 5 (x1, y1, x2, y2, score, class) = 17.0, 153.0, 75.0, 335.0, 0.266250, 2

output bounding boxes on 'output_bike_cars_street_416x416.bmp'
```

The table listed below provides the corresponding object name for each class number.

Class Number    | Object Name
--------------- | :----------------
0               | Person
1               | Bicycle
2               | Car
3               | Motorbike
4               | Aeroplane
5               | Bus
6               | Train
7               | Truck
8               | Boat
9               | Traffic Light
10              | Fire Hydrant
11              | Stop Sign
12              | Parking Meter
13              | Bench
14              | Bird
15              | Cat
16              | Dog
17              | Horse
18              | Sheep
19              | Cow
20              | Elephant
21              | Bear
22              | Zebra
23              | giraffe
24              | Backpack
25              | Umbrella
26              | Handbag
27              | Tie
28              | Suitcase
29              | Frisbee
30              | Skis
31              | Snowboard
32              | Sports Ball
33              | Kite
34              | Baseball Bat
35              | Baseball Glove
36              | Skateboard
37              | Surfboard
38              | Tennis Racket
39              | Bottle
40              | Wine Glass
41              | Cup
42              | Fork
43              | Knife
44              | Spoon
45              | Bowl
46              | Banana
47              | Apple
48              | Sandwich
49              | Orange
50              | Broccoli
51              | Carrot
52              | Hot Dog
53              | Pizza
54              | Donut
55              | Cake
56              | Chair
57              | Sofa
58              | Pottedplant
59              | Bed
60              | Dining Table
61              | Toilet
62              | Tv Monitor
63              | Laptop
64              | Mouse
65              | Remote
66              | Keyboard
67              | Cell Phone
68              | Microwave
69              | Oven
70              | Toaster
71              | Sink
72              | Refrigerator
73              | Book
74              | Clock
75              | Vase
76              | Scissors
77              | Teddy Bear
78              | Hair Drier
79              | Toothbrush
