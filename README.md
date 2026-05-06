# 🤖 iCub Humanoid Robot - ROS 2 Jazzy

Ce package contient la description URDF et les outils de visualisation pour le robot **iCub**.

## 📸 Aperçu du Robot dans RViz
Voici les captures d'écran de la simulation actuelle :

![Vue de Face](images/face.png)
![Vue de Dos](images/back.png)
![Articulations](images/joints.png)

---

## 🛠 Installation & Lancement
```bash
# Compiler le package
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash

# Lancer la visualisation
ros2 launch humanoid_robot display.launch.py
