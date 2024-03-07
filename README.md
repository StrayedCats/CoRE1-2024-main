# CoRE1-2024-main
Bringup and configuration for CoRE-1 2024 Automatic robot

## Bringup

rosbag + detector

```bash
ROSBAG=/home/core2024/rosbag2_2024_02_25-03_32_06
ros2 launch core1_2024_bringup main.launch.py use_rosbag:=True rosbag_dir:=${ROSBAG} use_viewer:=True 
```
