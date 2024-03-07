# CoRE1-2024-main
Bringup and configuration for CoRE-1 2024 Automatic robot

## build

```bash
mkdir -p ~/ws_2024/src
cd ~/ws_2024/

wget https://raw.githubusercontent.com/StrayedCats/CoRE-1.env/main/repos/core1_2024auto.repos
vcs import ./src < ./core1_2024auto.repos

source /opt/ros/humble/setup.bash
colcon build --executor sequential --symlink-install
```

## Bringup

rosbag + detector

```bash
ROSBAG=/home/core2024/rosbag2_2024_02_25-03_32_06

source ~/ws_2024/install/setup.bash
ros2 launch core1_2024_bringup main.launch.py use_rosbag:=True rosbag_dir:=${ROSBAG} use_viewer:=True 
```
