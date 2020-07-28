try:
    import Box2D
    from gym.envs.box2d.lunar_lander import LunarLander
    from gym.envs.box2d.lunar_lander import LunarLanderContinuous
    from gym.envs.box2d.bipedal_walker import BipedalWalker, BipedalWalkerHardcore
    from gym.envs.box2d.car_racing import CarRacing
    from gym.envs.box2d.car_racing2 import CarRacing2
    from gym.envs.box2d.car_racing3 import CarRacing3
    from gym.envs.box2d.car_racing4 import CarRacing4
    from gym.envs.box2d.car_racing5 import CarRacing5
    from gym.envs.box2d.lunar_lander1 import LunarLander1, LunarLanderContinuous1
    from gym.envs.box2d.lunar_lander2 import LunarLander2, LunarLanderContinuous2
    from gym.envs.box2d.lunar_lander3 import LunarLander3, LunarLanderContinuous3
    from gym.envs.box2d.lunar_lander4 import LunarLander4, LunarLanderContinuous4
    from gym.envs.box2d.lunar_lander5 import LunarLander5, LunarLanderContinuous5
except ImportError:
    Box2D = None