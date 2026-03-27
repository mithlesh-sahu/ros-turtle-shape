import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute
from std_srvs.srv import Empty
import math
import time


class TurtleShapeDrawer(Node):
    def __init__(self):
        super().__init__('turtle_shape_drawer')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        # Service to teleport turtle to a specific position
        self.teleport_client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')

        # Service to clear the screen
        self.clear_client = self.create_client(Empty, '/clear')

        # Wait for services to be ready
        self.teleport_client.wait_for_service()
        self.clear_client.wait_for_service()
        time.sleep(1.0)

    def teleport(self, x, y, angle=0.0):
        """Teleport turtle to (x, y) with given angle (radians). No line drawn."""
        req = TeleportAbsolute.Request()
        req.x = float(x)
        req.y = float(y)
        req.theta = float(angle)
        future = self.teleport_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)
        time.sleep(0.3)

    def move(self, linear=0.0, angular=0.0, duration=0.0):
        """Publish velocity for a given duration, then stop."""
        msg = Twist()
        msg.linear.x = linear
        msg.angular.z = angular
        end_time = time.time() + duration
        while time.time() < end_time:
            self.publisher.publish(msg)
            time.sleep(0.05)
        self.stop()

    def stop(self):
        """Stop the turtle."""
        msg = Twist()
        self.publisher.publish(msg)
        time.sleep(0.2)

    def draw_square(self, side_length=2.0, speed=1.0):
        """Draw a square with accurate 90-degree turns."""
        self.get_logger().info('Drawing Square...')
        turn_speed = 1.5  # rad/s for turning
        turn_duration = (math.pi / 2) / turn_speed  # exact 90 degrees

        for _ in range(4):
            # Move one side forward
            self.move(linear=speed, duration=side_length / speed)
            # Turn exactly 90 degrees
            self.move(angular=turn_speed, duration=turn_duration)

        self.get_logger().info('Square complete.')
        time.sleep(1.0)

    def draw_circle(self, radius=1.0, speed=1.0):
        """Draw a full circle using arc motion."""
        self.get_logger().info('Drawing Circle...')
        angular_speed = speed / radius
        circumference = 2 * math.pi * radius
        duration = circumference / speed
        self.move(linear=speed, angular=angular_speed, duration=duration)
        self.get_logger().info('Circle complete.')
        time.sleep(1.0)

    def draw_triangle(self, side_length=2.0, speed=1.0):
        """Draw an equilateral triangle with 120-degree exterior turns."""
        self.get_logger().info('Drawing Triangle...')
        turn_speed = 1.5  # rad/s
        exterior_angle = (2 * math.pi) / 3  # 120 degrees
        turn_duration = exterior_angle / turn_speed

        for _ in range(3):
            self.move(linear=speed, duration=side_length / speed)
            self.move(angular=turn_speed, duration=turn_duration)

        self.get_logger().info('Triangle complete.')
        time.sleep(1.0)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleShapeDrawer()

    try:
        # --- Draw Square at left area ---
        node.teleport(2.5, 5.5, 0.0)   # bottom-left of square
        node.draw_square(side_length=2.0, speed=1.0)

        # --- Draw Circle in the middle ---
        node.teleport(5.5, 4.5, 0.0)   # start of circle arc
        node.draw_circle(radius=1.2, speed=1.0)

        # --- Draw Triangle on the right ---
        node.teleport(7.5, 4.0, 0.0)   # bottom-left of triangle
        node.draw_triangle(side_length=2.0, speed=1.0)

        node.get_logger().info('All shapes drawn successfully!')

    except KeyboardInterrupt:
        pass
    finally:
        node.stop()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
