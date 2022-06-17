## Yolo Object Name Mapping

After executing yolo related examples, there will be a class number shown in every bounding boxes.

### C example  

```bash
sudo ./kl520_demo_generic_image_inference_post_yolo
```

```bash
connect device ... OK
upload firmware ... OK
upload model ... OK
read image ... OK

starting inference loop 100 times:
....................................................................................................

inference loop is done, starting post-processing ...

doing tiny yolo v3 post-processing ...

detectable class count : 80
box count : 6
Box 0 (x1, y1, x2, y2, score, class) = 45.0, 57.0, 93.0, 196.0, 0.965018, 0
Box 1 (x1, y1, x2, y2, score, class) = 43.0, 95.0, 100.0, 211.0, 0.465116, 1
Box 2 (x1, y1, x2, y2, score, class) = 122.0, 68.0, 218.0, 185.0, 0.997959, 2
Box 3 (x1, y1, x2, y2, score, class) = 87.0, 84.0, 131.0, 118.0, 0.499075, 2
Box 4 (x1, y1, x2, y2, score, class) = 28.0, 77.0, 55.0, 100.0, 0.367952, 2
Box 5 (x1, y1, x2, y2, score, class) = 1.0, 84.0, 50.0, 181.0, 0.229727, 2

output bounding boxes on 'output_bike_cars_street_224x224.bmp'
```

### Python example  

```bash
$ python3 KL520DemoGenericInferencePostYolo.py

[Connect Device]
 - Success
[Set Device Timeout]
 - Success
[Upload Firmware]
 - Success
[Upload Model]
 - Success
[Read Image]
 - Success
[Starting Inference Work]
 - Starting inference loop 50 times
 - ..................................................
[Retrieve Inference Node Output ]
 - Success
[Tiny Yolo V3 Post-Processing]
 - Success
[Result]
{
    "class_count": 80,
    "box_count": 6,
    "box_list": {
        "0": {
            "x1": 46,
            "y1": 62,
            "x2": 91,
            "y2": 191,
            "score": 0.965,
            "class_num": 0
        },
        "1": {
            "x1": 44,
            "y1": 96,
            "x2": 99,
            "y2": 209,
            "score": 0.4651,
            "class_num": 1
        },
        "2": {
            "x1": 122,
            "y1": 70,
            "x2": 218,
            "y2": 183,
            "score": 0.998,
            "class_num": 2
        },
        "3": {
            "x1": 87,
            "y1": 85,
            "x2": 131,
            "y2": 117,
            "score": 0.4991,
            "class_num": 2
        },
        "4": {
            "x1": 28,
            "y1": 77,
            "x2": 55,
            "y2": 100,
            "score": 0.368,
            "class_num": 2
        },
        "5": {
            "x1": 3,
            "y1": 84,
            "x2": 48,
            "y2": 181,
            "score": 0.2297,
            "class_num": 2
        }
    }
}
[Output Result Image]
 - Output bounding boxes on 'output_bike_cars_street_224x224.bmp'
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
58              | Potted Plant
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
