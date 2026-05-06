# Humanoid Robot Project: iCub Integration

Ce projet se concentre sur la modélisation et la visualisation d'un robot humanoïde (inspiré de l'iCub) dans l'environnement ROS2.

## ⚠️ Notes de Correction (Build Fixes)
- **Naming Convention** : Le package doit être nommé en minuscules (ex: `icub_description` au lieu de `iCub`).
- **URDF Parsing** : Si vous rencontrez l'erreur "Unable to parse robot_description", assurez-vous d'utiliser `ParameterValue` dans votre fichier launch pour forcer le format String.

## 🛠 Installation & Compilation
```bash
# Compilation avec lien symbolique pour faciliter le debug URDF
cd ~/ros2_ws
colcon build --symlink-install --packages-select humanoid_robot icub_description
source install/setup.bash
```

## 🚀 Utilisation

### Visualisation dans RViz
Pour lancer le modèle et voir la structure du robot (TF, RobotModel) :
```bash
ros2 launch humanoid_robot display.launch.py
```

### Vérification de l'URDF
Si le modèle ne s'affiche pas, vérifiez la syntaxe XML :
```bash
check_urdf src/humanoid_robot/urdf/humanoid.urdf
```

## 📁 Structure du Projet
- `urdf/` : Contient le fichier `humanoid.urdf` décrivant les articulations et les liens du robot.
- `launch/` : Scripts Python pour charger le `robot_state_publisher` et lancer RViz.
- `meshes/` : (Optionnel) Fichiers STL/DAE pour le design visuel du iCub.

## 👤 Auteurs
- **Maria Lagab** - Spécialité Robotique et Système Intelligent
