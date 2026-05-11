🤖 iCub Humanoid Robot - ROS 2 Jazzy

Ce package contient la description URDF et les outils de visualisation pour le robot humanoïde iCub. Ce modèle est optimisé pour la simulation et la visualisation dans l'écosystème ROS 2.
📸 Aperçu du Robot



🛠 Installation & Compilation

Suivez ces étapes pour préparer votre environnement de travail :
# Accéder au workspace
cd ~/ros2_ws

# Compiler le package avec les liens symboliques (pratique pour l'URDF)
colcon build --symlink-install

# Sourcer l'installation
source install/setup.bash



🚀 Lancement de la Visualisation
<img width="1716" height="1061" alt="Capture d’écran du 2026-05-11 22-06-17" src="https://github.com/user-attachments/assets/f9e69cfa-8d1d-4bc7-aea8-cb93553bb28f" />
<img width="1369" height="891" alt="Capture d’écran du 2026-05-11 22-08-27" src="https://github.com/user-attachments/assets/d67d1edf-5e82-4789-ab92-ec364cdb19e1" />



Pour lancer le robot dans RViz avec le joint_state_publisher_gui (pour manipuler les membres) :
ros2 launch humanoid_robot display.launch.py


Structure du Package

    urdf/ : Contient le fichier XML décrivant la structure cinématique (links, joints, materials).

    meshes/ : Fichiers .dae (Collada) utilisés pour le rendu visuel détaillé.

    launch/ : Scripts Python pour démarrer les nœuds robot_state_publisher et rviz2.

⚙️ Détails Techniques (URDF)
This project was co-authored and implemented by the team: Amira Malak Daoui, Maria Lagab

Le modèle définit une hiérarchie complexe respectant les standards de l'iCub :

    Torse : 3 degrés de liberté (Pitch, Roll, Yaw).

    Membres Supérieurs : Épaules, coudes et mains avec doigts détaillés (Index, Middle, Ring, Pinky, Thumb).
    ![Aperçu du iCub](images/face.png)
   Membres Inférieurs : Hanches, genoux et chevilles équipés de capteurs de force/couple (FT sensors).




   
   Amira, [May 11, 2026 at 21:52]
This project was co-authored and implemented by the team: Amira Malak Daoui, Maria Lagab, and Romaissa Athmani.

    Matériaux : Définition des couleurs red, grey, white, dark, skin, et black.
