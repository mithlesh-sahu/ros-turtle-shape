# 🐢 ROS2 Turtle Shape Drawer

## 📌 Overview

This project demonstrates how to control the **turtlesim** robot in ROS2 to draw geometric shapes such as a **square, circle, and triangle** using velocity commands and services.

The turtle is programmatically moved, teleported to specific positions, and commanded to trace precise shapes using mathematical calculations.

---

## 🚀 Features

* Draws **Square**
* Draws **Circle**
* Draws **Triangle**
* Uses **Teleport service** to position turtle
* Clears and manages drawing space
* Smooth and accurate motion control

---

## 🧠 Concepts Used

* ROS2 Nodes (`rclpy`)
* Publishers (`/turtle1/cmd_vel`)
* Services:

  * `/turtle1/teleport_absolute`
  * `/clear`
* Message types:

  * `geometry_msgs/Twist`
* Motion control using:

  * Linear velocity
  * Angular velocity
* Basic geometry & math:

  * π (pi)
  * Angles (90°, 120°)
  * Circle equations

---

## 📦 Project Structure

```
turtle_shape_drawer.py   # Main Python script
README.md                # Project documentation
```

---

## ⚙️ How It Works

### 1. Teleportation

The turtle is moved to a specific position using:

```
/turtle1/teleport_absolute
```

### 2. Movement

Velocity commands are published to:

```
/turtle1/cmd_vel
```

### 3. Shape Drawing Logic

* **Square** → 4 sides + 90° turns
* **Circle** → Continuous arc motion
* **Triangle** → 3 sides + 120° turns

---

## ▶️ How to Run

### Step 1: Start ROS2

```bash
source /opt/ros/jazzy/setup.bash
```

### Step 2: Create Workspace (if not created)

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash
```

### Step 3: Run turtlesim

```bash
ros2 run turtlesim turtlesim_node
```

### Step 4: Run your script

```bash
python3 turtle_shape_drawer.py
```

---

## 🎯 Output

The turtle will:

1. Draw a **square** on the left
2. Draw a **circle** in the center
3. Draw a **triangle** on the right

---

## 🧩 Code Explanation

### 🔹 Publisher

Publishes velocity commands:

```python
self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
```

### 🔹 Teleport Service

Moves turtle without drawing:

```python
self.teleport_client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
```

### 🔹 Movement Function

Controls linear and angular motion:

```python
def move(self, linear=0.0, angular=0.0, duration=0.0):
```

---

## 📐 Shape Logic

### Square

* Move forward
* Turn 90° using:

```
π/2 radians
```

### Circle

* Uses:

```
angular_speed = linear_speed / radius
```

### Triangle

* Uses:

```
120° turns (2π/3 radians)
```

---

## 🛠️ Requirements

* ROS2 (Jazzy or compatible)
* Python 3
* turtlesim package

Install turtlesim if needed:

```bash
sudo apt install ros-jazzy-turtlesim
```

---

## 📌 Future Improvements

* Add keyboard control
* Add GUI interface
* Add more shapes (hexagon, star)
* Integrate with ROS2 launch files

---

## 👨‍💻 Author

**Mithlesh Sahu**
B.Tech ECE | Robotics Enthusiast 🤖

---

## ⭐ Acknowledgment

This project is built for learning ROS2 concepts like:

* Node communication
* Motion control
* Geometry-based robotics

---

## 📷 Demo (Optional)

(Add screenshots or GIF here later for better presentation)

---
